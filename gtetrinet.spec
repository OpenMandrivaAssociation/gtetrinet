%define version 0.7.11

Summary:	TetriNET game client for Linux
Name:		gtetrinet
Version:	%{version}
Release:	9
License:	GPLv2+
Group:		Games/Arcade
Source:		ftp://ftp.gnome.org/pub/gnome/sources/%{name}/0.7/%{name}-%{version}.tar.bz2
URL:		https://gtetrinet.sourceforge.net/
Patch0:     gtetrinet-0.7.11-fix_default_server.diff
Patch1:     gtetrinet-0.7.11-fix_format_error.diff 
Buildrequires:	pkgconfig(libgnomeui-2.0)
BuildRequires:  perl-XML-Parser
BuildRequires:	imagemagick
Requires(post):		GConf2 >= 2.3.3
Requires(preun):		GConf2 >= 2.3.3

%description
GTetrinet is a client program for the popular TetriNET game, a multiplayer
tetris game that is played over the internet. It is written in GTK.
(If you don't know what TetriNET is, check out tetrinet.org)

Its features include:
  * Fully network compatible with Tetrinet v1.13 for Win95/98/NT
  * Theme support with sound
  * Spectator support on Tetrinet-X servers with the qirc patch by Drslum.


%prep
%setup -q
%patch0 -p0
%patch1 -p0

%build
%configure2_5x --enable-detach --enable-ipv6
%make

%install
rm -fr $RPM_BUILD_ROOT
GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 %makeinstall_std

# icon
mkdir -p $RPM_BUILD_ROOT%{_iconsdir} \
	 $RPM_BUILD_ROOT%{_liconsdir} \
	 $RPM_BUILD_ROOT%{_miconsdir}
convert -geometry 48x48 gtetrinet.png $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png
convert -geometry 32x32 gtetrinet.png $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
convert -geometry 16x16 gtetrinet.png $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png

# menu
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=GTetrinet
Comment=TetriNET game client for Linux
Exec=%_gamesbindir/gtetrinet
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;ArcadeGame;X-MandrivaLinux-MoreApplications-Games-Arcade;
EOF

%find_lang %{name}

%if %mdkversion < 200900
%post
%{update_menus}
%post_install_gconf_schemas gtetrinet
%endif

%preun
%preun_uninstall_gconf_schemas gtetrinet

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_gamesbindir}/*
%{_datadir}/gtetrinet
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*
%{_mandir}/man?/*
%{_sysconfdir}/gconf/schemas/*
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png




%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.7.11-7mdv2011.0
+ Revision: 619282
- the mass rebuild of 2010.0 packages

* Fri Sep 11 2009 Thierry Vignaud <tv@mandriva.org> 0.7.11-6mdv2010.0
+ Revision: 437822
- rebuild

* Sun Mar 29 2009 Michael Scherer <misc@mandriva.org> 0.7.11-5mdv2009.1
+ Revision: 362136
- fix default tetrinet server, bug 49270, patch 0
- fix build ( patch 1 )
- fix license

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.7.11-4mdv2009.0
+ Revision: 246671
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
    - use %%preun_uninstall_gconf_schemas
    - use %%post_install_gconf_schemas/%%preun_uninstall_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Dec 18 2007 Thierry Vignaud <tv@mandriva.org> 0.7.11-2mdv2008.1
+ Revision: 132324
- drop old menu entry
- kill re-definition of %%buildroot on Pixel's request
- kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

* Mon Aug 20 2007 Thierry Vignaud <tv@mandriva.org> 0.7.11-2mdv2008.0
+ Revision: 67951
- convert prereq


* Fri Dec 01 2006 Jérôme Soyer <saispo@mandriva.org> 0.7.11-1mdv2007.0
+ Revision: 89906
- New release 0.7.11
- Import gtetrinet

* Wed Sep 06 2006 Jerome Soyer <saispo@mandriva.org> 0.7.10-1mdv2007.0
- New release
- XDG

* Fri Jun 03 2005 Abel Cheung <deaddog@mandriva.org> 0.7.9-1mdk
- New release
- Drop upstream patch

* Tue Mar 22 2005 Abel Cheung <deaddog@mandrake.org> 0.7.8-2mdk
- P0: UTF8 support (CVS)

* Sun Dec 26 2004 Abel Cheung <deaddog@mandrakesoft.com> 0.7.8-1mdk
- New release 0.7.8

* Thu Apr 22 2004 Götz Waschk <waschk@linux-mandrake.com> 0.7.7-2mdk
- fix buildrequires

* Tue Apr 20 2004 Götz Waschk <waschk@linux-mandrake.com> 0.7.7-1mdk
- new version

