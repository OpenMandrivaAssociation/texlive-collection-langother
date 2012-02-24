# revision 22908
# category Collection
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collection-langother
Epoch:		1
Version:	20120224
Release:	1
Summary:	Other hyphenation patterns
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-langother.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-hyphen-afrikaans
Requires:	texlive-hyphen-armenian
Requires:	texlive-hyphen-coptic
Requires:	texlive-hyphen-esperanto
Requires:	texlive-hyphen-estonian
Requires:	texlive-hyphen-icelandic
Requires:	texlive-hyphen-indonesian
Requires:	texlive-hyphen-interlingua
Requires:	texlive-hyphen-irish
Requires:	texlive-hyphen-kurmanji
Requires:	texlive-hyphen-lao
Requires:	texlive-hyphen-romanian
Requires:	texlive-hyphen-serbian
Requires:	texlive-hyphen-slovenian
Requires:	texlive-hyphen-turkish
Requires:	texlive-hyphen-uppersorbian
Requires:	texlive-hyphen-welsh
Requires:	texlive-collection-basic

%description
Hyphenation patterns for languages without (much) other
support.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
