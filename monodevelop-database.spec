%include	/usr/lib/rpm/macros.mono
Summary:	Database Add-in for MonoDevelop
Summary(pl.UTF-8):	Dodatek Database do programu MonoDevelop
Name:		monodevelop-database
%define	mainver	5.0.1
%define	subver	0
Version:	%{mainver}.%{subver}
Release:	1
License:	MIT
Group:		Development/Tools
Source0:	http://download.mono-project.com/sources/monodevelop-database/%{name}-%{mainver}-%{subver}.tar.bz2
# Source0-md5:	1c893258e61cbdb983bbfeaba419eb56
URL:		http://monodevelop.com/
BuildRequires:	dotnet-gtk-sharp2-devel >= 2.12.8
BuildRequires:	gettext-devel
BuildRequires:	mono-addins-devel >= 0.4
BuildRequires:	mono-csharp >= 2.6.1
BuildRequires:	monodevelop >= 5.0.1
BuildRequires:	pkgconfig
Requires:	monodevelop >= 5.0.1
ExcludeArch:	i386
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Database Add-in for MonoDevelop - integrated database explorer and
editor.

%description -l pl.UTF-8
Dodatek Database do programu MonoDevelop - zintegrowany eksplorator i
edytor baz danych.

%prep
%setup -q -n %{name}-%{mainver}

%build
%configure

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%{__mv} $RPM_BUILD_ROOT%{_prefix}/lib/monodevelop/AddIns/MonoDevelop.Database/locale/{sl_SI,sl}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog
%dir %{_prefix}/lib/monodevelop/AddIns/MonoDevelop.Database
%{_prefix}/lib/monodevelop/AddIns/MonoDevelop.Database/MonoDevelop.Database.*.dll
%{_prefix}/lib/monodevelop/AddIns/MonoDevelop.Database/MonoDevelop.Database.*.dll.mdb
%{_prefix}/lib/monodevelop/AddIns/MonoDevelop.Database/MySql.Data.dll
%{_prefix}/lib/monodevelop/AddIns/MonoDevelop.Database/icons
%dir %{_prefix}/lib/monodevelop/AddIns/MonoDevelop.Database/locale
%lang(ca) %{_prefix}/lib/monodevelop/AddIns/MonoDevelop.Database/locale/ca
%lang(cs) %{_prefix}/lib/monodevelop/AddIns/MonoDevelop.Database/locale/cs
%lang(da) %{_prefix}/lib/monodevelop/AddIns/MonoDevelop.Database/locale/da
%lang(de) %{_prefix}/lib/monodevelop/AddIns/MonoDevelop.Database/locale/de
%lang(es) %{_prefix}/lib/monodevelop/AddIns/MonoDevelop.Database/locale/es
%lang(fr) %{_prefix}/lib/monodevelop/AddIns/MonoDevelop.Database/locale/fr
%lang(gl) %{_prefix}/lib/monodevelop/AddIns/MonoDevelop.Database/locale/gl
%lang(hu) %{_prefix}/lib/monodevelop/AddIns/MonoDevelop.Database/locale/hu
%lang(id) %{_prefix}/lib/monodevelop/AddIns/MonoDevelop.Database/locale/id
%lang(it) %{_prefix}/lib/monodevelop/AddIns/MonoDevelop.Database/locale/it
%lang(ja) %{_prefix}/lib/monodevelop/AddIns/MonoDevelop.Database/locale/ja
%lang(nl) %{_prefix}/lib/monodevelop/AddIns/MonoDevelop.Database/locale/nl
%lang(pl) %{_prefix}/lib/monodevelop/AddIns/MonoDevelop.Database/locale/pl
%lang(pt) %{_prefix}/lib/monodevelop/AddIns/MonoDevelop.Database/locale/pt
%lang(pt_BR) %{_prefix}/lib/monodevelop/AddIns/MonoDevelop.Database/locale/pt_BR
%lang(ru) %{_prefix}/lib/monodevelop/AddIns/MonoDevelop.Database/locale/ru
%lang(sl) %{_prefix}/lib/monodevelop/AddIns/MonoDevelop.Database/locale/sl
%lang(sv) %{_prefix}/lib/monodevelop/AddIns/MonoDevelop.Database/locale/sv
%lang(tr) %{_prefix}/lib/monodevelop/AddIns/MonoDevelop.Database/locale/tr
%lang(zh_CN) %{_prefix}/lib/monodevelop/AddIns/MonoDevelop.Database/locale/zh_CN
%lang(zh_TW) %{_prefix}/lib/monodevelop/AddIns/MonoDevelop.Database/locale/zh_TW
%{_pkgconfigdir}/monodevelop-database.pc
