# Anbernic RG 55G1

The RG 55G1 is built on the Qualcomm SM4450 ("ravelinp"), sharing most of its
board design with the Retroid Pocket Classic.

Hardware support comes from the RG55G1 bring-up in
[JPyke3/armada `feat-rg55g1`](https://github.com/JPyke3/armada/tree/feat-rg55g1),
which in turn builds on ROCKNIX's SM4450 work:

- `packaging/rpm/kernel-rg55g1/` carries the SM4450 kernel series, the armada
  patches it depends on, and the board DTS. `PATCHES.md` records provenance.
- `mkosi.extra/` carries the ADSP/WPSS/amplifier/GPU zap firmware, the ALSA UCM
  profile and audio topology, and the InputPlumber device definition.
  `usr/share/doc/ultramarine/rg55g1-sources.md` records their origin; the
  `a613_zap.mbn` GPU zap shader was added in armada's initial RG55G1 bring-up
  commit without a separate source note.

## boot chain

The image is booted through UEFI firmware, not through the stock Android ABL
or the ROCKNIX ABL used by armada:

- UEFI loads systemd-boot from the ESP (p1).
- systemd-boot loads the kernel, the mkosi-built systemd initrd and
  `qcom/sm4450-anbernic-rg55g1.dtb` from the ESP.
- The root partition (p2) has a fixed PARTUUID passed as `root=PARTUUID=`
  from `/etc/kernel/cmdline`, rather than relying on gpt-auto discovery, which
  needs EFI runtime variables that Qualcomm UEFI often lacks. On first boot
  systemd-repart grows it into the rest of the card.

Storage, display, SoC clocks and interconnect are built into the kernel, so the
initrd does not need any modules. Despite `KernelModulesInitrd=no`, the built
image still ships a `kernel-modules.initrd`, and udev in the initrd loads
`qcom_q6v5_pas` before the root partition, which holds the ADSP/WPSS firmware,
is mounted. Their auto-boot then fails with `-ENOENT` and is never retried, so
`qcom-remoteproc-start.service` starts any remoteproc still offline once the
rootfs is up. Without it, neither wifi (WPSS) nor audio (ADSP) come up.

## Build

The mkosi configuration is composed of `base`, the `rg55g1` board profile and
the `rg55g1-mainline` boot stack:

```bash
just --justfile mkosi.profiles/rg55g1/justfile kernel-rpms
just --justfile mkosi.profiles/rg55g1/justfile mainline-image
just --justfile mkosi.profiles/rg55g1/justfile flash /dev/sdX
```

or, through the top-level dispatcher, `just profile=rg55g1 image`.

## Status

This profile has not been booted on hardware yet. Unverified assumptions:

- The Sway output name (`DSI-1`) and its `transform 90` rotation, taken from
  armada's `ARMADA_PANEL_ORIENTATION=right`.
- The serial console on `ttyMSM0` (DT `serial0 = &uart7`).
- The USB gadget, which needs the DWC3 controller in device role.
