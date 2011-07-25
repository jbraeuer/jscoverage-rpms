Name:		jscoverage
Version:	0.5.1
Release:	1%{?dist}
Summary:	JSCoverage is a tool that measures code coverage for JavaScript programs.

Group:		unknown
License:	GPLv2
URL:		http://siliconforks.com/jscoverage/
Source0:	http://siliconforks.com/jscoverage/download/jscoverage-0.5.1.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description


%prep
%setup -q

%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
/usr/bin/jscoverage
/usr/bin/jscoverage-server
/usr/share/man/man1/jscoverage-server.1.gz
/usr/share/man/man1/jscoverage.1.gz

%doc

%changelog
* Mon Jul 25 2011 Jens Braeuer <jens@numberfour.eu> - 0.5.1-1
- Initial packaging.

