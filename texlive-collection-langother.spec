# revision 31014
# category Collection
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collection-langother
Epoch:		1
Version:	20131013
Release:	1
Summary:	Other languages
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-langother.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-collection-basic
Requires:	texlive-amsldoc-vn
Requires:	texlive-aramaic-serto
Requires:	texlive-babel-bahasa
Requires:	texlive-babel-esperanto
Requires:	texlive-babel-georgian
Requires:	texlive-babel-hebrew
Requires:	texlive-babel-interlingua
Requires:	texlive-babel-sorbian
Requires:	texlive-babel-thai
Requires:	texlive-babel-vietnamese
Requires:	texlive-cjhebrew
Requires:	texlive-ctib
Requires:	texlive-fonts-tlwg
Requires:	texlive-hyphen-afrikaans
Requires:	texlive-hyphen-coptic
Requires:	texlive-hyphen-esperanto
Requires:	texlive-hyphen-georgian
Requires:	texlive-hyphen-indonesian
Requires:	texlive-hyphen-interlingua
Requires:	texlive-hyphen-thai
Requires:	texlive-hyphen-turkmen
Requires:	texlive-lshort-thai
Requires:	texlive-lshort-vietnamese
Requires:	texlive-ntheorem-vn
Requires:	texlive-vntex

%description
Support for languages not otherwise listed, including Thai,
Vietnamese, Hebrew, Indonesian, and plenty more.  The split is
made simply on the basis of the size of the support, to keep
both collection sizes and the number of collections reasonable.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
