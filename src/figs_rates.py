import math
from math import sin, cos, sqrt, pi

from svg import F, fig, register
from shapes import curve


# --- §4.8 kinematika ---
register("t_c29", lambda: curve(lambda t: 3 * t ** 4 - 32 * t ** 3 + 114 * t * t - 144 * t + 40, 0, 5, -22, 46,
                                "t", "x", xt=[1, 3, 4, 5], yt=[-19, 13, 40]))
register("t_c29v", lambda: curve(lambda t: 12 * (t - 1) * (t - 3) * (t - 4), 0, 5, -150, 100, "t", "v",
                                 xt=[1, 3, 4], yt=[-144, 25]))


@fig
def t_c30():
    f = F(0, 16, 0, 6, w=300)
    f.line((1, 5), (1, 1.4), (15, 1.4)).spring((1, 2.2), (10, 2.2), coils=7, amp=.55)
    f.rect(10, 1.4, 2, 1.8, fill="g").text((11, 2.3), "M").text((5.5, 3.5), "k")
    f.arrow((12.2, 2.3), (14.8, 2.3), c="b").text((13.7, 3), "F δ(t−t₀)")
    return f.arrow((8, .5), (11, .5)).text((8, .9), "x = 0").text((11.5, .5), "x")


@fig
def t_c31():
    f = F(-3.5, 13, -3.5, 5, w=320)
    A = (0, 1)
    th = math.radians(68)
    B = (2.4 * cos(th), 1 + 2.4 * sin(th))
    C = (B[0] + sqrt(81 - B[1] ** 2), 0)
    f.ellipse(0, 1, 2.4, c="d").line((-3, 0), (12.5, 0), c="thin")
    f.line(A, B, C, c="a").line(A, (0, 0), c="d").line(A, (B[0], 1), B, c="d").rect(C[0] - .5, -.35, 1, .7, fill="g")
    f.angle(A, 0, 68, .75, "θ").angle(C, 180 - math.degrees(math.asin(B[1] / 9)), 180, 1.7, "φ")
    for p in (A, B):
        f.dot(p)
    f.text(A, "A", dx=-11).text(B, "B", dy=-11).text(C, "C", dy=-14).text((-.5, .4), "e")
    return f.text((.0, 2.7), "r").text((5.2, 2.2), "L").dim((0, -1.6), (C[0], -1.6), "x", off=(0, 12))


register("t_flat", lambda: curve(lambda t: (t - 2) ** 3 + 8, 0, 4, 0, 17, "t", "x", xt=[2], yt=[8],
                                 mark=(2, 8), label="titik belok horizontal", w=260))
register("t_speed", lambda: curve(lambda t: t - 2, 0, 4, -2.2, 2.4, "t", "", xt=[2], yt=[-2, 2],
                                  label="v (biru), |v| (jingga)",
                                  extra=[(lambda t: abs(t - 2), 0, 4, "b")], w=260))


def _x(th):
    return 2 * cos(th) + sqrt(81 - (1 + 2 * sin(th)) ** 2)


def _v(th):
    s = 1 + 2 * sin(th)
    return -2 * pi * 2 * (sin(th) + cos(th) * s / sqrt(81 - s * s))


register("t_p24x", lambda: curve(_x, 0, 2 * pi, 0, 12, "θ", "x (cm)", xt=[(pi, "π"), (2 * pi, "2π")], yt=[5, 10]))
register("t_p24v", lambda: curve(_v, 0, 2 * pi, -15, 15, "θ", "v (cm/s)", xt=[(pi, "π"), (2 * pi, "2π")],
                                 yt=[-10, 10]))


@fig
def t_p25b():
    f = F(-1, 12, -1.2, 5.5, w=290)
    f.axes(-.5, 11.2, -.5, 4.8)
    f.plot(lambda x: 3.5 * (3 * (x / 9) ** 2 - 2 * (x / 9) ** 3), 0, 9)
    f.line((9, 0), (9, 3.5), c="d").arrow((9, 4.2), (6.8, 4.2), c="b").text((8, 4.8), "U")
    f.dim((9.7, 0), (9.7, 3.5), "h", off=(10, 0))
    return f.dim((0, -.8), (9, -.8), "D", off=(0, 12))


