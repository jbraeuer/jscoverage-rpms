Name:		jscoverage
Version:	0.5.1
Release:	4%{?dist}
Summary:	JSCoverage is a tool that measures code coverage for JavaScript programs.

Group:		unknown
License:	GPLv2
URL:		http://siliconforks.com/jscoverage/
Source0:	http://siliconforks.com/jscoverage/download/jscoverage-0.5.1.tar.bz2
Source1:	jscoverage.init
Source2:	jscoverage.conf
Source3:	jscoverage.no-instrument
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  /usr/bin/g++
Requires:	/usr/sbin/start-stop-daemon
Requires:	ruby

%description

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/etc/rc.d/init.d
install -m 755 %SOURCE1 $RPM_BUILD_ROOT/etc/rc.d/init.d/jscoverage-server
install -m 644 %SOURCE2 $RPM_BUILD_ROOT/etc/
install -m 644 %SOURCE3 $RPM_BUILD_ROOT/etc/
mkdir -p $RPM_BUILD_ROOT/var/lib/jscoverage/root
mkdir -p $RPM_BUILD_ROOT/var/lib/jscoverage/reports
mkdir -p $RPM_BUILD_ROOT/var/run/jscoverage

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
/etc/
/var/lib/jscoverage
/var/run/jscoverage
/usr/bin/jscoverage
/usr/bin/jscoverage-server
/usr/share/man/man1/jscoverage-server.1.gz
/usr/share/man/man1/jscoverage.1.gz

%doc

%changelog
* Wed Oct 12 2011  <braeuer.jens@googlemail.com> - 0.5.1-2
- Update dependency information for SL6.

* Mon Jul 25 2011 Jens Braeuer <jens@numberfour.eu> - 0.5.1-1
- Initial packaging.

