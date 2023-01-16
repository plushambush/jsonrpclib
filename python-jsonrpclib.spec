%global dist_raw %(%{__grep} -oP "release \\K[0-9]+\\.[0-9]+" /etc/system-release | tr -d ".")

%global pkgname jsonrpclib

Name:      python-%{pkgname}
Version:   0.4.0
Release:   CROC2%{?dist}
Summary:   JSON-RPC v2.0 client library for Python
License:   ASL 2.0
URL:       http://github.com/tcalmant/jsonrpclib/
Source0:   %{pkgname}-%{version}.tar.gz
BuildArch: noarch

%global _description\
This project is an implementation of the JSON-RPC v2.0 specification\
(backwards-compatible) as a client library, for Python 3.\
This version is a fork of jsonrpclib by Josh Marshall, usable with Pelix\
remote services.\

%description %_description

%package -n python%{python3_pkgversion}-%{pkgname}
Summary: %summary
BuildRequires:  python%{python3_pkgversion}

%description -n python%{python3_pkgversion}-%{pkgname} %_description

%prep
%setup -q -n %{pkgname}-%{version}

%build
%py3_build

%install
[ %buildroot = "/" ] || rm -rf %buildroot

%py3_install

%clean
rm -rf %{buildroot}

%files -n python%{python3_pkgversion}-%{pkgname}
%license LICENSE
%{python3_sitelib}/*

%changelog
* Mon Jan 16 2023 Ivan Konov <ikonov@croc.ru> - 0.4.0-2
- Build for rhel8 (without python2)
- Remove py2 support

* Mon Sep 30 2019 Croc Cloud Engineering - 0.4.0-1
- Build for py2/py3 for Croc cloud