# --- §4.9 laju berkaitan ---
def lamp(f, x, h):
    f.line((x, 0), (x, h)).ellipse(x, h + .25, .25, .25 * f.sx / f.sy, fill="g")
    return f


@fig
def t_c32():
    f = F(-1.5, 13, -1.6, 9.5, w=280)
    f.hatch(-.5, 12.5, 0, .35, .6)
    lamp(f, 0, 8)
    f.person(6.6, 0, 2.2).line((0, 8), (6.6, 2.2), (8.8, 0), c="a")
    f.dim((-.8, 0), (-.8, 8), "8", off=(-9, 0)).dim((5.6, 0), (5.6, 2.2), "2", off=(-9, 0))
    return f.dim((0, -1), (6.6, -1), "x", off=(0, 12)).dim((6.6, -1), (8.8, -1), "s", off=(0, 12))


@fig
def t_c33():
    f = F(-2.5, 19, -3, 16, w=210)
    f.line((0, 14.5), (0, 0), (18, 0)).line((0, 13.2), (15, 0), c="a")
    f.arrow((1, 13.4), (1, 10.6), c="b").arrow((14.5, 1.1), (17.5, 1.1), c="b")
    f.text((8.7, 7.6), "20").dim((-1.2, 0), (-1.2, 13.2), "y", off=(-9, 0))
    return f.dim((0, -1.6), (15, -1.6), "x", off=(0, 12))


@fig
def t_c34():
    f = F(-5, 5.5, -.8, 7.5, w=210)
    f.poly((-1.5, 3), (0, 0), (1.5, 3), c=None, fill="f")
    f.line((-3, 6), (0, 0), (3, 6), (-3, 6)).line((-1.5, 3), (1.5, 3), c="a").line((0, 0), (0, 6), c="d")
    f.line((0, 3.4), (1.5, 3.4), c="thin").text((.75, 3.9), "r").text((0, 6.8), "6 m (diameter)")
    f.dim((-4, 0), (-4, 6), "6", off=(-9, 0))
    return f.dim((3.7, 0), (3.7, 3), "D", off=(11, 0))


@fig
def t_c35():
    f = F(-2, 16, -3, 11, w=310)
    f.poly((0, 0), (11, 4.5), (15, 1), (4, -3.0), c=None, fill="f")
    lamp(f, 0, 7)
    M, S = (9, .2), (12.6, .28)
    f.person(9, .2, 2).line((0, 7), (9, 2.2), (12.6, .28), c="d").line((0, 0), M, c="a").line(M, S, c="b")
    f.line((0, 0), (3.6, -2.0), c="thin").line((3.6, -2.0), M, c="thin")
    return (f.text((-.7, 3.8), "8").text((4.5, 1), "y").text((11, -.6), "s").text((1.4, -1.8), "10")
            .text((6.6, -1.6), "x"))


@fig
def t_c36():
    f = F(-2, 11, -1.6, 6.6, w=260)
    f.hatch(-.5, 10, 0, .3, .5)
    f.ellipse(0, 5, .25).line((0, 5), (0, 2.4), c="a").line((.2, 5.2), (6, 1), c="a")
    f.rect(-.45, 1.6, .9, .8, fill="g").rect(6, .6, 3, 1.2, fill="f").ellipse(6.7, .4, .4).ellipse(8.4, .4, .4)
    f.dim((-1.2, 0), (-1.2, 5), "5", off=(-9, 0)).dim((5.5, 0), (5.5, 1), "1", off=(-8, 0))
    f.text((1.1, 1.0), "y").text((3.4, 3.5), "z")
    return f.dim((0, -.9), (6, -.9), "x", off=(0, 12))


