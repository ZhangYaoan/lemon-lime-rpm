Name: lemon-lime
Version: 0.3.5
Release: %autorelease
Summary: A tiny judging environment for OI contest based on Lemon + LemonPlus
BuildArch: x86_64
License: GPLv3
URL: https://github.com/Project-LemonLime/Project_LemonLime
Source0: https://github.com/Project-LemonLime/Project_LemonLime/releases/download/%{version}/Lemon-%{version}-source-all.7z
# Add icon to panel
Patch0: panel-icon.patch

BuildRequires:  p7zip
BuildRequires:  cmake >= 3.9
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-linguist
BuildRequires:  qt6-qtsvg-devel
BuildRequires:  qt6-qttools-devel
BuildRequires:  desktop-file-utils
BuildRequires:  ninja-build
BuildRequires:  xcb-util-cursor

%description
A tiny judging environment for OI contest based on Lemon + LemonPlus

%prep
%setup -c Lemon-%{version}-source-all
cd %{_builddir}/%{name}-%{version}
%patch 0 -p1
%define INSTALL_PREFIX %{buildroot}/usr
%define BUILD_SOURCE %{_builddir}/%{name}-%{version}
%define BUILD_DIR %{_builddir}/%{name}-%{version}/build

%build
export _LEMON_BUILD_INFO_="LemonLime built by Fedora COPR"
export _LEMON_BUILD_EXTRA_INFO_="(Unofficial Build) $(uname -a | cut -d ' ' -f3,13), Qt $(pkg-config --modversion Qt6Core)"
cmake -S %{BUILD_SOURCE} -B %{BUILD_DIR} \
    -DCMAKE_INSTALL_PREFIX="%{INSTALL_PREFIX}" \
    -DCMAKE_BUILD_TYPE=Release \
    -DLEMON_QT6=ON \
    -GNinja
ninja -C %{BUILD_DIR}

%install
ninja -C %{BUILD_DIR} install

%files
%license LICENSE
%doc README.md
%{_bindir}/lemon
%{_datadir}/applications/lemon-lime.desktop
%{_datadir}/icons/hicolor
%{_datadir}/metainfo/lemon-lime.metainfo.xml
%{_datadir}/mime/application/x-lemon-contest.xml
%{_includedir}/testlib_for_lemons.h
