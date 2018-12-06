# Run tests in check section
%bcond_without check

%global goipath         github.com/jellevandenhooff/dkim
%global commit          f50fe3d243e1a9c9369eea29813517f3af190518

%global common_description %{expand:
Pure Go DKIM verification library.}

%gometa

Name:           %{goname}
Version:        0
Release:        0.2%{?dist}
Summary:        Pure Go DKIM verification library
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.gitf50fe3d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 24 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1-20180417gitf50fe3d
- First package for Fedora

