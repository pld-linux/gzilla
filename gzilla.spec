Summary:	Gzilla is a web browser written in the Gtk+ framework.
Summary(pl):	Gzilla to przeglądarka WWW napisana w GTK+
Name:		gzilla
Version:	0.3.10
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Group(de):	X11/Applikationen/Netzwerkwesen
Group(pl):	X11/Aplikacje/Sieciowe
Source0:	http://www.gzilla.com/Downloads/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
URL:		http://www.gzilla.com/
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	libjpeg-devel
BuildRequires:	glib-devel
BuildRequires:	XFree86-devel
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	gtk+ >= 1.2.0

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Gzilla is a Web browser, written in C using the GTK+ widget set.
Gzilla is still in alpha development (like Lynx with pictures). The
project's design goal is to eventually create a fast, small and easily
extensible browser compatible (at minimum) with HTML 4.0 and CSS 1.
Another design goal is to provide a user interface which supports
integration of the graphical and textual shells in a unique and
powerful way.

%description -l pl
Gzilla jest przeglądarką WWW napisaną w języku C i wykorzystującą bibliotekę 
GTK+. Jest wciąż w fazie rozwojowej, na razie przypomina "obrazkowego Lynxa".
Celem projektu jest stworzenie szybkiej, małej i łatwo rozszerzalnej 
przeglądarki zgodnej co najmniej z HTML 4.0 i CSS 1. Innym celem jest 
stworzenie interfejsu użytkownika umożliwiającego integrację powłok 
graficznych i tekstowych w sprawny i oryginalny sposób.

%prep
%setup -q

%build
./configure --prefix=%{_prefix}
%{__make}

%install

rm -rf $RPM_BUILD_ROOT

%{__install} -d $RPM_BUILD_ROOT%{_bindir}
%{__install} -d $RPM_BUILD_ROOT%{_applnk}/Network/WWW
%{__install} src/gzilla $RPM_BUILD_ROOT%{_bindir}/gzilla
%{__install} %{SOURCE1} $RPM_BUILD_ROOT%{_applnk}/Network/WWW/gzilla.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%doc doc/*
%attr(755,root,root) %{_bindir}/gzilla
%{_applnk}/Network/WWW/gzilla.desktop
