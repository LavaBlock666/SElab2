# -*- coding: utf-8 -*-
"""八张 UI 原型界面。"""
from ui_kit import *  # noqa
import ui_kit as K

W, H = 1440, 900


def gradient(img, box, c1, c2):
    x0, y0, x1, y1 = box
    d = ImageDraw.Draw(img)
    r1, g1, b1 = Image.new("RGB", (1, 1), c1).getpixel((0, 0))
    r2, g2, b2 = Image.new("RGB", (1, 1), c2).getpixel((0, 0))
    h = y1 - y0
    for i in range(h):
        t = i / max(1, h - 1)
        d.line((x0, y0 + i, x1, y0 + i),
               fill=(int(r1 + (r2 - r1) * t), int(g1 + (g2 - g1) * t), int(b1 + (b2 - b1) * t)))


def thumb(d, x, y, w, h, kind, bg="#EAF0FF", color="#9DB4E8", label=None, r=10):
    rect(d, (x, y, x + w, y + h), fill=bg, r=r)
    icon_draw(d, kind, x + w / 2, y + h / 2 - (10 if label else 0), min(w, h) * 0.34, color)
    if label:
        text(d, (x + w / 2, y + h - 18), label, 11, color, anchor="mm")


def screen_login():
    img, d = canvas()
    gradient(img, (0, 0, 780, H), "#2F6BFF", "#16307F")
    d = ImageDraw.Draw(img)
    # 装饰
    d.ellipse((520, -120, 980, 340), fill="#3D77FF")
    d.ellipse((-160, 640, 260, 1060), fill="#2549B8")
    d.ellipse((600, 600, 860, 860), fill="#2A55C9")
    rect(d, (88, 84, 132, 128), fill="#FFFFFF", r=12)
    text(d, (110, 106), "易", 26, PRIMARY, bold=True, anchor="mm")
    text(d, (150, 106), "校园易物", 26, "#FFFFFF", bold=True, anchor="lm")
    text(d, (88, 210), "让闲置物品", 46, "#FFFFFF", bold=True)
    text(d, (88, 274), "在校园里流动起来", 46, "#FFFFFF", bold=True)
    text(d, (88, 352), "发布 · 审核 · 预约 · 确认，一条流程走完一次二手交易。", 17, "#CBD9FF")
    items = [("校园内实名认证，交易对象可追溯", 430),
             ("同一商品仅一条有效预约，先到先得", 484),
             ("举报与操作日志全程留痕，纠纷可查", 538)]
    for s, y in items:
        d.ellipse((88, y - 11, 110, y + 11), fill="#FFFFFF")
        icon_draw(d, "check", 99, y, 13, PRIMARY)
        text(d, (124, y), s, 16, "#E6EDFF", anchor="lm")
    text(d, (88, 820), "软件工程 · 实验二 设计与建模", 13, "#9DB4E8")

    # 表单
    fx = 900
    text(d, (fx, 190), "欢迎回来", 32, TEXT, bold=True)
    text(d, (fx, 238), "登录后即可预约商品、发布闲置", 15, SUB)
    text(d, (fx, 306), "登录", 18, PRIMARY, bold=True)
    rect(d, (fx, 336, fx + 44, 339), fill=PRIMARY, r=0)
    text(d, (fx + 92, 306), "注册", 18, MUTED)
    text(d, (fx, 380), "手机号 / 校园邮箱", 13, SUB)
    field(d, fx, 404, 400, 48, "241220082@smail.nju.edu.cn", icon="user")
    text(d, (fx, 476), "密码", 13, SUB)
    field(d, fx, 500, 400, 48, "••••••••", icon="shield")
    icon_draw(d, "search", fx + 376, 524, 14, MUTED)
    rect(d, (fx, 574, fx + 18, 592), fill=PRIMARY, r=4)
    icon_draw(d, "check", fx + 9, 583, 11, "#FFFFFF")
    text(d, (fx + 28, 583), "记住我", 13, SUB, anchor="lm")
    text(d, (fx + 400, 583), "忘记密码？", 13, PRIMARY, anchor="rm")
    button(d, fx, 620, 400, 50, "登 录", "primary", 16)
    line(d, (fx, 706, fx + 150, 706))
    text(d, (fx + 200, 706), "或", 12, MUTED, anchor="mm")
    line(d, (fx + 250, 706, fx + 400, 706))
    button(d, fx, 730, 400, 48, "使用校园统一身份认证登录", "ghost", 14)
    text(d, (fx, 816), "还没有账号？", 13, SUB)
    text(d, (fx + 88, 816), "立即注册", 13, PRIMARY, bold=True)
    text(d, (fx, 862), "登录即表示同意《用户协议》与《隐私政策》", 11, MUTED)
    return img


