Name:           plasma-pipewire-settings
Version:        1.2
Release:        1%{?dist}
Summary:        Simple Plasma 6 widget to change Pipewire quantum and sample rate

License:        GPL-3.0-only
URL:            https://github.com/magillos/Pipewire-Settings-Widget-for-Plasma-6
Source0:        %{url}/archive/refs/heads/main.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       plasma-desktop

%description
An easy-to-use widget to change Pipewire's quantum and sample rate from
the KDE Plasma 6 Desktop Environment.

%prep
%autosetup -n Pipewire-Settings-Widget-for-Plasma-6-main

%build
# No build required

%install
mkdir -p %{buildroot}%{_datadir}/plasma/plasmoids/org.kde.plasma.pipewiresettings
cp -r package/* %{buildroot}%{_datadir}/plasma/plasmoids/org.kde.plasma.pipewiresettings/

%files
%license LICENSE
%doc README.md
%{_datadir}/plasma/plasmoids/org.kde.plasma.pipewiresettings/

%changelog
* Thu Jan 15 2026 Erich Eickmeyer <erich@ericheickmeyer.com> - 1.2-1
- Initial RPM package