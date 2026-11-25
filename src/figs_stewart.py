import math
from math import sin, cos, sqrt, pi

from svg import F, fig, register
from shapes import (curve, box_net, cyl_dims, semicircle_rect, sector_cone, beam_wall, two_lights)


@fig
def s_c1a():
    f = F(0, 36, 0, 14, w=360, cap="tiga cara menata 1200 m pagar")
    f.rect(0, 0, 36, 2.4, c=None, fill="f")
    for x0, w, d, lab, a in ((0.5, 10, 1.6, "100 | 1000", "100 000 m²"), (15, 5.5, 5.5, "400 | 400", "160 000 m²"),
                             (28, 3, 8, "500 | 200", "100 000 m²")):
        f.line((x0, 2.4), (x0, 2.4 + d), (x0 + w, 2.4 + d), (x0 + w, 2.4), c="b")
        f.text((x0 + w / 2, 3.4 + d), lab).text((x0 + w / 2, 1.2), a)
    return f


@fig
def s_c1b():
    f = F(0, 10, 0, 6.5, w=220, cap="kasus umum")
    f.rect(0.3, 0.2, 9.4, 1.4, c=None, fill="f").text((5, .9), "sungai")
    f.rect(2, 1.6, 6, 3.5, c=None, fill="g").line((2, 1.6), (2, 5.1), (8, 5.1), (8, 1.6), c="b")
    return f.text((1.5, 3.3), "x").text((8.5, 3.3), "x").text((5, 5.7), "y").text((5, 3.3), "A")


@fig
def s_c2():
    return cyl_dims("r", "h", diameter="2r")


@fig
def s_c3():
    f = F(-1.5, 7, -4, 5, w=260)
    f.axes(-1.2, 6.3, -3.6, 4.6, xt=[1, 2, 3, 4], yt=[1])
    ys = [-3.5 + 7 * i / 100 for i in range(101)]
    f.line(*[(y * y / 2, y) for y in ys], c="b")
    f.dot((1, 4)).dot((2, 2)).line((1, 4), (2, 2), c="a")
    return f.text((1, 4), "(1, 4)", anchor="start", dx=7).text((2, 2), "(x, y)", anchor="start", dx=7, dy=6).text((5.2, 3.6), "y² = 2x")


@fig
def s_c4():
    f = F(-2, 7, -1, 10, w=200)
    f.rect(0, -0.3, 3, 9.6, c=None, fill="f")
    f.line((0, -.3), (0, 9.3)).line((3, -.3), (3, 9.3))
    A, C, D, B = (0, 8.5), (3, 8.5), (3, 5.1), (3, .5)
    f.arrow(A, C, c="thin").line(A, D, B, c="b").line(A, B, c="d")
    for p in (A, C, D, B):
        f.dot(p)
    f.text(A, "A", dx=-12).text(C, "C", dx=12).text(D, "D", dx=12).text(B, "B", dx=12)
    f.text((1.5, 9.2), "3 km").text((3.6, 6.8), "x")
    return f.dim((5.2, .5), (5.2, 8.5), "8 km", off=(24, 0))


@fig
def s_c5a():
    return semicircle_rect(3, 2.12, "(x, y)", "r")


@fig
def s_c5b():
    f = F(-3.8, 4.8, -1, 3.8, w=260)
    f.rect(-2.12, 0, 4.24, 2.12, fill="g").arc(0, 0, 3, 0, 180, c="a").line((-3.3, 0), (3.3, 0))
    f.line((0, 0), (2.12, 2.12), c="b").angle((0, 0), 0, 45, .7, "θ")
    return f.text((1, 1.4), "r").text((3.3, 1.1), "r sin θ").text((1.2, -.45), "r cos θ")


@fig
def s_p11():
    f = F(0, 12, 0, 7, w=240)
    f.rect(1, 1, 10, 5, fill="g")
    for X in (3.5, 6, 8.5):
        f.line((X, 1), (X, 6), c="b")
    return f.text((.5, 3.5), "x").text((6, 6.5), "y")


@fig
def s_p12():
    return box_net(3, 3, .5, "3 m", "3 m")


@fig
def s_p14():
    f = F(0, 12, 0, 8, w=260)
    f.poly((2, 6.8), (9, 3), (9, 5.2), (12, 3.6), c=None)
    f.poly((2, 1.5), (9, 1.5), (9, 3.4), (2, 7.2), c=None, fill="g")
    f.line((0.5, 8), (11.5, 2), c="a").line((2, 7.2), (2, 1.5), (9, 1.5), (9, 3.4), c="b")
    f.right_angle((2, 1.5), 0, .35).right_angle((9, 1.5), 90, .35)
    return f.text((1.3, 4.2), "3x").text((9.6, 2.4), "x").text((5.5, 1), "400 − 4x").text((7.5, 5.6), "sungai")


