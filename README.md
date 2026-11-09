# 实验二：软件设计与建模 — 校园二手交易系统

## 目录
- `实验报告.docx` / `实验报告.pdf`：设计报告（项目概述、功能、架构、UML、UI、AI 使用记录、版本信息）
- `UML/`：7 张 PlantUML 图（.puml 源码 + .png 导出）
- `UI/`：8 个界面原型（1440×900 PNG）
- `src/`：报告与界面生成脚本（python-docx / Pillow）
- `设计初稿.md`：AI 生成的设计初稿（第一次提交内容）

## 设计要点
- 五层架构：表现层 / 接口层 / 应用层 / 领域层 / 基础设施层
- 7 个业务模块：用户与权限、商品管理、商品检索、预约交易、举报处理、操作日志、统计汇总
- 同一商品最多一条有效预约：`item.active_item_id` 生成列 + 唯一索引，并发插入由数据库兜底
- 商品状态机 7 状态，已完成与已下架为终态

## 提交记录
- `41cbad3` AI 初稿
- `b099808` UML 人工修改
- `eeeb252` UI 与文案人工修改
- `0f9a8fc` 包图二次精简
- 定稿提交：报告、导出图与打包文件

## 生成方式
```bash
python src/build_ui.py       # 生成 UI/*.png
python src/build_report.py   # 生成 实验报告.docx（再用 LibreOffice 导出 PDF）
```
UML 使用 PlantUML 渲染：`java -jar plantuml.jar -tpng UML/*.puml`
