%define name quickly
%define version 0.4
%define release %mkrel 1

Name:		%{name}
Summary:    Command line tools to ease the creation of a new project
Version:	%{version}
Release:	%{release}

License:	GPLv3
Group:		Development/Other
URL:		https://launchpad.net/quickly
Source:		http://launchpad.net/quickly/0.x/%{version}/+download/%{name}_%{version}.orig.tar.gz
BuildRequires:  python-devel 
BuildRequires:  python-distutils-extra >= 2.18 
BuildRequires:  intltool
BuildArch:	noarch


%description
Quickly helps you create software programs (and other things) quickly. You 
can select from a set of application templates and use some simple quickly 
commands to create, edit code and GUI, and publish your software for others 
to use. Quickly's templates are easy to write. So if you are a fan of 
language foo, you can create a foo-project template. Or if you want to 
help people making plugins for your killer app, you can make a 
killer-app-plugin template. You can even create a template for managing 
corporate documents, creating your awesome LaTeX helpers

%prep

%setup -q
%build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --root=$RPM_BUILD_ROOT 
%find_lang %name

# bug that should be fixed with newer python-distutils-extra according to upstream
rm -f $RPM_BUILD_ROOT/%_datadir/applications/project_name.desktop

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
%_sysconfdir//bash_completion.d/%name
