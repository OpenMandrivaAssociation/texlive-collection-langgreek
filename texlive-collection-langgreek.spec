# revision 15748
# category Collection
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collection-langgreek
Version:	20120223
Release:	1
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
