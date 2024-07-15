Name: lemon-lime
Version: 0.3.4.4
Release: %autorelease
Summary: A tiny judging environment for OI contest based on Lemon + LemonPlus
BuildArch: x86_64
License: GPLv3
URL: https://github.com/Project-LemonLime/Project_LemonLime
Source0: https://github.com/Project-LemonLime/Project_LemonLime/releases/download/%{version}/Lemon-%{version}-source-all.7z
# Add icon to panel
Patch0: panel-icon.patch

BuildRequires:  cmake >= 3.9
BuildRequires:  qt5-qtbase-devel >= 5.11
BuildRequires:  qt5-linguist
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  desktop-file-utils
BuildRequires:  ninja-build

%description
A tiny judging environment for OI contest based on Lemon + LemonPlus

%prep
%setup -c Lemon-%{version}-source-all
cd %{_builddir}/%{name}-%{version}
%patch0 -p1

%build
%cmake -DCMAKE_BUILD_TYPE=Release \
       -GNinja
cd redhat-linux-build
%ninja_build

%install
cd redhat-linux-build
%ninja_install

%files
%license LICENSE
%doc README.md
%{_bindir}/lemon
%{_datadir}/applications/lemon-lime.desktop
%{_datadir}/icons/hicolor
%{_datadir}/metainfo/lemon-lime.metainfo.xml
%{_datadir}/mime/application/x-lemon-contest.xml
%{_includedir}/testlib_for_lemons.h
# %{_datadir}/lemon-lime/lang/*.qm
# %dir %{_datadir}/lemon-lime
# %dir %{_datadir}/lemon-lime/lang
