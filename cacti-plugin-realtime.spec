%define		plugin	realtime
%define		ver	%(echo %{version} |tr _ -)
%define		php_min_version 5.1.1
%include	/usr/lib/rpm/macros.php
Summary:	Plugin for Cacti - realtime
Summary(pl.UTF-8):	Wtyczka do Cacti - realtime
Name:		cacti-plugin-%{plugin}
Version:	0.5_2
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://docs.cacti.net/_media/plugin:%{plugin}-v%{ver}.tgz
# Source0-md5:	94562c20ab4784c27a1463028886b313
URL:		http://docs.cacti.net/plugin:realtime
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	cacti
Requires:	cacti(pia) >= 2.8
Requires:	php(core) >= %{php_min_version}
Requires:	php(date)
Requires:	php(pcre)
Requires:	php(session)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		cactidir		/usr/share/cacti
%define		plugindir		%{cactidir}/plugins/%{plugin}

%description
Provides a method to view Cacti graphs with a resolution of upto 5
seconds. Features

Allows Syncronization between windows. Dynamically sizes viewing
window based upon graph size. Uses Ajax for Graph generation.

%prep
%setup -qc
mv %{plugin}/{LICENSE,README} .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a %{plugin}/* $RPM_BUILD_ROOT%{plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{plugindir}
