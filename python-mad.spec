%define		module	mad
Summary:	A Python module for the MPEG Audio Decoder library
Name:		python-%{module}
Version:	0.5.3
Release:	1
License:	GPL
Group:		Libraries/Python
Source0:	http://spacepants.org/src/pymad/download/pymad-%{version}.tar.gz
# Source0-md5:	2c4e23386862b6e9ec6a04a172b241fa
URL:		http://spacepants.org/src/pymad/
BuildRequires:	libmad-devel
BuildRequires:	rpmbuild(macros) >= 1.174
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pymad is a Python module that allows Python programs to use the MPEG
Audio Decoder library. pymad provides a high-level API, similar to the
pyogg module, which makes reading PCM data from MPEG audio streams a
piece of cake.

%prep
%setup -q -n pymad-%{version}

%build
python config_unix.py \
	--prefix %{_prefix}
python setup.py config
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--optimize=2 \
	--root $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README NEWS THANKS
%doc test/*
%attr(755,root,root) %{py_sitedir}/%{module}module.so