@fig
def t_l6():
    f = F(-3.5, 10.5, -3.5, 3.8, w=300)
    th = math.radians(55)
    B = (2.4 * cos(th), 2.4 * sin(th))
    A = (B[0] + sqrt(49 - B[1] ** 2), 0)
    f.ellipse(0, 0, 2.4, c="d").axes(-3, 10, -2.8, 3.2)
    f.line((0, 0), B, A, c="a").rect(A[0] - .35, -.25, .7, .5, fill="g").angle((0, 0), 0, 55, .75, "θ")
    f.dot(B)
    return (f.text((.3, 1.4), "l").text((5, 1.6), "L").text(B, "B", dy=-11).text(A, "A", dy=16)
            .text((-.35, -.4), "O"))


@fig
def t_l2():
    f = F(-2, 10, -1.6, 6.6, w=240)
    f.hatch(-1, 9.5, 0, .3, .5).person(-.4, 0, 2.4)
    f.ellipse(.2, 5, .25).line((0, 5), (-.2, 1.7), c="a").line((.4, 5.15), (6, 1), c="a")
    f.rect(6, .55, 2.6, .75, fill="g").ellipse(6.6, .3, .3).ellipse(8, .3, .3)
    f.dim((-1.3, 0), (-1.3, 5), "5 m", off=(-18, 0)).dim((9.3, 0), (9.3, 1), "1 m", off=(18, 0))
    return f.dim((0, -.9), (6, -.9), "s", off=(0, 12))


@fig
def t_l3():
    f = F(-1.5, 24, -3, 8, w=300)
    f.hatch(0, 21, 0, .4, .8).rect(20, 0, 1.6, 7, fill="f").ellipse(0, .25, .3)
    f.person(10, 0, 2).line((0, 0), (20, 4), c="a").line((20, 0), (20, 4), c="b")
    f.text((18.9, 2), "H").text((9, 1), "2")
    return f.dim((0, -1.5), (20, -1.5), "20 m", off=(0, 12))


@fig
def t_l5():
    f = F(-5.5, 5.5, -.8, 5.2, w=200)
    f.rect(-1.5, 1, 3, 2.1, c=None, fill="f").poly((-1.5, 1), (0, 0), (1.5, 1), c=None, fill="f")
    f.line((-1.5, 4), (-1.5, 1), (0, 0), (1.5, 1), (1.5, 4))
    f.ellipse(0, 4, 1.5, .3).line((-1.5, 3.1), (1.5, 3.1), c="a")
    f.dim((2.4, 1), (2.4, 4), "3 m", off=(18, 0)).dim((2.4, 0), (2.4, 1), "1 m", off=(18, 0))
    return f.dim((-1.5, 4.7), (1.5, 4.7), "3 m", off=(0, -9))


@fig
def t_l7():
    f = F(-2, 22, -4.8, 2, w=320, cap="penampang memanjang")
    f.poly((10, -2), (20, -2), (20, -3), c=None, fill="f")
    f.poly((0, 0), (20, 0), (20, -3), (0, -1)).line((10, -2), (20, -2), c="a")
    f.dim((-1, -1), (-1, 0), "1", off=(-9, 0)).dim((21, -3), (21, 0), "3", off=(10, 0))
    f.dim((0, 1), (20, 1), "20 m", off=(0, -9))
    return f.text((17, -1.4), "air").text((12, -4), "lebar kolam 10 m")


@fig
def t_l10():
    f = F(-1, 13, -6, 2.5, w=300)
    f.rect(0, -5.5, 12, 5.5, c=None, fill="f").line((0, 0), (12, 0), c="a")
    f.poly((9.5, .1), (12, .1), (11.5, .8), (10, .8), fill="g")
    B, S, P = (10, .5), (2.5, 0), (2.5, -3.8)
    f.line(B, P, c="b").line(S, P, c="d").line(S, (10, 0), c="d").arrow(P, (2.5, -5), c="a").dot(P)
    return (f.text((1.3, -2), "3t").text((6, .6), "100 + 2t").text((6.8, -2.4), "z").text((3.5, -4.2), "ikan")
            .text((11, 1.6), "perahu"))


