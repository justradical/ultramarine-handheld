Name:           kernel-rg55g1
Version:        7.2.6
Release:        1.rg55g1%{?dist}
Summary:        Fedora-style alternate mainline kernel for the Anbernic RG 55G1
License:        GPL-2.0-only
URL:            https://github.com/torvalds/linux
Source0:        https://cdn.kernel.org/pub/linux/kernel/v7.x/linux-%{version}.tar.xz
# Board device tree and its armada DTS delta, from JPyke3/armada feat-rg55g1
# (2862ae96da5493b35365ab692c81e11d7ada1fa2). See PATCHES.md.
Source1:        sm4450-anbernic-rg55g1.dts
Source2:        sm4450-anbernic-rg55g1-touch-orientation.patch
Source1000:     rg55g1.config
Source1001:     required.config

# The SM4450 bring-up series and the armada/ROCKNIX patches it is rebased on,
# in armada's series order. Provenance for every entry is in PATCHES.md.
Patch1001: 0004-drm-msm-a6xx-Enable-IFPC-on-Adreno-740.patch
Patch1002: 0010-msm-resource-cleanup.patch
Patch1003: 0048-drm-msm-dsi-reparent-byte-pixel-src-to-xo-on-disable.patch
Patch1004: 0048a-drm-msm-dsi-round-byte-clock-rate-after-reparenting-to-PLL.patch
Patch1005: 0066-drm-msm-dpu-enable-inline-rotation.patch
Patch1006: 0068-drm-msm-dpu-lutdma-dspp-igc-gamut.patch
Patch1007: 1006-tty-serial-qcom-geni-mask-non-console-irq-on-suspend.patch
Patch1008: 0036_ASoC--qcom--sc8280xp-Add-support-for-Primary-I2S.patch
Patch1009: 0032-ASoC-codecs-aw88166-AYN-Products-Specific-modificati.patch
Patch1010: 0505-msm_gem-lock-before-put_iova_spaces.patch
Patch1011: 0204-thermal-qcom-tsens-mask-lower-threshold-irqs-across-suspend.patch
Patch1012: 0121-pmdomain-qcom-rpmhpd-presync-floor-gmu-rails.patch
Patch1013: 0501-ROCKNIX-fix-wifi-and-bt-mac.patch
Patch1014: 0503-ROCKNIX-battery-name.patch
Patch1015: 0901-power-supply-qcom-battmgr-fix-charge-unit.patch
Patch1016: 0902-power-supply-qcom-battmgr-expose-charge-now.patch
Patch1017: sm4450-0001-drm-msm-adreno-add-a613-catalog-entry.patch
Patch1018: sm4450-0002-pmdomain-qcom-rpmhpd-add-lcx-for-sm4450.patch
Patch1019: sm4450-0003-remoteproc-qcom-pas-add-sm4450-adsp-wpss.patch
Patch1020: sm4450-0004-regulator-qcom-rpmh-add-pm6450.patch
Patch1021: sm4450-0005-soc-qcom-pd-mapper-add-sm4450.patch
Patch1022: sm4450-0006-interconnect-qcom-add-sm4450.patch
Patch1023: sm4450-0008-iommu-arm-smmu-qcom-add-sm4450.patch
Patch1024: sm4450-0009-drm-msm-add-sm4450-display.patch
Patch1025: sm4450-0009a-drm-msm-dpu-rename-sm4450-rotation-formats.patch
Patch1026: sm4450-0009b-drm-msm-dpu-allow-argb8888-inline-rotation.patch
Patch1027: sm4450-0011-clk-qcom-dispcc-sm4450-fix-mdp-clk-src-ops.patch
Patch1028: sm4450-0012-clk-qcom-dispcc-sm4450-quiesce-splash.patch
Patch1029: sm4450-0013-clk-qcom-gpucc-sm4450-add-hlos1-vote-gpu-smmu.patch
Patch1030: sm4450-0014-clk-qcom-gpucc-sm4450-enable-gx-gdsc.patch
Patch1031: sm4450-0015-drm-msm-a6xx-avoid-gmu-cx-reads-on-a613.patch
Patch1032: sm4450-0017-clk-qcom-gpucc-sm4450-fix-gfx3d-rcg-ops.patch
Patch1033: sm4450-0018-clk-qcom-gpucc-sm4450-retain-gx-gdsc-regs.patch
Patch1034: sm4450-0019-drm-msm-dpu-stop-boot-scanout.patch
Patch1035: sm4450-0022-regulator-qcom-rpmh-add-pbs-type.patch
Patch1036: sm4450-0023-leds-qcom-lpg-add-pm6450-pwm.patch
Patch1037: sm4450-0024-serial-qcom-geni-restart-terminated-rx-command.patch
Patch1038: sm4450-0030-ASoC-qcom-sc8280xp-i2s-clk-support.patch
Patch1039: sm4450-0031-ASoC-codecs-aw88166-support-changing-sample-rate-and-bit-width.patch
Patch1040: sm4450-0032-ASoC-codecs-aw88166-reduce-log-spam.patch
Patch1041: sm4450-0033-ASoC-codecs-aw88166-remove-fade-in-out-on-start-stop.patch
Patch1042: sm4450-0034-ASoC-codecs-aw88166-make-volume-control-usable.patch
Patch1043: sm4450-0035-ASoC-codecs-aw88166-drop-duplicate-dai-stubs.patch
Patch1044: sm4450-0039-soundwire-qcom-arm-wake-detector-for-clock-stop.patch
Patch1045: sm4450-0040-phy-qcom-qmp-combo-add-sm4450.patch
Patch1046: sm4450-0040a-phy-qcom-qmp-combo-use-existing-calibration.patch
Patch1047: sm4450-0042-phy-qcom-qmp-combo-prevent-pm-runtime-suspend-at-boot.patch
Patch1048: sm4450-0045-ath10k-use-soc-serial.patch
Patch1049: sm4450-0046-bluetooth-hci_qca-include-wcn3950-in-wcn-family-switches.patch
Patch1050: sm4450-0047-bluetooth-hci_qca-drop-baudrate-vendor-event-for-wcn3950.patch
Patch1051: sm4450-0048-bluetooth-hci_qca-keep-ibs-disabled-for-wcn3950.patch
Patch1052: sm4450-0049-usb-typec-ucsi_glink-add-sm4450-quirk.patch
Patch1053: sm4450-0050-drm-panel-add-focaltech-ft7131m.patch
Patch1054: sm4450-0051-power-supply-qcom_battmgr-allow-setting-the-USB-input-current-limit.patch
Patch1055: sm4450-0052-power-supply-qcom_battmgr-report-the-USB-adapter-type.patch
Patch1056: sm4450-0053-input-add-singleadc-joypad.patch
Patch1057: sm4450-0053a-input-singleadc-joypad-rgb-leds.patch
Patch1058: sm4450-0054-power-supply-rename-qcom-battmgr-sysfs.patch

