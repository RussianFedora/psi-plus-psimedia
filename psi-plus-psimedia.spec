%define rev 20110530svn3956
Name:           psi-plus-psimedia
Version:        1.0.3
Release:        1.%{rev}%{?dist}
Summary:        Audio and video RTP services for Psi+

Group:          Applications/Internet
License:        LGPLv2+
URL:            http://delta.affinix.com/psimedia/
Source0:        http://koji.russianfedora.ru/storage/psi-plus/%{name}-%{version}-20110530svn3956.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  qt-devel
BuildRequires:  gstreamer-plugins-base-devel >= 0.10.22
BuildRequires:  liboil-devel >= 0.3
BuildRequires:  speex-devel
BuildRequires:  qconf >= 1.4-2
Requires:       psi-plus > 0.15-0.17.20110119svn3559

%description
PsiMedia is a thick abstraction layer for providing audio and
video RTP services to Psi-like IM clients. The implementation
is based on GStreamer.

The modified version from psi-dev team.

%prep
%setup -q -n %{name}-%{version}-%{rev}


%build
qconf-qt4
./configure
make %{?_smp_mflags}


%install
install -D -m 755 gstprovider/libgstprovider.so $RPM_BUILD_ROOT%{_libdir}/psi-plus/plugins/libgstprovider.so

%files
%defattr(-,root,root,-)
%{_libdir}/psi-plus/plugins/libgstprovider.so

%changelog
* Mon May 30 2011 Ivan Romanov <drizt@land.ru> - 1.0.3-0.1.20110530svn3956
- initial version of package
