import math
from math import sin, cos, sqrt, pi

from svg import F, fig, register
from shapes import (curve, cyl_dims, circle_beam, sector_cone, beam_wall)

register("t_c20", lambda: curve(lambda x: (x ** 3 - 2 * x * x + x + 20) / (x * x + 5), 0, 6, 0, 4.6, "x", "y",
                                xt=[(2.72, "2,72"), 6], yt=[(2.262, "2,262"), 4], mark=(2.7188, 2.262)))
for _n, _a in (("t_c21a", 5), ("t_c21b", 1)):
    register(_n, lambda a=_a: curve(lambda x: (2 * x * x + 3 * x) / (x * x + 4), a, 30, 0, 2.8, "x", "y",
                                    xt=[a, 30], yt=[1, 2], mark=(6, 2.25), hline=2, w=260))


def river_field(side, top):
    f = F(0, 10, 0, 6.2, w=240)
    f.rect(.3, .2, 9.4, 1.5, c=None, fill="f").text((5, .9), "tepi sungai")
    f.rect(2, 1.7, 6, 3.3, c=None, fill="g").line((2, 1.7), (2, 5), (8, 5), (8, 1.7), c="b")
    return f.text((1.5, 3.4), side).text((8.5, 3.4), side).text((5, 5.6), top)


register("t_c22", lambda: river_field("w", "l"))
register("t_c23a", lambda: cyl_dims("r", "h", diameter="2r"))


@fig
def t_c23b():
    f = F(0, 20, 0, 9, w=300)
    f.ellipse(2.6, 4, 2.2, fill="g").ellipse(7.4, 4, 2.2, fill="g")
    for X in (2.6, 7.4):
        f.dot((X, 4)).line((X, 4), (X + 2.2, 4), c="thin").text((X + 1.1, 4.5), "r")
    f.rect(10.5, 1.2, 8, 5.6, fill="f").dim((10.5, 7.8), (18.5, 7.8), "2πr", off=(0, -9))
    f.dim((19.5, 1.2), (19.5, 6.8), "h", off=(10, 0))
    return f.text((2.6, 7), "tutup").text((7.4, 7), "alas").text((14.5, 4), "selimut")


@fig
def t_c24():
    f = F(-5, 5, -5.6, 4.6, w=210)
    f.ellipse(0, 0, 4)
    a0, a1 = 218, 322
    f.arc(0, 0, 4, a0, a1, c="a", fill="f")
    p, q = [(4 * cos(math.radians(a)), 4 * sin(math.radians(a))) for a in (a0, a1)]
    f.line(p, (0, 0), q, c="thin").line(p, q, c="a").angle((0, 0), a0, a1, .8, "θ")
    return f.text((-2.1, -.9), "R").text((2.1, -.9), "R").text((0, -4.9), "keliling basah")


@fig
def t_c25():
    f = F(-1.5, 11, -1.8, 7.5, w=310)
    f.rect(-1, 1, 11.5, 6, c=None, fill="f").line((-1, 1), (10.5, 1))
    A, P, C = (1, 6), (5.5, 1), (9, 1)
    f.line(A, P, c="a").line(P, C, c="b").line(A, (1, 1), c="d")
    for p in (A, P, C):
        f.dot(p)
    f.text(A, "mercusuar", anchor="start", dx=8).text(C, "pondok", dy=-12).text((.4, 3.5), "6")
    f.dim((1, .3), (5.5, .3), "x", off=(0, 12))
    return f.dim((1, -1), (9, -1), "9", off=(0, 12))


register("t_c26a", lambda: circle_beam("", "d", "w"))


@fig
def t_c26b():
    f = F(-6, 6, -6, 6, w=190)
    f.ellipse(0, 0, 5, fill="g").rect(-3.6, -3.47, 7.2, 6.94, fill="f")
    f.line((0, 0), (3.6, 3.47), (0, 3.47), (0, 0), c="b").right_angle((0, 3.47), -90, .45).dot((0, 0))
    return f.text((2.3, 1.2), "R").text((-1, 1.7), "d/2").text((1.8, 4.2), "w/2")