@fig
def s_p15():
    f = F(0, 11, 0, 7.5, w=240)
    f.rect(2, 5, 7, 1.8, fill="f").text((5.5, 5.9), "lumbung")
    f.rect(2.5, 1, 6, 4, c=None, fill="g").line((8.5, 5), (8.5, 1), (2.5, 1), c="b").line((2.5, 1), (2.5, 5), c="ad")
    return f.text((5.5, .5), "L").text((9.1, 3), "W").text((1.2, 3), "W (½)").text((10.3, 6), "utara ↑")


@fig
def s_p20():
    f = F(-.3, 2.35, -.25, 1.15, w=300)
    x = .13
    f.rect(0, 0, 2, 1, fill="f")
    for X in (x, 2 - x):
        f.line((X, 0), (X, 1), c="d")
    for Y in (x, 1 - 2 * x, 1 - x):
        f.line((0, Y), (2, Y), c="d")
    for cx in (0, 2 - x):
        f.rect(cx, 0, x, x, c="d").rect(cx, 1 - 2 * x, x, 2 * x, c="d")
    f.text((2.08, x / 2), "x").text((2.1, 1 - x), "2x").text((x / 2 + .0, 1.08), "x")
    return f.dim((0, -.13), (2, -.13), "2 m", off=(0, 12)).dim((-.12, 0), (-.12, 1), "1 m", off=(-18, 0))


@fig
def s_p23():
    f = F(0, 16, 0, 9, w=320)
    f.cuboid(1, 1, 3, 6, 1.2, .9).line((1, 4), (4, 4), (5.2, 4.9), c="b").line((1, 4), (2.2, 4.9), (5.2, 4.9), c="ad")
    f.text((.4, 6), "L").text((6.4, 3), "lingkar").text((2.5, .5), "x")
    f.line((9, 1.4), (13.2, 7.4)).line((10.2, .6), (14.4, 6.6)).ellipse(13.8, 7, .75, .55, fill="g")
    return f.arc(11.7, 4, .75, 180, 360, ry=.45, c="b").text((10.2, 5.4), "L").text((13.8, 2.8), "lingkar")


@fig
def s_p31():
    f = F(-1, 11, -1.2, 9.5, w=220)
    f.poly((0, 0), (10, 0), (5, 8.66), fill="f").rect(2.5, 0, 5, 4.33, c="b", fill="g")
    return f.text((5, -.7), "w").text((7, 2.2), "h").text((1.7, 4.6), "L")


@fig
def s_p32():
    f = F(-3.8, 3.8, -.8, 3.6, w=250)
    f.poly((-3, 0), (3, 0), (1.5, 2.6), (-1.5, 2.6), c="b", fill="g").arc(0, 0, 3, 0, 180, c="a")
    f.line((0, 0), (1.5, 2.6), c="d").angle((0, 0), 0, 60, .6, "t")
    return f.text((.4, 1.5), "1").text((0, -.45), "diameter = 2")


@fig
def s_p37():
    f = F(-4, 4, -3.6, 3.6, w=200)
    f.ellipse(0, 0, 3, fill="g").cylinder(0, -1.73, 2.45, 3.46, ry=.45)
    f.line((0, 0), (2.45, 1.73), c="b").line((0, 0), (0, 1.73), c="d").dot((0, 0))
    return f.text((1.5, .6), "r").text((-.35, .85), "y")


@fig
def s_p38():
    f = F(-5, 5, -1.8, 8, w=210)
    f.cone(0, 0, 4, 7, ry=.9).cylinder(0, 0, 2.67, 2.33, ry=.55)
    f.dim((-4.6, 0), (-4.6, 7), "h", off=(-10, 0))
    return f.line((0, 0), (4, 0), c="b").text((3.3, -.4), "r").text((1.3, 2.9), "x")


@fig
def s_p40():
    f = F(-5, 5, -1, 10.5, w=170)
    f.rect(-3.2, 0, 6.4, 5.6, fill="f").arc(0, 5.6, 3.2, 0, 180, fill="g")
    for a in (45, 90, 135):
        f.line((0, 5.6), (3.2 * cos(math.radians(a)), 5.6 + 3.2 * sin(math.radians(a))), c="thin")
    for X in (-1.07, 1.07):
        f.line((X, 0), (X, 5.6), c="thin")
    return f.text((3.8, 2.8), "h").text((0, -.6), "2r")


