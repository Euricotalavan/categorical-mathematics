#!/usr/bin/env python3
"""Build the standalone research HTML from Markdown and fixed public v8 PDFs.

Dependencies: Python 3, Markdown, PyMuPDF. No manuscript edits or LaTeX builds.
Use --pdf-dir for already verified local volume-0.pdf, volume-1.pdf, volume-2.pdf.
Otherwise the fixed public PDFs are downloaded into a temporary directory.
"""
from pathlib import Path
import argparse
import base64
import hashlib
import html
import re
import tempfile
import urllib.request

import fitz
import markdown

ROOT = Path(__file__).resolve().parents[1]
COMMIT = "60fe8d1910c06c309958edb9efcd20d63cbb08ac"
BASE = f"https://raw.githubusercontent.com/Euricotalavan/categorical-mathematics/{COMMIT}/archive/v0-v2/readflow-editorial-v8-2026-11-19/reading"
EXPECTED = {
    0: "4d931401a3bcbec3d7bae6b593c8e7d98d2821ac76c577ea40441f9631f15e85",
    1: "4bc998ed7a28d073247fe863036f875c4af3dec3c391e5e9349da452bd19eb43",
    2: "ad29b6392b95938ff9f471c05a6f53332f4afda1761d4c43818a6166dbb59537",
}

CSS = """
:root{--ink:#233c40;--muted:#567075;--green:#176a61;--gold:#a56f32;--line:#d8e4df;--paper:#f4f7f4;--panel:#fff}
*{box-sizing:border-box}html{scroll-behavior:smooth;scroll-padding-top:24px}body{margin:0;background:var(--paper);color:var(--ink);font:17px/1.85 system-ui,-apple-system,"Noto Sans CJK TC","Microsoft JhengHei",sans-serif}
a{color:var(--green);text-underline-offset:3px;overflow-wrap:anywhere}a:hover{color:#0c443e}header{padding:48px max(28px,calc((100vw - 1250px)/2));background:#e1ede7;border-bottom:1px solid #c3d9cf}header .eyebrow{letter-spacing:.13em;font-size:13px;color:#30665a;font-weight:700}header h1{font-size:clamp(28px,4vw,44px);line-height:1.35;max-width:950px;margin:14px 0}header p{max-width:880px;margin:12px 0}header .meta{font-size:14px;color:var(--muted)}
.layout{display:grid;grid-template-columns:230px minmax(0,960px);gap:42px;max-width:1290px;margin:auto;padding:35px 24px 80px}aside{position:sticky;top:22px;align-self:start;font-size:13px;line-height:1.6;max-height:92vh;overflow:auto}aside h2{font-size:15px;margin:0 0 12px}.toc ul{list-style:none;padding-left:0;margin:0}.toc ul ul{padding-left:12px;margin:6px 0 10px}.toc li{margin:6px 0}.toc>ul>li>a{font-weight:600}.toc ul ul ul{display:none}.toc a{text-decoration:none;color:var(--muted)}main{min-width:0;background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:35px 42px;box-shadow:0 8px 28px #1d4d3710}main>h1{display:none}h2{font-size:26px;line-height:1.45;border-top:1px solid var(--line);padding-top:28px;margin:42px 0 18px}h2:first-of-type{border-top:0;padding-top:0;margin-top:18px}h3{font-size:21px;line-height:1.5;margin:30px 0 12px}p{margin:14px 0}strong{font-weight:700}blockquote{border-left:4px solid #4b8c79;background:#edf5f0;padding:10px 20px;margin:20px 0}blockquote p{margin:8px 0}code{font:0.85em/1.6 "DejaVu Sans Mono",monospace;background:#edf3ef;padding:2px 4px;border-radius:3px;overflow-wrap:anywhere}pre{background:#eff4f1;border:1px solid #dce7df;border-radius:8px;padding:16px;overflow-x:auto;white-space:pre-wrap;overflow-wrap:anywhere;font-size:14px}pre code{padding:0;background:none}.table-wrap{overflow-x:auto;margin:22px 0}table{border-collapse:collapse;width:100%;font-size:14px;line-height:1.65}th,td{text-align:left;vertical-align:top;padding:11px 12px;border-bottom:1px solid var(--line)}th{background:#e6f0eb;color:#194f43}td code{font-size:12px}tr:nth-child(even) td{background:#fafcfb}ul,ol{padding-left:25px}li{margin:8px 0}figure{margin:24px 0;padding:15px;border:1px solid var(--line);background:#f8faf8;border-radius:10px}figure img{display:block;width:100%;height:auto;max-width:760px;margin:auto}figcaption{font-size:13px;color:var(--muted);margin:12px 4px 0}details{margin:25px 0;border:1px solid #e0d5be;border-radius:8px;padding:14px 18px;background:#fcfaf4}summary{cursor:pointer;font-weight:650;color:#765b30}footer{border-top:1px solid var(--line);padding:22px;font-size:13px;text-align:center;color:var(--muted)}.note{font-size:14px;color:var(--muted)}
@media(max-width:1050px){.layout{grid-template-columns:1fr;max-width:950px;gap:20px}aside{position:static;max-height:none}.toc>ul>li>ul{display:grid;grid-template-columns:1fr 1fr;gap:4px 18px}.toc ul ul ul{display:none}main{padding:26px}}
@media(max-width:600px){body{font-size:16px}.layout{padding:18px 10px 40px}header{padding:28px 20px}main{padding:20px 16px;border-radius:8px}h2{font-size:23px}h3{font-size:19px}.toc>ul>li>ul{display:block}table{min-width:580px}figure{padding:7px}blockquote{padding:8px 13px}pre{font-size:12px}code{word-break:break-word}}
@media print{body{background:white;font-size:11pt}header{padding:18pt;border-bottom:1pt solid #bbb}.layout{display:block;padding:0;max-width:none}aside{display:none}main{border:0;box-shadow:none;padding:16pt}h2{break-after:avoid}figure,blockquote{break-inside:avoid}a{color:inherit}details{display:block}table{font-size:9pt}}
"""


