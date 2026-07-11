%global tl_name listofsymbols
%global tl_revision 16134

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2
Release:	%{tl_revision}.1
Summary:	Create and manipulate lists of symbols
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/listofsymbols
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/listofsymbols.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/listofsymbols.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/listofsymbols.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Listofsymbols provides commands to automatically create a list of
symbols (also called notation or nomenclature), and to handle symbols
logically, i.e. define a macro that is expanded to the desired output
and use the macro in the text rather than `hardcoding' the output into
the text. This helps to ensure consistency throughout the text,
especially if there is a chance that symbols will be changed at some
stage. The package is more or less a combination of what the packages
nomencl and formula do. The concept of creating the list of symbols,
though, is different from the way nomencl.sty does it.

