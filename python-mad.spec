%define		module	mad
Summary:	A Python module for the MPEG Audio Decoder library
Summary(pl):	Modu³ Pythona do biblioteki MPEG Audio Decoder
Name:		python-%{module}
Version:	0.5.4
Release:	1
License:	GPL
Group:		Libraries/Python
Source0:	http://spacepants.org/src/pymad/download/pymad-%{version}.tar.gz
# Source0-md5:	5a2b86cf3b3501a620ef8156b49289cb
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

%description -l pl
pymad to modu³ Pythona pozwalaj±cy programom w Pythonie u¿ywaæ
biblioteki MPEG Audio Decoder (dekodera d¼wiêku MPEG). pymad
udostêpnia wysokopoziomowe API podobne do modu³u pyogg, co czyni
odczyt danych PCM ze strumieni d¼wiêkowych MPEG bardzo ³atwym.

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
