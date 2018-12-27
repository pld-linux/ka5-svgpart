%define		kdeappsver	18.12.0
%define		qtver		5.9.0
%define		kaname		svgpart
Summary:	svgpart
Summary(pl.UTF-8):	svgpart
Name:		ka5-%{kaname}
Version:	18.12.0
Release:	1
License:	GPL v2+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	2fef3bc555371e370e6d7c0819d5fd26
URL:		http://www.kde.org/
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Svg-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= 5.53.0
BuildRequires:	kf5-kcoreaddons-devel >= 5.18.0
BuildRequires:	kf5-kparts-devel >= 5.18.0
BuildRequires:	qt5-build >= 5.5.0
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kpart for viewing SVGs.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/qt5/plugins/svgpart.so
%{_datadir}/kservices5/svgpart.desktop
%dir %{_datadir}/kxmlgui5/svgpart
%{_datadir}/kxmlgui5/svgpart/svgpart.rc
