"""Bentuk yang dipakai berulang oleh beberapa buku."""
import math
from math import sqrt

from svg import F


def curve(fn, a, b, ymin, ymax, xl="x", yl="y", xt=(), yt=(), mark=None, label=None,
          extra=(), hline=None, w=320, h=210):
    """Grafik fungsi dengan sumbu; skala x dan y terpisah."""
    xs = [t[0] if isinstance(t, tuple) else t for t in xt]
    lo = min([a, 0] + xs)
    hi = max([b, 0] + xs)
    span, ys = hi - lo, ymax - ymin
    f = F(lo - .14 * span, hi + .08 * span, ymin - .1 * ys, ymax + .06 * ys, w=w, h=h)
    f.axes(lo - .03 * span, hi + .03 * span, min(ymin, 0), ymax, xl, yl, xt, yt)
    clip = lambda g: (lambda x: max(min(g(x), ymax), ymin))
    f.plot(clip(fn), a, b)
    for g, c, d, cls in extra:
        f.plot(clip(g), c, d, c=cls)
    if hline is not None:
        f.line((a, hline), (b, hline), c="d")
    if mark:
        f.line((mark[0], 0), mark, c="d").dot(mark)
    if label:
        f.text(((lo + hi) / 2, ymax), label, dy=-4)
    return f


def box_net(L, W, x, lab_l, lab_w, cap=None, lab_x="x"):
    """Lembaran persegi panjang dengan potongan persegi di sudut."""
    u = max(L, W)
    f = F(-.2 * u, L + .17 * u, -.17 * u, W + .06 * u, w=260 if L < 1.4 * W else 320, cap=cap)
    pts = [(x, 0), (L - x, 0), (L - x, x), (L, x), (L, W - x), (L - x, W - x), (L - x, W),
           (x, W), (x, W - x), (0, W - x), (0, x), (x, x)]
    f.poly(*pts, fill="g")
    f.rect(x, x, L - 2 * x, W - 2 * x, c="d")
    for cx, cy in ((0, 0), (L - x, 0), (0, W - x), (L - x, W - x)):
        f.rect(cx, cy, x, x, c="d")
    f.text((x / 2, W - x / 2), lab_x).text((L - x / 2, x / 2), lab_x)
    f.dim((0, -.08 * u), (L, -.08 * u), lab_l, off=(0, 12))
    return f.dim((-.08 * u, 0), (-.08 * u, W), lab_w, off=(-22, 0))


def cyl_dims(r="r", h="h", diameter=None, cap=None):
    f = F(-5, 6, -1.5, 10, w=170, cap=cap)
    f.cylinder(0, 0, 3.5, 7.5, ry=1)
    f.dim((4.6, 0), (4.6, 7.5), h, off=(11, 0))
    if diameter:
        f.dim((-3.5, 9.4), (3.5, 9.4), diameter, off=(0, -9))
    else:
        f.line((0, 7.5), (3.5, 7.5), c="b").text((1.7, 7.9), r, dy=-5)
    return f


def semicircle_rect(R, x, corner=None, rlab="r", wh=False):
    f = F(-1.35 * R, 1.55 * R, -.3 * R, 1.3 * R, w=300)
    y = sqrt(R * R - x * x)
    f.rect(-x, 0, 2 * x, y, fill="g")
    f.arc(0, 0, R, 0, 180, c="a")
    f.arrow((-1.25 * R, 0), (1.3 * R, 0))
    f.dot((x, y))
    if wh:
        f.text((0, y), "w", dy=-11).text((-x, y / 2), "h", dx=-11)
        f.line((0, 0), (R, 0), c="b").dot((0, 0)).text((R / 2, 0), rlab, dy=14)
    else:
        f.line((0, 0), (x, y), c="b").text((x / 2, y / 2), rlab, dx=-8, dy=-8)
        f.text((x, y), corner, anchor="start", dx=7, dy=-9)
        f.text((x, 0), "x", dy=14).text((-x, 0), "−x", dy=14).text((R, 0), f"{rlab}", dy=14)
        f.text((-R, 0), f"−{rlab}", dy=14)
    return f


def rect_under(fn, a, b, ymin, ymax, x, label, half=False, xt=None, yt=()):
    """Persegi panjang di bawah kurva (simetris, atau di kuadran I jika half)."""
    f = F(a - .08 * (b - a), b + .12 * (b - a), ymin, ymax, w=300, h=210)
    y = fn(x)
    left = 0 if half else -x
    f.rect(left, 0, x - left, y, fill="g")
    f.axes(a - .04 * (b - a), b + .06 * (b - a), ymin * .6, ymax * .95, xt=xt or [], yt=yt)
    lo = a
    while fn(lo) < (ymin * .8) and lo < b:
        lo += (b - a) / 200
    hi = b
    while fn(hi) < (ymin * .8) and hi > a:
        hi -= (b - a) / 200
    f.plot(fn, lo, hi).dot((x, y))
    f.text((x, y), "(x, y)", anchor="start", dx=7, dy=-8)
    return f.text(((a + b) / 2 + .3 * (b - a), .85 * ymax), label)