@fig
def t_c27():
    th = 0.9314
    x = 2 + 5 / math.tan(th)
    top = x * math.tan(th)
    f = F(-2.2, x + 2, -1.4, top + 2, w=270)
    f.line((0, 0), (x + 1.4, 0)).line((0, 0), (0, top + 1.5))
    n = (.55 * sin(th), .55 * cos(th))
    E, Fp = (x, 0), (0, top)
    C, G = (x + n[0], n[1]), (n[0], top + n[1])
    f.poly(E, C, G, Fp, fill="f")
    f.rect(1.8, 0, .2, 5, fill="g").angle(E, 180 - math.degrees(th), 180, 1.3, "θ")
    f.text((-1.2, top * .45), "gedung").text((2.9, 2.2), "tembok").text((x * .62, top * .55), "balok")
    f.text((1.2, 2.6), "5").dim((0, -.7), (2, -.7), "2", off=(0, 12))
    f.text(E, "E", dy=14).text(Fp, "F", dx=-10)
    return f.text((x + 1.4, 0), "x", dx=8)


@fig
def t_c28():
    f = F(-3.5, 13, -3.5, 4, w=320)
    A, e = (0, 1), 1
    B = (2.0 * cos(.75), 1 + 2.0 * sin(.75))
    C = (B[0] + sqrt(81 - B[1] ** 2), 0)
    f.ellipse(0, 1, 2, c="d").line((-3, 0), (12.5, 0), c="thin")
    f.line(A, B, C, c="a").line(A, (0, 0), c="d").rect(C[0] - .5, -.35, 1, .7, fill="g")
    for p in (A, B):
        f.dot(p)
    return (f.text(A, "A", dx=-11).text(B, "B", dy=-11).text(C, "C", dy=-14).text((.45, .5), "e")
            .text((.6, 2.1), "r").text((5.5, 1.6), "L"))


def soil(sym):
    f = F(-1.5, 13, -1.6, 6.5, w=310)
    f.rect(0, 0, 12, 5, c=None, fill="f").rect(0, -1.2, 12, 1.2, c=None, fill="g")
    f.line((0, 5), (12, 5), c="a").line((0, 0), (12, 0), c="a")
    A, C, E, B = (1, 5), (3, 0), (9, 0) if sym else (6, 0), (11, 5)
    f.line(A, C, E, B, c="b")
    for p in (A, C, E, B):
        f.dot(p)
    f.angle(A, -68, 0, .9, "θ").angle(B, 180, 248 if sym else 225, .9, "θ" if sym else "φ")
    f.dim((-.6, 0), (-.6, 5), "D", off=(-10, 0)).dim((1, 6), (11, 6), "s", off=(0, -9))
    return (f.text(A, "A", dx=-11).text(B, "B", dx=11).text(C, "C", dy=14).text(E, "E", dy=14)
            .text((6, 2.6), "tanah (v₁)").text((6, -.7), "batuan (v₂)"))


register("t_l5a", lambda: soil(False))
register("t_l5b", lambda: soil(True))


@fig
def t_l5c():
    f = F(-1, 11, -.8, 6, w=260, cap="garis terbaik: kemiringan m, intersep b")
    f.axes(-.5, 10.2, -.4, 5.4, "s", "t̄")
    f.line((0, 1.2), (9.5, 5), c="d")
    for s, d in ((1, .08), (2.5, -.1), (4, .12), (5.5, -.08), (7, -.15), (8.5, .12)):
        f.dot((s, 1.2 + .4 * s + d))
    return f.text((-.35, 1.2), "b")


@fig
def t_p11():
    f = F(-1.5, 11, -2.5, 3, w=290)
    f.line((0, -1.3), (0, 1.8))
    for k in range(7):
        f.line((0, -1.2 + .45 * k), (-.5, -1.6 + .45 * k), c="thin")
    f.line((0, 0), (10, 0), c="d")
    f.plot(lambda x: -(2 * (x / 10) ** 4 - 5 * (x / 10) ** 3 + 3 * (x / 10) ** 2) * 6.5, 0, 10)
    f.poly((10, 0), (9.5, -.7), (10.5, -.7), fill="g")
    return f.dim((0, 1.2), (10, 1.2), "L", off=(0, -9)).text((10.7, .4), "x")


