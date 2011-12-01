Summary:	[incr Widgets] - object-oriented widget set based in [incr Tcl] and [incr Tk]
Summary(pl.UTF-8):	[incr Widgets] - zbiór obiektowo zorientowanych widgetów opartych na [incr Tcl] i [incr Tk]
Name:		iwidgets
Version:	4.0.2
%define snap	20080403
Release:	1
License:	distributable
Group:		Development/Languages/Tcl
#Source0:	http://downloads.sourceforge.net/incrtcl/iwidgets%{iwidgets_version}.tar.gz
Source0:	%{name}-CVS-%{snap}.tar.bz2
# Source0-md5:	7741d7e0b231a4875b0998d6b5c00615
Patch0:		%{name}-standalone.patch
URL:		http://incrtcl.sourceforge.net/iwidgets/index.html
BuildRequires:	autoconf >= 2.13
BuildRequires:	tcl >= 8.4.6
BuildRequires:	tk >= 8.4.6
Requires:	itcl >= 3.4.1
Requires:	itk >= 3.4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_ulibdir	%{_prefix}/lib

%description
[incr Widgets] is an object-oriented mega-widget set which extends
Tcl/Tk and is based on [incr Tcl] and [incr Tk]. This set of
mega-widgets delivers many new, general purpose widgets like option
menus, comboboxes, selection boxes, and various dialogs whose
couterparts are found in Motif and Windows. Since [incr Widgets] is
based on the [incr Tk] extension, the Tk framework of configuration
options, widget commands, and default bindings is maintained. In other
words, each [incr Widgets] mega-widget seamlessly blends with the
standard Tk widgets. They look, act and feel like Tk widgets. In
addition, all [incr Widgets] mega-widgets are object oriented and may
themselves be extended, using either inheritance or composition.

%description -l pl.UTF-8
[incr Widgets] to zbiór zorientowanych obiektowo mega-widgetów
rozszerzający Tcl/Tk, oparty na [incr Tcl] i [incr Tk]. Ten zbiór
mega-widgetów zawiera wiele nowych widgetów ogólnego przeznaczenia,
takich jak menu opcji, kontrolki combobox, kontrolki wyboru oraz różne
okna dialogowe, których odpowiedniki można znaleźć w Motifie lub
Windows. Jako że [incr Widgets] jest oparty na rozszerzeniu [incr Tk],
zachowany jest szkielet Tk opcji konfiguracyjnych, polecenia widgetów
oraz domyślne powiązania. Innymi słowy, każdy mega-widget [incr
Widgets] komponują się idealnie ze standardowymi widgetami Tk.
Wyglądają i zachowują się tak samo, jak widgety Tk. Ponadto wszystkie
mega-widgety [incr Widgets] są zorientowane obiektowo i mogą być
rozszerzane - poprzez dziedziczenie lub składanie.

%package examples
Summary:	Examples for iwidgets
Summary(pl.UTF-8):	Przykłady dla biblioteki iwidgets
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description examples
Examples for iwidgets.

%description examples -l pl.UTF-8
Przykłady dla biblioteki iwidgets.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%{__autoconf}
%configure \
	--libdir=%{_ulibdir} \
	--with-itcl=%{_ulibdir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

ln -sf %{_ulibdir}/iwidgets%{version} $RPM_BUILD_ROOT%{_ulibdir}/iwidgets

mv -f $RPM_BUILD_ROOT%{_ulibdir}/iwidgets%{version}/demos/* \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES ChangeLog README license.terms
%{_ulibdir}/iwidgets
%dir %{_ulibdir}/iwidgets%{version}
%{_ulibdir}/iwidgets%{version}/*.tcl
%{_ulibdir}/iwidgets%{version}/scripts
%{_mandir}/mann/iwidgets_*.n*

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