@fig
def t_l12():
    f = F(-4, 4.5, -.8, 7, w=180)
    f.cylinder(0, 0, 1.8, 5.6, ry=.45, fill=None).cylinder(0, 0, 1.8, 3.4, ry=.45, fill="g")
    f.line((-1.8, 3.4), (0, 4.8), (1.8, 3.4), c="b").line((0, 6.6), (0, 4.8), c="d")
    return f.text((.8, 6.3), "pasir").dim((-1.8, -.7), (1.8, -.7), "1 m", off=(0, 13))


@fig
def t_l13():
    f = F(-1, 15, -1.5, 8, w=270)
    f.rect(3, 1, 8, 5, c=None, fill="f").arc(3, 3.5, 2.5, 90, 270, c="a", fill="f")
    f.arc(11, 3.5, 2.5, -90, 90, c="a", fill="f").line((3, 6), (11, 6), c="a").line((3, 1), (11, 1), c="a")
    f.line((3, 1), (3, 6), c="d").line((11, 1), (11, 6), c="d").line((11, 3.5), (13.5, 3.5), c="b")
    return f.text((12.2, 4.1), "r").dim((3, 6.8), (11, 6.8), "l", off=(0, -9))


@fig
def t_l14():
    f = F(-115, 130, -75, 75, w=320)
    f.line((-50, 50), (50, 50), c="a").line((-50, -50), (50, -50), c="a")
    f.arc(50, 0, 50, -90, 90, c="a").arc(-50, 0, 50, 90, 270, c="a")
    f.arrow((0, 0), (122, 0)).arrow((0, -55), (0, 70))
    pts = {"O": (0, 0), "C": (50, 0), "B": (100, 0), "A": (0, -50), "D": (50, -50),
           "E": (75, -50 * sqrt(.75))}
    for k, p in pts.items():
        f.dot(p).text(p, k, dx=9, dy=11)
    f.text((68, 10), "mobil 1").text((108, -42), "mobil 2")
    return f.text((-62, 0), "100").dim((-50, 62), (50, 62), "100", off=(-26, -8))


@fig
def t_l16():
    f = F(-4, 13, -4.5, 4, w=280)
    f.ellipse(0, 0, 3, fill="f")
    R = (2.0 * cos(-pi / 4), 2.0 * sin(-pi / 4))
    P = (3 * cos(-pi / 4), 3 * sin(-pi / 4))
    Q = (11, 0)
    f.line((0, 0), Q).line((0, 0), P, c="thin").line(R, Q, c="b").angle((0, 0), -45, 0, .9, "θ")
    for p in ((0, 0), R, P, Q):
        f.dot(p)
    return (f.text((0, 0), "O", dx=-11).text(R, "R", dx=-11, dy=5).text(P, "P", dx=9, dy=10).text(Q, "Q", dx=11)
            .dim((0, 3.6), (11, 3.6), "1 m", off=(0, -8)))


@fig
def t_l19():
    f = F(-1.5, 12, -1.5, 17, w=220)
    f.rect(0, 0, 11, 10, c=None, fill="f").line((0, 0), (11, 0), c="a").line((0, 10), (11, 10), c="a")
    f.line((0, 15), (11, 15))
    A, B = (3, 0), (5.4, 10)
    C = (3 + 1.5 * 2.4, 15)
    f.line(A, C, c="d")
    for p in (A, B, C):
        f.dot(p)
    f.arrow(A, (5, 0), c="b").arrow(B, (2.8, 10), c="b")
    return (f.text(A, "A", dy=14).text(B, "B", dx=10, dy=12).text(C, "C", dy=-12)
            .dim((-.8, 0), (-.8, 10), "10", off=(-12, 0)).dim((-.8, 10), (-.8, 15), "5", off=(-10, 0)))