@fig
def s_p41():
    f = F(0, 10, 0, 12, w=180)
    f.rect(1.5, .5, 7, 11, fill="f").rect(3, 3, 4, 6, fill="g").text((5, 6), "384 cm²")
    f.dim((5, 9), (5, 11.5), "6", off=(10, 0)).dim((5, .5), (5, 3), "6", off=(10, 0))
    return f.dim((1.5, 6.8), (3, 6.8), "4", off=(0, -10)).dim((7, 6.8), (8.5, 6.8), "4", off=(0, -10))


@fig
def s_p46():
    return beam_wall(2, 1, "2 m", "1 m", "tangga", "gedung")


@fig
def s_p47():
    f = F(0, 18, 0, 9, w=300)
    c = (4.2, 4.3)
    a, b = [(c[0] + 3.6 * cos(math.radians(t)), c[1] + 3.6 * sin(math.radians(t))) for t in (120, 60)]
    f.arc(c[0], c[1], 3.6, 120, 420, c="a", fill="f").line(a, c, b, c="b")
    f.text(a, "A", dy=-10).text(b, "B", dy=-10).text(c, "C", dy=14).text((5.9, 5.6), "R")
    return f.arrow((8.8, 4.3), (11, 4.3)).cone(14.4, 7, 2.8, 1.2, ry=.7)


@fig
def s_p49():
    f = F(-5, 5, -1.5, 8.5, w=210)
    f.cone(0, 0, 4, 7.5, ry=.9).cone(0, 2.5, 2.67, 0, ry=.55, fill="g")
    f.dim((-4.6, 0), (-4.6, 7.5), "H", off=(-10, 0))
    return f.dim((3.2, 0), (3.2, 2.5), "h", off=(10, 0))


@fig
def s_p50():
    f = F(0, 10, 0, 5, w=230)
    f.hatch(.5, 9.5, 1, .35, .5).rect(2, 1, 3, 1.6, fill="f")
    f.arrow((4.2, 1.8), (8.2, 4), c="b").line((4.2, 1.8), (8, 1.8), c="d").angle((4.2, 1.8), 0, 29, 1.6, "θ")
    return f.text((8.6, 4.3), "F").text((3, 1.8), "W")


@fig
def s_p56():
    f = F(-4.5, 4.5, -4, 4, w=220)
    f.ellipse(0, 0, 3.3, fill="f")
    A, B, C = (-3.3, 0), (3.3 * cos(pi / 3), 3.3 * sin(pi / 3)), (3.3, 0)
    f.line(A, C, c="thin").arrow(A, B, c="b").arc(0, 0, 3.3, 0, 60, c="b").angle(A, 0, 30, .9, "θ")
    for p in (A, B, C, (0, 0)):
        f.dot(p)
    return f.text(A, "A", dx=-10).text(B, "B", dx=10, dy=-6).text(C, "C", dx=10).text((-1.6, -.4), "3").text((1.6, -.4), "3")


def refinery(north):
    f = F(-1.5, 12, -2.2, 5, w=320)
    f.rect(-1, 0, 12.5, 2, c=None, fill="f").line((-1, 0), (11.5, 0)).line((-1, 2), (11.5, 2))
    P, T = (7, 2), (9.6, 0)
    start = (.8, 3.6) if north else (.8, 2)
    f.line(start, P, c="a").line(P, T, c="b")
    for p in (start, P, T):
        f.dot(p)
    f.text(start, "kilang", dy=-12).text(P, "P", dy=-12).text(T, "tangki", dy=14)
    if north:
        f.line(start, (.8, 2), c="d").text((.2, 2.8), "1")
    f.dim((10.9, 0), (10.9, 2), "2 km", off=(24, 0)).dim((.8, -1.4), (9.6, -1.4), "6 km", off=(0, 12))
    return f.text((3.8, 1.5), "x", dy=-2)


register("s_p57", lambda: refinery(False))
register("s_p58", lambda: refinery(True))
register("s_p59", lambda: two_lights("x", "4 − x", "3I", "I"))


@fig
def s_p74():
    f = F(0, 12, 0, 8, w=240)
    L, T, R, Bt = (1, 4), (4, 7), (11, 4), (4, 1)
    f.poly(L, T, R, Bt, fill="f").line(L, R, c="b").line(T, Bt, c="b")
    return f.text((2, 5.9), "a").text((2, 2.1), "a").text((7.9, 5.9), "b").text((7.9, 2.1), "b")


