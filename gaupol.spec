Name:           gaupol
Version:        0.17.2
Release:        %mkrel 1
Summary:        Subtitle editor
License:        GPLv3+
Group:          Video
URL:            http://home.gna.org/gaupol/
Source0:        http://download.gna.org/gaupol/0.17/%{name}-%{version}.tar.bz2
Source1:        http://download.gna.org/gaupol/0.17/%{name}-%{version}.tar.bz2.sig
BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:	python-devel
Requires:	pygtk2.0 >= 2.16
Requires:	python-aeidon
Suggests:	python-enchant >= 1.4.0
Suggests:	python-chardet
Suggests:	mplayer
BuildArch:      noarch

%package -n python-aeidon
Summary:	Python package for Reading, writing and manipulating text-based subtitle files
Group:		Development/Python
Url:		http://users.tkk.fi/~otsaloma/gaupol/doc/api/aeidon.html
Provides:	aeidon = %{version}-%{release}

%description
Editor for text-based subtitle files. It supports multiple subtitle file 
formats and provides means of correcting texts and timing subtitles to match
video. The user interface is designed with attention to batch processing of
multiple documents and convenience of translating.

%description -n python-aeidon
aeidon is a Python package that provides classes and functions for dealing
with text-based subtitle files of many different formats. Functions exist
for reading and writing subtitle files as well as manipulating subtitle data,
i.e. positions (times or frames) and texts.

%prep
%setup -q

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install \
	--root=%{buildroot} \
	--no-compile

%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS NEWS README TODO
%{_bindir}/gaupol
%{python_sitelib}/gaupol*
%{_datadir}/applications/gaupol.desktop
%{_mandir}/man1/gaupol.1*
%{_datadir}/gaupol
%{_datadir}/icons/hicolor/*/apps/gaupol.*

%files -n python-aeidon
%doc README.aeidon
%{python_sitelib}/aeidon/
