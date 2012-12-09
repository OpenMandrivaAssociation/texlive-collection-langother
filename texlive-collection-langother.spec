# revision 26614
# category Collection
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collection-langother
Epoch:		1
Version:	20120810
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
Requires:	texlive-hyphen-friulan
Requires:	texlive-hyphen-icelandic
Requires:	texlive-hyphen-indonesian
Requires:	texlive-hyphen-interlingua
Requires:	texlive-hyphen-irish
Requires:	texlive-hyphen-kurmanji
Requires:	texlive-hyphen-romanian
Requires:	texlive-hyphen-romansh
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


%changelog
* Fri Aug 10 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:20120810-1
+ Revision: 813928
- Update to latest release.

* Fri Feb 24 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:20120224-1
+ Revision: 780451
- Update to latest release.
- Import texlive-collection-langother
- Import texlive-collection-langother

