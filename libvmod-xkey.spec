%global libvmod_xkey_git_branch 4.1

Name:              libvmod-xkey
Version:           20151209
Release:           1%{?dist}
Summary:           Varnish Cookie VMOD
License:           FreeBSD
Source:            https://github.com/varnish/libvmod-xkey/archive/%{libvmod_xkey_git_branch}.tar.gz#/libvmod-xkey-%{libvmod_xkey_git_branch}.tar.gz
URL:               https://www.varnish-cache.org/vmod/xkey
Requires:          varnish >= 4.1.0
BuildRequires:     varnish-libs-devel >= 4.1.0
BuildRequires:     git
BuildRequires:     automake
BuildRequires:     autoconf
BuildRequires:     libtool
BuildRequires:     python-docutils

%description
This vmod adds secondary hashes to objects, allowing fast purging on all objects with this hash key.

You can use this to indicate relationships, a bit like a "tag". Then clear out all object that have this tag set. Two good use cases are news sites, where one might add all the stories mentioned on a particular page by article ID, letting each article referenced create an xkey header.

Similarly with an e-commerce site, where various SKUs are often referenced on a page.

Hash keys are specified in the xkey response header. Multiple keys can be specified per header line with a space separator. Alternatively, they can be specified in multiple xkey response headers.

Developed by Varnish Software. Sponsored by Softonic.com

%prep
%setup -q -n %{name}-%{libvmod_xkey_git_branch}

%build
./autogen.sh
./configure --prefix=%{_prefix}
make

%install
make install DESTDIR=%{buildroot}
rm %{buildroot}%{_libdir}/varnish/vmods/libvmod_xkey.la

%files
%doc %{_docdir}/libvmod-xkey/LICENSE
%doc %{_docdir}/libvmod-xkey/README.rst
%doc %{_mandir}/man3/vmod_xkey.3.gz
%{_libdir}/varnish/vmods/libvmod_xkey.so

%changelog
* Wed Dec  9 2015 Hiroaki Nakamura <hnakamur@gmail.com> - 20151209-1
- Initial package