%global krel %{version}-rg55g1
%global dtb qcom/sm4450-anbernic-rg55g1.dtb
%global debug_package %{nil}
%global _binary_payload w3T.xzdio
%global _lto_cflags %{nil}
%global _disable_source_fetch 0
%undefine _include_frame_pointers

Provides:       kernel = %{version}-%{release}

BuildRequires:  bash
BuildRequires:  bc
BuildRequires:  binutils
BuildRequires:  bison
BuildRequires:  curl
BuildRequires:  dtc
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  gcc-aarch64-linux-gnu
BuildRequires:  gcc-c++
BuildRequires:  kmod
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  patch
BuildRequires:  perl-interpreter
BuildRequires:  python3
BuildRequires:  tar
BuildRequires:  elfutils-libelf-devel

%description
A Fedora-style alternate kernel package for the Anbernic RG 55G1 (Qualcomm
SM4450). The package applies the RG55G1 SM4450 bring-up series from armada
through RPM Patch preambles, builds the matched arm64 kernel and modules, and
installs normal Fedora-compatible kernel paths for EFI/systemd-boot.

%package core
Summary:        Core files for the RG55G1 alternate kernel
Requires:       %{name} = %{version}-%{release}
Provides:       kernel-core = %{version}-%{release}
Provides:       kernel-uname-r = %{krel}
Provides:       kernel-core-uname-r = %{krel}

%description core
The bootable Image, board device tree, and built-in kernel metadata for the
RG55G1 alternate kernel.

%package modules
Summary:        Loadable modules for the RG55G1 alternate kernel
Requires:       %{name}-core = %{version}-%{release}
Provides:       kernel-modules = %{version}-%{release}
Provides:       kernel-modules-uname-r = %{krel}