def screen_browse():
    img, d = canvas()
    topbar(d, W, "全部商品", "自行车")
    text(d, (32, 96), "全部商品", 24, TEXT, bold=True, anchor="lm")
    text(d, (32, 132), "共 128 件在售商品 · 按发布时间倒序", 13, SUB, anchor="lm")
    # 筛选卡
    card(d, 32, 160, 268, 700)
    text(d, (56, 192), "筛选", 16, TEXT, bold=True, anchor="lm")
    text(d, (276, 192), "重置", 12, PRIMARY, anchor="rm")
    line(d, (56, 214, 276, 214))
    text(d, (56, 240), "商品分类", 13, SUB, bold=True, anchor="lm")
    cats = [("全部分类", 128, True), ("教材书籍", 46, False), ("数码电子", 38, False),
            ("生活用品", 22, False), ("运动户外", 16, False), ("其他", 6, False)]
    y = 272
    for name, n, active in cats:
        if active:
            d.ellipse((56, y - 6, 68, y + 6), outline=PRIMARY, width=2)
            d.ellipse((59, y - 3, 65, y + 3), fill=PRIMARY)
            text(d, (80, y), name, 13, PRIMARY, bold=True, anchor="lm")
        else:
            d.ellipse((56, y - 6, 68, y + 6), outline="#C9CED6", width=2)
            text(d, (80, y), name, 13, SUB, anchor="lm")
        text(d, (276, y), str(n), 12, MUTED, anchor="rm")
        y += 34
    line(d, (56, 486, 276, 486))
    text(d, (56, 512), "价格区间", 13, SUB, bold=True, anchor="lm")
    field(d, 56, 534, 96, 36, "0", muted=True)
    text(d, (162, 552), "—", 13, MUTED, anchor="mm")
    field(d, 178, 534, 98, 36, "1000", muted=True)
    text(d, (56, 596), "商品状态", 13, SUB, bold=True, anchor="lm")
    chip(d, 56, 618, "可预约", PRIMARY, PRIMARY_SOFT, 12, 12, 28)
    chip(d, 132, 618, "已预约", MUTED, "#F2F3F5", 12, 12, 28)
    text(d, (56, 676), "排序方式", 13, SUB, bold=True, anchor="lm")
    opts = [("最新发布", True), ("价格从低到高", False), ("价格从高到低", False)]
    yy = 706
    for name, active in opts:
        d.ellipse((56, yy - 6, 68, yy + 6), outline=PRIMARY if active else "#C9CED6", width=2)
        if active:
            d.ellipse((59, yy - 3, 65, yy + 3), fill=PRIMARY)
        text(d, (80, yy), name, 13, SUB, anchor="lm")
        yy += 30
    button(d, 56, 800, 204, 40, "应用筛选", "primary", 14)

    # 商品网格
    gx, gy = 324, 160
    cw, ch, gap = 340, 320, 20
    data = [
        ("book", "#EAF0FF", "#8FA9E8", "高等数学 第七版 上下册", "¥ 25", "教材书籍", "九成新", "林同学", "可预约"),
        ("monitor", "#EAF7FF", "#7FB6D8", "27 英寸 2K 显示器", "¥ 620", "数码电子", "八成新", "郑镜汗", "可预约"),
        ("bike", "#E9F8F1", "#7FC0A3", "捷安特山地自行车", "¥ 480", "运动户外", "九成新", "王同学", "已预约"),
        ("box", "#FFF1E8", "#E8A87C", "宿舍收纳箱 三件套", "¥ 35", "生活用品", "全新", "陈同学", "可预约"),
        ("phone", "#F3EDFF", "#A58FE0", "蓝牙耳机 降噪版", "¥ 129", "数码电子", "九成新", "周同学", "可预约"),
        ("book", "#FFF7E0", "#D9B96B", "考研英语真题 2020-2025", "¥ 40", "教材书籍", "七成新", "吴同学", "可预约"),
    ]
    for i, (kind, bg, fg, title, price, cat, cond, seller, status) in enumerate(data):
        col, row = i % 3, i // 3
        x = gx + col * (cw + gap)
        y = gy + row * (ch + gap)
        card(d, x, y, cw, ch)
        thumb(d, x + 16, y + 16, cw - 32, 150, kind, bg, fg, None, 8)
        text(d, (x + 18, y + 192), title, 15, TEXT, bold=True)
        text(d, (x + 18, y + 222), price, 20, ACCENT, bold=True)
        chip(d, x + 18, y + 254, cat, SUB, "#F2F3F5", 11, 8, 22)
        chip(d, x + 18 + tw(d, cat, 11) + 24, y + 254, cond, SUB, "#F2F3F5", 11, 8, 22)
        avatar(d, x + 28, y + 296, 12, seller[0], "#F2F4F7", SUB)
        text(d, (x + 46, y + 296), seller, 12, SUB, anchor="lm")
        chip(d, x + cw - 84, y + 286, status,
             SUCCESS if status == "可预约" else WARNING,
             SUCCESS_SOFT if status == "可预约" else WARNING_SOFT, 11, 8, 22)
    # 分页
    py = 822
    for i, label in enumerate(["‹", "1", "2", "3", "4", "›"]):
        x = 1000 + i * 46
        active = label == "1"
        rect(d, (x, py, x + 36, py + 36), fill=PRIMARY if active else SURFACE,
             outline=None if active else BORDER, r=8)
        text(d, (x + 18, py + 18), label, 13, "#FFFFFF" if active else SUB, anchor="mm")
    return img


