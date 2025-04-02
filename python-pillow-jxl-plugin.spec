Name:		python-pillow-jxl-plugin
Version:	1.3.2
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/p/pillow_jxl_plugin/pillow_jxl_plugin-%{version}.tar.gz
Summary:	Pillow plugin for JPEG-XL
URL:		https://pypi.org/project/pillow-jxl-plugin
License:	GPL3.0
Group:		Development/Python
BuildRequires:  rust-packaging
BuildRequires:  pkgconfig(python3)
BuildRequires:	python%{py_ver}dist(pip)
BuildRequires:  python%{py_ver}dist(maturin)
BuildRequires:  pkgconfig(libjxl)
BuildSystem:  python
BuildArch:	noarch

%description
Pillow plugin for JPEG-XL, using Rust for bindings.

%files
%license LICENSE
%doc README.md
