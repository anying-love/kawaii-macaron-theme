# 从零重制指南 · Kawaii Macaron Theme

这份文档是完整蓝图，照着做可以重新制作一份**一模一样**的「卡哇伊马卡龙」VS Code 主题插件。所有路径均使用相对路径，不依赖任何特定机器环境。

---

## 0. 设计定位

- **风格**：软萌马卡龙，甜软少女感，低饱和暖调。
- **主色调**：暖调粉色（边框/点缀）、奶油白、米奶白、暖黄。
- **硬性要求**：可爱但不影响代码可读性——所有语法颜色都在浅色背景上保证足够对比度。
- **主题形态**：浅色（light）主题，`uiTheme: "vs"`。

## 1. 先决条件

- Python 3（打包与绘图脚本用，仅标准库 + Pillow）
- 生成图标需要 `Pillow`：`pip install Pillow`
- （可选）VS Code 用于预览和安装

## 2. 完整色板

### UI 颜色（两个主题共用，仅代码区底色不同）

| 用途 | 色值 | 说明 |
| --- | --- | --- |
| 边框粉 | `#F2B4C4` | 所有分界线/边框统一色 |
| 强调粉 | `#E58AA8` | 光标、激活标签、按钮、焦点框 |
| 活动栏底 | `#F7DAE2` | 最左侧竖条（奶油款用 `#F8DCE5`） |
| 侧边栏底 | `#FAF3E7` | 米奶白（奶油款用 `#FAF3EC`） |
| 代码区暖黄 | `#FFF7E5` | 暖黄款 `editor.background` |
| 代码区奶油白 | `#FDF5F0` | 奶油款 `editor.background` |
| 主文字 | `#5B4A3E` | `foreground` / `editor.foreground` |
| 选中背景 | `#F6D9E1` | 选区、高亮 |
| 标题/状态栏文字 | `#8A3D55` | 深玫瑰棕 |
| 次要文字 | `#8A7568` | 描述、图标 |

### 语法高亮（tokenColors，两个主题完全一致）

| 语法元素 | 色值 | 字体样式 |
| --- | --- | --- |
| 注释 | `#A79380` | 斜体 |
| 字符串 | `#A8763F` | 无 |
| 数字 / 布尔 / null | `#C0784F` | 无 |
| 关键字（keyword/storage） | `#C2587F` | 无 |
| 函数名 / 内置函数 | `#B34A6E` | 无 |
| 类型 / 类 / 命名空间 | `#A268B8` | 无 |
| 变量 | `#6B5A4C` | 无 |
| 参数 / 对象属性 | `#8A6B5C` | 无 |
| 标签（HTML/JSX） | `#D05E85` | 无 |
| 属性名 | `#B9763F` | 无 |
| 对象键 / CSS 属性名 | `#8A5C7E` | 无 |
| Markdown 标题 | `#C4617F` | 加粗 |
| 装饰器 / 注解 | `#B268B8` | 无 |
| 错误（invalid） | `#D4738B` | 下划线 |

> 完整、逐字段的配色定义直接参考 `themes/kawaii-macaron-warm.json` 与 `themes/kawaii-macaron-cream.json` —— 这两个文件本身就是最精确的模板，重制时直接复制改名即可。

## 3. 目录结构

```
vscode-kawaii-macaron-theme/
├── package.json
├── themes/
│   ├── kawaii-macaron-warm.json
│   └── kawaii-macaron-cream.json
├── images/
│   └── icon.png
├── scripts/
│   ├── make_icon.py
│   └── build_vsix.py
├── preview/
│   └── preview.html
├── docs/
│   └── REBUILD_GUIDE.md
├── README.md
├── CHANGELOG.md
├── LICENSE
├── .gitignore
└── .vscodeignore
```

## 4. 步骤 1：编写 `package.json`

关键字段：