def screen_detail():
    img, d = canvas()
    topbar(d, W, "全部商品")
    text(d, (32, 92), "首页 / 运动户外 / 捷安特山地自行车", 12, MUTED, anchor="lm")
    card(d, 32, 116, 640, 440, 12)
    thumb(d, 44, 128, 616, 416, "bike", "#E9F8F1", "#6FB79A", None, 8)
    for i, (kind, bg, fg) in enumerate([("bike", "#E9F8F1", "#6FB79A"), ("bike", "#EAF0FF", "#8FA9E8"),
                                        ("bike", "#FFF1E8", "#E8A87C"), ("bike", "#F3EDFF", "#A58FE0")]):
        thumb(d, 32 + i * 112, 572, 100, 76, kind, bg, fg, None, 8)
    # 右侧信息
    x = 700
    text(d, (x, 130), "捷安特山地自行车 27.5 寸", 24, TEXT, bold=True)
    text(d, (x, 180), "¥ 480", 34, ACCENT, bold=True)
    text(d, (x + 110, 194), "原价 ¥ 1299", 12, MUTED, anchor="lm")
    chip(d, x, 236, "九成新", SUCCESS, SUCCESS_SOFT, 12, 10, 26)
    chip(d, x + 82, 236, "运动户外", SUB, "#F2F3F5", 12, 10, 26)
    chip(d, x + 174, 236, "可预约", PRIMARY, PRIMARY_SOFT, 12, 10, 26)
    line(d, (x, 286, 1408, 286))
    meta = [("发布时间", "2026-11-08 14:20"), ("浏览次数", "126 次"), ("交易地点", "仙林校区 · 四组团"),
            ("商品编号", "IT202611080012")]
    yy = 312
    for k, v in meta:
        text(d, (x, yy), k, 13, MUTED, anchor="lm")
        text(d, (x + 96, yy), v, 13, TEXT, anchor="lm")
        yy += 32
    # 卖家卡
    card(d, x, 462, 708, 96)
    avatar(d, x + 46, 510, 26, "郑")
    text(d, (x + 86, 494), "郑镜汗", 15, TEXT, bold=True, anchor="lm")
    text(d, (x + 86, 520), "校园实名认证 · 在售 12 件 · 已完成 26 单", 12, SUB, anchor="lm")
    button(d, x + 588, 486, 100, 40, "查看主页", "ghost", 13)
    # 预约说明
    card(d, x, 578, 708, 110, fill="#F7FAFF", outline="#D6E2FF")
    icon_draw(d, "shield", x + 34, 610, 18, PRIMARY)
    text(d, (x + 54, 610), "预约须知", 14, PRIMARY, bold=True, anchor="lm")
    text(d, (x + 22, 642), "同一商品仅允许一条有效预约；预约后等待卖家确认，确认前可取消。", 12, SUB)
    text(d, (x + 22, 666), "平台仅记录线下交易，不涉及在线支付与物流。", 12, SUB)
    # 按钮
    button(d, x, 706, 300, 52, "立即预约", "primary", 17)
    button(d, x + 320, 706, 140, 52, "收藏", "ghost", 15)
    button(d, x + 480, 706, 140, 52, "举报", "ghost", 15)
    # 描述
    card(d, 32, 668, 640, 190)
    text(d, (56, 700), "商品描述", 15, TEXT, bold=True, anchor="lm")
    desc = ["2024 年 3 月购入，骑行约 300 公里，变速与刹车均正常，无磕碰。",
            "随车赠送车锁与打气筒。毕业出清，可到四组团看车，满意再交易。",
            "价格可小刀，不接受邮寄。"]
    yy = 736
    for s in desc:
        text(d, (56, yy), s, 13, SUB)
        yy += 30
    return img


