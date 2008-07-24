%define version 0.7.11

Summary:	TetriNET game client for Linux
Name:		gtetrinet
Version:	%{version}
Release:	%mkrel 4
License:	GPL
Group:		Games/Arcade
Source:		ftp://ftp.gnome.org/pub/gnome/sources/%{name}/0.7/%{name}-%{version}.tar.bz2
URL:		http://gtetrinet.sourceforge.net/
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Buildrequires:	libgnomeui2-devel
BuildRequires:  perl-XML-Parser
BuildRequires:	ImageMagick
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


