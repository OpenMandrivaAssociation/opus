%define major 0
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d
# Set to alpha, beta, rc or %{nil} for stable
%define pre %{nil}

Summary:	Opus Interactive Audio Codec
Name:		opus
Version:	1.1.3
%if "%{pre}" != ""
Release:	0.%{pre}.1
Source0:	http://downloads.xiph.org/releases/opus/%{name}-%{version}-%{pre}.tar.gz
%else
Release:	3
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
%{_mandir}/man3/opus_*.3*

#----------------------------------------------------------------------------

%prep
%if "%{pre}" != ""
%setup -qn %{name}-%{version}-%{pre}
%else
%setup -q
%endif

%build
%configure2_5x \
	--disable-static \
	--enable-custom-modes
%make

%install
%makeinstall_std
rm -f %{buildroot}%{_docdir}/opus/doxygen-build.stamp
rm -rf %{buildroot}%{_docdir}/opus