def screen_publish():
    img, d = canvas()
    topbar(d, W, "卖家中心")
    text(d, (32, 96), "发布商品", 24, TEXT, bold=True, anchor="lm")
    steps = [("1", "填写信息", True), ("2", "提交审核", False), ("3", "审核通过", False)]
    sx = 900
    for i, (n, label, active) in enumerate(steps):
        d.ellipse((sx, 84, sx + 24, 108), fill=PRIMARY if active else "#E9EBF0")
        text(d, (sx + 12, 96), n, 11, "#FFFFFF" if active else MUTED, bold=True, anchor="mm")
        text(d, (sx + 32, 96), label, 12, TEXT if active else MUTED, anchor="lm")
        sx += 92
    card(d, 32, 132, 860, 700)
    text(d, (56, 168), "基本信息", 15, TEXT, bold=True, anchor="lm")
    text(d, (56, 208), "商品标题", 13, SUB, anchor="lm")
    field(d, 56, 230, 812, 44, "捷安特山地自行车 27.5 寸 九成新", muted=False)
    text(d, (56, 300), "商品分类", 13, SUB, anchor="lm")
    field(d, 56, 322, 392, 44, "运动户外", muted=True)
    text(d, (476, 300), "成色", 13, SUB, anchor="lm")
    field(d, 476, 322, 392, 44, "九成新", muted=True)
    text(d, (56, 392), "价格", 13, SUB, anchor="lm")
    field(d, 56, 414, 250, 44, "480", muted=False)
    text(d, (322, 436), "元", 13, SUB, anchor="lm")
    text(d, (476, 392), "交易地点", 13, SUB, anchor="lm")
    field(d, 476, 414, 392, 44, "仙林校区 · 四组团", muted=True)
    text(d, (56, 484), "商品描述", 13, SUB, anchor="lm")
    rect(d, (56, 506, 868, 646), fill="#FAFBFC", outline=BORDER, r=8)
    for i, s in enumerate(["2024 年 3 月购入，骑行约 300 公里，变速与刹车正常。",
                           "随车赠送车锁与打气筒，毕业出清。", "可到四组团看车，满意再交易。"]):
        text(d, (72, 530 + i * 26), s, 13, SUB)
    text(d, (72, 620), "0 / 500", 11, MUTED, anchor="lm")
    text(d, (56, 676), "商品图片", 13, SUB, anchor="lm")
    for i in range(4):
        x = 56 + i * 120
        rect(d, (x, 698, x + 104, 798), fill="#FAFBFC", outline=BORDER, r=8)
        if i == 0:
            icon_draw(d, "bike", x + 52, 742, 28, "#8FA9E8")
            text(d, (x + 52, 776), "已上传", 10, MUTED, anchor="mm")
        else:
            icon_draw(d, "image", x + 52, 740, 22, "#C4C9D2")
            text(d, (x + 52, 776), "上传图片", 10, MUTED, anchor="mm")


    # 右侧提示
    card(d, 920, 132, 488, 400, fill="#FBFCFE")
    text(d, (948, 168), "发布规范", 15, TEXT, bold=True, anchor="lm")
    tips = ["标题写清品类、型号与成色，避免出现联系方式。",
            "同一商品请勿重复发布，重复发布将被驳回。",
            "价格修改后需要重新提交审核。",
            "图片最多 6 张，建议首图使用实物照片。"]
    yy = 206
    for s in tips:
        d.ellipse((948, yy - 3, 954, yy + 3), fill=PRIMARY)
        text(d, (968, yy), s, 12, SUB, anchor="lm")
        yy += 54
    card(d, 920, 556, 488, 276, fill="#FFF9EC", outline="#F5DFB0")
    icon_draw(d, "warn", 950, 594, 18, WARNING)
    text(d, (972, 594), "审核说明", 14, "#B4740A", bold=True, anchor="lm")
    for i, s in enumerate(["提交后进入管理员待审核列表，", "一般 1 个工作日内完成审核。",
                           "驳回时会给出理由，可在草稿中", "修改后重新提交。"]):
        text(d, (948, 632 + i * 28), s, 12, "#8A6420")
    button(d, 1090, 756, 150, 46, "保存草稿", "ghost", 14)
    button(d, 1258, 756, 150, 46, "提交审核", "primary", 14)
    return img


