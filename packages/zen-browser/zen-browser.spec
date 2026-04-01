# Fedora Copr 仓库 https://copr.fedorainfracloud.org/coprs/architektapx/zen-browser/
# 参考文件 https://github.com/ArchitektApx/zen-browser-copr/blob/master/zen-browser.spec
# 源代码仓库 https://github.com/ArchitektApx/zen-browser-copr
# git clone --depth=1 https://github.com/ArchitektApx/zen-browser-copr.git


# ==============================================================================
# 1. 宏定义与全局设置
# ==============================================================================
%global             full_name zen-browser
%global             application_name zen
%global             debug_package %{nil}


# ==============================================================================
# 2. 包基本信息 (Header)
# ==============================================================================
Name:               zen-browser
Version:            1.19.5b
Release:            1%{?dist}
Summary:            Zen Browser
License:            MPLv2.0
URL:                https://github.com/zen-browser/desktop
Source0:            https://github.com/zen-browser/desktop/releases/download/1.19.5b/zen.linux-aarch64.tar.xz
Source1:            %{full_name}.desktop
Source2:            policies.json
Source3:            %{full_name}


# ==============================================================================
# 3. 依赖关系 (Build & Runtime Requirements)
# ==============================================================================
ExclusiveArch:      aarch64
Recommends:         (plasma-browser-integration if plasma-workspace)
Recommends:         (gnome-browser-connector if gnome-shell)
Requires(post):     gtk-update-icon-cache


# ==============================================================================
# 4. 描述信息
# ==============================================================================
%description
This is a package of the Zen web browser for aarch64. 
Zen Browser is a fork of Firefox that aims to improve the browsing experience by focusing on a simple,
performant, private and beautifully designed browser.
Bugs related to Zen should be reported directly to the Zen Browser GitHub repo: 
<https://github.com/zen-browser/desktop/issues>
Bugs related to this package should be reported at this Git project:
<https://github.com/ArchitektApx/zen-browser-copr>


# ==============================================================================
# 5. 准备阶段 (%prep)
# ==============================================================================
%prep
%setup -q -n %{application_name}

%install
%__rm -rf %{buildroot}

%__install -d %{buildroot}{/opt/%{full_name},%{_bindir},%{_datadir}/applications,%{_datadir}/icons/hicolor/128x128/apps,%{_datadir}/icons/hicolor/64x64/apps,%{_datadir}/icons/hicolor/48x48/apps,%{_datadir}/icons/hicolor/32x32/apps,%{_datadir}/icons/hicolor/16x16/apps}

%__cp -r * %{buildroot}/opt/%{full_name}

%__install -D -m 0644 %{SOURCE1} -t %{buildroot}%{_datadir}/applications

%__install -D -m 0444 %{SOURCE2} -t %{buildroot}/opt/%{full_name}/distribution

%__install -D -m 0755 %{SOURCE3} -t %{buildroot}%{_bindir}

%__ln_s ../../../../../../opt/%{full_name}/browser/chrome/icons/default/default128.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/%{full_name}.png
%__ln_s ../../../../../../opt/%{full_name}/browser/chrome/icons/default/default64.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/%{full_name}.png
%__ln_s ../../../../../../opt/%{full_name}/browser/chrome/icons/default/default48.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{full_name}.png
%__ln_s ../../../../../../opt/%{full_name}/browser/chrome/icons/default/default32.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{full_name}.png
%__ln_s ../../../../../../opt/%{full_name}/browser/chrome/icons/default/default16.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/%{full_name}.png

if [ -d /usr/share/hunspell ]; then ln -Tsf /usr/share/hunspell %{buildroot}/opt/%{full_name}/dictionaries; fi
if [ -d /usr/share/hyphen ]; then ln -Tsf /usr/share/hyphen %{buildroot}/opt/%{full_name}/hyphenation; fi

%post
gtk-update-icon-cache -f -t %{_datadir}/icons/hicolor

%files
%{_datadir}/applications/%{full_name}.desktop
%{_datadir}/icons/hicolor/128x128/apps/%{full_name}.png
%{_datadir}/icons/hicolor/64x64/apps/%{full_name}.png
%{_datadir}/icons/hicolor/48x48/apps/%{full_name}.png
%{_datadir}/icons/hicolor/32x32/apps/%{full_name}.png
%{_datadir}/icons/hicolor/16x16/apps/%{full_name}.png
%{_bindir}/%{full_name}
/opt/%{full_name}

%changelog
* Sun Mar 29 2026 ArchitektApx <architektapx@gehinors.ch> - 1.19.5b
- Update to upstream release 1.19.5b

* Sat Mar 28 2026 ArchitektApx <architektapx@gehinors.ch> - 1.19.3b
- Update to upstream release 1.19.3b

* Fri Mar 27 2026 ArchitektApx <architektapx@gehinors.ch> - 1.19.4b
- Update to upstream release 1.19.4b

* Mon Mar 16 2026 ArchitektApx <architektapx@gehinors.ch> - 1.19.3b
- Update to upstream release 1.19.3b

* Wed Mar 11 2026 ArchitektApx <architektapx@gehinors.ch> - 1.19.2b
- Update to upstream release 1.19.2b

* Thu Mar 05 2026 ArchitektApx <architektapx@gehinors.ch> - 1.19.1b
- Update to upstream release 1.19.1b

* Sun Mar 01 2026 ArchitektApx <architektapx@gehinors.ch> - 1.19b
- Update to upstream release 1.19b

* Sat Feb 21 2026 ArchitektApx <architektapx@gehinors.ch> - 1.18.10b
- Update to upstream release 1.18.10b

* Fri Feb 20 2026 ArchitektApx <architektapx@gehinors.ch> - 1.18.9b
- Update to upstream release 1.18.9b

* Tue Feb 17 2026 ArchitektApx <architektapx@gehinors.ch> - 1.18.8b
- Update to upstream release 1.18.8b

* Sat Feb 14 2026 ArchitektApx <architektapx@gehinors.ch> - 1.18.7b
- Update to upstream release 1.18.7b

* Fri Feb 13 2026 ArchitektApx <architektapx@gehinors.ch> - 1.18.6b
- Update to upstream release 1.18.6b

* Fri Feb 06 2026 ArchitektApx <architektapx@gehinors.ch> - 1.18.5b
- Update to upstream release 1.18.5b

* Wed Feb 04 2026 ArchitektApx <architektapx@gehinors.ch> - 1.18.4b
- Update to upstream release 1.18.4b

* Fri Jan 30 2026 ArchitektApx <architektapx@gehinors.ch> - 1.18.3b
- Update to upstream release 1.18.3b

* Wed Jan 28 2026 ArchitektApx <architektapx@gehinors.ch> - 1.18.2b
- Update to upstream release 1.18.2b

* Sun Jan 25 2026 ArchitektApx <architektapx@gehinors.ch> - 1.18.1b
- Update to upstream release 1.18.1b

* Sat Jan 24 2026 ArchitektApx <architektapx@gehinors.ch> - 1.18b
- Update to upstream release 1.18b

* Sun Jan 04 2026 ArchitektApx <architektapx@gehinors.ch> - 1.17.15b
- Update to upstream release 1.17.15b

* Sat Jan 03 2026 ArchitektApx <architektapx@gehinors.ch> - null
- Update to upstream release null

* Fri Jan 02 2026 ArchitektApx <architektapx@gehinors.ch> - 1.17.15b
- Update to upstream release 1.17.15b

* Thu Jan 01 2026 ArchitektApx <architektapx@gehinors.ch> - null
- Update to upstream release null
