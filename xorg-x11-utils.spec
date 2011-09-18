%define pkgname utils

Summary: X.Org X11 X client utilities
Name: xorg-x11-%{pkgname}
Version: 7.4
Release: 8%{?dist}
License: MIT
Group: User Interface/X
URL: http://www.x.org
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:  ftp://ftp.x.org/pub/individual/app/xdpyinfo-1.0.3.tar.bz2
Source2:  ftp://ftp.x.org/pub/individual/app/xev-1.0.4.tar.bz2
Source5:  ftp://ftp.x.org/pub/individual/app/xlsatoms-1.0.2.tar.bz2
Source6:  ftp://ftp.x.org/pub/individual/app/xlsclients-1.0.1.tar.bz2
Source7:  ftp://ftp.x.org/pub/individual/app/xlsfonts-1.0.2.tar.bz2
Source8:  ftp://ftp.x.org/pub/individual/app/xprop-1.1.0.tar.bz2
Source9:  ftp://ftp.x.org/pub/individual/app/xvinfo-1.0.2.tar.bz2
Source10: ftp://ftp.x.org/pub/individual/app/xwininfo-1.0.5.tar.bz2

Source100: edid-decode-20100611.tar.xz
Source101: make-edid-decode-snapshot.sh

BuildRequires: pkgconfig(dmx) pkgconfig(gl) pkgconfig(xext) pkgconfig(xft)
BuildRequires: pkgconfig(xi) pkgconfig(xinerama) pkgconfig(xmu)
BuildRequires: pkgconfig(xpm) pkgconfig(xt) pkgconfig(xtst) pkgconfig(xv)
BuildRequires: pkgconfig(xxf86dga) pkgconfig(xxf86misc) pkgconfig(xxf86vm)

Provides: xdpyinfo xev xlsatoms xlsclients xlsfonts xprop xvinfo xwininfo
Provides: edid-decode

%description
A collection of client utilities which can be used to query the X server
for various information.

%prep
%setup -q -c %{name}-%{version} -a2 -a5 -a6 -a7 -a8 -a9 -a10 -a100

%build
# Build all apps
{
   for app in * ; do
      pushd $app
      if [ -e ./configure ] ; then
        %configure
      fi
      make
      popd
   done
}

%install
rm -rf $RPM_BUILD_ROOT
# Install all apps
{
   for app in * ; do
      pushd $app
      make install DESTDIR=$RPM_BUILD_ROOT
      popd
   done
}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc
%{_bindir}/edid-decode
%{_bindir}/xdpyinfo
%{_bindir}/xev
%{_bindir}/xlsatoms
%{_bindir}/xlsclients
%{_bindir}/xlsfonts
%{_bindir}/xprop
%{_bindir}/xvinfo
%{_bindir}/xwininfo
%{_mandir}/man1/xdpyinfo.1*
%{_mandir}/man1/xev.1*
%{_mandir}/man1/xlsatoms.1*
%{_mandir}/man1/xlsclients.1*
%{_mandir}/man1/xlsfonts.1*
%{_mandir}/man1/xprop.1*
%{_mandir}/man1/xvinfo.1*
%{_mandir}/man1/xwininfo.1*

%changelog
* Fri Jun 11 2010 Adam Jackson <ajax@redhat.com> 7.4-8
- edid-decode snapshot (#492995)

* Tue Oct 13 2009 Adam Jackson <ajax@redhat.com> 7.4-7
- xev 1.0.4
- xlsatoms 1.0.2
- xprop 1.1.0
- xwininfo 1.0.5

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 02 2009 Adam Jackson <ajax@redhat.com> 7.4-5
- Drop xfd and xfontsel, move them to -apps to isolate libXaw deps.

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jul 27 2008 Adam Jackson <ajax@redhat.com> 7.4-3
- Drop xdriinfo.  Would be better suited to being in Mesa's glx-utils
  subpackage anyway. (#456609)

* Tue Jul 15 2008 Adam Jackson <ajax@redhat.com> 7.4-2
- Fix license tag.

* Wed Jul 02 2008 Adam Jackson <ajax@redhat.com> 7.4-1
- xdpyinfo 1.0.3
- xprop 1.0.4
- xwininfo 1.0.4

* Fri Apr 25 2008 Adam Jackson <ajax@redhat.com> 7.3-3
- xdpyinfo-1.0.2-silence-misc-errors.patch: Make xf86misc and xf86dga protocol
  errors non-fatal. (#442176)

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 7.3-2
- Autorebuild for GCC 4.3

* Mon Sep 24 2007 Adam Jackson <ajax@redhat.com> 7.3-1
- xdriinfo 1.0.2
- xwininfo 1.0.3
- Bump to 7.3

* Fri Aug 17 2007 Dave Airlie <airlied@redhat.com> 7.2-1
- xfontsel 1.0.2, xlsfonts 1.0.2, xvinfo 1.0.2, xprop 1.0.3

* Mon Mar 26 2007 Adam Jackson <ajax@redhat.com> 7.1-4
- xdpyinfo 1.0.2

* Tue Jan 30 2007 Adam Jackson <ajax@redhat.com> 7.1-3
- Fix man page glob and rebuild for FC7.

* Wed Jul 19 2006 Mike A. Harris <mharris@redhat.com> 7.1-2.fc6
- Remove app-defaults dir from file manifest, as it is owned by libXt (#174021)
- Add 'dist' tag to package release string.

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> 7.1-1.1
- rebuild

* Wed Jun 21 2006 Mike A. Harris <mharris@redhat.com> 7.1-1
- Bump package version to 7.1 to reflect the X11 release the utilities
  are aggregated from.
- Updated to xdriinfo-1.0.1, xev-1.0.2, xwininfo-1.0.2 from X11R7.1

* Wed May 31 2006 Adam Jackson <ajackson@redhat.com> 1.0.1-3
- Fix BuildRequires (#191966)

* Tue Apr 25 2006 Adam Jackson <ajackson@redhat.com> 1.0.1-2
- Remove a spurious Xprint dependency from xdpyinfo.

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> 1.0.1-1.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> 1.0.1-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Wed Jan 18 2006 Mike A. Harris <mharris@redhat.com> 1.0.1-1
- Updated all tarballs to versions from X11R7.0

* Sat Dec 17 2005 Mike A. Harris <mharris@redhat.com> 1.0.0-1
- Updated all tarballs to version 1.0.0 from X11R7 RC4.
- Changed manpage dir from man1x to man1 to match upstream RC4 default.
- Moved all app-defaults files from _libdir to _datadir

* Mon Nov 14 2005 Jeremy Katz <katzj@redhat.com> 0.99.2-3
- require newer filesystem package (#172610)

* Mon Nov 14 2005 Jeremy Katz <katzj@redhat.com> 0.99.2-2
- rebuild 

* Fri Nov 11 2005 Mike A. Harris <mharris@redhat.com> 0.99.2-1
- Initial build, with all apps taken from X11R7 RC2
- Use "make install DESTDIR=$RPM_BUILD_ROOT" as the makeinstall macro fails on
  some packages.
