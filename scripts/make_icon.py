# -*- coding: utf-8 -*-
"""生成 Kawaii Macaron 主题插件的 128x128 图标。

用法：在本项目根目录下执行
    python scripts/make_icon.py
输出：images/icon.png（粉色渐变背景 + 三色马卡龙堆叠）

依赖：Pillow（pip install Pillow）
"""
import os
from PIL import Image, ImageDraw

# 项目根目录（scripts/ 的上一级），避免硬编码绝对路径
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "images", "icon.png")

S = 128
img = Image.new("RGBA", (S, S), (0, 0, 0, 0))
d = ImageDraw.Draw(img)

# 粉色渐变背景（樱花粉 -> 草莓粉）
top = (247, 218, 226)     # F7DAE2
bottom = (229, 138, 168)  # E58AA8
for y in range(S):
    t = y / (S - 1)
    r = int(top[0] + (bottom[0] - top[0]) * t)
    g = int(top[1] + (bottom[1] - top[1]) * t)
    b = int(top[2] + (bottom[2] - top[2]) * t)
    d.line([(0, y), (S, y)], fill=(r, g, b, 255))

# 圆角遮罩
mask = Image.new("L", (S, S), 0)
ImageDraw.Draw(mask).rounded_rectangle([0, 0, S - 1, S - 1], radius=30, fill=255)
img.putalpha(mask)


def macaron(d, cx, cy, w, h, color, highlight=True):
    """画一个马卡龙：上下两个圆帽 + 中间奶油层"""
    r = w // 3
    d.rounded_rectangle([cx - w // 2, cy - h // 2, cx + w // 2, cy], radius=r, fill=color)
    d.rounded_rectangle([cx - w // 2, cy - h // 2, cx + w // 2, cy - h // 4], radius=r, fill=color)
    d.rectangle([cx - w // 2, cy - 3, cx + w // 2, cy + 1], fill=(255, 249, 239, 255))
    if highlight:
        d.ellipse([cx - w // 4, cy - h // 2 + 4, cx - w // 8, cy - h // 4 + 2],
                  fill=(255, 255, 255, 110))


# 三个马卡龙：草莓粉、奶油白、暖黄（品字形堆叠）
macaron(d, 62, 48, 62, 40, (229, 138, 168, 255))   # 草莓粉
macaron(d, 40, 82, 50, 34, (255, 249, 239, 255))   # 奶油白
macaron(d, 88, 86, 52, 36, (249, 227, 168, 255))   # 暖黄

os.makedirs(os.path.dirname(OUT), exist_ok=True)
img.save(OUT)
print("icon saved ->", OUT)
