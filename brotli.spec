#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v20
# autospec commit: 4d029647d79e
#
%define keepstatic 1
Name     : brotli
Version  : 1.0.9
Release  : 19
URL      : https://github.com/google/brotli/archive/v1.0.9/brotli-1.0.9.tar.gz
Source0  : https://github.com/google/brotli/archive/v1.0.9/brotli-1.0.9.tar.gz
Summary  : Brotli common dictionary library
Group    : Development/Tools
License  : MIT
Requires: brotli-bin = %{version}-%{release}
Requires: brotli-lib = %{version}-%{release}
Requires: brotli-license = %{version}-%{release}
Requires: brotli-man = %{version}-%{release}
BuildRequires : buildreq-cmake
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
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
%patch -P 1 -p1
pushd ..
cp -a brotli-1.0.9 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1728611053
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1728611053
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/brotli
cp %{_builddir}/brotli-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/brotli/c045813a6c514f2d30d60a07c6aaf3603850e608 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
## install_append content
install -d %{buildroot}/usr/share/man/man{1,3}
install -pm0644 docs/*.1 %{buildroot}/usr/share/man/man1
install -pm0644 docs/*.3 %{buildroot}/usr/share/man/man3
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/brotli
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
/V3/usr/lib64/libbrotlicommon.so.1.0.9
/V3/usr/lib64/libbrotlidec.so.1.0.9
/V3/usr/lib64/libbrotlienc.so.1.0.9
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