```json
{
  "name": "kawaii-macaron-theme",
  "displayName": "Kawaii Macaron Theme · 卡哇伊马卡龙主题",
  "description": "软萌马卡龙风格的 VS Code 主题：低饱和暖调粉色边框 + 暖黄/奶油白代码区。",
  "version": "1.0.0",
  "publisher": "your-publisher-id",
  "license": "MIT",
  "icon": "images/icon.png",
  "engines": { "vscode": "^1.60.0" },
  "categories": ["Themes"],
  "contributes": {
    "themes": [
      { "label": "Kawaii Macaron · Warm Yellow 暖黄", "uiTheme": "vs", "path": "./themes/kawaii-macaron-warm.json" },
      { "label": "Kawaii Macaron · Cream Milk 奶油白", "uiTheme": "vs", "path": "./themes/kawaii-macaron-cream.json" }
    ]
  }
}
```

要点：
- `categories` 必须是 `["Themes"]`。
- 每个主题条目：`label`（主题选择器里显示的名字）、`uiTheme: "vs"`（浅色）、`path`（相对主题 JSON 路径）。
- `publisher` 改成你自己的 ID（只开源不上架可留占位符）。

## 5. 步骤 2：编写主题 JSON

每个主题 JSON 由三部分组成：

1. **`name` / `type` / `semanticHighlighting`**：`type: "light"`。
2. **`colors`**：编辑器 UI 颜色（背景、边框、文字、选区、终端 ANSI 色等）。按第 2 节色板填写。
3. **`tokenColors`**：语法高亮规则，每条形如：
   ```json
   { "scope": ["keyword", "storage.type"], "settings": { "foreground": "#C2587F" } }
   ```

`colors` 里必须覆盖的核心键（保证「粉色边框」效果）：

```
editorGroup.border, editorGroupHeader.tabsBorder,
tab.border, activityBar.border, sideBar.border,
panel.border, editorWidget.border, statusBar.border,
titleBar.border, menu.border, notificationCenter.border
```
这些统一填 `#F2B4C4`。

> 直接复制仓库里现成的 `kawaii-macaron-warm.json` 改 `editor.background` 等背景值，即可得到奶油款 `kawaii-macaron-cream.json`。两者差异仅在：代码区背景、侧边栏/活动栏背景的细微冷暖。

## 6. 步骤 3：生成图标

运行（在项目根目录）：

```bash
python scripts/make_icon.py
```

脚本用 Pillow 画一个 128×128 图标：粉色渐变背景（`#F7DAE2`→`#E58AA8`）+ 三个堆叠马卡龙（草莓粉 `#E58AA8`、奶油白 `#FFF9EF`、暖黄 `#F9E3A8`），输出到 `images/icon.png`。

## 7. 步骤 4：打包 .vsix

运行（在项目根目录）：

```bash
python scripts/build_vsix.py
```

原理：`.vsix` 本质是 zip，结构为：

```
[Content_Types].xml
extension.vsixmanifest
extension/
    package.json
    themes/*.json
    images/icon.png
    README.md / CHANGELOG.md / LICENSE
```

脚本自动生成两个 XML 清单（`[Content_Types].xml`、`extension.vsixmanifest`），把 `package.json`/`themes`/`images` 拷进 `extension/`，再用标准库 `zipfile` 压缩。**无需安装 `@vscode/vsce`**（离线、零依赖）。

## 8. 步骤 5：安装与验证

1. VS Code 中 `Ctrl+Shift+P` → `Extensions: Install from VSIX...` → 选择生成的 `.vsix`。
2. 重启后 `Ctrl+K Ctrl+T`，应看到两个主题：
   - `Kawaii Macaron · Warm Yellow 暖黄`
   - `Kawaii Macaron · Cream Milk 奶油白`
3. 验证「粉色边框 + 暖黄/奶油白代码区 + 可读的语法高亮」三项是否符合预期。

## 9. 复现清单（Checklist）

- [ ] 建目录结构（第 3 节）
- [ ] 写 `package.json`（第 4 节）
- [ ] 写两个主题 JSON（第 5 节，直接复制现成文件）
- [ ] `pip install Pillow` 后跑 `make_icon.py` 生成图标
- [ ] 跑 `build_vsix.py` 打包
- [ ] 安装 `.vsix` 并在主题选择器验证两个变体
- [ ] （可选）改 `publisher` 为自己的 ID

---

许可证：MIT。字体/图片等第三方资源若使用，请自行确认其授权。
