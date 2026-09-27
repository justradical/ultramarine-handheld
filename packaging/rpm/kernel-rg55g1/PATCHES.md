# Patches

Linux 7.2.6 patches carried for the Anbernic RG 55G1, taken from
[JPyke3/armada `feat-rg55g1`](https://github.com/JPyke3/armada/tree/2862ae96da5493b35365ab692c81e11d7ada1fa2/packages/kernel)
at `2862ae96`. This is the `sm4450-*` series plus the armada/ROCKNIX patches it is
rebased on (display, AW88166, sc8280xp MI2S, battmgr, SoC serial) and generic
Qualcomm fixes armada ships to every device. Patches for other armada boards
are not carried. Entries below are copied from armada's `PATCHES.md`.

Ultramarine changes:

- `sm4450-0053-input-add-singleadc-joypad.patch` and
  `sm4450-0053a-input-singleadc-joypad-rgb-leds.patch`: joystick `Kconfig` and
  `Makefile` context refreshed, because the other armada joystick drivers they
  were diffed against are not carried. The code is unchanged.
- `sm4450-anbernic-rg55g1.dts` is vendored verbatim. Its armada delta
  (`dts/sm4450-anbernic-rg55g1.dts.patch`) is carried as
  `sm4450-anbernic-rg55g1-touch-orientation.patch`.

- `0004-drm-msm-a6xx-Enable-IFPC-on-Adreno-740.patch`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8550/patches/linux/0004-drm-msm-a6xx-Enable-IFPC-on-Adreno-740.patch
  upstream: unknown
- `0010-msm-resource-cleanup.patch`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/packages/linux/patches/7.0/0010-msm-resource-cleanup.patch
  upstream: unknown
  notes: Armada initialises cstate before the num_mixers reset it adds; the ROCKNIX version writes through an uninitialised pointer.
- `0048-drm-msm-dsi-reparent-byte-pixel-src-to-xo-on-disable.patch`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8750/patches/linux/0048-drm-msm-dsi-reparent-byte-pixel-src-to-xo-on-disable.patch
  upstream: unknown
- `0048a-drm-msm-dsi-round-byte-clock-rate-after-reparenting-to-PLL.patch`
  source: https://git.kernel.org/torvalds/c/2028280686f4fa78e2f1f6dede4b6c1fd782b9e3
  upstream: https://lore.kernel.org/r/20260903-fix-eliza-dsi-v1-1-3474a6c9f2e0@oss.qualcomm.com
  notes: Context of the struct msm_dsi_host hunk refreshed to apply after `0048`.
- `0066-drm-msm-dpu-enable-inline-rotation.patch`
  source: https://github.com/ROCKNIX/distribution/blob/60bb58c1db053255b700f3953b72d619ec5aa85d/projects/ROCKNIX/devices/SM8550/patches/linux/0066-drm-msm-dpu-enable-sm8550-inline-rotation.patch
  upstream: unknown
  notes: Armada merged the ROCKNIX SM8550, SM8650 and SM8750 patches into one for the combined kernel, with one shared feature mask and rotation config.
- `0068-drm-msm-dpu-lutdma-dspp-igc-gamut.patch`
  source: armada
  upstream: local
- `1006-tty-serial-qcom-geni-mask-non-console-irq-on-suspend.patch`
  source: https://github.com/thorch-os/thorch/blob/2614a262d7de3f31bd47a0c92981461146663847/packages/linux-thorch/patches/0010-tty-serial-qcom-geni-mask-non-console-irq-on-suspend.patch
  upstream: unknown
- `0036_ASoC--qcom--sc8280xp-Add-support-for-Primary-I2S.patch`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8550/patches/linux/0036_ASoC--qcom--sc8280xp-Add-support-for-Primary-I2S.patch
  upstream: https://lore.kernel.org/r/20251008-topic-sm8x50-next-hdk-i2s-v2-3-6b7d38d4ad5e@linaro.org
- `0032-ASoC-codecs-aw88166-AYN-Products-Specific-modificati.patch`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8750/patches/linux/0032-ASoC-codecs-aw88166-AYN-Products-Specific-modificati.patch
  upstream: unknown
- `0505-msm_gem-lock-before-put_iova_spaces.patch`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8250/patches/linux/0505-msm_gem-lock-before-put_iova_spaces.patch
  upstream: unknown
- `0204-thermal-qcom-tsens-mask-lower-threshold-irqs-across-suspend.patch`
  source: armada
  upstream: local
  notes: Lower threshold crossings during the suspend transition cannot be serviced while thermal zones are quiesced, so the level IRQ storms and aborts suspend; masking LOWER across the transition removes the cause and keeps upper/critical wake armed.
- `0121-pmdomain-qcom-rpmhpd-presync-floor-gmu-rails.patch`
  source: https://github.com/ROCKNIX/distribution/blob/ef264a238d5e2ba960145e3fda663dc27de49a80/projects/ROCKNIX/devices/SM8550/patches/linux/0121-pmdomain-qcom-rpmhpd-presync-floor-gmu-rails.patch
  source: https://github.com/ROCKNIX/distribution/blob/ef264a238d5e2ba960145e3fda663dc27de49a80/projects/ROCKNIX/devices/SM8750/patches/linux/0052-pmdomain-qcom-rpmhpd-presync-floor-gmu-rails.patch
  upstream: unknown
  notes: Armada applies the presync_floor and skip_retention_level flags via private descriptors (gfx_gmu for SM8550+SM8750, gmxc_sm8750) so GMU rail pre-sync behavior cannot change on other SoCs; ROCKNIX instead flags the shared gfx/gmxc structs, which would leak onto every SoC sharing them in a combined kernel. SM8250 and SM8650 have no Linux-side voter on these rails (their gpucc/gmu nodes reference only gpucc GDSCs), so the flags would be inert there today; revisit the scoping if the upstream gpucc power plumbing series lands and adds voters on more SoCs.
- `0501-ROCKNIX-fix-wifi-and-bt-mac.patch`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8550/patches/linux/0501-ROCKNIX-fix-wifi-and-bt-mac.patch
  upstream: unknown
  notes: Armada refreshed only the ath12k insertion context for Linux 7.1's rate-table macros; MAC derivation behavior is unchanged.
- `0503-ROCKNIX-battery-name.patch`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8550/patches/linux/0503-ROCKNIX-battery-name.patch
  upstream: unknown
- `0901-power-supply-qcom-battmgr-fix-charge-unit.patch`
  source: https://lkml.iu.edu/2608.3/10893.html
  upstream: https://lkml.iu.edu/2608.3/10893.html
  notes: Carries the upstream SM8350-class fix that initializes the charge unit to mAh so CHARGE_FULL* is available to userspace.
- `0902-power-supply-qcom-battmgr-expose-charge-now.patch`
  source: https://lkml.iu.edu/2608.3/10890.html
  upstream: https://lkml.iu.edu/2608.3/10890.html
  notes: Carries the upstream SM8350/SM8550 mapping of the firmware remaining-charge counter to CHARGE_NOW.
- `sm4450-0001-drm-msm-adreno-add-a613-catalog-entry.patch`
  source: https://github.com/ROCKNIX/distribution/blob/05efe5552ba5d908a121ae0f2b35dd9e46a46c74/projects/ROCKNIX/devices/SM4450/patches/linux/0001-drm-msm-adreno-add-a613-catalog-entry.patch
  upstream: unknown
- `sm4450-0002-pmdomain-qcom-rpmhpd-add-lcx-for-sm4450.patch`
  source: https://github.com/ROCKNIX/distribution/blob/05efe5552ba5d908a121ae0f2b35dd9e46a46c74/projects/ROCKNIX/devices/SM4450/patches/linux/0002-pmdomain-qcom-rpmhpd-add-lcx-for-sm4450.patch
  upstream: unknown
- `sm4450-0003-remoteproc-qcom-pas-add-sm4450-adsp-wpss.patch`
  source: https://github.com/ROCKNIX/distribution/blob/05efe5552ba5d908a121ae0f2b35dd9e46a46c74/projects/ROCKNIX/devices/SM4450/patches/linux/0003-remoteproc-qcom-pas-add-sm4450-adsp-wpss.patch
  upstream: unknown
- `sm4450-0004-regulator-qcom-rpmh-add-pm6450.patch`
  source: https://github.com/ROCKNIX/distribution/blob/05efe5552ba5d908a121ae0f2b35dd9e46a46c74/projects/ROCKNIX/devices/SM4450/patches/linux/0004-regulator-qcom-rpmh-add-pm6450.patch
  upstream: unknown
- `sm4450-0005-soc-qcom-pd-mapper-add-sm4450.patch`
  source: https://github.com/ROCKNIX/distribution/blob/05efe5552ba5d908a121ae0f2b35dd9e46a46c74/projects/ROCKNIX/devices/SM4450/patches/linux/0005-soc-qcom-pd-mapper-add-sm4450.patch
  upstream: unknown
- `sm4450-0006-interconnect-qcom-add-sm4450.patch`
  source: https://github.com/ROCKNIX/distribution/blob/05efe5552ba5d908a121ae0f2b35dd9e46a46c74/projects/ROCKNIX/devices/SM4450/patches/linux/0006-interconnect-qcom-add-sm4450.patch
  upstream: unknown
- `sm4450-0008-iommu-arm-smmu-qcom-add-sm4450.patch`
  source: https://github.com/ROCKNIX/distribution/blob/05efe5552ba5d908a121ae0f2b35dd9e46a46c74/projects/ROCKNIX/devices/SM4450/patches/linux/0008-iommu-arm-smmu-qcom-add-sm4450.patch
  upstream: unknown
- `sm4450-0009-drm-msm-add-sm4450-display.patch`
  source: https://github.com/ROCKNIX/distribution/blob/05efe5552ba5d908a121ae0f2b35dd9e46a46c74/projects/ROCKNIX/devices/SM4450/patches/linux/0009-drm-msm-add-sm4450-display.patch
  upstream: unknown
  notes: Refreshed for Armada's combined DPU catalog.
- `sm4450-0009a-drm-msm-dpu-rename-sm4450-rotation-formats.patch`
  source: Armada corrective patch
  upstream: unknown
  notes: Gives the SM4450 rotation format list a unique name.
- `sm4450-0009b-drm-msm-dpu-allow-argb8888-inline-rotation.patch`
  source: Armada corrective patch
  upstream: unknown
  notes: Allows Gamescope's UBWC ARGB8888 and XRGB8888 output through SM4450 inline rotation.
- `sm4450-0011-clk-qcom-dispcc-sm4450-fix-mdp-clk-src-ops.patch`
  source: https://github.com/ROCKNIX/distribution/blob/05efe5552ba5d908a121ae0f2b35dd9e46a46c74/projects/ROCKNIX/devices/SM4450/patches/linux/0011-clk-qcom-dispcc-sm4450-fix-mdp-clk-src-ops.patch
  upstream: unknown
  notes: Corrects a malformed source hunk header.
- `sm4450-0012-clk-qcom-dispcc-sm4450-quiesce-splash.patch`
  source: https://github.com/ROCKNIX/distribution/blob/05efe5552ba5d908a121ae0f2b35dd9e46a46c74/projects/ROCKNIX/devices/SM4450/patches/linux/0012-clk-qcom-dispcc-sm4450-quiesce-splash.patch
  upstream: unknown
- `sm4450-0013-clk-qcom-gpucc-sm4450-add-hlos1-vote-gpu-smmu.patch`
  source: https://github.com/ROCKNIX/distribution/blob/05efe5552ba5d908a121ae0f2b35dd9e46a46c74/projects/ROCKNIX/devices/SM4450/patches/linux/0013-clk-qcom-gpucc-sm4450-add-hlos1-vote-gpu-smmu.patch
  upstream: unknown
- `sm4450-0014-clk-qcom-gpucc-sm4450-enable-gx-gdsc.patch`
  source: https://github.com/ROCKNIX/distribution/blob/05efe5552ba5d908a121ae0f2b35dd9e46a46c74/projects/ROCKNIX/devices/SM4450/patches/linux/0014-clk-qcom-gpucc-sm4450-enable-gx-gdsc.patch
  upstream: unknown
- `sm4450-0015-drm-msm-a6xx-avoid-gmu-cx-reads-on-a613.patch`
  source: https://github.com/ROCKNIX/distribution/blob/05efe5552ba5d908a121ae0f2b35dd9e46a46c74/projects/ROCKNIX/devices/SM4450/patches/linux/0015-drm-msm-a6xx-avoid-gmu-cx-reads-on-a613.patch
  upstream: unknown
- `sm4450-0017-clk-qcom-gpucc-sm4450-fix-gfx3d-rcg-ops.patch`
  source: https://github.com/ROCKNIX/distribution/blob/05efe5552ba5d908a121ae0f2b35dd9e46a46c74/projects/ROCKNIX/devices/SM4450/patches/linux/0017-clk-qcom-gpucc-sm4450-fix-gfx3d-rcg-ops.patch
  upstream: unknown
- `sm4450-0018-clk-qcom-gpucc-sm4450-retain-gx-gdsc-regs.patch`
  source: https://github.com/ROCKNIX/distribution/blob/05efe5552ba5d908a121ae0f2b35dd9e46a46c74/projects/ROCKNIX/devices/SM4450/patches/linux/0018-clk-qcom-gpucc-sm4450-retain-gx-gdsc-regs.patch
  upstream: unknown
  notes: Corrects a malformed source hunk header.
- `sm4450-0019-drm-msm-dpu-stop-boot-scanout.patch`
  source: https://github.com/ROCKNIX/distribution/blob/05efe5552ba5d908a121ae0f2b35dd9e46a46c74/projects/ROCKNIX/devices/SM4450/patches/linux/0019-drm-msm-dpu-stop-boot-scanout.patch
  upstream: unknown
  notes: Rebased after Armada's DPU changes.
- `sm4450-0022-regulator-qcom-rpmh-add-pbs-type.patch`
  source: https://github.com/ROCKNIX/distribution/blob/05efe5552ba5d908a121ae0f2b35dd9e46a46c74/projects/ROCKNIX/devices/SM4450/patches/linux/0022-regulator-qcom-rpmh-add-pbs-type.patch
  upstream: unknown
- `sm4450-0023-leds-qcom-lpg-add-pm6450-pwm.patch`
  source: https://github.com/ROCKNIX/distribution/blob/05efe5552ba5d908a121ae0f2b35dd9e46a46c74/projects/ROCKNIX/devices/SM4450/patches/linux/0023-leds-qcom-lpg-add-pm6450-pwm.patch
  upstream: unknown
- `sm4450-0024-serial-qcom-geni-restart-terminated-rx-command.patch`
  source: https://github.com/ROCKNIX/distribution/blob/05efe5552ba5d908a121ae0f2b35dd9e46a46c74/projects/ROCKNIX/devices/SM4450/patches/linux/0024-serial-qcom-geni-restart-terminated-rx-command.patch
  upstream: unknown
- `sm4450-0030-ASoC-qcom-sc8280xp-i2s-clk-support.patch`
  source: https://github.com/ROCKNIX/distribution/blob/05efe5552ba5d908a121ae0f2b35dd9e46a46c74/projects/ROCKNIX/devices/SM4450/patches/linux/0030-ASoC-qcom-sc8280xp-i2s-clk-support.patch
  upstream: unknown
  notes: Carries the Senary MI2S delta on top of Armada's existing Primary MI2S support.
- `sm4450-0031-ASoC-codecs-aw88166-support-changing-sample-rate-and-bit-width.patch`
  source: https://github.com/ROCKNIX/distribution/blob/05efe5552ba5d908a121ae0f2b35dd9e46a46c74/projects/ROCKNIX/devices/SM4450/patches/linux/0031-ASoC-codecs-aw88166-support-changing-sample-rate-and-bit-width.patch
  upstream: unknown
  notes: Rebased on Armada's AW88166 changes.
- `sm4450-0032-ASoC-codecs-aw88166-reduce-log-spam.patch`
  source: https://github.com/ROCKNIX/distribution/blob/05efe5552ba5d908a121ae0f2b35dd9e46a46c74/projects/ROCKNIX/devices/SM4450/patches/linux/0032-ASoC-codecs-aw88166-reduce-log-spam.patch
  upstream: unknown
- `sm4450-0033-ASoC-codecs-aw88166-remove-fade-in-out-on-start-stop.patch`
  source: https://github.com/ROCKNIX/distribution/blob/05efe5552ba5d908a121ae0f2b35dd9e46a46c74/projects/ROCKNIX/devices/SM4450/patches/linux/0033-ASoC-codecs-aw88166-remove-fade-in-out-on-start-stop.patch
  upstream: unknown
- `sm4450-0034-ASoC-codecs-aw88166-make-volume-control-usable.patch`
  source: https://github.com/ROCKNIX/distribution/blob/05efe5552ba5d908a121ae0f2b35dd9e46a46c74/projects/ROCKNIX/devices/SM4450/patches/linux/0034-ASoC-codecs-aw88166-make-volume-control-usable.patch
  upstream: unknown
  notes: Rebased on Armada's AW88166 changes.
- `sm4450-0035-ASoC-codecs-aw88166-drop-duplicate-dai-stubs.patch`
  source: armada
  notes: Present in armada's series without a PATCHES.md entry.
- `sm4450-0039-soundwire-qcom-arm-wake-detector-for-clock-stop.patch`
  source: https://github.com/ROCKNIX/distribution/blob/05efe5552ba5d908a121ae0f2b35dd9e46a46c74/projects/ROCKNIX/devices/SM4450/patches/linux/0039-soundwire-qcom-arm-wake-detector-for-clock-stop.patch
  upstream: unknown
- `sm4450-0040-phy-qcom-qmp-combo-add-sm4450.patch`
  source: https://github.com/ROCKNIX/distribution/blob/05efe5552ba5d908a121ae0f2b35dd9e46a46c74/projects/ROCKNIX/devices/SM4450/patches/linux/0040-phy-qcom-qmp-combo-add-sm4450.patch
  upstream: unknown
- `sm4450-0040a-phy-qcom-qmp-combo-use-existing-calibration.patch`
  source: armada
  notes: Present in armada's series without a PATCHES.md entry.
- `sm4450-0042-phy-qcom-qmp-combo-prevent-pm-runtime-suspend-at-boot.patch`
  source: https://github.com/ROCKNIX/distribution/blob/05efe5552ba5d908a121ae0f2b35dd9e46a46c74/projects/ROCKNIX/devices/SM4450/patches/linux/0042-phy-qcom-qmp-combo-prevent-pm-runtime-suspend-at-boot.patch
  upstream: unknown
- `sm4450-0045-ath10k-use-soc-serial.patch`
  source: https://github.com/ROCKNIX/distribution/blob/05efe5552ba5d908a121ae0f2b35dd9e46a46c74/projects/ROCKNIX/devices/SM4450/patches/linux/0045-drivers-use-soc-serial-for-wifi-and-bluetooth.patch
  upstream: unknown
  notes: Carries only the ath10k delta; Armada's existing patch carries the shared Bluetooth and SoC changes.
- `sm4450-0046-bluetooth-hci_qca-include-wcn3950-in-wcn-family-switches.patch`
  source: https://github.com/ROCKNIX/distribution/blob/05efe5552ba5d908a121ae0f2b35dd9e46a46c74/projects/ROCKNIX/devices/SM4450/patches/linux/0046-bluetooth-hci_qca-include-wcn3950-in-wcn-family-switches.patch
  upstream: unknown
- `sm4450-0047-bluetooth-hci_qca-drop-baudrate-vendor-event-for-wcn3950.patch`
  source: https://github.com/ROCKNIX/distribution/blob/05efe5552ba5d908a121ae0f2b35dd9e46a46c74/projects/ROCKNIX/devices/SM4450/patches/linux/0047-bluetooth-hci_qca-drop-baudrate-vendor-event-for-wcn3950.patch
  upstream: unknown
- `sm4450-0048-bluetooth-hci_qca-keep-ibs-disabled-for-wcn3950.patch`
  source: https://github.com/ROCKNIX/distribution/blob/05efe5552ba5d908a121ae0f2b35dd9e46a46c74/projects/ROCKNIX/devices/SM4450/patches/linux/0048-bluetooth-hci_qca-keep-ibs-disabled-for-wcn3950.patch
  upstream: unknown
- `sm4450-0049-usb-typec-ucsi_glink-add-sm4450-quirk.patch`
  source: https://github.com/ROCKNIX/distribution/blob/05efe5552ba5d908a121ae0f2b35dd9e46a46c74/projects/ROCKNIX/devices/SM4450/patches/linux/0049-usb-typec-ucsi_glink-add-sm4450-quirk.patch
  upstream: unknown
- `sm4450-0050-drm-panel-add-focaltech-ft7131m.patch`
  source: https://github.com/ROCKNIX/distribution/blob/05efe5552ba5d908a121ae0f2b35dd9e46a46c74/projects/ROCKNIX/devices/SM4450/patches/linux/0050-drm-panel-add-focaltech-ft7131m.patch
  upstream: unknown
  notes: Kconfig and Kbuild context is refreshed for Armada's combined kernel.
- `sm4450-0051-power-supply-qcom_battmgr-allow-setting-the-USB-input-current-limit.patch`
  source: https://github.com/ROCKNIX/distribution/blob/05efe5552ba5d908a121ae0f2b35dd9e46a46c74/projects/ROCKNIX/devices/SM4450/patches/linux/0051-power-supply-qcom_battmgr-allow-setting-the-USB-input-current-limit.patch
  upstream: unknown
- `sm4450-0052-power-supply-qcom_battmgr-report-the-USB-adapter-type.patch`
  source: https://github.com/ROCKNIX/distribution/blob/05efe5552ba5d908a121ae0f2b35dd9e46a46c74/projects/ROCKNIX/devices/SM4450/patches/linux/0052-power-supply-qcom_battmgr-report-the-USB-adapter-type.patch
  upstream: unknown
- `sm4450-0053-input-add-singleadc-joypad.patch`
  source: https://github.com/ROCKNIX/distribution/blob/05efe5552ba5d908a121ae0f2b35dd9e46a46c74/projects/ROCKNIX/devices/SM4450/patches/linux/0053-input-add-singleadc-joypad.patch
  upstream: unknown
  notes: Kconfig and Kbuild context is refreshed for Armada's combined kernel.
- `sm4450-0053a-input-singleadc-joypad-rgb-leds.patch`
  source: https://github.com/batocera-linux/batocera.linux/blob/master/board/batocera/qualcomm/sm4450/linux_patches/0055-bato-singleadc-joypad-rgb-leds.patch
  upstream: unknown
  notes: Adapted to expose the stock RG55G1 MCU lighting attributes needed by Armada RGB; command commits include the required tag and CRC-16/XMODEM.
- `sm4450-0054-power-supply-rename-qcom-battmgr-sysfs.patch`
  source: https://github.com/ROCKNIX/distribution/blob/05efe5552ba5d908a121ae0f2b35dd9e46a46c74/projects/ROCKNIX/devices/SM4450/patches/linux/0054-power-supply-rename-qcom-battmgr-sysfs.patch
  upstream: unknown
  notes: Drops the SM8550 hunk already carried by Armada.
- `sm4450-anbernic-rg55g1.dts`
  source: https://github.com/ROCKNIX/distribution/blob/05efe5552ba5d908a121ae0f2b35dd9e46a46c74/projects/ROCKNIX/devices/SM4450/linux/dts/qcom/sm4450-anbernic-rg55g1.dts
  notes: Imported verbatim from ROCKNIX; SHA-256 `e970b25b2756b140a51738c11b97400ae13ca7f2780bac88d606db253cfc533d`.
- `sm4450-anbernic-rg55g1-touch-orientation.patch` (armada `dts/sm4450-anbernic-rg55g1.dts.patch`)
  source: armada
  notes: Inverts both touchscreen axes to match the displayed panel orientation.
