Name:		texlive-iso
Version:	15878
Release:	1
Summary:	Generic ISO standards typesetting macros
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/isostds/iso
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/iso.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/iso.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/iso.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%define		_unpackaged_subdirs_terminate_build	0

%description
Generic class and package files for typesetting ISO
International Standard documents. Several standard documents
have been printed by ISO from camera-ready copy prepared using
LaTeX and these files.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/makeindex/iso/iso.ist
%{_texmfdistdir}/tex/latex/iso/askincv1.sty
%{_texmfdistdir}/tex/latex/iso/iso10.clo
%{_texmfdistdir}/tex/latex/iso/iso11.clo
%{_texmfdistdir}/tex/latex/iso/iso9.clo
%{_texmfdistdir}/tex/latex/iso/isov2.4ht
%{_texmfdistdir}/tex/latex/iso/isov2.cls
%doc %{_texmfdistdir}/doc/latex/iso/README
%doc %{_texmfdistdir}/doc/latex/iso/iso4ht.pdf
%doc %{_texmfdistdir}/doc/latex/iso/isoe.pdf
%doc %{_texmfdistdir}/doc/latex/iso/isofwdbp.tex
%doc %{_texmfdistdir}/doc/latex/iso/isoman.pdf
%doc %{_texmfdistdir}/doc/latex/iso/isoman.tex
%doc %{_texmfdistdir}/doc/latex/iso/trfwd1.tex
%doc %{_texmfdistdir}/doc/latex/iso/tspasfwdbp.tex
#- source
%doc %{_texmfdistdir}/source/latex/iso/iso4ht.dtx
%doc %{_texmfdistdir}/source/latex/iso/iso4ht.ins
%doc %{_texmfdistdir}/source/latex/iso/isoe.dtx
%doc %{_texmfdistdir}/source/latex/iso/isoe.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar makeindex tex doc source %{buildroot}%{_texmfdistdir}
