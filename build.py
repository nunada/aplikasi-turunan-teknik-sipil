"""Generator situs statis: src/content/*.md + src/figs*.py -> docs/*.html

Format konten:
    @@ id | label | judul | topik | halaman
    teks soal ... {{fig:nama}}
    ===
    teks penyelesaian ...
"""
import html
import importlib
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent
SRC = ROOT / "src"
OUT = ROOT / "docs"
sys.path.insert(0, str(SRC))
from svg import FIGS  # noqa: E402
import autoplot  # noqa: E402

for mod in sorted(SRC.glob("figs_*.py")):
    importlib.import_module(mod.stem)

TOPICS = {
    "dasar": "Dasar & Teori",
    "geometri": "Geometri & Luas",
    "volume": "Wadah & Volume",
    "struktur": "Struktur & Konstruksi",
    "air": "Air & Hidraulika",
    "biaya": "Biaya & Manajemen",
    "lintasan": "Jarak, Lintasan & Waktu",
    "gerak": "Kinematika & Fisika",
    "laju": "Laju yang Berkaitan",
}

PAGES = [
    ('hass', 'Thomas 4.6',
     "Hass, Heil & Weir — Thomas' Calculus: Early Transcendentals (SI), ed. 15",
     '§4.6 Applied Optimization'),
    ('stewart', 'Stewart 4.7',
     'Stewart, Clegg & Watson — Calculus: Early Transcendentals, ed. 9',
     '§4.7 Optimization Problems'),
    ('larson-optimasi', 'Larson 3.7',
     'Larson & Edwards — Calculus, ed. 12',
     '§3.7 Optimization Problems'),
    ('trim-optimasi', 'Trim 4.7',
     'Trim — Calculus for Engineers, ed. 4',
     '§4.7 Absolute Maxima and Minima'),
    ('thomas-laju', 'Thomas 3.10',
     "Hass, Heil & Weir — Thomas' Calculus: Early Transcendentals (SI), ed. 15",
     '§3.10 Related Rates'),
    ('stewart-laju', 'Stewart 3.9',
     'Stewart, Clegg & Watson — Calculus: Early Transcendentals, ed. 9',
     '§3.9 Related Rates'),
    ('larson-laju', 'Larson 2.6',
     'Larson & Edwards — Calculus, ed. 12',
     '§2.6 Related Rates'),
    ('trim-laju', 'Trim 4.9',
     'Trim — Calculus for Engineers, ed. 4',
     '§4.9 Related Rates'),
    ('trim-gerak', 'Trim 4.8',
     'Trim — Calculus for Engineers, ed. 4',
     '§4.8 Velocity and Acceleration'),
]

GROUPS = [("Optimisasi Terapan", "Optimisasi", ["hass", "stewart", "larson-optimasi", "trim-optimasi"]),
          ("Laju yang Berkaitan (Related Rates)", "Laju Berkaitan", ["thomas-laju", "stewart-laju", "larson-laju", "trim-laju"]),
          ("Kecepatan dan Percepatan", "Kinematika", ["trim-gerak"])]

MATH = re.compile(r"\$\$.+?\$\$|\$[^$\n]+?\$", re.S)


def inline(text):
    text = html.escape(text, quote=False)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    return text


def render(src, used):
    """Markdown mini: paragraf, daftar '- ', tabel '|', judul '### ', gambar."""
    maths = []

    def stash(m):
        maths.append(m.group(0))
        return f"\x00{len(maths) - 1}\x00"

    src = MATH.sub(stash, src.strip())
    out = []
    for block in re.split(r"\n\s*\n", src):
        lines = [l.rstrip() for l in block.split("\n") if l.strip()]
        buf, items, rows = [], [], []

        def flush():
            if buf:
                out.append("<p>" + inline(" ".join(buf)) + "</p>")
                buf.clear()
            if items:
                out.append("<ul>" + "".join(f"<li>{inline(i)}</li>" for i in items) + "</ul>")
                items.clear()
            if rows:
                body = ""
                for n, r in enumerate(rows):
                    tag = "th" if n == 0 else "td"
                    body += "<tr>" + "".join(f"<{tag}>{inline(c.strip())}</{tag}>" for c in r) + "</tr>"
                out.append(f'<div class="tbl"><table>{body}</table></div>')
                rows.clear()

        for line in lines:
            s = line.strip()
            fig = re.fullmatch(r"\{\{fig:([\w\- ]+)\}\}", s)
            if fig:
                flush()
                figs = []
                for name in fig.group(1).split():
                    if name not in FIGS:
                        raise SystemExit(f"gambar tidak ada: {name}")
                    used.add(name)
                    figs.append(FIGS[name]())
                out.append('<div class="figs">' + "".join(figs) + "</div>")
            elif s.startswith("- "):
                if buf or rows:
                    flush()
                items.append(s[2:])
            elif s.startswith("|"):
                if buf or items:
                    flush()
                rows.append(s.strip("|").split("|"))
            elif s.startswith("### "):
                flush()
                out.append(f"<h4>{inline(s[4:])}</h4>")
            elif items and line.startswith("  "):
                items[-1] += " " + s
            else:
                if items or rows:
                    flush()
                buf.append(s)
        flush()
    result = "\n".join(out)
    return re.sub(r"\x00(\d+)\x00", lambda m: html.escape(maths[int(m.group(1))], quote=False), result)


