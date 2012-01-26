Summary:	Prosilica GigE Vision Gigabit Ethernet cameras support
Summary(pl.UTF-8):	Obsługa kamer Prosilica GigE Vision podłączanych przez Gigabit Ethernet
Name:		AVT_GigE_SDK
Version:	1.26
Release:	1
License:	non-distributable
Group:		Libraries
Source0:	http://www.alliedvisiontec.com/fileadmin/content/PDF/Software/Prosilica_software/Prosilica_SDK/%{name}_Linux.tgz
# NoSource0-md5:	1caa78c27d069b0fa1adab916433f248
NoSource:	0
URL:		http://www.alliedvisiontec.com/us/products/software/linux/gige-linux-sdk.html
BuildRequires:	wxGTK2-unicode-devel
ExclusiveArch:	%{ix86} %{x8664} arm ppc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# gcc version of static libs (see tarball for available versions)
%define		armgccver	4.4
%define		ppcgccver	4.4
%define		x86gccver	4.5

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

%package viewer
Summary:	wxWidgets-based sample viewer
Summary(pl.UTF-8):	Przeglądarka oparta na wxWidgets
Group:		X11/Applications/Graphics
Requires:	%{name} = %{version}-%{release}

%description viewer
wxWidgets-based sample viewer.

%description viewer -l pl.UTF-8
Przeglądarka oparta na wxWidgets.

%prep
%setup -q -n "AVT GigE SDK"

%build
%ifarch %{ix86}
PLATFORM=x86
%endif
%ifarch %{x8664}
PLATFORM=x64
%endif
%ifarch arm
PLATFORM=arm
%endif
%ifarch ppc
PLATFORM=ppc
%endif
%{__make} -C examples/CLIpConfig sample \
	CPU=$PLATFORM \
	OPT="%{rpmcxxflags}" \
	CC="%{__cxx}"

%{__make} -C examples/SampleViewer sample \
	CPU=$PLATFORM \
	OPT="%{rpmcxxflags}" \
	CC="%{__cxx}" \
	WX_FLAGS="$(wx-gtk2-unicode-config --cxxflags)" \
	WXLIB="$(wx-gtk2-unicode-config --libs)"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_includedir}}

%ifarch %{ix86}
install bin-pc/x86/libPv{API,JNI}.so $RPM_BUILD_ROOT%{_libdir}
install lib-pc/x86/%{x86gccver}/lib*.a $RPM_BUILD_ROOT%{_libdir}
%endif
%ifarch %{x8664}
install bin-pc/x64/libPv{API,JNI}.so $RPM_BUILD_ROOT%{_libdir}
install lib-pc/x64/%{x86gccver}/lib*.a $RPM_BUILD_ROOT%{_libdir}
%endif
%ifarch arm
install bin-pc/arm/libPvAPI.so $RPM_BUILD_ROOT%{_libdir}
install lib-pc/arm/%{armgccver}/lib*.a $RPM_BUILD_ROOT%{_libdir}
%endif
%ifarch ppc
install bin-pc/ppc/libPvAPI.so $RPM_BUILD_ROOT%{_libdir}
install lib-pc/ppc/%{ppcgccver}/lib*.a $RPM_BUILD_ROOT%{_libdir}
%endif
install inc-pc/*.h $RPM_BUILD_ROOT%{_includedir}
install examples/CLIpConfig/CLIpConfig $RPM_BUILD_ROOT%{_bindir}
install examples/SampleViewer/SampleViewer $RPM_BUILD_ROOT%{_bindir}/AVTSampleViewer

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

%files viewer
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/AVTSampleViewer
