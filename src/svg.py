"""Pustaka gambar SVG kecil dengan koordinat matematika (sumbu y ke atas)."""
import math
from html import escape

FIGS = {}


def fig(fn):
    FIGS[fn.__name__] = lambda: fn().svg()
    return fn


def ribuan(v):
    """1000 -> 1.000 dan 2.5 -> 2,5."""
    s = f"{v:,.6f}".rstrip("0").rstrip(".")
    return s.replace(",", " ").replace(".", ",").replace(" ", ".").replace("-", "−")


def register(name, maker):
    FIGS[name] = lambda: maker().svg()


class F:
    def __init__(self, x0, x1, y0, y1, w=320, h=None, cap=None, pad=22):
        self.x0, self.y1 = x0, y1
        self.sx = w / (x1 - x0)
        self.sy = self.sx if h is None else h / (y1 - y0)
        self.w, self.h = w, (y1 - y0) * self.sy
        self.pad, self.cap, self.el = pad, cap, []

    def P(self, p):
        return (self.pad + (p[0] - self.x0) * self.sx, self.pad + (self.y1 - p[1]) * self.sy)

    def _pts(self, pts):
        return " ".join("%.1f,%.1f" % self.P(p) for p in pts)

    # --- primitif ---
    def line(self, *pts, c="s"):
        self.el.append(f'<polyline class="{c}" points="{self._pts(pts)}"/>')
        return self

    def poly(self, *pts, c="s", fill=None):
        if fill:
            self.el.append(f'<polygon class="{fill}" points="{self._pts(pts)}"/>')
        if c:
            self.el.append(f'<polygon class="{c}" points="{self._pts(pts)}"/>')
        return self

    def rect(self, x, y, w, h, c="s", fill=None):
        return self.poly((x, y), (x + w, y), (x + w, y + h), (x, y + h), c=c, fill=fill)

    def dot(self, p, r=3.2):
        x, y = self.P(p)
        self.el.append(f'<circle class="dot" cx="{x:.1f}" cy="{y:.1f}" r="{r}"/>')
        return self

    def ellipse(self, cx, cy, rx, ry=None, c="s", fill=None):
        ry = rx if ry is None else ry
        x, y = self.P((cx, cy))
        for cls in (fill, c):
            if cls:
                self.el.append(f'<ellipse class="{cls}" cx="{x:.1f}" cy="{y:.1f}" '
                               f'rx="{rx * self.sx:.1f}" ry="{ry * self.sy:.1f}"/>')
        return self

    def arc(self, cx, cy, rx, a0, a1, ry=None, c="s", fill=None, n=72):
        """Busur elips dari sudut a0 ke a1 (derajat)."""
        ry = rx if ry is None else ry
        pts = [(cx + rx * math.cos(math.radians(a0 + (a1 - a0) * i / n)),
                cy + ry * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
        if fill:
            self.el.append(f'<polygon class="{fill}" points="{self._pts(pts)}"/>')
        if c:
            self.line(*pts, c=c)
        return self

    def angle(self, v, a0, a1, r, label=None, c="thin", lr=1.5):
        """Tanda sudut di titik v; r dalam satuan sumbu-x."""
        self.arc(v[0], v[1], r, a0, a1, ry=r * self.sx / self.sy, c=c, n=24)
        if label:
            m = math.radians((a0 + a1) / 2)
            self.text((v[0] + lr * r * math.cos(m), v[1] + lr * r * math.sin(m) * self.sx / self.sy), label)
        return self

    def right_angle(self, v, a0, size):
        c, s = math.cos(math.radians(a0)), math.sin(math.radians(a0))
        k = self.sx / self.sy
        p = (v[0] + size * c, v[1] + size * s * k)
        q = (v[0] + size * (c - s), v[1] + size * (s + c) * k)
        r = (v[0] - size * s, v[1] + size * c * k)
        return self.line(p, q, r, c="thin")

    def text(self, p, s, anchor="middle", dx=0, dy=0, c=None):
        x, y = self.P(p)
        cls = f' class="{c}"' if c else ""
        self.el.append(f'<text{cls} x="{x + dx:.1f}" y="{y + dy + 4.5:.1f}" text-anchor="{anchor}">{escape(s)}</text>')
        return self

    def _head(self, tip, tail, cls="head"):
        (x, y), (a, b) = self.P(tip), self.P(tail)
        d = math.hypot(x - a, y - b) or 1
        ux, uy = (x - a) / d, (y - b) / d
        pts = [(x, y), (x - 9 * ux - 3.5 * uy, y - 9 * uy + 3.5 * ux), (x - 9 * ux + 3.5 * uy, y - 9 * uy - 3.5 * ux)]
        self.el.append(f'<polygon class="{cls}" points="' + " ".join("%.1f,%.1f" % q for q in pts) + '"/>')

    def arrow(self, p, q, c="thin"):
        self.line(p, q, c=c)
        self._head(q, p)
        return self

    def dim(self, p, q, label, off=(0, 0), at=0.5):
        """Garis ukuran dua panah; off = geser label (piksel)."""
        self.line(p, q, c="thin")
        self._head(q, p)
        self._head(p, q)
        m = (p[0] + (q[0] - p[0]) * at, p[1] + (q[1] - p[1]) * at)
        return self.text(m, label, dx=off[0], dy=off[1])

    def plot(self, f, a, b, c="a", n=160, fill=None, base=0):
        pts = [(a + (b - a) * i / n, f(a + (b - a) * i / n)) for i in range(n + 1)]
        if fill:
            self.poly((a, base), *pts, (b, base), c=None, fill=fill)
        return self.line(*pts, c=c)

    def axes(self, xa, xb, ya, yb, xl="x", yl="y", xt=(), yt=()):
        self.arrow((xa, 0), (xb, 0))
        self.arrow((0, ya), (0, yb))
        self.text((xb, 0), xl, dx=10)
        self.text((0, yb), yl, dy=-12)
        for t in xt:
            v, lab = t if isinstance(t, tuple) else (t, ribuan(t))
            x, y = self.P((v, 0))
            self.el.append(f'<line class="thin" x1="{x:.1f}" y1="{y - 3:.1f}" x2="{x:.1f}" y2="{y + 3:.1f}"/>')
            self.text((v, 0), lab, dy=14)
        for t in yt:
            v, lab = t if isinstance(t, tuple) else (t, ribuan(t))
            x, y = self.P((0, v))
            self.el.append(f'<line class="thin" x1="{x - 3:.1f}" y1="{y:.1f}" x2="{x + 3:.1f}" y2="{y:.1f}"/>')
            self.text((0, v), lab, anchor="end", dx=-6)
        return self

    # --- bentuk gabungan ---
    def cylinder(self, cx, y, r, h, ry=None, fill="f", c="s"):
        ry = r * 0.28 if ry is None else ry
        if fill:
            self.rect(cx - r, y, 2 * r, h, c=None, fill=fill)
            self.arc(cx, y, r, 180, 360, ry=ry, c=None, fill=fill)
        self.line((cx - r, y), (cx - r, y + h), c=c)
        self.line((cx + r, y), (cx + r, y + h), c=c)
        self.arc(cx, y, r, 180, 360, ry=ry, c=c)
        self.arc(cx, y, r, 0, 180, ry=ry, c="d")
        return self.ellipse(cx, y + h, r, ry, c=c)

    def cone(self, cx, base_y, r, apex_y, ry=None, fill="f"):
        """Kerucut dengan alas di base_y dan puncak di apex_y (boleh terbalik)."""
        ry = r * 0.25 if ry is None else ry
        up = apex_y > base_y
        if fill:
            self.poly((cx - r, base_y), (cx, apex_y), (cx + r, base_y), c=None, fill=fill)
        self.line((cx - r, base_y), (cx, apex_y), (cx + r, base_y))
        if up:
            self.arc(cx, base_y, r, 180, 360, ry=ry)
            self.arc(cx, base_y, r, 0, 180, ry=ry, c="d")
        else:
            self.ellipse(cx, base_y, r, ry)
        return self

    def cuboid(self, x, y, w, h, dx, dy, fill="f", open_top=False):
        """Balok miring: sisi depan (x,y,w,h), kedalaman (dx,dy)."""
        A, B, C, D = (x, y), (x + w, y), (x + w, y + h), (x, y + h)
        E, G, H, I = [(p[0] + dx, p[1] + dy) for p in (A, B, C, D)]
        if fill:
            self.poly(A, B, G, H, I, D, c=None, fill=fill)
        self.poly(A, B, C, D)
        self.line(B, G, H, C)
        self.line(D, I, H)
        self.line(A, E, G, c="d")
        self.line(E, I, c="d")
        return self

    def person(self, x, y, h):
        r = h * 0.12
        self.ellipse(x, y + h - r, r, r * self.sx / self.sy)
        self.line((x, y + h - 2 * r), (x, y + 0.42 * h))
        self.line((x - 0.16 * h, y), (x, y + 0.42 * h), (x + 0.16 * h, y))
        return self.line((x - 0.18 * h, y + 0.55 * h), (x, y + 0.7 * h), (x + 0.18 * h, y + 0.55 * h))

    def hatch(self, x0, x1, y, depth, step):
        """Permukaan tanah berarsir."""
        self.line((x0, y), (x1, y))
        x = x0 + step
        while x <= x1:
            self.line((x, y), (x - step * 0.7, y - depth), c="thin")
            x += step
        return self

    def spring(self, p, q, coils=8, amp=1.0):
        (x0, y0), (x1, y1) = p, q
        d = math.hypot(x1 - x0, y1 - y0)
        ux, uy = (x1 - x0) / d, (y1 - y0) / d
        pts = [p, (x0 + ux * d * .1, y0 + uy * d * .1)]
        n = coils * 2
        for i in range(n):
            t = .1 + .8 * (i + .5) / n
            s = amp if i % 2 == 0 else -amp
            pts.append((x0 + ux * d * t - uy * s, y0 + uy * d * t + ux * s))
        pts += [(x0 + ux * d * .9, y0 + uy * d * .9), q]
        return self.line(*pts)

    def svg(self):
        W, H = self.w + 2 * self.pad, self.h + 2 * self.pad
        cap = ""
        if self.cap:
            cap = f'<text class="cap" x="{W / 2:.0f}" y="{H + 12:.0f}" text-anchor="middle">{escape(self.cap)}</text>'
            H += 18
        return (f'<svg viewBox="0 0 {W:.0f} {H:.0f}" width="{W:.0f}" height="{H:.0f}" role="img" '
                f'aria-label="{escape(self.cap or "diagram soal")}">' + "".join(self.el) + cap + "</svg>")