def parse(page):
    problems = []
    for path in sorted((SRC / "content").glob(f"{page}.*.md")):
        text = path.read_text(encoding="utf-8")
        for chunk in re.split(r"^@@ ", text, flags=re.M)[1:]:
            head, body = chunk.split("\n", 1)
            parts = [p.strip() for p in head.split("|")]
            if len(parts) != 5:
                raise SystemExit(f"header salah di {path.name}: {head}")
            if "\n===" not in body:
                raise SystemExit(f"tanpa penyelesaian: {path.name} {parts[0]}")
            q, a = body.split("\n===", 1)
            if parts[3] not in TOPICS:
                raise SystemExit(f"topik tidak dikenal: {parts}")
            problems.append(dict(id=parts[0], label=parts[1], title=parts[2], topic=parts[3],
                                 hal=parts[4], q=q, a=a, graphs=[]))
    byid = {p["id"]: p for p in problems}
    for path in sorted((SRC / "content").glob(f"{page}.grafik*.txt")):
        for line in path.read_text(encoding="utf-8").splitlines():
            if not line.strip() or line.startswith("#"):
                continue
            pid, spec = [s.strip() for s in line.split("|", 1)] if line.count("|") == 1 else (
                line.split("|", 1)[0].strip(), line.split("|", 1)[1].strip())
            if pid not in byid:
                raise SystemExit(f"{path.name}: id tidak dikenal {pid}")
            byid[pid]["graphs"].append(autoplot.make(spec, f"{page} {pid}"))
    return problems


def key(p):
    m = re.match(r"([CPL])(\d+)", p["id"])
    return ({"C": 0, "P": 1, "L": 2}[m.group(1)], int(m.group(2)))


def navigation(active):
    """Tiga menu ringkas sesuai GROUPS; grup berisi satu halaman jadi tautan langsung."""
    short = {p: s for p, s, _, _ in PAGES}
    current = ' aria-current="page"'
    parts = []
    for _, label, names in GROUPS:
        on = " class=\"on\"" if active in names else ""
        if len(names) == 1:
            parts.append(f'<a href="{names[0]}.html"{on}{current if on else ""}>{label}</a>')
            continue
        items = ""
        for p in names:
            book, section = short[p].rsplit(" ", 1)
            items += (f'<li><a href="{p}.html"{current if p == active else ""}>'
                      f'{book}<span>§{section}</span></a></li>')
        parts.append(f'<details class="menu"><summary{on}>{label}</summary><ul>{items}</ul></details>')
    return "".join(parts)


def shell(title, active, body, scripts=True):
    nav = navigation(active)
    home = ' aria-current="page"' if active == "index" else ""
    katex = """<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js"></script>
<script defer src="app.js"></script>""" if scripts else ""
    return f"""<!doctype html>
<html lang="id">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex">
<title>{html.escape(title)}</title>
<script>
(function () {{
  var t = null;
  try {{ t = localStorage.getItem("tema"); }} catch (e) {{}}
  if (t !== "light" && t !== "dark") t = matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
  document.documentElement.dataset.theme = t;
}})();
</script>
<link rel="stylesheet" href="style.css">
{katex}
</head>
<body>
<header><div class="hbar">
<a class="brand" href="index.html" title="Beranda"{home}>Aplikasi Turunan<span> · Teknik Sipil</span></a>
<nav aria-label="Navigasi utama">{nav}</nav>
<button id="tema" type="button" hidden></button>
</div></header>
<main>
{body}
</main>
<footer>Soal diringkas dengan kata-kata sendiri untuk keperluan belajar; penyelesaian dan gambar dibuat ulang.
Teks asli dan hak cipta tetap milik penulis serta penerbit masing-masing buku.</footer>
</body>
</html>
"""


