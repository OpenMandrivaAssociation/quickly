%define name quickly
%define version 0.2.5
%define release %mkrel 1

Name:		%{name}
Summary:    FOOO	
Version:	%{version}
Release:	%{release}

License:	GPLv3
Group:		TODO
URL:		https://launchpad.net/quickly
Source:		http://launchpad.net/quickly/0.x/%{version}/+download/%{name}-%{version}.tar.gz
Requires:	python
BuildRequires:  python-devel 
BuildArch:	noarch


%description
FOO
%prep

%setup -q -n %name
%build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --root=$RPM_BUILD_ROOT 
%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-,root,root)
%doc NEWS README 
%_datadir/%name
%python_sitelib/%name
%python_sitelib/*egg-info
%_bindir/%name
%_mandir/man1/*
%_sysconfdir//bash_completion.d/quickly
%_datadir/applications/project_name.desktop
