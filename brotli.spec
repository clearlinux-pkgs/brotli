#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : brotli
Version  : 1.0.9
Release  : 14
URL      : https://github.com/google/brotli/archive/v1.0.9/brotli-1.0.9.tar.gz
Source0  : https://github.com/google/brotli/archive/v1.0.9/brotli-1.0.9.tar.gz
Summary  : Brotli encoder library
Group    : Development/Tools
License  : MIT
Requires: brotli-bin = %{version}-%{release}
Requires: brotli-lib = %{version}-%{release}
Requires: brotli-license = %{version}-%{release}
Requires: brotli-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-distutils3
Patch1: 0001-Revert-Add-runtime-linker-path-to-pkg-config-files-7.patch

%description
BROTLI DATA COMPRESSION LIBRARY
Brotli is a generic-purpose lossless compression algorithm that compresses data
using a combination of a modern variant of the LZ77 algorithm, Huffman coding
and 2nd order context modeling, with a compression ratio comparable to the best
currently available general-purpose compression methods. It is similar in speed
with deflate but offers more dense compression.

%package bin
Summary: bin components for the brotli package.
Group: Binaries
Requires: brotli-license = %{version}-%{release}

%description bin
bin components for the brotli package.


%package dev
Summary: dev components for the brotli package.
Group: Development
Requires: brotli-lib = %{version}-%{release}
Requires: brotli-bin = %{version}-%{release}
Provides: brotli-devel = %{version}-%{release}
Requires: brotli = %{version}-%{release}

%description dev
dev components for the brotli package.


%package lib
Summary: lib components for the brotli package.
Group: Libraries
Requires: brotli-license = %{version}-%{release}

%description lib
lib components for the brotli package.


%package license
Summary: license components for the brotli package.
Group: Default

%description license
license components for the brotli package.


%package man
Summary: man components for the brotli package.
Group: Default

%description man
man components for the brotli package.


%package staticdev
Summary: staticdev components for the brotli package.
Group: Default
Requires: brotli-dev = %{version}-%{release}

%description staticdev
staticdev components for the brotli package.


%prep
%setup -q -n brotli-1.0.9
cd %{_builddir}/brotli-1.0.9
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1646334311
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1646334311
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/brotli
cp %{_builddir}/brotli-1.0.9/LICENSE %{buildroot}/usr/share/package-licenses/brotli/c045813a6c514f2d30d60a07c6aaf3603850e608
pushd clr-build
%make_install
popd
## install_append content
install -d %{buildroot}/usr/share/man/man{1,3}
install -pm0644 docs/*.1 %{buildroot}/usr/share/man/man1
install -pm0644 docs/*.3 %{buildroot}/usr/share/man/man3
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/brotli

%files dev
%defattr(-,root,root,-)
/usr/include/brotli/decode.h
/usr/include/brotli/encode.h
/usr/include/brotli/port.h
/usr/include/brotli/types.h
/usr/lib64/libbrotlicommon.so
/usr/lib64/libbrotlidec.so
/usr/lib64/libbrotlienc.so
/usr/lib64/pkgconfig/libbrotlicommon.pc
/usr/lib64/pkgconfig/libbrotlidec.pc
/usr/lib64/pkgconfig/libbrotlienc.pc
/usr/share/man/man3/constants.h.3
/usr/share/man/man3/decode.h.3
/usr/share/man/man3/encode.h.3
/usr/share/man/man3/types.h.3

%files lib
%defattr(-,root,root,-)
/usr/lib64/libbrotlicommon.so.1
/usr/lib64/libbrotlicommon.so.1.0.9
/usr/lib64/libbrotlidec.so.1
/usr/lib64/libbrotlidec.so.1.0.9
/usr/lib64/libbrotlienc.so.1
/usr/lib64/libbrotlienc.so.1.0.9

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/brotli/c045813a6c514f2d30d60a07c6aaf3603850e608

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/brotli.1

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libbrotlicommon-static.a
/usr/lib64/libbrotlidec-static.a
/usr/lib64/libbrotlienc-static.a