def screen_seller():
    img, d = canvas()
    topbar(d, W, "卖家中心")
    sidebar(d, 0, 64, 220, 836,
            [("概览", "chart"), ("我的商品", "box"), ("预约管理", "clock"), ("数据统计", "chart")], "我的商品",
            "卖家中心")
    x = 220
    text(d, (x + 32, 112), "我的商品", 24, TEXT, bold=True, anchor="lm")
    text(d, (x + 32, 146), "管理在售、待审核与已完成的商品", 13, SUB, anchor="lm")
    cards = [("在售中", "8", "+2 本周"), ("待审核", "2", "1 条已驳回"), ("预约中", "3", "2 条待确认"),
             ("已完成", "26", "+4 本月")]
    for i, (label, value, delta) in enumerate(cards):
        stat_card(d, x + 32 + i * 292, 174, 272, 120, label, value, delta)
    # 待确认提示
    rect(d, (x + 32, 318, W - 32, 378), fill="#FFF7E6", outline="#F7DDA8", r=10)
    icon_draw(d, "warn", x + 58, 348, 16, WARNING)
    text(d, (x + 76, 348), "有 2 条预约等待确认，请在 24 小时内处理，超时将自动关闭。", 13, "#8A6420", anchor="lm")
    text(d, (W - 128, 348), "去处理", 13, "#B4740A", bold=True, anchor="rm")
    # 表格
    headers = ["商品", "价格", "状态", "浏览", "预约", "操作"]
    widths = [380, 130, 130, 90, 90, 240]
    rows = []
    items = [("bike", "#E9F8F1", "捷安特山地自行车 27.5 寸", "¥ 480", ("chip", "已预约", WARNING, WARNING_SOFT), "126", "3"),
             ("monitor", "#EAF7FF", "27 英寸 2K 显示器", "¥ 620", ("chip", "在售中", SUCCESS, SUCCESS_SOFT), "98", "5"),
             ("book", "#EAF0FF", "高等数学 第七版 上下册", "¥ 25", ("chip", "待审核", PRIMARY, PRIMARY_SOFT), "42", "1"),
             ("box", "#FFF1E8", "宿舍收纳箱 三件套", "¥ 35", ("chip", "已完成", MUTED, "#F2F3F5"), "77", "2")]
    ty = 400
    rect(d, (x + 32, ty, W - 32, ty + 44), fill="#F7F8FA")
    cx = x + 50
    for h, cw in zip(headers, widths):
        text(d, (cx, ty + 22), h, 12, SUB, bold=True, anchor="lm")
        cx += cw
    yy = ty + 44
    for kind, bg, name, price, status, views, res in items:
        rect(d, (x + 32, yy, W - 32, yy + 84), outline=BORDER, r=0)
        thumb(d, (x + 50), yy + 14, 80, 56, kind, bg, "#8FA9E8", None, 6)
        text(d, (x + 144, yy + 32), name, 13, TEXT, bold=True, anchor="lm")
        text(d, (x + 144, yy + 56), "编号 IT202611080012", 11, MUTED, anchor="lm")
        text(d, (x + 430, yy + 42), price, 14, ACCENT, bold=True, anchor="lm")
        chip(d, x + 560, yy + 30, status[1], status[2], status[3], 11, 10, 24)
        text(d, (x + 700, yy + 42), views, 13, SUB, anchor="lm")
        text(d, (x + 790, yy + 42), res, 13, SUB, anchor="lm")
        button(d, x + 860, yy + 26, 62, 32, "编辑", "ghost", 12)
        button(d, x + 930, yy + 26, 62, 32, "下架", "ghost", 12)
        button(d, x + 1000, yy + 26, 88, 32, "确认预约", "primary", 12)
        yy += 84
    text(d, (x + 32, yy + 28), "共 4 条记录，仅展示最近更新", 12, MUTED, anchor="lm")
    return img


