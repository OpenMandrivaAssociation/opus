%define	major      	0

%define libname		%mklibname %name %major
%define libnamedev	%mklibname -d %name


Summary:	Opus Interactive Audio Codec
Name:		opus
Version:	0.9.14
Release:	%mkrel 1
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
rmdir %buildroot//usr/share/doc/opus


%files -n %{libname}
%defattr(644,root,root,755)
%doc COPYING README
%{_libdir}/*.so.%{major}*

%files -n %{libnamedev}
%defattr(644,root,root,755)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