def card(p, used):
    kind = {"C": "contoh", "P": "latihan", "L": "proyek"}[p["id"][0]]
    graphs = ""
    if p["graphs"]:
        graphs = ('<p class="glabel">Grafik pemeriksaan</p><div class="figs">'
                  + "".join(p["graphs"]) + "</div>")
    return f"""<article class="soal {kind}" id="{p['id']}" data-topic="{p['topic']}" data-kind="{kind}">
<h3><a href="#{p['id']}">{html.escape(p['label'])}</a> {inline(p['title'])}</h3>
<div class="meta"><span class="tag">{TOPICS[p['topic']]}</span><span>hlm. {p['hal']}</span></div>
{render(p['q'], used)}
<details><summary>Penyelesaian</summary><div class="solusi">
{render(p['a'], used)}
{graphs}
</div></details>
</article>"""


def main():
    OUT.mkdir(exist_ok=True)
    used, stats = set(), []
    for page, short, book, sec in PAGES:
        if not list((SRC / "content").glob(f"{page}.*.md")):
            continue
        probs = sorted(parse(page), key=key)
        ids = [p["id"] for p in probs]
        dup = {i for i in ids if ids.count(i) > 1}
        if dup:
            raise SystemExit(f"id ganda di {page}: {dup}")
        count = {k: sum(1 for i in ids if i[0] == k) for k in "CPL"}
        stats.append((page, short, book, sec, count))
        topics = sorted({p["topic"] for p in probs}, key=list(TOPICS).index)
        options = "".join(f'<option value="{t}">{TOPICS[t]}</option>' for t in topics)
        body = [f"<h1>{sec}</h1><p class='book'>{html.escape(book)}</p>",
                f"""<div class="bar">
<input id="q" type="search" placeholder="Cari soal…" aria-label="Cari soal">
<select id="topik" aria-label="Topik"><option value="">Semua topik</option>{options}</select>
<select id="jenis" aria-label="Jenis"><option value="">Contoh &amp; latihan</option><option value="contoh">Contoh soal</option><option value="latihan">Soal latihan</option><option value="proyek">Proyek</option></select>
<button id="buka" type="button">Buka semua</button><button id="tutup" type="button">Tutup semua</button>
<span id="hitung"></span></div>"""]
        for kind, heading in (("C", "Contoh Soal"), ("P", "Soal Latihan"), ("L", "Proyek Terapan")):
            group = [p for p in probs if p["id"][0] == kind]
            if not group:
                continue
            chips = "".join(f'<a href="#{p["id"]}">{p["id"][1:]}</a>' for p in group)
            body.append(f"<section><h2>{heading}</h2><div class='chips'>{chips}</div>")
            body += [card(p, used) for p in group]
            body.append("</section>")
        (OUT / f"{page}.html").write_text(shell(f"{short} — {sec}", page, "\n".join(body)), encoding="utf-8")

    intro = render((SRC / "content" / "index.txt").read_text(encoding="utf-8"), used)
    by = {s[0]: s for s in stats}
    grid = ""
    for heading, _, names in GROUPS:
        cards = ""
        for page, short, book, sec, c in (by[n] for n in names if n in by):
            extra = f" · {c['L']} proyek" if c["L"] else ""
            cards += (f'<a class="buku" href="{page}.html"><b>{sec}</b><span>{html.escape(book)}</span>'
                      f'<em>{c["C"]} contoh · {c["P"]} latihan{extra}</em></a>')
        grid += f"<h2>{heading}</h2><div class='grid'>{cards}</div>"
    total = sum(sum(s[4].values()) for s in stats)
    body = (f"<h1>Aplikasi Turunan untuk Mahasiswa S1 Teknik Sipil</h1>"
            f"<p class='book'>{total} soal dengan penyelesaian yang dapat dibuka-tutup.</p>"
            f"{grid}{intro}")
    (OUT / "index.html").write_text(shell("Aplikasi Turunan · Teknik Sipil", "index", body), encoding="utf-8")
    (OUT / ".nojekyll").write_text("")
    for name in ("style.css", "app.js"):
        (OUT / name).write_text((SRC / name).read_text(encoding="utf-8"), encoding="utf-8")
    for s in stats:
        print(s[0], s[4])
    print("total", total, "| gambar dipakai", len(used), "| tak dipakai", sorted(set(FIGS) - used))


if __name__ == "__main__":
    main()
