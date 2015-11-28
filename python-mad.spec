Summary:	A Python module for the MPEG Audio Decoder library
Summary(pl.UTF-8):	Moduł Pythona do biblioteki MPEG Audio Decoder
Name:		python-mad
Version:	0.6
Release:	4
License:	GPL
Group:		Libraries/Python
Source0:	http://spacepants.org/src/pymad/download/pymad-%{version}.tar.gz
# Source0-md5:	a1405fb4b610348565c8d0e400c5ff18
URL:		http://spacepants.org/src/pymad/
BuildRequires:	libmad-devel
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.174
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pymad is a Python module that allows Python programs to use the MPEG
Audio Decoder library. pymad provides a high-level API, similar to the
pyogg module, which makes reading PCM data from MPEG audio streams a
piece of cake.

%description -l pl.UTF-8
pymad to moduł Pythona pozwalający programom w Pythonie używać
biblioteki MPEG Audio Decoder (dekodera dźwięku MPEG). pymad
udostępnia wysokopoziomowe API podobne do modułu pyogg, co czyni
odczyt danych PCM ze strumieni dźwiękowych MPEG bardzo łatwym.

%prep
%setup -q -n pymad-%{version}

%build
python config_unix.py \
	--prefix %{_prefix}
python setup.py config
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install \
	--root $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README NEWS THANKS
%doc test/*
%attr(755,root,root) %{py_sitedir}/madmodule.so
%{py_sitedir}/pymad-*.egg-info