@fig
def s_p75():
    f = F(-3.5, 5.5, -1, 6, w=240)
    A, P, B, C, D = (0, 5), (0, 1.4), (-2, 0), (3, 0), (0, 0)
    f.line(A, P, c="b").line(B, P, C, c="b").line(P, D, c="d").line(B, C, c="d").right_angle(D, 0, .25)
    for p in (A, P, B, C):
        f.dot(p)
    f.text(A, "A", dx=10).text(P, "P", dx=10, dy=-6).text(B, "B", dy=14).text(C, "C", dy=14).text(D, "D", dy=14)
    f.text((-1, -.4), "2 m").text((1.5, -.4), "3 m").text((-.4, 3.2), "x")
    return f.dim((4.4, 0), (4.4, 5), "5 m", off=(18, 0))


@fig
def s_p76():
    f = F(-18, 150, -1.2, 6, w=300, h=200)
    f.axes(-5, 140, -.3, 5.4, "v", "c", xt=[40, 80, 120])
    c = lambda v: 1.6 + (v - 55) ** 2 / 2625
    f.plot(c, 0, 125, c="b").line((0, 0), (125, 125 * c(85) / 85), c="ad").dot((85, c(85)))
    return f.line((85, 0), (85, c(85)), c="d").text((95, 1.7), "≈ 85")


@fig
def s_p77():
    f = F(0, 12, -4.5, 4.5, w=270)
    f.rect(.3, -4, 11.4, 4, c=None, fill="f").line((.3, 0), (11.7, 0))
    A, C, B = (1.5, 3.4), (7, 0), (10, -3.5)
    f.line(A, C, B, c="b").line(A, (1.5, 0), c="thin").line(B, (10, 0), c="thin")
    for p in (A, C, B):
        f.dot(p)
    f.text(A, "A", dx=-10).text(C, "C", dy=-12).text(B, "B", dx=10)
    return f.text((2.3, 2.1), "θ₁").text((9.4, -2), "θ₂")


@fig
def s_p78():
    f = F(0, 12, -1, 7, w=260)
    f.hatch(.5, 11.5, 0, .3, .55)
    P, Q, R, S, T = (2, 5.8), (2, 0), (7, 0), (10, 3.5), (10, 0)
    f.line(P, Q).line(S, T).line(P, R, S, c="b").angle(R, 131, 180, 1.0, "θ₁").angle(R, 0, 49, 1.0, "θ₂")
    for p, lab, dy in ((P, "P", -12), (Q, "Q", 16), (R, "R", 16), (S, "S", -12), (T, "T", 16)):
        f.text(p, lab, dy=dy)
    return f


@fig
def s_p79():
    f = F(-3, 36, -3, 23, w=300)
    f.rect(0, 0, 30, 20)
    T, R, U, Q = (30, 20), (30, 5), (8.8, 20), (15.9, 0)
    f.poly(U, Q, R, c="b", fill="g").line(U, T, R, c="d")
    f.text((21, 13.6), "y").text((32, 12), "x").text((19.5, 21.3), "a")
    return f.dim((0, -1.8), (30, -1.8), "30", off=(0, 12)).dim((-1.8, 0), (-1.8, 20), "20", off=(-12, 0))


@fig
def s_p80():
    f = F(-1, 9, -1, 7, w=240)
    f.line((0, 0), (0, 5.5), (8.5, 5.5), c="a").line((3, 0), (3, 3.5), (8.5, 3.5), c="a")
    f.line((0, 1.9), (6.4, 5.5), c="b").dot((3, 3.5)).angle((0, 1.9), 29, 90, .8, "θ")
    return f.dim((0, .5), (3, .5), "3", off=(0, -10)).dim((7.8, 3.5), (7.8, 5.5), "2", off=(10, 0))


@fig
def s_p81():
    f = F(-1, 9, -1, 6, w=240)
    f.line((-.5, 0), (8.5, 0), c="a").line((-.5, .5), (8.5, .5), c="thin")
    P, S, a, b = (1, 5), (1, 0), (3, 0), (7, 0)
    f.line(P, S, c="thin").line(a, P, b, c="b").right_angle(S, 90, .25).angle(P, -68, -40, 1.2, "θ")
    for p in (P, S, a, b):
        f.dot(p)
    return f.text(P, "P", dy=-12).text(S, "S", dy=14).text((.5, 2.6), "1").text(a, "pelari 1", dy=14).text(b, "pelari 2", dy=14)