@fig
def t_p12():
    f = F(0, 18, 0, 8, w=260)
    f.rect(1, 1, 16, 6, fill="g")
    for k in range(1, 8):
        f.line((1 + 2 * k, 1), (1 + 2 * k, 7), c="b")
    return f.text((2, .4), "x").text((.4, 4), "y")


@fig
def t_p16():
    f = F(-6.5, 22, -2.5, 9, w=320)
    f.rect(0, 0, 15, 6, c="d").rect(2, 0, 11, 6, c="s", fill="g")
    f.line((0, 0), (15, 0), c="a").line((0, 6), (15, 6), c="a")
    f.arc(15, 3, 3, -90, 90, c="a").arc(0, 3, 3, 90, 270, c="a")
    f.text((7.5, 3), "area permainan").text((1, 3), "10").text((14, 3), "10")
    return f.dim((2, 7), (13, 7), "l", off=(0, -9)).dim((20.3, 0), (20.3, 6), "w", off=(10, 0))


@fig
def t_p20():
    f = F(-6, 6, -1.5, 11, w=190)
    A, B, C, D, P = (0, 10), (-5, 0), (5, 0), (0, 0), (0, 2.9)
    f.poly(A, B, C, fill="f").line(A, D, c="d").line(A, P, c="b").line(B, P, C, c="b")
    for p in (A, B, C, D, P):
        f.dot(p)
    return (f.text(A, "A", dy=-12).text(B, "B", dy=14).text(C, "C", dy=14).text(D, "D", dy=14)
            .text(P, "P", dx=11, dy=-6).text((-.6, 1.4), "y"))


@fig
def t_p25():
    f = F(-5, 6, -2, 8.5, w=190)
    f.ellipse(0, 0, 4, 1.1, fill="f")
    S, O, E = (0, 7), (0, 0), (4, 0)
    f.line(S, O, E, S).dot(S).angle(S, -90, -60, 1.5, "θ")
    return f.text(S, "sumber", anchor="start", dx=8).text((-.5, 3.4), "h").text((2.5, 3.8), "d").text((2, .45), "r")


@fig
def t_p27():
    f = F(-.35, 2.35, -.35, 1.1, w=290)
    A, B, C, D = (.3, .7), (.8, 0), (1.5, 0), (2.0, .7)
    f.poly(A, B, C, D, c=None, fill="f").line(A, B, C, D, c="a")
    f.line((0, 0), B, c="d").line(C, (2.3, 0), c="d")
    f.angle(B, 126, 180, .2, "θ").angle(C, 0, 54, .2, "θ")
    return f.text(A, "A", dy=-12).text(D, "D", dy=-12).text(B, "B", dy=14).text(C, "C", dy=14)


@fig
def t_p39():
    f = F(-6, 7.5, -6, 6, w=210)
    f.ellipse(0, 0, 5, fill="f").rect(-2.89, -4.08, 5.77, 8.16, c="s")
    X = 4.0
    f.rect(2.89, -3.0, X - 2.89, 6.0, c="b", fill="g").rect(-X, -3.0, X - 2.89, 6.0, c="b", fill="g")
    return f.text((0, 0), "balok utama").text((6.2, 1), "balok sisa")


@fig
def t_p40():
    f = F(-1.5, 12, -1, 5, w=300)
    f.axes(-.5, 11.3, -.4, 4.4)
    f.plot(lambda x: 1.2 + .9 * x - .1 * x * x, 0, 10.2)
    f.arrow((0, 1.2), (1.6, 2.65), c="b").line((0, 1.2), (2, 1.2), c="d").angle((0, 1.2), 0, 42, .8, "θ")
    f.dim((-.8, 0), (-.8, 1.2), "h", off=(-9, 0))
    return f.dim((0, -.65), (10.2, -.65), "R", off=(0, 12))


