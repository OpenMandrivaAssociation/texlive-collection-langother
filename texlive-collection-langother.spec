%global tl_name collection-langother
%global tl_revision 78607

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Other languages
Group:		Publishing
URL:		https://www.ctan.org/pkg/collection-langother
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-langother.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Requires:	texlive(aalok)
Requires:	texlive(akshar)
Requires:	texlive(amsldoc-vn)
Requires:	texlive(aramaic-serto)
Requires:	texlive(babel-azerbaijani)
Requires:	texlive(babel-esperanto)
Requires:	texlive(babel-georgian)
Requires:	texlive(babel-hebrew)
Requires:	texlive(babel-indonesian)
Requires:	texlive(babel-interlingua)
Requires:	texlive(babel-malay)
Requires:	texlive(babel-sorbian)
Requires:	texlive(babel-thai)
Requires:	texlive(babel-vietnamese)
Requires:	texlive(bangla)
Requires:	texlive(bangtex)
Requires:	texlive(bengali)
Requires:	texlive(burmese)
Requires:	texlive(chhaya)
Requires:	texlive(cjhebrew)
Requires:	texlive(collection-basic)
Requires:	texlive(ctib)
Requires:	texlive(culmus)
Requires:	texlive(ebong)
Requires:	texlive(ethiop)
Requires:	texlive(ethiop-t1)
Requires:	texlive(fc)
Requires:	texlive(fonts-arundina)
Requires:	texlive(fonts-tlwg)
Requires:	texlive(hebrew-fonts)
Requires:	texlive(hindawi-latex-template)
Requires:	texlive(hyphen-afrikaans)
Requires:	texlive(hyphen-armenian)
Requires:	texlive(hyphen-coptic)
Requires:	texlive(hyphen-esperanto)
Requires:	texlive(hyphen-ethiopic)
Requires:	texlive(hyphen-georgian)
Requires:	texlive(hyphen-hebrew)
Requires:	texlive(hyphen-indic)
Requires:	texlive(hyphen-indonesian)
Requires:	texlive(hyphen-interlingua)
Requires:	texlive(hyphen-sanskrit)
Requires:	texlive(hyphen-thai)
Requires:	texlive(hyphen-turkmen)
Requires:	texlive(hyphen-vietnamese)
Requires:	texlive(latex-mr)
Requires:	texlive(latexbangla)
Requires:	texlive(latino-sine-flexione)
Requires:	texlive(lshort-thai)
Requires:	texlive(lshort-vietnamese)
Requires:	texlive(marathi)
Requires:	texlive(ntheorem-vn)
Requires:	texlive(quran-bn)
Requires:	texlive(quran-id)
Requires:	texlive(quran-ur)
Requires:	texlive(sanskrit)
Requires:	texlive(sanskrit-t1)
Requires:	texlive(thaienum)
Requires:	texlive(thaispec)
Requires:	texlive(tuzuk)
Requires:	texlive(unicode-alphabets)
Requires:	texlive(velthuis)
Requires:	texlive(vntex)
Requires:	texlive(wnri)
Requires:	texlive(wnri-latex)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Support for languages not otherwise listed, including Indic, Thai,
Vietnamese, Hebrew, Indonesian, African languages, and plenty more. The
split is made simply on the basis of the size of the support, to keep
both collection sizes and the number of collections reasonable.

