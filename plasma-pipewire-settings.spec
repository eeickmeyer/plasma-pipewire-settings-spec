%global commit 601eb68e778f4507cec98c951b8f6cec3633efd5
%global shortcommit %{sub %{commit} 1 7}
%global commitdate 20251231

Name:           plasma-pipewire-settings
Version:        1.2~git%{commitdate}.%{shortcommit}
Release:        1%{?dist}
Summary:        Simple Plasma 6 widget to change Pipewire quantum and sample rate

License:        GPL-3.0-or-later
URL:            https://github.com/magillos/Pipewire-Settings-Widget-for-Plasma-6
Source0:        %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz
Patch0:         change_namespace.patch

BuildArch:      noarch

Requires:       plasma-desktop

%description
An easy-to-use widget to change Pipewire's quantum and sample rate from
the KDE Plasma 6 Desktop Environment.

%prep
%autosetup -C
%patch 0 -p1

%build
# No build required

%install
mkdir -p %{buildroot}%{_datadir}/plasma/plasmoids/com.github.magillos.pipewiresettings
cp -r package/* %{buildroot}%{_datadir}/plasma/plasmoids/com.github.magillos.pipewiresettings/

%files
%license LICENSE
%doc README.md
%{_datadir}/plasma/plasmoids/com.github.magillos.pipewiresettings/

%changelog
* Thu Jan 15 2026 Erich Eickmeyer <erich@ericheickmeyer.com> - 1.2-1
- Initial RPM package