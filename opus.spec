%define	major	0
%define libname	%mklibname %{name} %major
%define devname	%mklibname -d %{name}

Summary:	Opus Interactive Audio Codec
Name:		opus
Version:	1.1
Release:	1
License:	BSD
Group:		Sound
Url:		http://opus-codec.org/
Source0:	http://downloads.xiph.org/releases/opus/%{name}-%{version}.tar.gz

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

%package -n	%{devname}
Summary:	Files needed to compile a program with Opus support
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}

%description -n	%{devname}
This package provides the library that implements the Opus codec.

%prep
%setup -q

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std
rm -f %{buildroot}%{_docdir}/opus/doxygen-build.stamp
rm -rf %{buildroot}%{_docdir}/opus

%files -n %{libname}
%{_libdir}/libopus.so.%{major}*

%files -n %{devname}
%doc COPYING README
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/aclocal/opus.m4