@fig
def s_p82():
    f = F(-1, 31, -4, 12, w=300)
    f.poly((10, 0), (20, 0), (25, 8.66), (5, 8.66), c=None, fill="f")
    f.line((5, 8.66), (10, 0), (20, 0), (25, 8.66), c="b").line((0, 0), (10, 0), c="d").line((20, 0), (30, 0), c="d")
    f.angle((10, 0), 120, 180, 2.2, "θ").angle((20, 0), 0, 60, 2.2, "θ")
    for a in (0, 10, 20):
        f.dim((a, -2), (a + 10, -2), "10 cm", off=(0, 12))
    return f


@fig
def s_p83():
    f = F(-1.2, 5.8, -.8, 3.8, w=270)
    A, B, P = (0, 0), (0, 3), (0, 2)
    f.line(A, B, c="a").line(B, (2, 3), P, (5, 0), A, c="a").angle(P, -22, 27, .45, "θ")
    for p in (A, B, P):
        f.dot(p)
    f.text(A, "A", dy=14).text(B, "B", dy=-12).text(P, "P", dx=-12).text((1, 3.3), "2").text((2.5, -.35), "5")
    return f.dim((-.65, 0), (-.65, 3), "3", off=(-10, 0))


@fig
def s_p84():
    f = F(-1, 12, -1, 6, w=300)
    E, lo, hi = (0, 0), (9, 1.4), (9, 4.8)
    f.line(E, (9, 0), c="d").line((9, -.3), (9, 5.4)).line(E, lo, c="b").line(E, hi, c="b")
    f.line((9, 1.4), (9, 4.8), c="a").angle(E, 9, 28, 2.4, "θ").dot(E)
    f.text(E, "mata", dy=14).text((10, 3.1), "h").text((10, .7), "d")
    return f.text((4.5, -.5), "x")


@fig
def s_p85():
    f = F(-2.5, 8, -3, 5.5, w=260)
    t = math.radians(25)
    L, W = 5, 2.5
    f.rect(0, 0, L, W, c="a", fill="f")
    a, b = cos(t), sin(t)
    p1 = (L * a * a, -L * a * b)
    p2 = (L + W * a * b, W * b * b)
    p3 = (L - L * a * a, W + L * a * b)
    p4 = (-W * a * b, W - W * b * b)
    f.poly(p1, p2, p3, p4, c="b").angle((0, 0), -25, 0, 1.3, "θ")
    return f.text((L / 2, W - .45), "L").text((.4, W / 2), "W")


@fig
def s_p88():
    f = F(-.5, 12.5, -1.5, 5, w=310)
    f.line((0, 3.6), (11.5, 3.6), c="a").text((12, 3.6), "ℓ")
    f.dot((4, 3.6)).text((4, 4.3), "P")
    for X in (1, 11):
        f.ellipse(X, .2, .45, fill="g")
    f.line((1, .2), (11, .2), c="d")
    f.dim((1, 2.9), (4, 2.9), "x", off=(0, 12)).dim((7, .2), (7, 3.6), "d", off=(10, 0))
    return f.dim((1, -.8), (11, -.8), "10 m", off=(0, 12))


@fig
def s_can1():
    f = F(0, 10, 0, 10, w=170, cap="cakram dari persegi")
    for i in range(3):
        for j in range(3):
            f.rect(.5 + 3 * i, .5 + 3 * j, 3, 3, c="thin").ellipse(2 + 3 * i, 2 + 3 * j, 1.5, c="thin", fill="g")
    return f


@fig
def s_can2():
    f = F(-1, 15, -1.5, 9.5, w=250, cap="cakram dari heksagon")
    r = 1.5
    R = 2 * r / sqrt(3)
    for row in range(3):
        for i in range(4):
            cx, cy = 1.2 + 2 * r * i + (r if row % 2 else 0), 1 + 1.5 * R * row
            f.poly(*[(cx + R * cos(math.radians(30 + 60 * k)), cy + R * sin(math.radians(30 + 60 * k)))
                     for k in range(6)], c="thin")
            f.ellipse(cx, cy, r, c="thin", fill="g")
    return f


register("s_can4", lambda: curve(lambda x: (pi * x) ** (1 / 3) * (2 * pi - x) / (pi * x - 4 * sqrt(3)),
                                 2.35, 2 * pi, 0, 14, "h/r", "∛V / k",
                                 xt=[(4 * sqrt(3) / pi, "2,21"), (2 * pi, "2π")], yt=[5, 10]))