def corridor(a, b, wide):
    f = F(-1.5, 12, -1.5, 9.5, w=250)
    f.line((0, 0), (0, 8), (11, 8), c="a").line((a, 0), (a, b), (11, b), c="a")
    P, Q = (0, 1.6), (9.4, 8)
    if wide:
        f.poly((0, 1.6), (9.4, 8), (9.75, 7.5), (.35, 1.1), c="b", fill="g")
    else:
        f.line(P, Q, c="b")
    f.angle(P, 34, 90, 1.2, "θ")
    return f.dim((0, .5), (a, .5), "3 m", off=(0, -10)).dim((10.3, b), (10.3, 8), "6 m", off=(24, 0))


register("t_p41", lambda: corridor(3, 3, False))
register("t_p42", lambda: corridor(3.6, 3.4, True))


@fig
def t_win():
    f = F(-5, 5.5, -1, 10.5, w=170)
    f.rect(-3.5, 0, 7, 5.5, fill="f").arc(0, 5.5, 3.5, 0, 180, c="b", fill="g")
    f.line((0, 5.5), (3.5, 5.5), c="thin").text((1.7, 6), "r")
    return f.text((4.2, 2.7), "h").text((0, -.6), "2r")


@fig
def t_p50():
    f = F(-1.5, 12, -5, 5.5, w=300)
    f.rect(0, 0, 11, 4.6, c=None, fill="f").rect(0, -4.4, 11, 4.4, c=None, fill="g")
    f.arrow((-.3, 0), (11.4, 0)).arrow((0, -.5), (0, 5))
    A, P, B = (0, 3.8), (7, 0), (10, -3.4)
    f.line(A, P, B, c="b").line((7, 3.4), (7, -3.8), c="d")
    for p in (A, P, B):
        f.dot(p)
    f.angle(P, 90, 151, 1.1, "θ₁").angle(P, 270, 311, 1.3, "θ₂")
    return (f.text(A, "A(0, y₁)", anchor="start", dx=8, dy=-6).text(P, "(x, 0)", anchor="start", dx=8, dy=-10)
            .text(B, "B(x₂, y₂)", dy=14).text((9.8, 2.5), "I (c₁)").text((2, -2.6), "II (c₂)"))


@fig
def t_p52a():
    f = F(-2.5, 21, -2.5, 12.5, w=300, cap="(a) pola potong dan lipat")
    f.rect(0, 0, 20, 10, fill="f")
    for X in (6.7, 10, 16.7):
        f.line((X, 0), (X, 10), c="s")
    for Y in (1.7, 8.3):
        f.line((0, Y), (20, Y), c="d")
    for X, s in ((3.3, "l"), (8.3, "w"), (13.3, "l"), (18.3, "w")):
        f.text((X, 2.7), s)
    f.text((3, 5), "A    h").text((18.3, 5), "B")
    return f.dim((0, 11.4), (20, 11.4), "2", off=(0, -9)).dim((-1.3, 0), (-1.3, 10), "1", off=(-9, 0))


@fig
def t_p52b():
    f = F(0, 10, 0, 8, w=200, cap="(b) kotak jadi")
    f.cuboid(3.2, 1.2, 5, 3.8, -2.2, 1.7)
    return f.text((5.7, .6), "l").text((1.6, 1.8), "w").text((8.8, 3), "h")


register("t_p54", lambda: sector_cone("R", "θ", "R"))


@fig
def t_p55():
    f = F(-1, 13, -1.2, 8, w=300)
    f.line((0, 0), (12, 0)).line((10, 0), (10, 7), c="s")
    E, lo, hi = (1, 1.5), (10, 5), (10, 6.6)
    f.line(E, lo, c="b").line(E, hi, c="b").line(lo, hi, c="a").line(E, (10, 1.5), c="d")
    f.angle(E, 21, 30, 3.0, "θ").dot(E)
    f.text(E, "mata", dy=-14).text((11, 5.8), "1 m").dim((11.2, 0), (11.2, 5), "5 m", off=(22, 0))
    return f.dim((.4, 0), (.4, 1.5), "1,5", off=(-14, 0)).dim((1, -.7), (10, -.7), "x", off=(0, 12))


