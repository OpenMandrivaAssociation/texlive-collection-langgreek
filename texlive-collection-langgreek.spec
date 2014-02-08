# revision 26262
# category Collection
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collection-langgreek
Epoch:		1
Version:	20120810
Release:	2
Summary:	Greek
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-langgreek.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-betababel
Requires:	texlive-bgreek
Requires:	texlive-cbfonts
Requires:	texlive-gfsbaskerville
Requires:	texlive-gfsporson
Requires:	texlive-greek-inputenc
Requires:	texlive-greekdates
Requires:	texlive-greektex
Requires:	texlive-grverb
Requires:	texlive-ibycus-babel
Requires:	texlive-ibygrk
Requires:	texlive-kerkis
Requires:	texlive-levy
Requires:	texlive-lgreek
Requires:	texlive-lgrx
Requires:	texlive-mkgrkindex
Requires:	texlive-teubner
Requires:	texlive-xgreek
Requires:	texlive-yannisgr
Requires:	texlive-hyphen-greek
Requires:	texlive-hyphen-ancientgreek
Requires:	texlive-collection-basic

%description
Support for typesetting Greek.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install


%changelog
* Fri Aug 10 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:20120810-1
+ Revision: 813926
- Update to latest release.

* Fri Feb 24 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:20120224-1
+ Revision: 780417
- Update to latest release.
- Import texlive-collection-langgreek
- Import texlive-collection-langgreek

