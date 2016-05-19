%define debug_package %{nil}

%{!?luaver: %global luaver %(lua -e "print(string.sub(_VERSION, 5))")}
# for arch-independent modules
%global luapkgdir %{_datadir}/lua/%{luaver}

%define vermagic1 2.5
%define vermagic2 5

Name:           lua-cliargs
Version:        %{vermagic1}_%{vermagic2}
Release:        1%{?dist}
Summary:        A command-line argument parsing module for Lua

License:        MIT
URL:            https://github.com/amireh/lua_cliargs/
Source0:        https://github.com/amireh/lua_cliargs/archive/v%{vermagic1}-%{vermagic2}.tar.gz

BuildArch:      noarch
BuildRequires:  lua-devel >= %{luaver}
%if 0%{?rhel} == 6
Requires:       lua >= %{luaver}
Requires:       lua < 5.2
%else
Requires:       lua(abi) >= %{luaver}
%endif


%description
lua-cliargs is a command-line argument parser for Lua.


%prep
%setup -q -n lua_cliargs-%{vermagic1}-%{vermagic2}


%build


%install
install -p -m644 -D src/cliargs.lua %{buildroot}%{luapkgdir}/cliargs.lua


%files
%license LICENSE
%doc README.md doc examples
%{luapkgdir}/cliargs.lua


%changelog
* Thu May 19 2016 Jajauma's Packages <jajauma@yandex.ru> - 2.5_5-1
- Public release