@fig
def t_l22():
    f = F(-2, 22, -2.5, 9.5, w=290)
    f.hatch(-.5, 21, 0, .4, .8)
    lamp(f, 0, 8)
    f.line((0, 8), (16, 0), c="a").line((7, 0), (7, 8), c="d").dot((7, 8 - 3.5), r=5)
    f.line((0, 8), (7, 8), c="d")
    f.dim((-1, 0), (-1, 8), "25", off=(-12, 0)).dim((0, -1.4), (7, -1.4), "10", off=(0, 12))
    return f.text((8.3, 6.4), "d").text((16, .7), "bayangan").dim((7, -1.4), (16, -1.4), "x − 10", off=(0, 12))


@fig
def t_l25():
    f = F(-6, 7, -1.5, 11, w=180)
    f.poly((-3.5, 0), (3.5, 0), (1.6, 9), (-1.6, 9), fill="g").line((0, 0), (0, 9), c="d")
    f.dim((-1.6, 10), (1.6, 10), "2r", off=(0, -9)).dim((-3.5, -.8), (3.5, -.8), "2R", off=(0, 12))
    return f.dim((5, 0), (5, 9), "h", off=(10, 0))


@fig
def t_l26():
    f = F(-5, 5.5, -.8, 7.5, w=210)
    f.poly((0, 0), (-2, 3), (0, 6), (2, 3), c="b", fill="g").line((-2, 3), (2, 3), c="d")
    f.line((-4, 6), (0, 0), (4, 6))
    f.dim((-4, 6.8), (4, 6.8), "4", off=(0, -9)).dim((-4.6, 0), (-4.6, 3), "h", off=(-9, 0))
    f.dim((-4.6, 3), (-4.6, 6), "h", off=(-9, 0))
    return f.dim((5, 0), (5, 6), "3", off=(10, 0))


@fig
def t_l27():
    f = F(-3.5, 13, -3.5, 5, w=310)
    th = math.radians(55)
    B = (2.4 * cos(th), 2.4 * sin(th))
    A = (B[0] + sqrt(36 - B[1] ** 2), 0)
    C = (11, 3.2)
    f.ellipse(0, 0, 2.4, c="d").axes(-3, 12.4, -2.6, 4.4)
    f.line((0, 0), B, A, C, c="a").line((11, 0), C, c="d").angle((0, 0), 0, 55, .75, "θ")
    for p in (B, A, C):
        f.dot(p)
    return (f.text((.3, 1.4), "l").text((4, 1.6), "L").text(B, "B", dy=-11).text(A, "A", dy=16)
            .text(C, "C", dx=11).text((11.6, 1.6), "y").dim((0, -1), (A[0], -1), "x", off=(0, 12))
            .dim((0, -2.2), (11, -2.2), "k", off=(0, 12)))


@fig
def t_l28():
    f = F(-7, 9, -4.5, 6.5, w=280)
    O = (0, 0)
    f.arrow(O, (-5.5, -3.5)).arrow(O, (7.5, -2)).line(O, (0, 4.5))
    plane, car = (3.6, 3.55), (-3.3, -2.1)
    f.line((0, 4.5), plane, c="d").line(car, plane, c="b").dot(plane).dot(car)
    return (f.text(plane, "pesawat", dy=-12).text(car, "mobil", dx=22, dy=10).text((-.8, 2.2), "1 km")
            .text((-5.8, -4), "timur").text((8, -2.5), "utara"))


@fig
def t_l29():
    f = F(-7, 33, -5, 32, w=250)
    f.poly((0, 0), (27, 0), (27, 27), (0, 27), fill="f")
    S, R, B = (2, 27), (20.25, 0), (14.5, 13.5)
    f.line(S, (27, 0), c="d").arrow(S, B, c="b").arrow(R, (24, 0), c="a").line(B, R, c="thin")
    for p in (S, R, B):
        f.dot(p)
    return (f.text((0, 0), "home", dy=14).text((27, 0), "base 1", dx=8, dy=14).text((27, 27), "base 2", dy=-11)
            .text((0, 27), "base 3", dx=-14, dy=-11).text(B, "bola", dx=20, dy=-6).text(R, "pelari", dy=14)
            .text((3.5, 29), "2 m"))


