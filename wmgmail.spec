Summary:	Yet another Gmail notifier
Summary(pl):	Kolejny powiadamiacz Gmail	
Name:		wmgmail
Version:	0.6.0
Release:	0.1
License:	GPL v2
Group:		X11/Window Managers/Tools
Source0:	http://varg.dyndns.org/psi/files/misc/%{name}-%{version}.tar.gz	
# Source0-md5:	bc35a237a8e81da93e0d0dcf90030dbe
Source1:	%{name}.desktop
URL:		http://varg.dyndns.org/psi/pub/code/misc/wmgmail.html
Requires:	python-libgmail
Requires:	pywmgeneral
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
wmgmail checks your gmail account for new mail. Its has (optional) GUI
configuration and quick mail preview.

Functionality includes:
- Checking for new mail in Gmail (strictly speaking it's using
  "is:unread" -query)
- Variable checking time (from 2min to several hours)
- GUI for settings
- Mail contents preview (shows same snippets that Gmail inbox does)

#%description -l pl

%prep
%setup -q -n %{name}

%build
./setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}/docklets

./setup.py install \
	--root $RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/docklets

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{py_sitescriptdir}/*
%{_desktopdir}/docklets/wmgmail.desktop
