# TODO: build SampleViewer from sources? (using dynamic wxWidgets)
Summary:	Prosilica GigE Vision Gigabit Ethernet cameras support
Summary(pl.UTF-8):	Obsługa kamer Prosilica GigE Vision podłączanych przez Gigabit Ethernet
Name:		AVT_GigE_SDK
Version:	1.24
Release:	1
License:	non-distributable
Group:		Libraries
Source0:	http://www.alliedvisiontec.com/fileadmin/content/PDF/Software/Prosilica_software/Prosilica_SDK/%{name}_%{version}_Linux.tgz
# NoSource0-md5:	f7e895aae4e8b2f0ca3cc72a2351bf70
NoSource:	0
URL:		http://www.alliedvisiontec.com/us/products/software/linux/gige-linux-sdk.html
ExclusiveArch:	%{ix86} %{x8664} arm ppc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# gcc version of static libs (see tarball for available versions)
%define		ppcgccver	4.2
%define		x86gccver	4.4

%description
The Linux SDK and Sample Viewer program allows users to control and
capture images from Prosilica's GigE Vision Gigabit Ethernet cameras
operating in a Linux environment on either an Intel x86 (32- and
64-bit), PowerPC (32-bit), and ARM processors (little endian). The SDK
includes sample code to allow programmers to integrate Prosilica's
cameras into their Linux-based applications.

%description -l pl.UTF-8
Linux SDK i program Sample Viewer pozwala na sterowanie oraz
przechwytywanie obrazu z kamer Prosilica GigE Vision podłączanych
przez Gigabit Ethernet w środowisku Linux na procesorach Intel x86
(32- i 64-bitowych), PowerPC (32-bitowych) oraz ARM (little endian).
SDK zawiera przykładowy kod pozwalający zintegrować kamery firmy
Prosilica ze swoimi linuksowymi aplikacjami.

%package devel
Summary:	AVT GigE SDK/PvAPI development package
Summary(pl.UTF-8):	Pakiet programistyczny AVT GigE SDK/PvAPI
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
AVT GigE SDK development package, containing PvAPI and Imagelib header
files and static Imagelib library.

%description devel -l pl.UTF-8
Pakiet programistyczny AVT GigE SDK, zawierający pliki nagłówkowe
PvAPI i Imagelib oraz statyczną bibliotekę Imagelib.

%package static
Summary:	Static PvAPI library
Summary(pl.UTF-8):	Statyczna biblioteka PvAPI
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static PvAPI library.

%description static -l pl.UTF-8
Statyczna biblioteka PvAPI.

%prep
%setup -q -n "AVT GigE SDK"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_includedir}}

%ifarch %{ix86}
install bin-pc/x86/{CLIpConfig,SampleViewer} $RPM_BUILD_ROOT%{_bindir}
install bin-pc/x86/libPv{API,JNI}.so $RPM_BUILD_ROOT%{_libdir}
install lib-pc/x86/%{x86gccver}/lib*.a $RPM_BUILD_ROOT%{_libdir}
%endif
%ifarch %{x8664}
install bin-pc/x64/{CLIpConfig,SampleViewer} $RPM_BUILD_ROOT%{_bindir}
install bin-pc/x64/libPv{API,JNI}.so $RPM_BUILD_ROOT%{_libdir}
install lib-pc/x64/%{x86gccver}/lib*.a $RPM_BUILD_ROOT%{_libdir}
%endif
%ifarch arm
install bin-pc/arm/CLIpConfig $RPM_BUILD_ROOT%{_bindir}
install bin-pc/arm/libPvAPI.so $RPM_BUILD_ROOT%{_libdir}
install lib-pc/arm/3.3.5/lib*.a $RPM_BUILD_ROOT%{_libdir}
%endif
%ifarch ppc
install bin-pc/ppc/CLIpConfig $RPM_BUILD_ROOT%{_bindir}
install bin-pc/ppc/libPvAPI.so $RPM_BUILD_ROOT%{_libdir}
install lib-pc/ppc/%{ppcgccver}/lib*.a $RPM_BUILD_ROOT%{_libdir}
%endif
install inc-pc/*.h $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.txt
%attr(755,root,root) %{_bindir}/CLIpConfig
%attr(755,root,root) %{_libdir}/libPvAPI.so
%ifarch %{ix86} %{x8664}
%attr(755,root,root) %{_bindir}/SampleViewer
%attr(755,root,root) %{_libdir}/libPvJNI.so
%endif

%files devel
%defattr(644,root,root,755)
%doc documents/AVT*.pdf
# static-only
%{_libdir}/libImagelib.a
%{_includedir}/ImageLib.h
%{_includedir}/PvApi.h
%{_includedir}/PvRegIo.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libPvAPI.a
