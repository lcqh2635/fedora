# git clone --depth=1 https://github.com/hermes83/compiz-alike-magic-lamp-effect.git
# cd compiz-alike-magic-lamp-effect

%global uuid s76-scheduler@mattjakeman.com

# 定义软件包名、版本、发布号。版本号可从仓库的 metadata.json 或 Tag 中获取
Name:        gnome-shell-extension-system76-scheduler
Version:     {{{ git_dir_version }}}
Release:     1%{?dist}
Summary:	 Standalone GNOME Shell integration for system76-scheduler to make the desktop more responsive.

# 许可证和项目主页，请根据仓库信息填写
Group:       User Interface/Desktops
License:     GPLv3
URL:         https://github.com/KyleGospo/s76-scheduler-plugin
Source0:     https://github.com/KyleGospo/s76-scheduler-plugin/archive/refs/heads/master.tar.gz


BuildArch:   noarch

Requires:    gnome-shell >= 3.12
Requires:    system76-scheduler

# 描述
%description
This is a standalone extension that integrates system76-scheduler without needing pop-shell installed. The majority of code in this plugin comes from pop-shell and is used under the GPL-3.0 licence.

# 准备阶段：解压源码
%prep
%autosetup -n s76-scheduler-plugin-master

# 构建阶段：这是关键，将扩展文件复制到正确位置
%build
# Nothing to build

# 安装阶段：这是关键，将扩展文件复制到正确位置
%install
mkdir -p %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}
install -Dp -m 0644 {extension.js,metadata.json} \
  %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}/

# 清理：确保不打包 .git 等无关目录
rm -rf %{buildroot}%{_datadir}/gnome-shell/extensions/%{name}/.git

# 定义哪些文件将被打入最终的RPM包
%files
%license LICENSE
%{_datadir}/gnome-shell/extensions/%{uuid}/

# 更新日志（可选，但建议记录）
# 修正日期格式：将未来的日期 2026 改为过去或现在的有效日期
%changelog
{{{ git_dir_changelog }}}
