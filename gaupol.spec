Summary:        Subtitle editor
Name:           gaupol
Version:	1.15
Release:	1
License:        GPLv3+
Group:          Video
URL:            https://otsaloma.io/gaupol/
Source0:        https://github.com/otsaloma/gaupol/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:	pkgconfig(python)

Requires:	%{name}-i18n = %{version}-%{release}
Requires:	python3dist(pygobject)
Requires:	python-aeidon

Recommends:	gstreamer1.0-plugins-base
Recommends:	gstreamer1.0-plugins-good
Recommends:	python3dist(pyenchant)
Recommends:	python3dist(chardet)
Recommends:	iso-codes
Recommends:	mplayer

%description
Editor for text-based subtitle files. It supports multiple subtitle file 
formats and provides means of correcting texts and timing subtitles to match
video. The user interface is designed with attention to batch processing of
multiple documents and convenience of translating.

%package -n python-aeidon
Summary:	Python package for Reading, writing and manipulating text-based subtitle files
Group:		Development/Python
Url:		https://users.tkk.fi/~otsaloma/gaupol/doc/api/aeidon.html
Requires:	%{name}-i18n = %{version}-%{release}
Requires:	iso-codes
Recommends:	python-chardet
Recommends:	python-enchant
Provides:	aeidon = %{version}-%{release}

%description -n python-aeidon
aeidon is a Python package that provides classes and functions for dealing
with text-based subtitle files of many different formats. Functions exist
for reading and writing subtitle files as well as manipulating subtitle data,
i.e. positions (times or frames) and texts.

%package i18n
Summary:	Internationalization and locale data for gaupol and python-aeidon
Group:		System/Internationalization

%description i18n
Internationalization and locale data for %{name} and python-aeidon.

%prep
%setup -q

%build
%py_build

%install
%{__python} setup.py \
	--without-iso-codes \
	clean install \
	--root=%{buildroot} \
	--prefix=%{_prefix} \
	--no-compile

%find_lang %{name}

%files i18n -f %{name}.lang

%files
%doc AUTHORS.md NEWS.md README.md
%{_bindir}/gaupol
%{python_sitelib}/gaupol*
%{_datadir}/applications/io.otsaloma.gaupol.desktop
%{_mandir}/man1/gaupol.1*
%dir %{_datadir}/gaupol/
%{_datadir}/gaupol/ui/
%{_datadir}/gaupol/extensions/
%{_datadir}/icons/hicolor/*/apps/io.otsaloma.gaupol{,-symbolic}.*
%{_metainfodir}/io.otsaloma.gaupol.appdata.xml

%files -n python-aeidon
%doc README.aeidon.md
%{python_sitelib}/aeidon/
# aeidon shares data file location with gaupol
%{_datadir}/gaupol/headers/
%{_datadir}/gaupol/patterns/
