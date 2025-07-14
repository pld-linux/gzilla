Summary:	Gzilla is a web browser written in the GTK+ framework
Summary(pl.UTF-8):	Gzilla to przeglądarka WWW napisana w GTK+
Name:		gzilla
Version:	0.3.10
Release:	2
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://www.gzilla.com/Downloads/%{name}-%{version}.tar.gz
# Source0-md5:	896e0e7a7e938685d0a65adc46587ff1
Source1:	%{name}.desktop
Patch0:		%{name}-qelem.patch
URL:		http://www.gzilla.com/
BuildRequires:  XFree86-devel
BuildRequires:  glib-devel >= 1.2.0
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	libjpeg-devel
Requires:	gtk+ >= 1.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gzilla is a Web browser, written in C using the GTK+ widget set.
Gzilla is still in alpha development (like Lynx with pictures). The
project's design goal is to eventually create a fast, small and easily
extensible browser compatible (at minimum) with HTML 4.0 and CSS 1.
Another design goal is to provide a user interface which supports
integration of the graphical and textual shells in a unique and
powerful way.

%description -l pl.UTF-8
Gzilla jest przeglądarką WWW napisaną w języku C i wykorzystującą
bibliotekę GTK+. Jest wciąż w fazie rozwojowej, na razie przypomina
"obrazkowego Lynxa". Celem projektu jest stworzenie szybkiej, małej i
łatwo rozszerzalnej przeglądarki zgodnej co najmniej z HTML-em 4.0 i
CSS 1. Innym celem jest stworzenie interfejsu użytkownika
umożliwiającego integrację powłok graficznych i tekstowych w sprawny i
oryginalny sposób.

%prep
%setup -q
%patch -P0 -p1

%build
%configure2_13 \
	--disable-gtktest \
	--disable-glibtest
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/* AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/gzilla
%attr(755,root,root) %{_bindir}/gztest
%{_desktopdir}/gzilla.desktop
