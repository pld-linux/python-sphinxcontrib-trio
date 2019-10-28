#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests

Summary:	Make Sphinx better at documenting Python functions and methods
Summary(pl.UTF-8):	Usprawnienie Sphinksa przy dokumentowaniu funkcji i method w Pythonie
Name:		python-sphinxcontrib-trio
Version:	1.0.1
Release:	2
License:	Apache v2.0 or MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/sphinxcontrib-trio/
Source0:	https://files.pythonhosted.org/packages/source/s/sphinxcontrib-trio/sphinxcontrib-trio-%{version}.tar.gz
# Source0-md5:	f7b3250cadb18a9eeb1eb5e320abf587
URL:		https://github.com/python-trio/sphinxcontrib-trio
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-Sphinx
BuildRequires:	python3-cssselect
BuildRequires:	python3-lxml
BuildRequires:	python3-pytest
%endif
%if %{with doc}
BuildRequires:	sphinx-pdg-3
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This Sphinx extension helps you document Python code that uses
async/await, or abstract methods, or context managers, or generators,
or ... you get the idea. It works by making Sphinx's regular
directives for documenting Python functions and methods smarter and
more powerful.

%description -l pl.UTF-8
To rozszerzenie Sphinksa pozwala dokumentować kod Pythona
wykorzystujący async/await, metody abstrakcyjne, zarządców kontekstu,
generatory itp. Działa usprawniając zwykłe dyrektywy Sphinksa do
dokumentowania funkcji i method Pythona.

%package -n python3-sphinxcontrib-trio
Summary:	Make Sphinx better at documenting Python functions and methods
Summary(pl.UTF-8):	Usprawnienie Sphinksa przy dokumentowaniu funkcji i method w Pythonie
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.5

%description -n python3-sphinxcontrib-trio
This Sphinx extension helps you document Python code that uses
async/await, or abstract methods, or context managers, or generators,
or ... you get the idea. It works by making Sphinx's regular
directives for documenting Python functions and methods smarter and
more powerful.

%description -n python3-sphinxcontrib-trio -l pl.UTF-8
To rozszerzenie Sphinksa pozwala dokumentować kod Pythona
wykorzystujący async/await, metody abstrakcyjne, zarządców kontekstu,
generatory itp. Działa usprawniając zwykłe dyrektywy Sphinksa do
dokumentowania funkcji i method Pythona.

%package apidocs
Summary:	API documentation for Python sphinxcontrib_trio module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona sphinxcontrib_trio
Group:		Documentation

%description apidocs
API documentation for Python sphinxcontrib_trio module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona sphinxcontrib_trio.

%prep
%setup -q -n sphinxcontrib-trio-%{version}

%build
%py3_build

%if %{with tests}
PYTHONPATH=$(pwd) \
%{__python3} -m pytest tests
%endif

%if %{with doc}
%{__make} -C docs html \
	SPHINXBUILD=sphinx-build-3
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files -n python3-sphinxcontrib-trio
%defattr(644,root,root,755)
%doc LICENSE LICENSE.MIT README.rst
%{py3_sitescriptdir}/sphinxcontrib_trio
%{py3_sitescriptdir}/sphinxcontrib_trio-%{version}-py*.egg-info

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/build/html/{_static,*.html,*.js}
%endif