def cone_in_sphere(R, y, x):
    f = F(-4, 4, -3.8, 3.8, w=210)
    f.ellipse(0, 0, 3, fill="g")
    h, r = 1.0, sqrt(8)
    f.cone(0, -h, r, 3, ry=.55)
    f.line((0, 3), (0, -h), c="thin").line((0, 0), (r, -h), c="b").line((0, -h), (r, -h), c="b")
    f.right_angle((0, -h), 0, .22).dot((0, 0))
    return f.text((-.3, 1.5), R).text((1.6, -.05), R).text((-.45, -.5), y).text((1.2, -1.35), x)


def circle_beam(diam, d="d", w="w"):
    f = F(-6, 6, -6, 6, w=190)
    f.ellipse(0, 0, 5, fill="g")
    f.rect(-2.9, -4.07, 5.8, 8.14, fill="f")
    f.line((-2.9, -4.07), (2.9, 4.07), c="a").text((-.8, .5), diam)
    return f.text((3.5, 0), d).text((0, -3.4), w)


def sector_cone(R, ang, slant):
    f = F(0, 20, 0, 9, w=330)
    f.arc(4.2, 4.3, 3.6, -60 + 0, 240, c="a", fill="f")
    a, b = (4.2 + 3.6 * math.cos(math.radians(240)), 4.3 + 3.6 * math.sin(math.radians(240))), \
           (4.2 + 3.6 * math.cos(math.radians(-60)), 4.3 + 3.6 * math.sin(math.radians(-60)))
    f.line(a, (4.2, 4.3), b, c="b").angle((4.2, 4.3), 240, 300, 1.0, ang)
    f.text((2.7, 2.7), R).text((5.8, 2.7), R)
    f.arrow((9, 4.3), (11, 4.3))
    f.cone(15.5, 2.2, 3.6, 7, ry=1.0)
    f.line((15.5, 7), (13.4, 1.4), c="b").line((15.5, 7), (15.5, 2.2), c="d")
    return f.text((13.7, 4.4), slant)


def shore(off, x, total, start, goal):
    f = F(-1.5, 11, -1.8, 5.5, w=320)
    f.rect(-1, 1, 11.5, 4, c=None, fill="f")
    f.line((-1, 1), (10.5, 1))
    A, P, V = (1, 4.4), (5, 1), (9.3, 1)
    f.line(A, P, c="a").line(P, V, c="b").line(A, (1, 1), c="d")
    f.dot(A).dot(P).dot(V)
    f.text(A, start, anchor="start", dx=8).text(V, goal, dy=-12).text((.4, 2.7), off)
    f.dim((1, .3), (5, .3), x, off=(0, 12))
    return f.dim((1, -1), (9.3, -1), total, off=(0, 12))


def beam_wall(wall, gap, lw, lg, lbeam, lbuild):
    th = math.atan((wall / gap) ** (1 / 3))
    left = wall / math.tan(th)
    top = (left + gap) * math.tan(th)
    u = top
    f = F(-left - .1 * u, gap + .5 * u, -.2 * u, top + .1 * u, w=300)
    f.rect(gap, 0, .12 * u, top * 1.05, fill="g")
    f.line((-left - .05 * u, 0), (gap + .3 * u, 0))
    f.rect(-.03 * u, 0, .03 * u, wall, fill="g")
    f.line((-left, 0), (gap, top), c="a")
    f.angle((-left, 0), 0, math.degrees(th), .14 * u, "θ")
    f.text((.1 * u, wall / 2), lw, anchor="start").text((gap * .35, top * .72), lbeam)
    f.text((gap + .15 * u, top / 2), lbuild, anchor="start")
    return f.dim((0, -.1 * u), (gap, -.1 * u), lg, off=(0, 12))


def two_lights(x, rest, I1, I2):
    f = F(0, 14, 0, 5, w=300)
    f.line((1, 2), (13, 2))
    for X, lab in ((1, I1), (13, I2)):
        f.ellipse(X, 3, .55, fill="g").line((X, 2), (X, 2.45)).text((X, 4.2), lab)
    f.dot((9, 2)).text((9, 2.7), "titik P")
    return f.dim((1, 1.2), (9, 1.2), x, off=(0, 12)).dim((9, 1.2), (13, 1.2), rest, off=(0, 12))