@fig
def t_l30():
    f = F(-6, 16, -5, 5.5, w=300)
    f.ellipse(0, 0, 4.2).ellipse(0, 0, 1, fill="g").ellipse(9, 0, 1.8, fill="f").dot((0, 0)).dot((9, 0))
    f.line((0, 1), (9, 1.8), c="a").line((0, -1), (9, -1.8), c="a")
    f.line((0, 0), (-4.2 * .7, -4.2 * .71), c="b").dot((-4.2 * .94, 4.2 * .34), r=4.5)
    f.line((9, 0), (10.3, 1.25), c="b").line((0, 0), (0, 1), c="b")
    return f.text((-2.2, -1), "R̄").text((.6, .3), "r").text((10.4, .35), "R").text((-4.7, 2.4), "batu")


@fig
def t_l31():
    f = F(-4.8, 4.8, -4, 1.8, w=270)
    f.arc(0, 0, 3, 180, 360, c="a", fill="f").line((-3, 0), (3, 0))
    L, S = (-3, 0), (0, -2)
    lam = 18 / 13
    Sh = (-3 + 3 * lam, -2 * lam)
    f.line(L, S, Sh, c="b").line((0, 0), S, c="d").angle(L, -34, 0, .8, "α")
    for p in (L, S, Sh):
        f.dot(p)
    return (f.text(L, "lampu", dy=-12).text(S, "batu", dx=-18, dy=4).text(Sh, "bayangan", anchor="start", dx=7, dy=9)
            .text((.35, -1), "d").text((1.5, .45), "3 m"))


@fig
def t_l33():
    f = F(-4.5, 4.5, -4.5, 4.5, w=190)
    f.ellipse(0, 0, 4, fill="f")
    for h in range(1, 13):
        a = math.radians(90 - 30 * h)
        f.text((3.4 * cos(a), 3.4 * sin(a)), str(h))
    f.line((0, 2.7), (0, 0), (2.1, 0), c="a").line((0, 2.7), (2.1, 0), c="b").dot((0, 0))
    return f.text((-.45, 1.4), "10").text((1.0, -.45), "7,5").text((1.4, 1.65), "z")


@fig
def t_l34():
    f = F(-90, 95, -48, 48, w=330)
    f.line((-50, 30), (50, 30), c="a").line((-50, -30), (50, -30), c="a")
    f.arc(50, 0, 30, -90, 90, c="a").arc(-50, 0, 30, 90, 270, c="a")
    O, A, B = (0, 0), (0, 30), (51.86, 29.94)
    f.line(O, A, c="d").line(O, B, c="b").line(O, (70, 0), c="d").angle(O, 0, 30, 17, "π/6", lr=1.5)
    for p in (O, A, B):
        f.dot(p)
    f.text(O, "kamera", dy=15).text(A, "A", dy=-12).text(B, "B", dy=-12).text((-66, 0), "r = 30")
    return f.dim((-50, -40), (50, -40), "100 m", off=(0, 11))


@fig
def t_l35():
    f = F(-2, 17, -3.5, 10, w=300, cap="tampak miring; dinding 1 m di belakang orang")
    f.poly((0, 0), (12, 4.2), (15, 1.4), (3, -2.8), c=None, fill="f")
    f.line((4.2, -3.2), (16.5, 1.1), c="a").line((16.5, 1.1), (16.5, 5.5), c="a").line((4.2, 1.2), (4.2, -3.2), c="a")
    f.line((4.2, 1.2), (16.5, 5.5), c="a")
    lamp(f, 0, 7)
    f.person(9.5, .4, 2).line((0, 7), (9.5, 2.4), (11.4, 1.5), c="d").line((11.4, -.68), (11.4, 1.5), c="b").dot((11.4, 1.5))
    return f.text((-.7, 3.5), "8").text((8.6, 1.4), "2").text((12, .4), "z").text((1.6, -2), "10 + 1")
