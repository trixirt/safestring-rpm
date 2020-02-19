Summary:        Safestring a C11 Appendix K library
Name:           safestring
Version:        1.0.0
Release:        1
License:        MIT
Group:          Development/Libraries
Vendor:         Intel Corporation
Requires:       
URL:            https://github.com/intel/safestringlib/
Source0:        https://github.com/intel/safestringlib/archive/v%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  cmake

%description
Provides C11 Appendix K functions.

%package devel
Summary:    headers, sample source, and documentation
Group:      Development/Libraries

%description devel
headers, sample source, and documentation

%prep
%setup -q -n safestringlib-%{version}

%build
mkdir -p obj
make -j

%install
false


%clean

%post
ldconfig

%postun
ldconfig

%pre

%preun

%files
%defattr(-,root,root,-)

%files devel
%defattr(-,root,root,-)

%changelog

