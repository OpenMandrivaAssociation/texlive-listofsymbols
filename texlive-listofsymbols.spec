# revision 16134
# category Package
# catalog-ctan /macros/latex/contrib/listofsymbols
# catalog-date 2009-11-29 13:21:16 +0100
# catalog-license lppl
# catalog-version 0.2
Name:		texlive-listofsymbols
Version:	0.2
Release:	2
Summary:	Create and manipulate lists of symbols
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/listofsymbols
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/listofsymbols.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/listofsymbols.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/listofsymbols.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Listofsymbols provides commands to automatically create a list
of symbols (also called notation or nomenclature), and to
handle symbols logically, i.e. define a macro that is expanded
to the desired output and use the macro in the text rather than
`hardcoding' the output into the text. This helps to ensure
consistency throughout the text, especially if there is a
chance that symbols will be changed at some stage. The package
is more or less a combination of what the packages nomencl and
formula do. The concept of creating the list of symbols,
though, is different from the way nomencl.sty does it.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/listofsymbols/listofsymbols.sty
%doc %{_texmfdistdir}/doc/latex/listofsymbols/README
%doc %{_texmfdistdir}/doc/latex/listofsymbols/listofsymbols.pdf
#- source
%doc %{_texmfdistdir}/source/latex/listofsymbols/listofsymbols.dtx
%doc %{_texmfdistdir}/source/latex/listofsymbols/listofsymbols.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.2-2
+ Revision: 753400
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.2-1
+ Revision: 718870
- texlive-listofsymbols
- texlive-listofsymbols
- texlive-listofsymbols
- texlive-listofsymbols

