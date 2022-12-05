Name: {{{ git_dir_name }}}
Version: 0.1.0
Release: 1%{?dist}
Summary: Lua functions and utilities specifically for Hilbish.
License: MIT

Source: {{{ git_dir_pack }}}

Url: https://github.com/Rosettea/succulent
VCS: {{{ git_dir_vcs }}}
BuildArch: noarch

%description
Succulent is a small and simple pure Lua library which adds extra useful functions
to the standard library. Succulent is made for Hilbish specifically.

%prep
{{{ git_dir_setup_macro }}}

%build

%install
install -Dm644 init.lua -t %{buildroot}/usr/share/hilbish/libs/succulent/

%files
%doc README.md
%license LICENSE
/usr/share/hilbish/libs/succulent/init.lua
