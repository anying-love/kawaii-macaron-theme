# Kawaii Macaron Theme · 卡哇伊马卡龙主题

一款软萌马卡龙风格的 VS Code 主题。整体走「甜软少女感」路线：低饱和暖调粉色做边框与点缀，代码区用暖黄或奶油白打底，配色柔和但不失代码可读性。

## 特色

- **粉色边框**：编辑区、侧边栏、标签页、面板、状态栏等所有分界线统一使用低饱和暖调粉色，甜而不腻。
- **护眼暖调代码区**：暖黄 / 奶油白两种底色，长时间写代码不刺眼。
- **马卡龙配色**：粉、白、米奶白、暖黄为主，注释、关键字、字符串等用低饱和甜色区分，层次清晰。
- **代码友好**：语法高亮经过对比度权衡，保证在浅色背景上依然清晰可读。

## 两个主题变体

| 变体 | 代码区底色 | 适合场景 |
| --- | --- | --- |
| `Kawaii Macaron · Warm Yellow 暖黄` | 暖黄 `#FFF7E5` | 偏爱奶油暖阳感，长时间阅读更柔和 |
| `Kawaii Macaron · Cream Milk 奶油白` | 奶油白 `#FDF5F0` | 偏爱清爽粉白感，界面更素净 |

两个变体的边框、侧边栏、标签页、状态栏均为同一套粉色系，仅在代码区与部分背景上略有差异。

## 色板

| 用途 | 颜色 | 色值 |
| --- | --- | --- |
| 边框粉 | 低饱和暖粉 | `#F2B4C4` |
| 强调粉（光标/激活） | 樱花粉 | `#E58AA8` |
| 活动栏 | 樱花粉底 | `#F7DAE2` |
| 侧边栏 | 米奶白 | `#FAF3E7` |
| 代码区（暖黄款） | 暖黄 | `#FFF7E5` |
| 代码区（奶油款） | 奶油白 | `#FDF5F0` |
| 关键字 | 覆盆子粉 | `#C2587F` |
| 字符串 | 焦糖棕 | `#A8763F` |
| 数字 | 蜜桃橙 | `#C0784F` |
| 注释 | 奶茶灰 | `#A79380` |

## 安装

### 方式一：VSIX 安装包（推荐）

1. 在 VS Code 中按 `Ctrl+Shift+P`，输入 `Extensions: Install from VSIX...` 并回车。
2. 选择 `kawaii-macaron-theme-1.0.0.vsix`。
3. 重启 VS Code 后，`Ctrl+K Ctrl+T` 选择主题即可。

### 方式二：源码安装（开发调试用）

把整个 `vscode-kawaii-macaron-theme` 文件夹复制到 VS Code 扩展目录：

- Windows: `%USERPROFILE%\.vscode\extensions\`
- macOS: `~/.vscode/extensions/`
- Linux: `~/.vscode/extensions/`

复制后重启 VS Code，在主题选择器中即可看到两个主题。

### 方式三：从源码重新打包

无需安装 `vsce`，直接运行仓库自带的打包脚本（仅需 Python 3 + 标准库）：

```bash
python scripts/build_vsix.py
```

会在项目根目录生成 `kawaii-macaron-theme-<version>.vsix`，再用方式一安装即可。

### 方式四：开发者调试运行

用 VS Code 打开本目录，按 `F5` 启动扩展开发宿主，实时预览主题效果。

## 自定义

主题为纯 JSON，直接编辑 `themes/kawaii-macaron-warm.json` 或 `themes/kawaii-macaron-cream.json`：

- 想换代码区底色：改 `colors` 里的 `"editor.background"` 和 `"editorGutter.background"`。
- 想换边框粉：全局搜索 `#F2B4C4` 替换为你喜欢的粉色。
- 想调语法颜色：改 `tokenColors` 里对应项的 `foreground`。

改完保存后，在 VS Code 里重新选择一次主题即可生效。

## 项目结构

```
vscode-kawaii-macaron-theme/
├── package.json           # 扩展清单（声明两个主题）
├── themes/                # 主题配色定义（核心）
│   ├── kawaii-macaron-warm.json     # 暖黄款
│   └── kawaii-macaron-cream.json    # 奶油白款
├── images/icon.png        # 扩展图标（128×128 马卡龙）
├── scripts/
│   ├── make_icon.py       # 生成图标（相对路径，可复现）
│   └── build_vsix.py      # 离线打包 .vsix（不依赖 vsce）
├── preview/preview.html   # 效果预览页
├── docs/REBUILD_GUIDE.md  # 从零重制一份的完整蓝图
├── README.md / CHANGELOG.md / LICENSE
```

## 从零重制

想重新做一份一模一样的主题？完整流程——配色表、目录结构、每个文件怎么写、图标绘制和打包步骤——都记录在 [docs/REBUILD_GUIDE.md](docs/REBUILD_GUIDE.md)，照着做即可。

## 许可

MIT License