@fig
def t_p57():
    f = F(0, 10, 0, 5, w=230)
    f.hatch(.5, 9.5, 1, .35, .5).rect(1.5, 1, 3, 1.6, fill="f")
    f.arrow((3.5, 1.8), (8, 4.2), c="b").line((3.5, 1.8), (7.5, 1.8), c="d").angle((3.5, 1.8), 0, 28, 1.7, "θ")
    return f.text((8.4, 4.4), "F").text((2.3, 1.8), "m")


@fig
def t_p63():
    f = F(-1, 9, -.8, 11, w=170)
    T, L, R, B = (4, 10), (.5, 6.5), (7.5, 6.5), (4, 0)
    f.poly(T, L, B, R, fill="f").line(L, R, c="b").line(T, B, c="b")
    f.angle(T, 225, 270, 1.2, "θ").angle(B, 90, 118, 1.7, "φ")
    return f.text((1.6, 8.7), "a").text((6.4, 8.7), "a").text((1.5, 3), "b").text((6.5, 3), "b")


@fig
def t_p64():
    f = F(-4.5, 6, -1.8, 7, w=270)
    f.axes(-4, 5.4, -.8, 6.4)
    q = lambda x: .35 * (x - .5) ** 2 - .3
    f.plot(q, -3.8, 5)
    P, Q, R = (-3, q(-3)), (4.5, q(4.5)), (.75, q(.75))
    f.poly(P, Q, R, c="b", fill="g")
    return f.text(P, "P", dx=-11).text(Q, "Q", dx=11).text(R, "R", dy=14)


@fig
def t_p66():
    f = F(-1.5, 11.5, -.8, 11.5, w=210)
    f.rect(0, 0, 10, 10, fill="f")
    r = 5.7
    a = math.degrees(math.acos(5 / r))
    for k in range(4):
        f.arc(5, 5, r, 90 * k + a, 90 * k + 90 - a, c="b")
    f.line((5, 5), (10, 5 + r * sin(math.radians(a))), c="b").line((5, 5), (10, 5), c="d")
    f.angle((5, 5), 0, a, 1.6, "α").dot((5, 5))
    return f.text((6.9, 6.6), "r").text((7.5, 4.3), "s/2").text((5, -.45), "s")


@fig
def t_p67():
    f = F(-.5, 5, -.5, 3.4, w=260)
    P = [(0, 2.2), (.55, 3.0), (4.1, 1.17), (2.1, 1.05)]
    P = [(0, 2.2), (.6, 3.0), (4.16, 1.18), (2.17, .33)]
    f.poly(*P, fill="f")
    for p in P:
        f.dot(p)
    for i, s in enumerate(("1 m", "4 m", "2 m", "3 m")):
        a, b = P[i], P[(i + 1) % 4]
        off = [(-18, -6), (0, -12), (12, 12), (-14, 12)][i]
        f.text(((a[0] + b[0]) / 2, (a[1] + b[1]) / 2), s, dx=off[0], dy=off[1])
    return f


@fig
def t_p68a():
    f = F(-7.5, 7.5, -3.8, 3.8, w=300, cap="situasi")
    f.ellipse(0, 0, 3, fill="f").line((-6.5, 0), (6.5, 0), c="thin").line((0, 0), (2.1, 2.14), c="thin")
    for X in (-6.5, 0, 6.5):
        f.dot((X, 0))
    f.text((-6.5, 0), "P", dy=-12).text((6.5, 0), "Q", dy=-12).text((.7, 1.4), "r").text((0, -1.2), "danau")
    return f.dim((-6.5, -3.4), (0, -3.4), "s", off=(0, 12)).dim((0, -3.4), (6.5, -3.4), "s", off=(0, 12))


