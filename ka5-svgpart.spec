#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	23.08.1
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		svgpart
Summary:	svgpart
Summary(pl.UTF-8):	svgpart
Name:		ka5-%{kaname}
Version:	23.08.1
Release:	1
License:	GPL v2+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	9849809e8fcb4fa3b7db4e63cebd3902
URL:		http://www.kde.org/
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Svg-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf5-kparts-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt5-build >= 5.5.0
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kpart for viewing SVGs.

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

# not supported by glibc yet
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ie

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/parts/svgpart.so
%{_datadir}/kservices5/svgpart.desktop
%{_datadir}/metainfo/org.kde.svgpart.metainfo.xml
