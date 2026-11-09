# -*- coding: utf-8 -*-
"""UI 原型绘制工具箱（Pillow）。"""
import os
from PIL import Image, ImageDraw, ImageFont

FONT_R = r"C:\Windows\Fonts\msyh.ttc"
FONT_B = r"C:\Windows\Fonts\msyhbd.ttc"
FONT_L = r"C:\Windows\Fonts\msyhl.ttc"

BG = "#F5F7FA"
SURFACE = "#FFFFFF"
PRIMARY = "#2F6BFF"
PRIMARY_DARK = "#1E4FD8"
PRIMARY_SOFT = "#EEF3FF"
ACCENT = "#FF7A45"
TEXT = "#1F2329"
SUB = "#646A73"
MUTED = "#9AA0A6"
BORDER = "#E5E8EF"
SUCCESS = "#00B578"
SUCCESS_SOFT = "#E8F8F2"
WARNING = "#FF9F0A"
WARNING_SOFT = "#FFF6E5"
DANGER = "#F5222D"
DANGER_SOFT = "#FEECEB"

_font_cache = {}


def font(size, bold=False, light=False):
    key = (size, bold, light)
    if key not in _font_cache:
        path = FONT_B if bold else (FONT_L if light else FONT_R)
        _font_cache[key] = ImageFont.truetype(path, size)
    return _font_cache[key]


def canvas(w=1440, h=900, bg=BG):
    img = Image.new("RGB", (w, h), bg)
    return img, ImageDraw.Draw(img)


def text(d, xy, s, size=14, color=TEXT, bold=False, light=False, anchor="la"):
    d.text(xy, s, font=font(size, bold, light), fill=color, anchor=anchor)


def tw(d, s, size=14, bold=False):
    return d.textlength(s, font=font(size, bold))


def rect(d, box, fill=None, outline=None, r=0, width=1):
    if r > 0:
        d.rounded_rectangle(box, radius=r, fill=fill, outline=outline, width=width)
    else:
        d.rectangle(box, fill=fill, outline=outline, width=width)


def card(d, x, y, w, h, r=12, fill=SURFACE, outline=BORDER):
    rect(d, (x, y, x + w, y + h), fill=fill, outline=outline, r=r)


def line(d, xy, fill=BORDER, width=1):
    d.line(xy, fill=fill, width=width)


def chip(d, x, y, s, fg=PRIMARY, bg=PRIMARY_SOFT, size=12, padx=8, h=24):
    w = tw(d, s, size) + padx * 2
    rect(d, (x, y, x + w, y + h), fill=bg, r=h / 2)
    text(d, (x + w / 2, y + h / 2), s, size, fg, anchor="mm")
    return w


def button(d, x, y, w, h, s, kind="primary", size=14):
    if kind == "primary":
        rect(d, (x, y, x + w, y + h), fill=PRIMARY, r=8)
        text(d, (x + w / 2, y + h / 2), s, size, "#FFFFFF", bold=True, anchor="mm")
    elif kind == "ghost":
        rect(d, (x, y, x + w, y + h), fill=SURFACE, outline=BORDER, r=8)
        text(d, (x + w / 2, y + h / 2), s, size, TEXT, anchor="mm")
    elif kind == "danger":
        rect(d, (x, y, x + w, y + h), fill=DANGER_SOFT, outline="#FFC9C7", r=8)
        text(d, (x + w / 2, y + h / 2), s, size, DANGER, anchor="mm")
    elif kind == "text":
        text(d, (x, y + h / 2), s, size, PRIMARY, anchor="lm")


def field(d, x, y, w, h=40, value="", placeholder="", icon=None, muted=False):
    rect(d, (x, y, x + w, y + h), fill="#FAFBFC", outline=BORDER, r=8)
    tx = x + 14
    if icon:
        icon_draw(d, icon, x + 22, y + h / 2, 16, MUTED)
        tx = x + 40
    if value:
        text(d, (tx, y + h / 2), value, 14, SUB if muted else TEXT, anchor="lm")
    else:
        text(d, (tx, y + h / 2), placeholder, 14, MUTED, anchor="lm")


