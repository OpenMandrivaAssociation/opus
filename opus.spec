%define	major		0

%define libname		%mklibname %name %major
%define libnamedev	%mklibname -d %name


Summary:	Opus Interactive Audio Codec
Name:		opus
Version:	1.0.2
Release:	1
Source0:	http://downloads.xiph.org/releases/opus/%{name}-%{version}.tar.gz
URL:		http://opus-codec.org/
License:	BSD
Group:		Sound

%description
The Opus codec is designed for interactive speech and audio transmission over
the Internet. It is designed by the IETF Codec Working Group and incorporates
technology from Skype's SILK codec and Xiph.Org's CELT codec. 

%package -n	%{libname}
Summary:	Opus library
Group:		System/Libraries

%description -n	%{libname}
This package provides the library that implements the Opus codec.
The Opus codec is designed for interactive speech and audio transmission over
the Internet. It is designed by the IETF Codec Working Group and incorporates
technology from Skype's SILK codec and Xiph.Org's CELT codec. 

%package -n	%{libnamedev}
Summary:	Files needed to compile a program with Opus support
Group:		Development/C
Requires:	%{libname} = %version

%description -n	%{libnamedev}
This package provides the library that implements the Opus codec.

%prep
%setup -q

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std
rm -f %buildroot//usr/share/doc/opus/doxygen-build.stamp
rm -rf %buildroot//usr/share/doc/opus


%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{libnamedev}
%doc COPYING README
%{_includedir}/*
%{_libdir}/*.so
#% {_mandir}/man3/*.xz
%{_libdir}/pkgconfig/*.pc
%{_datadir}/aclocal/opus.m4
