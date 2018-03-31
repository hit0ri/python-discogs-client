%global srcname discogs-client
%global sum Official Python Client for the Discogs API
%global desc This is the official Discogs API client for Python.\
It enables you to query the Discogs database for information on artists,\
releases, labels, users, Marketplace listings, and more.\
It also supports OAuth 1.0a authorization.

Name:           python-%{srcname}
Version:        2.2.1
Release:        1%{?dist}
Summary:        %{sum}

License:        BSD
URL:            https://github.com/discogs/discogs_client
Source0:        https://pypi.python.org/packages/1f/1f/62a8cee111ff72c5ad379039adef8c872813602ffd516ba35368726f14c2/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel python3-devel

%description
%{desc}


%package -n python2-%{srcname}
Summary:        %{sum}

%{?python_provide:%python_provide python2-%{srcname}}

Requires:       %{py2_dist requests}
Requires:       %{py2_dist six}
Requires:       %{py2_dist oauthlib}

%description -n python2-%{srcname}
%{desc}


%package -n python3-%{srcname}
Summary:        %{sum}

%{?python_provide:%python_provide python3-%{srcname}}

Requires:       %{py3_dist requests}
Requires:       %{py3_dist six}
Requires:       %{py3_dist oauthlib}

%description -n python3-%{srcname}
%{desc}


%prep
%autosetup -n %{srcname}-%{version}


%build
%py2_build
%py3_build


%install
%py2_install
%py3_install


%files -n python2-%{srcname}
%{python2_sitelib}/*


%files -n python3-%{srcname}
%{python3_sitelib}/*


%changelog
* Sat Mar 31 2018 Taras Dyshkant <hitori.gm@gmail.com> - 2.2.1-1
- Initial release