def screen_audit():
    img, d = canvas()
    topbar(d, W, "管理后台", nav=["首页", "全部商品", "管理后台"])
    sidebar(d, 0, 64, 220, 836,
            [("商品审核", "shield"), ("举报处理", "warn"), ("操作日志", "list"), ("统计报表", "chart")], "商品审核",
            "管理后台")
    x = 220
    text(d, (x + 32, 112), "商品审核", 24, TEXT, bold=True, anchor="lm")
    tabs = [("待审核 6", True), ("已通过 42", False), ("已驳回 8", False)]
    tx = x + 32
    for label, active in tabs:
        if active:
            text(d, (tx, 166), label, 14, PRIMARY, bold=True, anchor="lm")
            rect(d, (tx, 180, tx + tw(d, label, 14, True), 182), fill=PRIMARY)
        else:
            text(d, (tx, 166), label, 14, SUB, anchor="lm")
        tx += tw(d, label, 14, True) + 40
    line(d, (x + 32, 182, 872, 182))
    # 列表
    card(d, 252, 200, 620, 520, 12)
    headers = ["商品", "卖家", "价格", "操作"]
    widths = [280, 100, 90, 150]
    rect(d, (252, 200, 872, 244), fill="#F7F8FA")
    cx = 272
    for h, cw in zip(headers, widths):
        text(d, (cx, 222), h, 12, SUB, bold=True, anchor="lm")
        cx += cw
    rows = [("bike", "#E9F8F1", "捷安特山地自行车", "王同学", "¥ 480"),
            ("book", "#EAF0FF", "高等数学 第七版", "林同学", "¥ 25"),
            ("monitor", "#EAF7FF", "27 英寸 2K 显示器", "郑镜汗", "¥ 620"),
            ("box", "#FFF1E8", "宿舍收纳箱 三件套", "陈同学", "¥ 35"),
            ("phone", "#F3EDFF", "蓝牙耳机 降噪版", "周同学", "¥ 129")]
    yy = 244
    for i, (kind, bg, name, seller, price) in enumerate(rows):
        if i == 0:
            rect(d, (252, yy, 872, yy + 84), fill="#F5F8FF")
        line(d, (264, yy + 84, 872, yy + 84))
        thumb(d, 272, yy + 14, 88, 56, kind, bg, "#8FA9E8", None, 6)
        text(d, (372, yy + 32), name, 13, TEXT, bold=True, anchor="lm")
        text(d, (372, yy + 56), "IT202611080008", 11, MUTED, anchor="lm")
        text(d, (552, yy + 42), seller, 12, SUB, anchor="lm")
        text(d, (652, yy + 42), price, 13, ACCENT, bold=True, anchor="lm")
        button(d, 742, yy + 26, 50, 32, "通过", "primary", 12)
        button(d, 806, yy + 26, 50, 32, "驳回", "danger", 12)
        yy += 84
    # 详情面板
    px, pw = 900, 508
    card(d, px, 200, pw, 690, 12)
    text(d, (px + 24, 236), "审核详情", 15, TEXT, bold=True, anchor="lm")
    thumb(d, px + 24, 264, pw - 48, 220, "bike", "#E9F8F1", "#6FB79A", None, 8)
    text(d, (px + 24, 512), "捷安特山地自行车 27.5 寸", 16, TEXT, bold=True, anchor="lm")
    text(d, (px + 24, 544), "¥ 480", 22, ACCENT, bold=True, anchor="lm")
    info = [("卖家", "王同学"), ("分类", "运动户外"), ("成色", "九成新"), ("提交", "2026-11-09 09:12")]
    for i, (k, v) in enumerate(info):
        yy2 = 590 + i * 30
        text(d, (px + 24, yy2), k, 12, MUTED, anchor="lm")
        text(d, (px + 112, yy2), v, 12, SUB, anchor="lm")
    text(d, (px + 24, 726), "驳回理由（驳回时必填）", 12, SUB, anchor="lm")
    rect(d, (px + 24, 744, px + pw - 24, 792), fill="#FAFBFC", outline=BORDER, r=8)
    text(d, (px + 38, 768), "请说明具体原因，将同步给卖家", 11, MUTED, anchor="lm")
    button(d, px + 24, 812, 200, 44, "通过并发布", "primary", 14)
    button(d, px + 236, 812, 200, 44, "驳回并退回草稿", "danger", 14)
    return img


