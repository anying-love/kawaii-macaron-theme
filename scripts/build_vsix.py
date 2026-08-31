# -*- coding: utf-8 -*-
"""离线生成 Kawaii Macaron 主题的 .vsix 安装包（不依赖 vsce）。

用法：在本项目根目录下执行
    python scripts/build_vsix.py
输出：kawaii-macaron-theme-<version>.vsix

原理：.vsix 本质上是一个 zip 包，结构为
    [Content_Types].xml    内容类型清单
    extension.vsixmanifest 扩展清单（XML）
    extension/             扩展文件目录（package.json、themes/、images/...）
用标准库 zipfile 即可生成，无需安装 @vscode/vsce。
"""
import os
import json
import shutil
import zipfile

# 项目根目录（scripts/ 的上一级），避免硬编码绝对路径
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STAGE = os.path.join(ROOT, ".vsix-stage")


def xml_escape(s: str) -> str:
    return (s.replace("&", "&amp;")
             .replace("<", "&lt;")
             .replace(">", "&gt;"))


def main():
    pkg_path = os.path.join(ROOT, "package.json")
    with open(pkg_path, "r", encoding="utf-8") as f:
        pkg = json.load(f)

    name = pkg["name"]
    version = pkg["version"]
    publisher = pkg["publisher"]
    display_name = pkg.get("displayName", name)
    description = pkg.get("description", "")
    keywords = pkg.get("keywords", ["Themes"])
    engines_vscode = pkg.get("engines", {}).get("vscode", "^1.0.0").lstrip("^~")
    tags = " ".join(keywords)
    out = os.path.join(ROOT, f"{name}-{version}.vsix")

    # 清空并重建 staging（ignore_errors 避免残留删除失败中断构建）
    if os.path.exists(STAGE):
        shutil.rmtree(STAGE, ignore_errors=True)
    ext_dir = os.path.join(STAGE, "extension")
    os.makedirs(ext_dir, exist_ok=True)

    # [Content_Types].xml
    ct = (
        '<?xml version="1.0" encoding="utf-8"?>\n'
        '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">\n'
        '  <Default Extension="vsixmanifest" ContentType="text/xml"/>\n'
        '  <Default Extension="json" ContentType="application/json"/>\n'
        '  <Default Extension="png" ContentType="image/png"/>\n'
        '  <Default Extension="md" ContentType="text/markdown"/>\n'
        '  <Default Extension="txt" ContentType="text/plain"/>\n'
        '</Types>'
    )
    with open(os.path.join(STAGE, "[Content_Types].xml"), "w", encoding="utf-8") as f:
        f.write(ct)

    # extension.vsixmanifest
    man = (
        '<?xml version="1.0" encoding="utf-8"?>\n'
        '<PackageManifest Version="2.0.0" '
        'xmlns="http://schemas.microsoft.com/developer/vsx-schema/2011">\n'
        '  <Metadata>\n'
        f'    <Identity Language="en-US" Id="{xml_escape(name)}" '
        f'Version="{xml_escape(version)}" Publisher="{xml_escape(publisher)}"/>\n'
        f'    <DisplayName>{xml_escape(display_name)}</DisplayName>\n'
        f'    <Description xml:space="preserve">{xml_escape(description)}</Description>\n'
        f'    <Tags>{xml_escape(tags)}</Tags>\n'
        '    <Categories>Themes</Categories>\n'
        '    <GalleryFlags>public</GalleryFlags>\n'
        '  </Metadata>\n'
        '  <Installation>\n'
        f'    <InstallationTarget Version="[{xml_escape(engines_vscode)},)" '
        'Id="Microsoft.VisualStudio.Code"/>\n'
        '  </Installation>\n'
        '  <Assets>\n'
        '    <Asset Type="Microsoft.VisualStudio.Code.Manifest" '
        'Path="extension/package.json" Addressable="true"/>\n'
        '    <Asset Type="Microsoft.VisualStudio.Services.Icons.Default" '
        'Path="extension/images/icon.png" Addressable="true"/>\n'
        '  </Assets>\n'
        '</PackageManifest>'
    )
    with open(os.path.join(STAGE, "extension.vsixmanifest"), "w", encoding="utf-8") as f:
        f.write(man)

    # 拷贝插件文件到 extension/
    for fn in ("package.json", "README.md", "CHANGELOG.md", "LICENSE"):
        shutil.copyfile(os.path.join(ROOT, fn), os.path.join(ext_dir, fn))
    for sub in ("themes", "images"):
        shutil.copytree(os.path.join(ROOT, sub), os.path.join(ext_dir, sub))

    # 打包 zip（vsix = zip）；"w" 模式会直接覆盖旧文件，无需手动删除
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zf:
        for root, _, files in os.walk(STAGE):
            for fn in files:
                full = os.path.join(root, fn)
                arc = os.path.relpath(full, STAGE).replace("\\", "/")
                zf.write(full, arc)

    print(f"VSIX_OK -> {out} ({os.path.getsize(out)} bytes)")


if __name__ == "__main__":
    main()