def render_figure(pdfdir, volume, page, caption, crop=False):
    path = pdfdir / f"volume-{volume}.pdf"
    data = path.read_bytes()
    assert hashlib.sha256(data).hexdigest() == EXPECTED[volume], path
    with fitz.open(stream=data, filetype="pdf") as doc:
        p = doc[page - 1]
        clip = fitz.Rect(45, 620, p.rect.width - 45, p.rect.height) if crop else None
        pix = p.get_pixmap(matrix=fitz.Matrix(1.4, 1.4), clip=clip)
        b64 = base64.b64encode(pix.tobytes("png")).decode()
    url = f"https://github.com/Euricotalavan/categorical-mathematics/blob/{COMMIT}/archive/v0-v2/readflow-editorial-v8-2026-11-19/reading/volume-{volume}.pdf#page={page}"
    return f'<figure><img src="data:image/png;base64,{b64}" alt="{html.escape(caption)}"><figcaption>{html.escape(caption)} · <a href="{url}">固定公開 PDF</a></figcaption></figure>'


def build(pdfdir):
    md = markdown.Markdown(extensions=["tables", "fenced_code", "toc"], extension_configs={"toc": {"toc_depth": "1-2"}})
    body = md.convert((ROOT / "SUCCESS-ANALYSIS.md").read_text())
    body = re.sub(r"<table>(.*?)</table>", r'<div class="table-wrap"><table>\1</table></div>', body, flags=re.S)
    first = render_figure(pdfdir, 1, 9, "v8 V1 實體第 9 頁：存在要求、量詞依賴與相容性提示在同一頁；這張圖不是舊版。")
    second = render_figure(pdfdir, 0, 55, "v8 V0 實體第 55 頁：共同型別置於表頭，五步等式和理由保留，兩小題完整收束。")
    body = re.sub(r'(<h3[^>]*>3\.2\s)', lambda m: first + m.group(1), body, count=1)
    body = re.sub(r'(<h3[^>]*>3\.3\s)', lambda m: second + m.group(1), body, count=1)
    footers = '<details><summary>查看兩個已登錄的頁尾重疊（未修稿）</summary>'
    footers += render_figure(pdfdir, 0, 274, "V0 實體 274／印頁 262：正文末行與頁腳重疊。", True)
    footers += render_figure(pdfdir, 2, 175, "V2 實體 175／印頁 166：正文末行與頁腳重疊。", True)
    footers += "</details>"
    body = re.sub(r'(<h3[^>]*>6\.3\s)', lambda m: footers + m.group(1), body, count=1)
    public_root = "https://github.com/Euricotalavan/categorical-mathematics/blob/research/readability-methodology-20261117/research/readability/editorial-v8-20261119/"
    body = re.sub(r'href="(?!https?:|#)([^"]+)"', lambda m: 'href="' + public_root + m.group(1) + '"', body)
    output = f'''<!doctype html>
<html lang="zh-Hant"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>v8 閱讀成功：原因分析與可重用方法</title><style>{CSS}</style></head>
<body><header><div class="eyebrow">CATEGORICAL MATHEMATICS · SUCCESS STUDY</div>
<h1>v8 閱讀成功<br>把做對的事留下來</h1>
<p>使用者回饋：不同頁面約 <strong>85–93 分</strong>，整體能讀且滿意。<br>本報告用原文、PDF 和可重核數據，說明值得重用的做法與適用邊界。</p>
<p class="meta">2026-11-19 · 研究 v1 · 書稿固定 60fe8d1 · 正式 ReadFlow R1 與 A／B 不變</p></header>
<div class="layout"><aside><h2>閱讀導覽</h2>{md.toc}<p class="note">數據幫忙找位置；數學與閱讀各自核查。</p></aside><main>{body}</main></div>
<footer>研究文件，不改已滿意的教材。完整前後文、來源身份、OPEN 與角色交接可由文中連結追溯。</footer></body></html>'''
    path = ROOT / "SUCCESS-ANALYSIS.html"
    path.write_text(output, encoding="utf-8")
    print(f"Built {path.name}: {path.stat().st_size} bytes; four source-backed embedded images")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pdf-dir", type=Path)
    args = parser.parse_args()
    if args.pdf_dir:
        build(args.pdf_dir)
        return
    with tempfile.TemporaryDirectory(prefix="v8-success-pdfs-") as tmp:
        directory = Path(tmp)
        for v in range(3):
            with urllib.request.urlopen(f"{BASE}/volume-{v}.pdf", timeout=60) as r:
                data = r.read()
            assert hashlib.sha256(data).hexdigest() == EXPECTED[v]
            (directory / f"volume-{v}.pdf").write_bytes(data)
        build(directory)


if __name__ == "__main__":
    main()
