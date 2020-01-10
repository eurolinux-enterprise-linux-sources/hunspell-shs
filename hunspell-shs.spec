Name: hunspell-shs
Summary: Shuswap hunspell dictionaries
%define upstreamid 20090828
Version: 0.%{upstreamid}
Release: 5%{?dist}
Group: Applications/Text
Source: http://secpewt.sd73.bc.ca/hunspell/hunspell-shs-ca.tar.gz
URL: http://secpewt.sd73.bc.ca/wordlist
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: GPLv2+
BuildArch: noarch
BuildRequires: hunspell-devel

Requires: hunspell

%description
Shuswap hunspell dictionaries.

%prep
%setup -q -c

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p hunspell/shs_CA.* $RPM_BUILD_ROOT/%{_datadir}/myspell

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc hunspell/COPYING hunspell/Copyright hunspell/README
%{_datadir}/myspell/*

%changelog
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20090828-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20090828-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20090828-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20090828-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Aug 31 2009 Caolan McNamara <caolanm@redhat.com> - 0.20090828-1
- latest version

* Thu Aug 27 2009 Caolan McNamara <caolanm@redhat.com> - 0.20081107-1
- initial version