def avatar(d, cx, cy, r=18, name="兰", bg=PRIMARY_SOFT, fg=PRIMARY):
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=bg)
    text(d, (cx, cy), name, int(r * 0.95), fg, bold=True, anchor="mm")


def icon_draw(d, kind, cx, cy, size=18, color=SUB):
    s = size / 2.0
    lw = max(1, int(size / 9))
    if kind == "search":
        d.ellipse((cx - s * 0.75, cy - s * 0.75, cx + s * 0.25, cy + s * 0.25), outline=color, width=lw)
        d.line((cx + s * 0.15, cy + s * 0.15, cx + s * 0.75, cy + s * 0.75), fill=color, width=lw)
    elif kind == "bell":
        d.arc((cx - s * 0.6, cy - s * 0.75, cx + s * 0.6, cy + s * 0.45), 200, 340, fill=color, width=lw)
        d.line((cx - s * 0.6, cy + s * 0.2, cx - s * 0.6, cy + s * 0.5), fill=color, width=lw)
        d.line((cx + s * 0.6, cy + s * 0.2, cx + s * 0.6, cy + s * 0.5), fill=color, width=lw)
        d.line((cx - s * 0.6, cy + s * 0.5, cx + s * 0.6, cy + s * 0.5), fill=color, width=lw)
        d.arc((cx - s * 0.2, cy + s * 0.45, cx + s * 0.2, cy + s * 0.8), 0, 180, fill=color, width=lw)
    elif kind == "user":
        d.ellipse((cx - s * 0.42, cy - s * 0.9, cx + s * 0.42, cy - s * 0.06), outline=color, width=lw)
        d.arc((cx - s * 0.8, cy - s * 0.02, cx + s * 0.8, cy + s * 1.2), 200, 340, fill=color, width=lw)
    elif kind == "box":
        d.polygon([(cx, cy - s * 0.8), (cx + s * 0.8, cy - s * 0.4), (cx + s * 0.8, cy + s * 0.4),
                   (cx, cy + s * 0.8), (cx - s * 0.8, cy + s * 0.4), (cx - s * 0.8, cy - s * 0.4)],
                  outline=color, width=lw)
        d.line((cx - s * 0.8, cy - s * 0.4, cx, cy), fill=color, width=lw)
        d.line((cx + s * 0.8, cy - s * 0.4, cx, cy), fill=color, width=lw)
        d.line((cx, cy, cx, cy + s * 0.8), fill=color, width=lw)
    elif kind == "book":
        d.polygon([(cx - s * 0.75, cy - s * 0.75), (cx - s * 0.1, cy - s * 0.6),
                   (cx - s * 0.1, cy + s * 0.8), (cx - s * 0.75, cy + s * 0.62)], outline=color, width=lw)
        d.polygon([(cx + s * 0.75, cy - s * 0.75), (cx + s * 0.1, cy - s * 0.6),
                   (cx + s * 0.1, cy + s * 0.8), (cx + s * 0.75, cy + s * 0.62)], outline=color, width=lw)
        d.line((cx, cy - s * 0.62, cx, cy + s * 0.78), fill=color, width=lw)
    elif kind == "monitor":
        d.rectangle((cx - s * 0.85, cy - s * 0.75, cx + s * 0.85, cy + s * 0.35), outline=color, width=lw)
        d.line((cx, cy + s * 0.35, cx, cy + s * 0.65), fill=color, width=lw)
        d.line((cx - s * 0.45, cy + s * 0.65, cx + s * 0.45, cy + s * 0.65), fill=color, width=lw)
    elif kind == "bike":
        d.ellipse((cx - s * 0.9, cy - s * 0.1, cx - s * 0.2, cy + s * 0.6), outline=color, width=lw)
        d.ellipse((cx + s * 0.2, cy - s * 0.1, cx + s * 0.9, cy + s * 0.6), outline=color, width=lw)
        d.line((cx - s * 0.55, cy + s * 0.25, cx - s * 0.1, cy - s * 0.55), fill=color, width=lw)
        d.line((cx - s * 0.1, cy - s * 0.55, cx + s * 0.55, cy + s * 0.25), fill=color, width=lw)
        d.line((cx - s * 0.1, cy - s * 0.55, cx + s * 0.15, cy - s * 0.2), fill=color, width=lw)
    elif kind == "phone":
        d.rounded_rectangle((cx - s * 0.45, cy - s * 0.85, cx + s * 0.45, cy + s * 0.85), radius=4,
                            outline=color, width=lw)
        d.line((cx - s * 0.2, cy + s * 0.65, cx + s * 0.2, cy + s * 0.65), fill=color, width=lw)
    elif kind == "chart":
        d.line((cx - s * 0.8, cy + s * 0.8, cx - s * 0.8, cy - s * 0.8), fill=color, width=lw)
        d.line((cx - s * 0.8, cy + s * 0.8, cx + s * 0.85, cy + s * 0.8), fill=color, width=lw)
        d.line((cx - s * 0.45, cy + s * 0.8, cx - s * 0.45, cy + s * 0.15), fill=color, width=lw)
        d.line((cx, cy + s * 0.8, cx, cy - s * 0.25), fill=color, width=lw)
        d.line((cx + s * 0.45, cy + s * 0.8, cx + s * 0.45, cy - s * 0.05), fill=color, width=lw)
    elif kind == "list":
        for i in range(3):
            yy = cy - s * 0.55 + i * s * 0.6
            d.ellipse((cx - s * 0.8, yy - 1.5, cx - s * 0.65, yy + 1.5), fill=color)
            d.line((cx - s * 0.45, yy, cx + s * 0.8, yy), fill=color, width=lw)
    elif kind == "shield":
        d.polygon([(cx, cy - s * 0.85), (cx + s * 0.75, cy - s * 0.5), (cx + s * 0.6, cy + s * 0.35),
                   (cx, cy + s * 0.85), (cx - s * 0.6, cy + s * 0.35), (cx - s * 0.75, cy - s * 0.5)],
                  outline=color, width=lw)
    elif kind == "clock":
        d.ellipse((cx - s * 0.8, cy - s * 0.8, cx + s * 0.8, cy + s * 0.8), outline=color, width=lw)
        d.line((cx, cy - s * 0.45, cx, cy), fill=color, width=lw)
        d.line((cx, cy, cx + s * 0.4, cy + s * 0.25), fill=color, width=lw)
    elif kind == "check":
        d.line((cx - s * 0.7, cy, cx - s * 0.15, cy + s * 0.55), fill=color, width=lw + 1)
        d.line((cx - s * 0.15, cy + s * 0.55, cx + s * 0.75, cy - s * 0.55), fill=color, width=lw + 1)
    elif kind == "warn":
        d.polygon([(cx, cy - s * 0.85), (cx + s * 0.9, cy + s * 0.75), (cx - s * 0.9, cy + s * 0.75)],
                  outline=color, width=lw)
        d.line((cx, cy - s * 0.35, cx, cy + s * 0.25), fill=color, width=lw)
        d.ellipse((cx - 1, cy + s * 0.45, cx + 1, cy + s * 0.45 + 2), fill=color)
    elif kind == "image":
        d.rounded_rectangle((cx - s * 0.85, cy - s * 0.7, cx + s * 0.85, cy + s * 0.7), radius=3,
                            outline=color, width=lw)
        d.ellipse((cx - s * 0.5, cy - s * 0.4, cx - s * 0.15, cy - s * 0.05), outline=color, width=lw)
        d.polygon([(cx - s * 0.7, cy + s * 0.55), (cx - s * 0.1, cy - s * 0.1),
                   (cx + s * 0.35, cy + s * 0.3), (cx + s * 0.55, cy + s * 0.1),
                   (cx + s * 0.8, cy + s * 0.55)], outline=color, width=lw)


