%if 0%{?rhel} && 0%{?rhel} <= 6
%{!?__python2: %global __python2 /usr/bin/python2}
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%endif

%global dist_raw %(%{__grep} -oP "release \\K[0-9]+\\.[0-9]+" /etc/system-release | tr -d ".")

%if 0%{?fedora} > 12 || 0%{?rhel} && 0%{?dist_raw} >= 75
%bcond_without python3
%else
%bcond_with python3
%endif

%if 0%{?rhel} && 0%{?rhel} >= 8
%bcond_with python2
%else
%bcond_without python2
%endif

# centos 7.2 and lower versions don't have %py2_* macros, so define it manually
%if 0%{?rhel} && 0%{?dist_raw} <= 72
%{!?py2_build: %global py2_build %py_build}
%{!?py2_install: %global py2_install %py_install}
%endif

%global pkgname jsonrpclib

Name:      python-%{pkgname}
Version:   0.4.0
Release:   CROC0Test1227914%{?dist}
Summary:   JSON-RPC v2.0 client library for Python
License:   ASL 2.0
URL:       http://github.com/tcalmant/jsonrpclib/
Source0:   %{pkgname}-%{version}.tar.gz
BuildArch: noarch

%global _description\
This project is an implementation of the JSON-RPC v2.0 specification\
(backwards-compatible) as a client library, for Python 2.7 and Python 3.\
This version is a fork of jsonrpclib by Josh Marshall, usable with Pelix\
remote services.\

%description %_description

%if %{with python2}
%package -n python2-%{pkgname}
Summary: %summary
BuildRequires:  python2-devel

%description -n python2-%{pkgname} %_description
%endif

%if %{with python3}
%package -n python%{python3_pkgversion}-%{pkgname}
Summary: %summary
BuildRequires:  python%{python3_pkgversion}

%description -n python%{python3_pkgversion}-%{pkgname} %_description
%endif


%prep
%setup -q -n %{pkgname}-%{version}


%build
%if %{with python2}
%py2_build
%endif

%if %{with python3}
%py3_build
%endif


%install
[ %buildroot = "/" ] || rm -rf %buildroot

%if %{with python2}
%py2_install
%endif

%if %{with python3}
%py3_install
%endif


%clean
rm -rf %{buildroot}

%if %{with python2}
%files -n python2-%{pkgname}
%license LICENSE
%{python2_sitelib}/*
%endif

%if %{with python3}
%files -n python%{python3_pkgversion}-%{pkgname}
%license LICENSE
%{python3_sitelib}/*
%endif


%changelog
* Fri Oct 28 2022 Ivan Konov <ikonov@croc.ru> - 0.4.0-2
- Build for rhel8 (without python2)

* Mon Sep 30 2019 Croc Cloud Engineering - 0.4.0-1
- Build for py2/py3 for Croc cloud