def screen_reports():
    img, d = canvas()
    topbar(d, W, "管理后台", nav=["首页", "全部商品", "管理后台"])
    sidebar(d, 0, 64, 220, 836,
            [("商品审核", "shield"), ("举报处理", "warn"), ("操作日志", "list"), ("统计报表", "chart")], "举报处理",
            "管理后台")
    x = 220
    text(d, (x + 32, 112), "举报处理", 24, TEXT, bold=True, anchor="lm")
    text(d, (x + 32, 148), "待处理 5 条 · 今日新增 2 条", 13, SUB, anchor="lm")
    # 左列表
    card(d, x + 32, 180, 440, 660)
    text(d, (x + 56, 216), "待处理举报", 14, TEXT, bold=True, anchor="lm")
    text(d, (x + 448, 216), "按时间排序", 11, MUTED, anchor="rm")
    line(d, (x + 56, 240, x + 448, 240))
    items = [("虚假描述", "显示器 与描述不符", "买家 林同学 · 11-09 10:21", True),
             ("重复发布", "同款教材重复发布 3 次", "买家 吴同学 · 11-09 09:05", False),
             ("违禁物品", "疑似出售违规电器", "卖家 周同学 · 11-08 22:10", False),
             ("联系方式", "描述中留了手机号", "买家 陈同学 · 11-08 20:33", False),
             ("恶意举报", "举报内容与商品无关", "卖家 郑镜汗 · 11-08 16:12", False)]
    yy = 240
    for reason, title, meta, active in items:
        if active:
            rect(d, (x + 44, yy + 8, x + 452, yy + 104), fill="#F5F8FF", r=8)
        chip(d, x + 56, yy + 22, reason, DANGER, DANGER_SOFT, 11, 8, 22)
        text(d, (x + 56, yy + 62), title, 13, TEXT, bold=True, anchor="lm")
        text(d, (x + 56, yy + 86), meta, 11, MUTED, anchor="lm")
        line(d, (x + 56, yy + 112, x + 448, yy + 112))
        yy += 116
    # 右详情
    rx, rw = 700, 708
    card(d, rx, 180, rw, 680)
    text(d, (rx + 28, 216), "举报详情 #RP-20261109-003", 15, TEXT, bold=True, anchor="lm")
    chip(d, rx + 600, 204, "待处理", WARNING, WARNING_SOFT, 12, 10, 26)
    line(d, (rx + 28, 244, rx + 680, 244))
    thumb(d, rx + 28, 264, 200, 120, "monitor", "#EAF7FF", "#7FB6D8", None, 8)
    text(d, (rx + 248, 282), "27 英寸 2K 显示器", 15, TEXT, bold=True, anchor="lm")
    text(d, (rx + 248, 308), "¥ 620 · 数码电子 · 在售中", 12, SUB, anchor="lm")
    text(d, (rx + 248, 334), "卖家：郑镜汗", 12, SUB, anchor="lm")
    text(d, (rx + 248, 360), "当前有效预约：1 条（买家 林同学）", 12, SUB, anchor="lm")
    line(d, (rx + 28, 404, rx + 680, 404))
    fields = [("举报人", "林同学（买家）"), ("举报原因", "虚假描述"),
              ("举报说明", "屏幕右上角有 3 处亮斑，商品描述写的是「无瑕疵」，实际不符。"),
              ("提交时间", "2026-11-09 10:21")]
    yy = 428
    for k, v in fields:
        text(d, (rx + 28, yy), k, 12, MUTED, anchor="lm")
        text(d, (rx + 128, yy), v, 12, SUB, anchor="lm")
        yy += 36
    text(d, (rx + 28, 578), "证据图片", 12, MUTED, anchor="lm")
    for i in range(3):
        thumb(d, rx + 128 + i * 112, 564, 96, 56, "image", "#F3F4F6", "#B9BFC8", None, 6)
    rect(d, (rx + 28, 640, rx + 680, 700), fill="#F7F8FA", r=8)
    text(d, (rx + 44, 658), "该商品历史举报 2 条：1 条已驳回，1 条处理中", 12, SUB, anchor="lm")
    text(d, (rx + 44, 682), "多人举报可合并查看，逐条处理互不影响。", 11, MUTED, anchor="lm")
    rect(d, (rx + 28, 716, rx + 680, 780), fill="#FFF7E6", outline="#F7DDA8", r=8)
    icon_draw(d, "warn", rx + 50, 738, 16, WARNING)
    text(d, (rx + 68, 731), "判定成立将立即下架商品，并作废该商品的有效预约、通知买家。", 11, "#8A6420")
    text(d, (rx + 68, 759), "此操作会写入操作日志，不可撤销。", 11, "#8A6420")
    button(d, rx + 28, 796, 300, 44, "判定成立并下架", "danger", 14)
    button(d, rx + 344, 796, 200, 44, "判定不成立", "ghost", 14)
    return img


