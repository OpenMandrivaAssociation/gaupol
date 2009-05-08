Name:           gaupol
Version:        0.14
Release:        %mkrel 1
Summary:        Subtitle editor
License:        GPLv3+
Group:          Video
URL:            http://home.gna.org/gaupol/
Source0:        http://download.gna.org/gaupol/0.14/%{name}-%{version}.tar.bz2
Source1:        http://download.gna.org/gaupol/0.14/%{name}-%{version}.tar.bz2.sig
BuildRequires:  desktop-file-utils
BuildRequires:  intltool
%{py_requires -d}
Requires:	pygtk2.0
Requires:	pygtk2.0-libglade
Suggests:	python-enchant
Suggests:	python-chardet
Suggests:	mplayer
%if %mdkversion < 200900
Requires(post): desktop-common-data
Requires(postun): desktop-common-data
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
%endif
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Editor for text-based subtitle files. It supports multiple subtitle file 
formats and provides means of correcting texts and timing subtitles to match
video. The user interface is designed with attention to batch processing of
multiple documents and convenience of translating.

%prep
%setup -q

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install --root=%{buildroot}
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%if %mdkversion < 200900
%post
%{update_desktop_database}
%{update_menus}

%postun
%{clean_desktop_database}
%{clean_menus}
%endif

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS NEWS README TODO
%{_bindir}/gaupol
%{python_sitelib}/gaupol*
%{_datadir}/applications/gaupol.desktop
%{_mandir}/man1/gaupol.1*
%{_datadir}/gaupol
%{_datadir}/icons/hicolor/*/apps/gaupol.*

