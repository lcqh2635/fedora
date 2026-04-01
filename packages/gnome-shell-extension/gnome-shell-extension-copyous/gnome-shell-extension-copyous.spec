# ==============================================================================
# 1. 宏定义与全局设置
# ==============================================================================
# 禁用默认的 debuginfo 包生成，因为扩展通常不需要调试符号
%global debug_package %{nil}
# 定义扩展的 UUID，这是 GNOME Shell 识别扩展的唯一 ID
%global uuid copyous@boerdereinar.dev


# ==============================================================================
# 2. 包基本信息 (Header)
# ==============================================================================
# 包的名称。通常与扩展名或项目名一致。
Name:           gnome-shell-extension-copyous
# 版本号。
# 建议通过自动化工具（如 Renovate）管理，保持与 GitHub Release 同步。
Version:        2.0.0
# 发布版本。
# 每次修改 Spec 文件但未升级软件版本时，递增此数字。
Release:        3%{?dist}
# 简短描述。出现在软件中心的列表中。
Summary:        Modern Clipboard Manager for GNOME
# 许可证类型。必须与源码中的 LICENSE 文件一致。
License:        GPL-3.0-or-later
# 项目主页 URL。
URL:            https://github.com/boerdereinar/copyous
# 源代码压缩包。可以指向 GitHub 的 Release 或直接使用克隆的源码
# 方式1：指向 Release (推荐)
# 这里假设源码是以 Zip 包形式发布，且文件名包含 UUID
Source0:        https://github.com/boerdereinar/copyous/releases/download/v%{version}/%{uuid}.zip
# 方式2：使用本地克隆目录打包（用于测试）
# Source0: %{name}-%{version}.tar.gz

# ==============================================================================
# 3. 依赖关系 (Build & Runtime Requirements)
# ==============================================================================
# --- 构建依赖 (BuildRequires) 这些是编译或打包过程中需要的工具，用户安装时不需要 ---
# glib2-devel: 提供 glib-compile-schemas 工具。
# 这是必须的，因为我们需要在打包时或安装时编译 GSettings 的 XML 模式文件。
BuildRequires:  glib2-devel
# gnome-shell-devel: 提供 GNOME Shell 的开发宏和头文件。
# 虽然不是所有扩展都严格需要，但加上它可以确保环境一致性。
BuildRequires:  gnome-shell-devel
# --- 运行依赖 (Requires) 用户安装此包时必须存在的软件 ---
# gnome-shell: 扩展运行的宿主环境。
Requires:       gnome-shell
# glib2: 运行时库，用于处理 GSettings 配置。
Requires:       glib2
# --- 推荐依赖 (Recommends) 非强制，但强烈建议安装以获得完整功能 ---
# libgda-sqlite: Copyous 使用 SQLite 数据库存储剪贴板历史。
# 如果没有这个，扩展可能无法保存数据。使用 Recommends 而非 Requires 可以
# 避免在某些最小化安装环境中产生冲突。
Recommends:     libgda-sqlite
# --- 架构 ---
# noarch 表示此包不包含任何与 CPU 架构相关的二进制文件（如 C 编译的程序）。
# 它可以在 x86_64, aarch64 等任何架构上运行。
BuildArch:      noarch


# ==============================================================================
# 4. 描述信息
# ==============================================================================
%description
Copyous 是一个专为 GNOME 桌面设计的现代化剪贴板管理器。
它允许用户保存复制历史，快速搜索并重新粘贴之前的内容，
极大地提升了办公效率。


# ==============================================================================
# 5. 准备阶段 (%prep)
# ==============================================================================
# 准备阶段：解压源码
%prep
# -c: 创建目录
# -T: 不使用默认的 tar 结构（因为我们下载的是 zip 且结构可能不标准）
# -a 0: 使用 Source0
%setup -c -T -a 0

# 将下载的源码目录重命名为标准的 %{name}-%{version}，确保后续步骤能正确找到文件
mv %{uuid} %{name}-%{version}

%build
# 对于纯 JavaScript 的 GNOME 扩展，通常不需要编译步骤
# 如果项目有构建脚本（如 make, npm build），请在此处添加
# 本例中留空

%install
mkdir -p %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}
cp -r -p * %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}/
glib-compile-schemas %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}/schemas

cp %{SOURCE1} ./
cp %{SOURCE2} ./

%files
%license LICENSE
%doc README.md
%{_datadir}/gnome-shell/extensions/%{uuid}

%changelog
%autochangelog
