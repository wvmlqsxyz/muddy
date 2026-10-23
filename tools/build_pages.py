"""game/index.html(아티팩트용 본문)을 GitHub Pages용 완전한 HTML(/index.html)로 감싼다.
사용: python3 tools/build_pages.py
"""
from pathlib import Path
root = Path(__file__).resolve().parent.parent
body = (root / "game" / "index.html").read_text(encoding="utf-8")
head = """<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px);box-sizing:border-box;height:100%}body{margin:0;font:14px system-ui,sans-serif}</style>
</head>
<body>
"""
out = head + body + "\n</body>\n</html>\n"
(root / "index.html").write_text(out, encoding="utf-8")
print("wrote index.html", len(out), "bytes")
