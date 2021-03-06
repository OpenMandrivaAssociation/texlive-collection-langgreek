# revision 31679
# category Collection
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collection-langgreek
Epoch:		1
Version:	20190228
Release:	1
Summary:	Greek
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-langgreek.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-collection-basic
Requires:	texlive-babel-greek
Requires:	texlive-betababel
Requires:	texlive-bgreek
Requires:	texlive-cbfonts
Requires:	texlive-cbfonts-fd
Requires:	texlive-gfsbaskerville
Requires:	texlive-gfsporson
Requires:	texlive-greek-fontenc
Requires:	texlive-greek-inputenc
Requires:	texlive-greekdates
Requires:	texlive-greektex
Requires:	texlive-hyphen-greek
Requires:	texlive-hyphen-ancientgreek
Requires:	texlive-ibycus-babel
Requires:	texlive-ibygrk
Requires:	texlive-kerkis
Requires:	texlive-levy
Requires:	texlive-lgreek
Requires:	texlive-mkgrkindex
Requires:	texlive-teubner
Requires:	texlive-xgreek
Requires:	texlive-yannisgr

%description
Support for Greek.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