def screen_stats():
    img, d = canvas()
    topbar(d, W, "首页")
    sidebar(d, 0, 64, 220, 836,
            [("商品审核", "shield"), ("举报处理", "warn"), ("操作日志", "list"), ("统计报表", "chart")], "统计报表",
            "管理后台")
    x = 220
    text(d, (x + 32, 112), "统计报表", 24, TEXT, bold=True, anchor="lm")
    text(d, (x + 32, 146), "统计口径：仅计当前有效数据，已取消预约不计入成功", 12, MUTED, anchor="lm")
    # 筛选
    card(d, x + 32, 168, 1176, 64, 10)
    field(d, x + 52, 184, 170, 36, "2026-11-03", muted=True)
    text(d, (x + 232, 202), "至", 12, MUTED, anchor="lm")
    field(d, x + 252, 184, 170, 36, "2026-11-09", muted=True)
    field(d, x + 442, 184, 190, 36, "全部分类", muted=True)
    button(d, x + 652, 184, 90, 36, "查询", "primary", 13)
    button(d, x + 752, 184, 90, 36, "导出", "ghost", 13)
    # KPI
    kpis = [("今日新增商品", "24", "+6"), ("预约成功", "18", "+3"), ("待处理举报", "5", "-2"), ("活跃用户", "156", "+21")]
    for i, (label, value, delta) in enumerate(kpis):
        stat_card(d, x + 32 + i * 300, 248, 282, 112, label, value, delta)
    # 柱状图
    card(d, x + 32, 380, 640, 300)
    text(d, (x + 56, 412), "各分类商品数量", 14, TEXT, bold=True, anchor="lm")
    text(d, (x + 648, 412), "单位：件", 11, MUTED, anchor="rm")
    base_y = 640
    maxv = 46
    bars = [("教材", 46), ("数码", 38), ("生活", 22), ("运动", 16), ("其他", 6)]
    for i, (name, v) in enumerate(bars):
        bx = x + 78 + i * 118
        h = int(200 * v / maxv)
        rect(d, (bx, base_y - h, bx + 62, base_y), fill=PRIMARY if i < 2 else "#9FB8F5", r=6)
        text(d, (bx + 31, base_y - h - 14), str(v), 11, SUB, anchor="mm")
        text(d, (bx + 31, base_y + 20), name, 12, SUB, anchor="mm")
    line(d, (x + 56, base_y, x + 648, base_y), fill="#D9DEE7", width=1)
    # 折线图
    card(d, x + 692, 380, 516, 300)
    text(d, (x + 716, 412), "近 7 天预约成功", 14, TEXT, bold=True, anchor="lm")
    pts = [8, 12, 9, 15, 11, 18, 14]
    xs = [x + 736 + i * 66 for i in range(7)]
    ys = [620 - p * 9 for p in pts]
    for i in range(6):
        d.line((xs[i], ys[i], xs[i + 1], ys[i + 1]), fill=PRIMARY, width=3)
    for i, (px, py) in enumerate(zip(xs, ys)):
        d.ellipse((px - 4, py - 4, px + 4, py + 4), fill="#FFFFFF", outline=PRIMARY, width=2)
        text(d, (px, 650), "11-0%d" % (i + 3), 10, MUTED, anchor="mm")
    for gy in range(3):
        y = 470 + gy * 50
        line(d, (x + 716, y, x + 1184, y), fill="#F0F2F5")
    # 日志表
    card(d, x + 32, 700, 1176, 180)
    text(d, (x + 56, 730), "最近操作日志", 14, TEXT, bold=True, anchor="lm")
    text(d, (x + 1184, 730), "查看全部", 12, PRIMARY, anchor="rm")
    line(d, (x + 56, 750, x + 1184, 750))
    logs = [("10:21", "管理员 兰雨阳", "审核通过", "商品 IT202611080008"),
            ("09:47", "卖家 王同学", "确认预约", "预约 RS202611090021"),
            ("09:12", "管理员 兰雨阳", "驳回商品", "商品 IT202611080005"),
            ("08:40", "买家 林同学", "提交预约", "商品 IT202611080012")]
    yy = 772
    for t, who, act, obj in logs:
        text(d, (x + 56, yy), t, 11, MUTED, anchor="lm")
        text(d, (x + 116, yy), who, 12, SUB, anchor="lm")
        text(d, (x + 320, yy), act, 12, TEXT, anchor="lm")
        text(d, (x + 480, yy), obj, 12, SUB, anchor="lm")
        yy += 26
    return img


SCREENS = [
    ("界面1_登录注册.png", screen_login),
    ("界面2_商品检索.png", screen_browse),
    ("界面3_商品详情.png", screen_detail),
    ("界面4_发布商品.png", screen_publish),
    ("界面5_卖家中心.png", screen_seller),
    ("界面6_商品审核.png", screen_audit),
    ("界面7_举报处理.png", screen_reports),
    ("界面8_日志与统计.png", screen_stats),
]

