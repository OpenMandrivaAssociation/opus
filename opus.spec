# Opus is used by jackit, jackit is used by pulseaudio,
# pulseaudio is used by wine
%ifarch %{x86_64}
%bcond_without compat32
%endif

%define major 0
%define oldlibname %mklibname %{name} 0
%define libname %mklibname %{name}
%define devname %mklibname %{name} -d
%define oldlib32name %mklib32name %{name} 0
%define lib32name %mklib32name %{name}
%define dev32name %mklib32name %{name} -d
# Set to alpha, beta, rc or %{nil} for stable
%define pre %{nil}

%global optflags %optflags -O3

Summary:	Opus Interactive Audio Codec
Name:		opus
Version:	1.5.1
%if "%{pre}" != ""
Release:	0.%{pre}.1
Source0:	http://archive.mozilla.org/pub/opus/%{name}-%{version}-%{pre}.tar.gz
%else
Release:	6
Source0:	http://downloads.xiph.org/releases/opus/%{name}-%{version}.tar.gz
%endif
License:	BSD
Group:		Sound
Url:		http://opus-codec.org/
BuildRequires:	doxygen

%description
The Opus codec is designed for interactive speech and audio transmission over
the Internet. It is designed by the IETF Codec Working Group and incorporates
technology from Skype's SILK codec and Xiph.Org's CELT codec.

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Opus shared library
Group:		System/Libraries
%rename %{oldlibname}

%description -n %{libname}
This package provides the library that implements the Opus codec.
The Opus codec is designed for interactive speech and audio transmission over
the Internet. It is designed by the IETF Codec Working Group and incorporates
technology from Skype's SILK codec and Xiph.Org's CELT codec.

%files -n %{libname}
%{_libdir}/libopus.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Files needed to compile a program with Opus support
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
This package provides the library that implements the Opus codec.

%files -n %{devname}
%doc COPYING README
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/aclocal/opus.m4

#----------------------------------------------------------------------------
%if %{with compat32}
%package -n %{lib32name}
Summary:	Opus shared library (32-bit)
Group:		System/Libraries
%rename %{oldlib32name}

%description -n %{lib32name}
This package provides the library that implements the Opus codec.
The Opus codec is designed for interactive speech and audio transmission over
the Internet. It is designed by the IETF Codec Working Group and incorporates
technology from Skype's SILK codec and Xiph.Org's CELT codec.

%files -n %{lib32name}
%{_prefix}/lib/libopus.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{dev32name}
Summary:	Files needed to compile a program with Opus support (32-bit)
Group:		Development/C
Requires:	%{devname} = %{EVRD}
Requires:	%{lib32name} = %{EVRD}

%description -n %{dev32name}
This package provides the library that implements the Opus codec.

%files -n %{dev32name}
%{_prefix}/lib/*.so
%{_prefix}/lib/pkgconfig/*.pc
%endif

%prep
%if "%{pre}" != ""
%autosetup -p1 -n %{name}-%{version}-%{pre}
%else
%autosetup -p1
%endif

export CONFIGURE_TOP="$(pwd)"
%if %{with compat32}
mkdir build32
cd build32
%configure32 \
	--enable-custom-modes \
	--enable-hardening \
	--disable-doc

cd ..
%endif

mkdir build
cd build
%configure \
	--enable-custom-modes \
	--enable-hardening \
	--disable-doc


%build
%if %{with compat32}
%make_build -C build32
%endif
%make_build -C build

%install
%if %{with compat32}
%make_install -C build32
%endif
%make_install -C build


find %{buildroot} -type f -name "*.la" -delete
