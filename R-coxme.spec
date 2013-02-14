%global packname  coxme
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          2.2.3
Release:          1
Summary:          Mixed Effects Cox Models
Group:            Sciences/Mathematics
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/coxme_2.2-3.tar.gz
Requires:         R-survival R-bdsmatrix R-nlme R-Matrix R-methods
Requires:         R-mvtnorm R-kinship2
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-survival
BuildRequires:    R-bdsmatrix R-nlme R-Matrix R-methods R-mvtnorm R-kinship2

%description
Cox proportional hazards models containing Gaussian random effects, also
known as frailty models.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
