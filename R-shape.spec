#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-shape
Version  : 1.4.4
Release  : 18
URL      : https://cran.r-project.org/src/contrib/shape_1.4.4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/shape_1.4.4.tar.gz
Summary  : Functions for Plotting Graphical Shapes, Colors
Group    : Development/Tools
License  : GPL-3.0
BuildRequires : buildreq-R

%description
such as ellipses, circles, cylinders, arrows, ...

%prep
%setup -q -c -n shape

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552942240

%install
export SOURCE_DATE_EPOCH=1552942240
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library shape
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library shape
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library shape
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  shape || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/shape/DESCRIPTION
/usr/lib64/R/library/shape/INDEX
/usr/lib64/R/library/shape/Meta/Rd.rds
/usr/lib64/R/library/shape/Meta/demo.rds
/usr/lib64/R/library/shape/Meta/features.rds
/usr/lib64/R/library/shape/Meta/hsearch.rds
/usr/lib64/R/library/shape/Meta/links.rds
/usr/lib64/R/library/shape/Meta/nsInfo.rds
/usr/lib64/R/library/shape/Meta/package.rds
/usr/lib64/R/library/shape/Meta/vignette.rds
/usr/lib64/R/library/shape/NAMESPACE
/usr/lib64/R/library/shape/R/shape
/usr/lib64/R/library/shape/R/shape.rdb
/usr/lib64/R/library/shape/R/shape.rdx
/usr/lib64/R/library/shape/demo/colorshapes.r
/usr/lib64/R/library/shape/doc/index.html
/usr/lib64/R/library/shape/doc/shape.R
/usr/lib64/R/library/shape/doc/shape.Rnw
/usr/lib64/R/library/shape/doc/shape.pdf
/usr/lib64/R/library/shape/help/AnIndex
/usr/lib64/R/library/shape/help/aliases.rds
/usr/lib64/R/library/shape/help/paths.rds
/usr/lib64/R/library/shape/help/shape.rdb
/usr/lib64/R/library/shape/help/shape.rdx
/usr/lib64/R/library/shape/html/00Index.html
/usr/lib64/R/library/shape/html/R.css