def topbar(d, w, active="首页", search_text=None, name="兰", nav=None):
    rect(d, (0, 0, w, 64), fill=SURFACE)
    line(d, (0, 64, w, 64))
    # logo
    rect(d, (32, 14, 68, 50), fill=PRIMARY, r=10)
    text(d, (50, 32), "易", 20, "#FFFFFF", bold=True, anchor="mm")
    text(d, (80, 32), "校园易物", 19, TEXT, bold=True, anchor="lm")
    text(d, (80, 50), "CAMPUS MARKET", 8, MUTED, anchor="lm")
    # nav
    nav = nav or ["首页", "全部商品", "我的预约", "卖家中心"]
    x = 240
    for item in nav:
        if item == active:
            text(d, (x, 32), item, 15, PRIMARY, bold=True, anchor="lm")
            rect(d, (x, 52, x + tw(d, item, 15, True), 54), fill=PRIMARY, r=0)
        else:
            text(d, (x, 32), item, 15, SUB, anchor="lm")
        x += tw(d, item, 15, True) + 36
    # search
    sx = w - 520
    if search_text is not None:
        rect(d, (sx, 14, sx + 300, 50), fill="#F2F4F7", r=20)
        icon_draw(d, "search", sx + 22, 32, 15, MUTED)
        text(d, (sx + 40, 32), search_text, 14, TEXT, anchor="lm")
    # bell + avatar
    icon_draw(d, "bell", w - 170, 32, 20, SUB)
    d.ellipse((w - 156, 20, w - 137, 39), fill=ACCENT)
    text(d, (w - 146, 29), "3", 10, "#FFFFFF", bold=True, anchor="mm")
    avatar(d, w - 100, 32, 18, name)
    text(d, (w - 72, 32), name + "同学", 14, SUB, anchor="lm")