@fig
def t_p68b():
    f = F(-7.5, 7.5, -2, 4.4, w=300, cap="rute tercepat")
    f.arc(0, 0, 3, 0, 180, c="thin", fill="f").line((-6.5, 0), (6.5, 0), c="thin")
    p = math.radians(20)
    A, B = (-3 * cos(p), 3 * sin(p)), (3 * cos(p), 3 * sin(p))
    f.line((-6.5, 0), A, c="b").arc(0, 0, 3, 20, 160, c="a").line(B, (6.5, 0), c="b").line((0, 0), A, c="d")
    f.angle((0, 0), 160, 180, 1.5, "φ")
    return f.text((-6.5, 0), "P", dy=14).text((6.5, 0), "Q", dy=14)


@fig
def t_p71():
    f = F(-1, 12, -2, 7, w=310)
    f.rect(0, -.5, 11, 1, fill="g")
    f.poly((5.6, .5), (8.2, 5.8), (9.3, 5.3), (7.0, .5), fill="g")
    A, D, E, C, B = (.4, 0), (6, 0), (8.5, 0), (8.5, 5.1), (10.6, 0)
    f.line(A, B, c="a").line(D, C, c="a").line(C, E, c="d").right_angle(E, 90, .3).angle(D, 0, 64, .8, "θ")
    for p in (A, D, C, B):
        f.dot(p)
    return (f.text(A, "A", dy=-13).text(D, "D", dy=14).text(E, "E", dy=14).text(C, "C", dx=14).text(B, "B", dy=-13)
            .dim((.4, -1.4), (6, -1.4), "L₁", off=(0, 12)).text((6.3, 3), "L₂").text((2.5, 1.1), "2r₁").text((9.6, 6), "2r₂"))


@fig
def t_p72():
    f = F(-5, 6, -2, 8.5, w=200)
    f.cone(0, 0, 4, 7.5, ry=.9).cylinder(0, 0, 2, 3.75, ry=.45)
    f.dim((5, 0), (5, 7.5), "H", off=(11, 0))
    return f.dim((-4, -1.5), (4, -1.5), "2R", off=(0, 12))


@fig
def t_p74():
    f = F(0, 10, 0, 7, w=220)
    a, b, c = (2, 6), (8, 6), (5, 2.9)
    f.line(a, b, c, a, c="a").line(c, (5, 1.6), c="a").rect(4.1, .5, 1.8, 1.1, fill="g")
    for p in (a, b, c):
        f.ellipse(p[0], p[1], .22)
    f.angle(c, 46, 134, .8, "θ")
    return f.text((5, 1.05), "m").text(a, "cincin", dy=-13).text(b, "cincin", dy=-13)


@fig
def t_p75():
    f = F(-5, 5, -1.6, 5, w=240)
    f.rect(-4.7, -1.3, 9.4, 1.3, c=None, fill="f").text((0, -.65), "sungai")
    f.arc(0, 1.2, 3.4, -20.6, 200.6, c="b", fill="g").line((-3.18, 0), (3.18, 0))
    f.line((-3.18, 0), (0, 1.2), (3.18, 0), c="d").angle((0, 1.2), -20.6, 200.6, .55, "α")
    return f.text((3.4, 4.9), "busur 1000 m").text((1.9, 1.0), "R")


@fig
def t_p76():
    f = F(-2, 10, -1.8, 13, w=180)
    f.rect(0, 0, 8, 12)
    U, W, I = (6, 12), (0, 3.5), (8, 7.8)
    f.poly(U, W, I, c="b", fill="g").line((0, 12), U, c="d")
    f.text((7.6, 10.4), "x").text((2.4, 8.3), "y")
    return f.dim((9.2, 0), (9.2, 12), "b", off=(10, 0)).dim((0, -.9), (8, -.9), "a", off=(0, 12))


@fig
def t_p78():
    f = F(-1, 13, -2.2, 8, w=270)
    A, B = (1, 1), (4, 1)
    A2, B2 = (7, 6.5), (10, 6.5)
    for a, b in ((A, B), (A2, B2)):
        f.arc((a[0] + b[0]) / 2, a[1], 1.5, 180, 360, c="a", fill="f").line(a, b)
    f.line(A, A2).line(B, B2).line((2.5, -.5), (8.5, 5))
    f.text(A, "A", dx=-11).text(B, "B", dx=11).text((3, 5), "L")
    return f.text((2.5, -1.5), "lebar lembaran a")
