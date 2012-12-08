Name:           gaupol
Version:        0.18
%define subrel 1
Release:        %mkrel 2
Summary:        Subtitle editor
License:        GPLv3+
Group:          Video
URL:            http://home.gna.org/gaupol/
Source0:        http://download.gna.org/gaupol/0.18/%{name}-%{version}.tar.bz2
Source1:        http://download.gna.org/gaupol/0.18/%{name}-%{version}.tar.bz2.sig
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


%changelog
* Tue Sep 20 2011 Oden Eriksson <oeriksson@mandriva.com> 0.18-1.1
- built for updates

* Mon May 30 2011 Jani Välimaa <wally@mandriva.org> 0.18-1mdv2011.0
+ Revision: 681954
- new version 0.18

* Sun Apr 10 2011 Jani Välimaa <wally@mandriva.org> 0.17.2-1
+ Revision: 652324
- drop upstream applied patch
- drop buildroot definition
- update to new version 0.17.2

* Sun Apr 03 2011 Jani Välimaa <wally@mandriva.org> 0.17.1-2
+ Revision: 650092
- add patch to fix crash on startup

* Sun Nov 07 2010 Jani Välimaa <wally@mandriva.org> 0.17.1-1mdv2011.0
+ Revision: 594692
- new version 0.17.1
- drop obsolete py_requires macro
- disable byte-compiling

* Sun Oct 31 2010 Funda Wang <fwang@mandriva.org> 0.17-2mdv2011.0
+ Revision: 590864
- rebuild for py 2.7

* Sat Aug 07 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.17-1mdv2011.0
+ Revision: 567460
- update to 0.17
- remove 'mdkversion < 200900' bits, too old
- improve aeidon description

* Sat Jul 10 2010 Jani Välimaa <wally@mandriva.org> 0.16.2-1mdv2011.0
+ Revision: 550055
- new version 0.16.2
- fix requires/suggests
- split aeidon to a separate package

* Wed Mar 24 2010 Jani Välimaa <wally@mandriva.org> 0.15.1-1mdv2010.1
+ Revision: 527161
- enable byte-compiling
- new version 0.15.1

* Sun May 17 2009 Funda Wang <fwang@mandriva.org> 0.15-1mdv2010.0
+ Revision: 376519
- New version 0.15

* Sat May 09 2009 Anssi Hannula <anssi@mandriva.org> 0.14-1mdv2010.0
+ Revision: 373585
- initial Mandriva release (by Jani V?\195?\164limaa)

