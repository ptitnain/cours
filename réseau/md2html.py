import re, html, sys
path = sys.argv[1]; title = sys.argv[2] if len(sys.argv) > 2 else "Résumé"
src = open(path, encoding="utf-8").read().splitlines()
def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"(?<!\*)\*(?!\s)(.+?)(?<!\s)\*(?!\*)", r"<i>\1</i>", t)
    return t
out, i, lst = [], 0, None
def close():
    global lst
    if lst: out.append(f"</{lst}>"); lst = None
while i < len(src):
    l = src[i]; s = l.strip()
    if s.startswith("|") and i+1 < len(src) and re.match(r"^\|[-| ]+\|$", src[i+1].strip()):
        close(); rows = [s]; i += 2
        while i < len(src) and src[i].strip().startswith("|"):
            rows.append(src[i].strip()); i += 1
        cells = lambda r: [c.strip() for c in r.strip("|").split("|")]
        out.append("<table><tr>" + "".join(f"<th>{inline(c)}</th>" for c in cells(rows[0])) + "</tr>")
        for r in rows[1:]:
            out.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in cells(r)) + "</tr>")
        out.append("</table>"); continue
    m = re.match(r"^!\[(.*?)\]\((.+?)\)$", s)
    if m:
        close(); out.append(f'<p class="schema"><img src="{m.group(2)}" alt="{m.group(1)}"></p>'); i += 1; continue
    if s.startswith("```"):
        close(); i += 1; block = []
        while i < len(src) and not src[i].strip().startswith("```"):
            block.append(html.escape(src[i], quote=False)); i += 1
        out.append("<pre>" + chr(10).join(block) + "</pre>"); i += 1; continue
    if s == "---": close(); out.append("<hr>")
    elif s.startswith("### "): close(); out.append(f"<h3>{inline(s[4:])}</h3>")
    elif s.startswith("## "): close(); out.append(f"<h2>{inline(s[3:].strip('= '))}</h2>")
    elif s.startswith("- "):
        if lst != "ul": close(); out.append("<ul>"); lst = "ul"
        out.append(f"<li>{inline(s[2:])}</li>")
    elif re.match(r"^\d+\. ", s):
        if lst != "ol": close(); out.append("<ol>"); lst = "ol"
        out.append(f"<li>{inline(re.sub(r'^[0-9]+[.] ', '', s))}</li>")
    elif l.startswith("  ") and lst and s:
        out[-1] = out[-1][:-5] + "<br>" + inline(s) + "</li>"
    elif not s: close()
    else: close(); out.append(f"<p>{inline(s)}</p>")
    i += 1
close()
css = """body{font-family:'Times New Roman',serif;font-size:17px;line-height:1.5;max-width:820px;margin:30px auto;padding:0 20px;color:#111;background:#fff}
h2{text-align:center;font-size:18px;margin:28px 0 10px} h3{font-size:17px;margin:18px 0 6px;text-decoration:underline}
p{margin:8px 0} ul,ol{margin:4px 0 8px;padding-left:26px} li{margin:3px 0}
table{border-collapse:collapse;margin:8px 0} th,td{border:1px solid #555;padding:4px 10px;text-align:left} th{background:#eee}
code{font-family:Consolas,monospace;font-size:15px;background:#f2f2f2;padding:0 3px}
pre{font-family:Consolas,monospace;font-size:14px;background:#f6f6f6;border:1px solid #ccc;padding:6px 10px}
img{max-width:100%;height:auto} .schema{text-align:center;margin:10px 0} hr{border:none;border-top:2px dashed #999;margin:22px 0}"""
page = f'<!doctype html><html lang="fr"><head><meta charset="utf-8"><title>{title}</title><style>{css}</style></head><body>\n' + "\n".join(out) + "\n</body></html>"
open(path[:-3] + ".html", "w", encoding="utf-8").write(page); print("ok")