%description modules
Loadable kernel modules for the RG55G1 alternate kernel.

%prep
%autosetup -n linux-%{version} -p1
install -m 0644 %{SOURCE1} arch/arm64/boot/dts/qcom/sm4450-anbernic-rg55g1.dts
patch -p1 --fuzz=0 --no-backup-if-mismatch < %{SOURCE2}
printf '%s\n' 'dtb-$(CONFIG_ARCH_QCOM) += sm4450-anbernic-rg55g1.dtb' >> arch/arm64/boot/dts/qcom/Makefile
cp %{SOURCE1000} rg55g1.config
cp %{SOURCE1001} required.config

%global make %{__make} %{_make_output_sync} %{?_smp_mflags} %{?_make_verbose} CC="$CC" CXX="$CXX" HOSTCC="${HOSTCC:-gcc}" HOSTCXX="${HOSTCXX:-g++}" CROSS_COMPILE="${CROSS_COMPILE-}"
%build
export ARCH=arm64
export KBUILD_BUILD_USER=ultramarine
export KBUILD_BUILD_HOST=rg55g1-builder
export KBUILD_BUILD_TIMESTAMP="${SOURCE_DATE_EPOCH}"
%{make} defconfig
./scripts/kconfig/merge_config.sh -m .config rg55g1.config required.config
scripts/config --set-str CONFIG_LOCALVERSION "-rg55g1"
%{make} olddefconfig
# merge_config.sh only warns when Kconfig dependencies demote a request. Fail
# instead, so a boot-critical =y can never silently become =m or vanish.
fail=0
while IFS='=' read -r symbol value; do
    actual=$(sed -n "s/^${symbol}=//p" .config)
    if [ "$actual" != "$value" ]; then
        echo "config mismatch: ${symbol} requested ${value}, got ${actual:-unset}" >&2
        fail=1
    fi
done < <(grep -hE '^CONFIG_[A-Z0-9_]+=' rg55g1.config required.config)
test "$fail" -eq 0
%{make} Image modules %{dtb}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/lib/modules/%{krel}/dtb/qcom
test "$(make -s kernelrelease)" = "%{krel}"
install -m 0644 arch/arm64/boot/Image %{buildroot}/usr/lib/modules/%{krel}/vmlinuz
install -m 0644 .config %{buildroot}/usr/lib/modules/%{krel}/config
install -m 0644 System.map %{buildroot}/usr/lib/modules/%{krel}/System.map
install -m 0644 arch/arm64/boot/dts/%{dtb} %{buildroot}/usr/lib/modules/%{krel}/dtb/%{dtb}
make modules_install KERNELRELEASE="%{krel}" INSTALL_MOD_PATH=%{buildroot}/usr INSTALL_MOD_STRIP=
depmod -b %{buildroot} -m /usr/lib/modules %{krel}
rm -f %{buildroot}/usr/lib/modules/%{krel}/build %{buildroot}/usr/lib/modules/%{krel}/source

%files

%files core
/usr/lib/modules/%{krel}/vmlinuz
/usr/lib/modules/%{krel}/config
/usr/lib/modules/%{krel}/System.map
/usr/lib/modules/%{krel}/modules.builtin*
/usr/lib/modules/%{krel}/modules.order
/usr/lib/modules/%{krel}/modules.softdep
/usr/lib/modules/%{krel}/modules.symbols*
%dir /usr/lib/modules/%{krel}
%dir /usr/lib/modules/%{krel}/dtb
%dir /usr/lib/modules/%{krel}/dtb/qcom
/usr/lib/modules/%{krel}/dtb/%{dtb}

%files modules
/usr/lib/modules/%{krel}/kernel
/usr/lib/modules/%{krel}/modules.alias*
/usr/lib/modules/%{krel}/modules.dep*
/usr/lib/modules/%{krel}/modules.devname
/usr/lib/modules/%{krel}/modules.weakdep

%changelog
* Sun Sep 27 2026 Radical <radical@radical.fun> - 7.2.6-1.rg55g1
- Initial RG55G1 kernel: Linux 7.2.6 with the SM4450 bring-up series from
  JPyke3/armada feat-rg55g1, packaged for EFI/systemd-boot.
