Name: tg_owt

URL: https://github.com/desktop-app/tg_owt

Version: 0
Release: 1%{?autorelease}

# Library and 3rd-party bundled modules licensing:
# * tg_owt - BSD-3-Clause -- main tarball;
# * base64 - LicenseRef-Fedora-Public-Domain -- static dependency;
# * pffft - BSD-3-Clause -- static dependency;
# * sigslot - LicenseRef-Fedora-Public-Domain -- static dependency;
# * spl_sqrt_floor - LicenseRef-Fedora-Public-Domain -- static dependency.
License:	BSD-3-Clause AND BSD-2-Clause AND Apache-2.0 AND MIT AND LicenseRef-Fedora-Public-Domain
Summary:	WebRTC library for the Telegram Desktop

Source0:	%{name}-%{version}.tar.gz

Patch0:		0001-build-link-against-more-system-libraries-if-possible.patch
#Patch1:		0002-video_capture-fix-compat-for-pipewire-1.3.81.patch

ExcludeArch: s390x

BuildRequires: cmake
BuildRequires: gcc
BuildRequires: gcc-c++

BuildRequires: cmake(absl)
BuildRequires: cmake(Crc32c)

BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(epoxy)
BuildRequires: pkgconfig(gbm)
BuildRequires: pkgconfig(libavcodec)
BuildRequires: pkgconfig(libavfilter)
BuildRequires: pkgconfig(libavformat)
BuildRequires: pkgconfig(libavutil)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(libjpeg)
BuildRequires: pkgconfig(libpipewire-0.3)
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(libswresample)
BuildRequires: pkgconfig(libswscale)
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(opus)
BuildRequires: pkgconfig(vpx)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xcomposite)
BuildRequires: pkgconfig(xdamage)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(xfixes)
BuildRequires: pkgconfig(xrandr)
BuildRequires: pkgconfig(xrender)
BuildRequires: pkgconfig(xtst)
BuildRequires: pkgconfig(libyuv)
BuildRequires: pkgconfig(openh264)
BuildRequires: pkgconfig(libsrtp2)
BuildRequires: pkgconfig(rnnoise)

Provides: bundled(base64) = 0~git%{_shortcommit}
Provides: bundled(fft) = 0~git%{_shortcommit}
Provides: bundled(g711) = 1.1~git%{_shortcommit}
Provides: bundled(g722) = 1.14~git%{_shortcommit}
Provides: bundled(ooura) = 0~git%{_shortcommit}
Provides: bundled(sigslot) = 0~git%{_shortcommit}
Provides: bundled(spl_sqrt_floor) = 0~git%{_shortcommit}

Provides: bundled(pffft) = 0~git483453d

%description
Fork of the OpenWebRTC library used by Telegram Messenger.

%package devel
Summary: Header files and development documentation for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: cmake(Crc32c)
Requires: cmake(absl)
Requires: pkgconfig(libyuv)
Requires: pkgconfig(openh264)

%description devel
Fork of	the OpenWebRTC library used by Telegram Messenger.

This package contains the header files for %{name}.

%prep
%autosetup -p1

mkdir legal
cp -f -p src/third_party/pffft/LICENSE legal/LICENSE.pffft
cp -f -p src/third_party/pffft/README.chromium legal/README.pffft
cp -f -p src/common_audio/third_party/ooura/LICENSE legal/LICENSE.ooura
cp -f -p src/common_audio/third_party/ooura/README.chromium legal/README.ooura
cp -f -p src/common_audio/third_party/spl_sqrt_floor/LICENSE legal/LICENSE.spl_sqrt_floor
cp -f -p src/common_audio/third_party/spl_sqrt_floor/README.chromium legal/README.spl_sqrt_floor
cp -f -p src/modules/third_party/fft/LICENSE legal/LICENSE.fft
cp -f -p src/modules/third_party/fft/README.chromium legal/README.fft
cp -f -p src/modules/third_party/g711/LICENSE legal/LICENSE.g711
cp -f -p src/modules/third_party/g711/README.chromium legal/README.g711
cp -f -p src/modules/third_party/g722/LICENSE legal/LICENSE.g722
cp -f -p src/modules/third_party/g722/README.chromium legal/README.g722
cp -f -p src/rtc_base/third_party/base64/LICENSE legal/LICENSE.base64
cp -f -p src/rtc_base/third_party/base64/README.chromium legal/README.base64
cp -f -p src/rtc_base/third_party/sigslot/LICENSE legal/LICENSE.sigslot
cp -f -p src/rtc_base/third_party/sigslot/README.chromium legal/README.sigslot

%build
# CMAKE_BUILD_TYPE should always be Release due to some hardcoded checks.
%cmake -DCMAKE_BUILD_TYPE=Release \
  -DTG_OWT_USE_PROTOBUF:BOOL=ON \
  -DTG_OWT_PACKAGED_BUILD:BOOL=ON \
  -DTG_OWT_DLOPEN_PIPEWIRE:BOOL=OFF
%cmake_build

%install
%cmake_install

%files
%doc src/AUTHORS src/OWNERS legal/README.*
%license LICENSE src/PATENTS legal/LICENSE.*
%{_libdir}/lib%{name}.so.0*

%files devel
%doc src/AUTHORS src/OWNERS legal/README.*
%license LICENSE src/PATENTS legal/LICENSE.*
%{_includedir}/%{name}
%{_libdir}/cmake/%{name}
%{_libdir}/lib%{name}.so

%changelog

