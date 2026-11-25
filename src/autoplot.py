"""Grafik otomatis pada penyelesaian, sekaligus pemeriksaan numerik titik ekstrem.

Baris di <halaman>.grafik.txt:
    ID | ekspresi(x) ; a ; b ; label_x ; label_y ; jenis@x[,x2...] [; catatan]
jenis: max, min  -> ekstrem mutlak pada [a, b] (diperiksa)
       lmax, lmin -> ekstrem lokal (diperiksa)
       pt         -> hanya ditandai
"""
import math

from shapes import curve

ENV = {k: getattr(math, k) for k in dir(math) if not k.startswith("_")}
ENV.update(abs=abs, max=max, min=min, cot=lambda t: 1 / math.tan(t), sec=lambda t: 1 / math.cos(t),
           csc=lambda t: 1 / math.sin(t), cbrt=lambda t: math.copysign(abs(t) ** (1 / 3), t))


def num(s):
    return float(eval(s, ENV))


def fmt(v):
    if abs(v) >= 1000:
        return f"{v:.0f}"
    return f"{v:.3g}".replace(".", ",").replace("-", "−")


def make(spec, where):
    parts = [p.strip() for p in spec.split(";")]
    if len(parts) < 6:
        raise SystemExit(f"grafik salah: {where}: {spec}")
    expr, a, b, xl, yl, mark = parts[:6]
    note = parts[6] if len(parts) > 6 else None
    code = compile(expr, where, "eval")

    def f(x):
        return eval(code, ENV, {"x": x, "t": x})

    a, b = num(a), num(b)
    n = 1500
    span = b - a
    xs = [a + span * i / n for i in range(n + 1)]
    xs[0] += span * 1e-9
    xs[-1] -= span * 1e-9
    vals = [f(x) for x in xs]
    kind, at = mark.split("@")
    pts = [num(s) for s in at.split(",")]
    for p in pts:
        v = f(p)
        tol = 1e-3 * max(1.0, abs(v))
        if kind == "max" and max(vals) > v + tol:
            raise SystemExit(f"{where}: bukan maksimum di {p}: f={v}, ada {max(vals)} di {xs[vals.index(max(vals))]}")
        if kind == "min" and min(vals) < v - tol:
            raise SystemExit(f"{where}: bukan minimum di {p}: f={v}, ada {min(vals)} di {xs[vals.index(min(vals))]}")
        if kind in ("lmax", "lmin"):
            sign = 1 if kind == "lmax" else -1
            for q in (p - span / 100, p + span / 100):
                if sign * (f(q) - v) > 0:
                    raise SystemExit(f"{where}: bukan {kind} di {p}")
    marked = [f(p) for p in pts]
    lo, hi = min(vals), max(vals)
    # potong nilai yang meledak di dekat asimtot
    ref_lo, ref_hi = min(marked), max(marked)
    inner = sorted(vals)[int(.04 * n):int(.9 * n)]
    scale = max(inner[-1] - inner[0], abs(ref_lo) * .5, 1e-6)
    if hi > ref_hi + 2.2 * scale:
        hi = ref_hi + 1.6 * scale
    if lo < ref_lo - 2.2 * scale:
        lo = ref_lo - 1.6 * scale
    ymin, ymax = min(lo, 0), max(hi, 0)
    if lo > 0.6 * hi > 0:  # kurva jauh di atas nol: perbesar daerah optimum
        ymin = 0
    if ymax - ymin < 1e-9:
        ymax = ymin + 1
    xt = [(p, fmt(p)) for p in pts]
    yt = []
    for v in marked:
        if abs(v) > 1e-9 and all(abs(v - w) > .08 * (ymax - ymin) for w, _ in yt):
            yt.append((v, fmt(v)))
    g = curve(f, xs[0], xs[-1], ymin, ymax + (ymax - ymin) * .04, xl, yl, xt=xt, yt=yt, label=note)
    for p in pts:
        g.line((p, 0), (p, f(p)), c="d").dot((p, f(p)))
    return g.svg()
