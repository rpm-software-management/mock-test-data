%global		_source_filedigest_algorithm md5

Name:		daemontest
Version:	1
Release:	0%{?dist}
Summary:	start daemon during build, and in post-scriptlet

Group:		NONE
License:	GPL
URL:		http://example.com/

%if 0%{?rhel} && 0%{?rhel} < 8
Requires:	python-daemon
Requires:	python-setproctitle
BuildRequires:	python-daemon
BuildRequires:	python-setproctitle
%else
Requires:	python3-daemon
Requires:	python3-setproctitle
BuildRequires:	python3-daemon
BuildRequires:	python3-setproctitle
%endif

Requires:	/bin/ps
BuildRequires:	/bin/ps


BuildArch:	noarch

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Source0:	README.xz
Source1:	daemontest.py

%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

%description


%prep


%build
%if 0%{?rhel} && 0%{?rhel} < 8
sed 's|/usr/bin/python|/usr/bin/python2|' %SOURCE1 > daemontest.py
%else
sed 's|/usr/bin/python|/usr/bin/python3|' %SOURCE1 > daemontest.py
%endif
chmod +x daemontest.py


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_pkgdocdir}
xz -d %{SOURCE0} --stdout > $RPM_BUILD_ROOT/%{_pkgdocdir}/README
mkdir -p $RPM_BUILD_ROOT/%_bindir

install -m 755 daemontest.py $RPM_BUILD_ROOT/%_bindir/daemontest


%check
./daemontest.py


%clean
rm -rf $RPM_BUILD_ROOT

%posttrans
%_bindir/daemontest

%files
%doc %{_pkgdocdir}/README
%_bindir/daemontest

%changelog
* Thu Jun 05 2014 Pavel Raiskup <praiskup@redhat.com> - 0-1
- does nothing!