def sidebar(d, x, y, w, h, items, active, title="控制台"):
    rect(d, (x, y, x + w, y + h), fill=SURFACE)
    line(d, (x + w, y, x + w, y + h))
    text(d, (x + 24, y + 32), title, 12, MUTED, bold=True, anchor="lm")
    yy = y + 60
    for label, icon in items:
        if label == active:
            rect(d, (x + 12, yy, x + w - 12, yy + 44), fill=PRIMARY_SOFT, r=8)
            icon_draw(d, icon, x + 36, yy + 22, 18, PRIMARY)
            text(d, (x + 56, yy + 22), label, 14, PRIMARY, bold=True, anchor="lm")
        else:
            icon_draw(d, icon, x + 36, yy + 22, 18, SUB)
            text(d, (x + 56, yy + 22), label, 14, SUB, anchor="lm")
        yy += 52


def stat_card(d, x, y, w, h, label, value, delta=None, color=PRIMARY):
    card(d, x, y, w, h)
    text(d, (x + 20, y + 22), label, 13, SUB, anchor="lm")
    text(d, (x + 20, y + 60), value, 30, TEXT, bold=True, anchor="lm")
    if delta:
        chip(d, x + 20, y + h - 40, delta, SUCCESS, SUCCESS_SOFT, 11, 8, 22)


def table(d, x, y, w, headers, widths, rows, row_h=56, header_h=44, size=13):
    rect(d, (x, y, x + w, y + header_h), fill="#F7F8FA")
    line(d, (x, y + header_h, x + w, y + header_h))
    cx = x + 18
    for h, cw in zip(headers, widths):
        text(d, (cx, y + header_h / 2), h, size - 1, SUB, bold=True, anchor="lm")
        cx += cw
    yy = y + header_h
    for row in rows:
        cx = x + 18
        for cell, cw in zip(row, widths):
            cy = yy + row_h / 2
            if isinstance(cell, tuple):
                kind = cell[0]
                if kind == "chip":
                    chip(d, cx, cy - 12, cell[1], cell[2], cell[3], 11, 8, 24)
                elif kind == "bold":
                    text(d, (cx, cy), cell[1], size, TEXT, bold=True, anchor="lm")
                elif kind == "muted":
                    text(d, (cx, cy), cell[1], size, MUTED, anchor="lm")
                elif kind == "link":
                    text(d, (cx, cy), cell[1], size, PRIMARY, anchor="lm")
                elif kind == "price":
                    text(d, (cx, cy), cell[1], size, ACCENT, bold=True, anchor="lm")
            else:
                text(d, (cx, cy), cell, size, SUB, anchor="lm")
            cx += cw
        line(d, (x, yy + row_h, x + w, yy + row_h))
        yy += row_h
    rect(d, (x, y, x + w, yy), outline=BORDER, r=10)
    return yy
