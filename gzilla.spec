Summary:	Gzilla is a web browser written in the Gtk+ framework.
Summary(pl):	Gzilla to przegl±darka WWW napisana w GTK+
Name:		gzilla
Version:	0.3.10
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://www.gzilla.com/Downloads/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Patch0:		%{name}-qelem.patch
URL:		http://www.gzilla.com/
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	libjpeg-devel
BuildRequires:	glib-devel >= 1.2.0
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
Gzilla jest przegl±dark± WWW napisan± w jêzyku C i wykorzystuj±c±
bibliotekê GTK+. Jest wci±¿ w fazie rozwojowej, na razie przypomina
"obrazkowego Lynxa". Celem projektu jest stworzenie szybkiej, ma³ej i
³atwo rozszerzalnej przegl±darki zgodnej co najmniej z HTML 4.0 i CSS
1. Innym celem jest stworzenie interfejsu u¿ytkownika umo¿liwiaj±cego
integracjê pow³ok graficznych i tekstowych w sprawny i oryginalny
sposób.

%prep
%setup -q
%patch0 -p1

%build
%configure2_13 \
	--disable-gtktest \
	--disable-glibtest
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Network/WWW

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Network/WWW

gzip -9nf AUTHORS ChangeLog NEWS README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/* *.gz
%attr(755,root,root) %{_bindir}/gzilla
%{_applnkdir}/Network/WWW/gzilla.desktop
