"""Gambar untuk Thomas §3.10, Stewart §3.9, Larson §2.6 dan §3.7."""
import math
from math import sin, cos, sqrt, pi

from svg import F, fig, register
from shapes import curve, box_net, semicircle_rect, circle_beam, sector_cone, shore


# ---------- bentuk umum ----------
def triangle(xl, yl, hl=None, ang=None, top=None, base=None, arrows=(), W=6.0, H=4.5, w=240):
    """Segitiga siku-siku: dinding tegak di kiri, alas mendatar."""
    f = F(-2.4, W + 2.4, -1.6, H + 1.4, w=w)
    f.line((0, H + .8), (0, 0), (W + 1.2, 0))
    f.line((0, H), (W, 0), c="a").dot((0, H)).dot((W, 0)).right_angle((0, 0), 0, .35)
    f.text((W / 2, 0), xl, dy=15).text((0, H / 2), yl, anchor="end", dx=-7)
    if hl:
        f.text((W / 2, H / 2), hl, anchor="start", dx=6, dy=-6)
    if ang:
        f.angle((W, 0), 180 - math.degrees(math.atan2(H, W)), 180, 1.3, ang)
    if top:
        f.text((0, H), top, dy=-14)
    if base:
        f.text((W, 0), base, dy=-12, anchor="start", dx=6)
    for a, b in arrows:
        f.arrow(a, b, c="b")
    return f


def cone_tank(R, H, r="r", h="h", note=None, fill_to=.55):
    f = F(-5.6, 6.6, -.8, 8.6, w=230)
    y = 6.5 * fill_to
    rr = 3.4 * fill_to
    f.poly((-rr, y), (0, 0), (rr, y), c=None, fill="f").ellipse(0, y, rr, .35, c="a")
    f.line((-3.4, 6.5), (0, 0), (3.4, 6.5)).ellipse(0, 6.5, 3.4, .6)
    f.line((0, 6.5), (3.4, 6.5), c="thin").text((1.7, 7.5), R).line((0, y), (rr, y), c="b").text((rr / 2, y + .5), r)
    f.line((0, 0), (0, 6.5), c="d")
    f.dim((-4.4, 0), (-4.4, 6.5), H, off=(-14, 0)).dim((4.4, 0), (4.4, y), h, off=(14, 0))
    if note:
        f.text((0, 8.4), note)
    return f


def pile(note=None, h="h", d="d"):
    f = F(-5, 5, -1.2, 6, w=220)
    f.cone(0, 0, 3.6, 3.8, ry=.7, fill="g").line((0, 0), (0, 3.8), c="d").text((.45, 1.6), h)
    f.line((-4.6, 5.8), (-.4, 4.9), c="s").line((-4.6, 5.2), (-.4, 4.3), c="s").arrow((0, 4.5), (0, 3.9), c="b")
    f.dim((-3.6, -1), (3.6, -1), d, off=(0, 12))
    if note:
        f.text((2.4, 5.4), note)
    return f


def lamp_person(H, h, x="x", s="s", toward=False, tip=None):
    f = F(-2, 13.5, -1.8, 9.5, w=280)
    f.hatch(-.5, 12.8, 0, .35, .6).line((0, 0), (0, 8)).ellipse(0, 8.25, .25, fill="g")
    f.person(6.4, 0, 3).line((0, 8), (6.4, 3), (10.24, 0), c="a")
    f.dim((-.9, 0), (-.9, 8), H, off=(-16, 0)).dim((5.4, 0), (5.4, 3), h, off=(-14, 0))
    f.dim((0, -1.1), (6.4, -1.1), x, off=(0, 12)).dim((6.4, -1.1), (10.24, -1.1), s, off=(0, 12))
    f.arrow((5.8, .6), (4.2, .6), c="b") if toward else f.arrow((7.2, .9), (8.8, .9), c="b")
    return f


def diamond(side, runner_leg, labels=True):
    """Lapisan bisbol: home bawah, base1 kanan, base2 atas, base3 kiri."""
    f = F(-7, 7, -6.6, 6.8, w=250)
    H, B1, B2, B3 = (0, -5), (5, 0), (0, 5), (-5, 0)
    f.poly(H, B1, B2, B3, fill="f")
    for p in (H, B1, B2, B3):
        f.rect(p[0] - .25, p[1] - .25, .5, .5, fill="g")
    f.text(H, "home", dy=15).text(B1, "base 1", dx=30).text(B2, "base 2", dy=-13).text(B3, "base 3", dx=-30)
    f.text((-3.4, 3.1), side)
    a, b = {"12": (B1, B2), "01": (H, B1), "23": (B2, B3)}[runner_leg]
    P = (a[0] + (b[0] - a[0]) * .4, a[1] + (b[1] - a[1]) * .4)
    f.dot(P, r=4.5).arrow(P, (P[0] + (b[0] - a[0]) * .28, P[1] + (b[1] - a[1]) * .28), c="b")
    return f, P


def boat(hl, xl="x", Ll="L", ang=None):
    f = F(-1.5, 13, -2.4, 5.4, w=300)
    f.rect(-1, -2, 13.5, 2.6, c=None, fill="f").line((-1, .6), (9.5, .6), c="thin")
    f.rect(9.5, -2, 1.2, 4.4, fill="g")
    f.poly((.2, 1.3), (3.2, 1.3), (2.6, .4), (.8, .4), fill="g")
    P, B = (9.5, 4.2), (3.2, 1.3)
    f.line((9.5, 2.4), P).ellipse(P[0], P[1], .25).line(B, P, c="a").line(B, (9.5, 1.3), c="d").line((9.5, 1.3), P, c="d")
    f.text((5.6, 3.3), Ll).dim((10.9, 1.3), (10.9, 4.2), hl, off=(18, 0)).dim((3.2, -.7), (9.5, -.7), xl, off=(0, 12))
    if ang:
        f.angle(P, 205, 270, 1.4, ang)
    return f.arrow((.8, 2.2), (2.8, 2.2), c="b")


def camera_car(dist, xl="x", ang="θ", lab="kamera", obj="mobil"):
    f = F(-1.5, 12, -1.4, 7.4, w=280)
    f.hatch(0, 11, 0, .3, .55)
    C, A = (9, 6), (2, .35)
    f.line(C, (9, 0), c="d").line(A, C, c="a").rect(1.1, .1, 1.8, .55, fill="g").dot(C)
    f.angle(C, 219, 270, 1.4, ang)
    f.text(C, lab, dy=-13).text((1.6, 1.6), obj).dim((10, 0), (10, 6), dist, off=(20, 0))
    return f.dim((2, -.8), (9, -.8), xl, off=(0, 12)).arrow((3.2, .35), (5.4, .35), c="b")


def radar_plane(hl, xl="x", sl="s", ang=None, st="radar"):
    f = F(-1.5, 12.5, -1.4, 7.6, w=290)
    f.hatch(0, 11.5, 0, .3, .55)
    R, A = (1, 0), (9, 5.5)
    f.line((1, 5.5), A, c="d").line(R, (1, 5.5), c="d").line(R, A, c="a").dot(R).dot(A)
    f.arrow(A, (6.4, 5.5), c="b").text(A, "pesawat", dy=-13).text(R, st, dy=-12, anchor="end", dx=-4)
    f.text((5.7, 2.6), sl).dim((1, 6.6), (9, 6.6), xl, off=(0, -9)).dim((-.2, 0), (-.2, 5.5), hl, off=(-18, 0))
    if ang:
        f.angle(R, 0, 34, 2.0, ang)
    return f


def ball_shadow(H, d, note="bola"):
    f = F(-2.4, 22, -2.4, 9.8, w=300)
    f.hatch(-.5, 21, 0, .4, .8).line((0, 0), (0, 8)).ellipse(0, 8.25, .3, fill="g")
    B = (7, 4.8)
    S = (7 * 8 / (8 - 4.8), 0)
    f.line((0, 8), S, c="a").line((7, 0), (7, 8), c="d").dot((7, 8)).dot(B, r=5)
    f.text(B, note, anchor="start", dx=9, dy=-6).text(S, "bayangan", dy=-12, anchor="start", dx=2)
    f.dim((-1.2, 0), (-1.2, 8), H, off=(-18, 0)).dim((0, -1.3), (7, -1.3), d, off=(0, 12))
    return f


def lighthouse(dist, rot="θ"):
    f = F(-2.5, 12, -1.5, 7.5, w=270)
    f.rect(1.5, -1, 10, 8, c=None, fill="f").line((1.5, -1), (1.5, 7), c="a")
    L, P, Q = (9, 5.5), (1.5, 5.5), (1.5, 1)
    f.line(L, P, c="d").line(L, Q, c="b").dot(L).dot(Q).right_angle(P, -90, .35)
    f.angle(L, 180, 211, 1.6, rot)
    f.text(L, "mercusuar", dy=-13).dim((1.5, 6.5), (9, 6.5), dist, off=(0, -9)).text((.7, 3.2), "x")
    return f.text((-.6, 0), "pantai")


# ---------- Thomas §3.10 ----------
register("th_c1", lambda: cone_tank("1,5 m", "3 m", r="x", h="y"))


@fig
def th_c2():
    f = F(-2, 10, -1.4, 8.4, w=250)
    f.hatch(0, 9, 0, .3, .5)
    O, B = (.8, 0), (7, 6.2)
    f.line(O, B, c="a").line((7, 0), B, c="d").line(O, (7, 0), c="s").right_angle((7, 0), 90, .35)
    f.ellipse(7, 6.9, .9, 1.0, fill="g").rect(6.8, 5.8, .4, .3).dot(O)
    f.angle(O, 0, 45, 1.4, "θ").arrow((8.3, 3.6), (8.3, 5.8), c="b")
    return f.text(O, "pengukur", dy=-14, anchor="end").text((3.9, -.7), "150 m").text((7.5, 2.8), "y")


@fig
def th_c3():
    f = F(-2, 11, -1.4, 8, w=260)
    f.arrow((0, -.5), (0, 7.4)).arrow((-.5, 0), (10.2, 0))
    P, C = (0, 4.8), (7.2, 0)
    f.line(P, C, c="a").rect(-.35, 4.8, .7, 1.2, fill="g").rect(7.2, -.35, 1.3, .7, fill="f")
    f.arrow((-1, 5.8), (-1, 3.8), c="b").arrow((8.7, .8), (10.2, .8), c="b")
    return (f.text((1.4, 5.6), "polisi").text((7.9, -1), "mobil").text((4.1, 2.9), "s").text((-.5, 2.4), "y")
            .text((3.6, -.55), "x"))


@fig
def th_c4():
    f = F(-4.5, 9.5, -4.4, 4.8, w=270)
    f.ellipse(0, 0, 3).arrow((-3.8, 0), (9, 0)).arrow((0, -3.8), (0, 4.2))
    th = math.radians(60)
    P, Q = (3 * cos(th), 3 * sin(th)), (6, 0)
    f.line((-0.0, 3.46), (7.2, -.69), c="b").line((0, 0), P, c="a").angle((0, 0), 0, 60, .8, "θ")
    f.dot(P).dot(Q)
    return f.text(P, "P", dy=-13).text(Q, "Q (x, 0)", dy=15, dx=14).text((.4, 1.7), "10")


register("th_c5", lambda: radar_plane("10.000 m", ang="θ", st="R"))


@fig
def th_c6():
    f = F(-2.6, 11, -2.6, 8.4, w=260)
    f.hatch(-1.5, 10, -1.5, .3, .55).line((-1, 6), (2, 6))
    P, O, M = (0, 5.8), (0, 0), (7, 0)
    f.ellipse(0, 5.8, .25).line((-.25, 5.8), (-.25, 3.2), c="a").line(P, M, c="a").line(O, M, c="d")
    f.rect(-.75, 2.2, 1, 1, fill="g").person(7.6, -1.5, 2.6).dot(M)
    f.text((-1.2, 2.7), "W").text((.5, 6.5), "P").text(O, "O", dy=14).text(M, "M", dy=-12)
    return (f.text((4, 3.4), "z").text((3.5, -.5), "x").text((.45, 1), "h")
            .dim((9.4, -1.5), (9.4, 0), "1,5 m", off=(24, 0)))


register("th_p23", lambda: triangle("x(t)", "y(t)", "3,9 m", ang="θ", arrows=(((6.2, .5), (7.8, .5)),)))


@fig
def th_p29():
    f = F(-6, 7, -6, 2, w=260)
    f.arc(0, 0, 5, 180, 360)
    y = -2.6
    a = math.degrees(math.asin(-y / 5))
    f.arc(0, 0, 5, 180 + a, 360 - a, c=None, fill="f")
    x = sqrt(25 - y * y)
    f.line((-x, y), (x, y), c="a").line((0, 0), (x, y), c="b").line((0, 0), (0, -5), c="d").dot((0, 0))
    return f.text((0, .8), "pusat bola").text((2.7, -.8), "13").text((2, -3.1), "r").text((-.5, -3.9), "y")


register("th_p32", lambda: boat("2 m", ang="θ"))


@fig
def th_p33():
    f = F(-2, 11, -1.6, 9, w=250)
    f.arrow((-.5, 0), (10, 0)).arrow((0, -.5), (0, 8.2))
    B, S = (0, 6), (7, 0)
    f.ellipse(0, 6.9, .8, .95, fill="g").line(B, S, c="a").dot(B).dot(S).arrow((7.4, .6), (9, .6), c="b")
    return f.text((3.9, 3.5), "s(t)").text((-.8, 3), "y(t)").text((3.5, -.6), "x(t)").text((7, -.6), "sepeda")


@fig
def th_p34():
    f = F(-5.5, 6.5, -6.4, 6.4, w=210)
    f.poly((-1.8, 3.4), (0, .6), (1.8, 3.4), c=None, fill="g").line((-3, 5.2), (0, .6), (3, 5.2)).ellipse(0, 5.2, 3, .6)
    f.rect(-3, -5.2, 6, 2.6, c=None, fill="g").cylinder(0, -5.2, 3, 5, ry=.6, fill=None).ellipse(0, -2.6, 3, .55, c="a")
    f.dim((-3, 6.2), (3, 6.2), "15 cm", off=(0, -8)).dim((-4, .6), (-4, 5.2), "15 cm", off=(-24, 0))
    return f.text((5, 3), "turun").text((4.8, -3.4), "naik")


register("th_p38", lambda: camera_car("40 m", xl="x"))
register("th_p39", lambda: ball_shadow("15 m", "9 m"))
register("th_p40", lambda: triangle("18 m", "24 m", ang="θ", H=5.4, W=4.2, top="gedung"))


@fig
def th_p43():
    f, P = diamond("27 m", "12")
    B2, B3 = (0, 5), (-5, 0)
    f.line(B3, P, c="a")
    ang = math.degrees(math.atan2(P[1] - B3[1], P[0] - B3[0]))
    f.angle(B3, ang, 45, 1.9, "θ₂")
    back = math.degrees(math.atan2(B3[1] - P[1], B3[0] - P[0]))
    return f.angle(P, 135, back + 360 if back < 0 else back, .9, "θ₁")


register("th_p47", lambda: lighthouse("1 km"))

# ---------- Stewart §3.9 ----------
register("sw_c2", lambda: triangle("x", "y", "5", arrows=(((6.2, .5), (7.8, .5)),)))
register("sw_c3", lambda: cone_tank("2", "4", r="r", h="h"))


@fig
def sw_c4():
    f = F(-2, 10, -5.4, 1.6, w=250)
    C, A, B = (0, 0), (7, 0), (0, -4)
    f.line((-1, 0), (9, 0), c="thin").line((0, 1), (0, -5), c="thin").line(A, B, c="a")
    f.arrow(A, (3.5, 0), c="b").arrow(B, (0, -2), c="b")
    for p in (A, B, C):
        f.dot(p)
    return (f.text(C, "C", dx=-11, dy=-9).text(A, "A", dy=-12).text(B, "B", dx=-12).text((3.5, .7), "x")
            .text((-.7, -2), "y").text((4, -2.4), "z"))


@fig
def sw_c5():
    f = F(-2, 11, -1.5, 7.4, w=260)
    f.line((-1, 5), (10, 5), c="a")
    L, Q, M = (1, 0), (1, 5), (7, 5)
    f.line(L, Q, c="d").line(L, M, c="b").dot(L).right_angle(Q, 270, .35).person(7, 5, 1.8)
    f.angle(L, 40, 90, 1.4, "θ").arrow((7.8, 5.7), (9.6, 5.7), c="b")
    return f.text(L, "lampu", dy=15).text((.4, 2.5), "6").text((4, 5.6), "x")


@fig
def sw_p20():
    return diamond("18 m", "01")[0]


register("sw_p22", lambda: boat("1 m"))
register("sw_p29", lambda: pile(d="d = h"))


@fig
def sw_p30():
    f = F(-1.2, 12.4, -4.8, 1.8, w=320)
    pts = [(0, 0), (0, -1), (1.5, -3), (4.5, -3), (8.5, -1), (10, -1), (10, 0)]
    f.poly((.75, -2), (1.5, -3), (4.5, -3), (6.5, -2), c=None, fill="f").line((.75, -2), (6.5, -2), c="a")
    f.line(*pts)
    for a, b, s in ((0, 1.5, "1,5"), (1.5, 4.5, "3"), (4.5, 8.5, "4"), (8.5, 10, "1,5")):
        f.dim((a, -4), (b, -4), s, off=(0, 12))
    return f.dim((10.8, -1), (10.8, 0), "1", off=(10, 0)).dim((10.8, -3), (10.8, -1), "2", off=(10, 0))


@fig
def sw_p44():
    f = F(-7, 7, -1.8, 6.4, w=300)
    f.hatch(-6.5, 6.5, 0, .3, .55).line((-6.5, 5.4), (6.5, 5.4))
    P = (0, 4.4)
    f.line((0, 5.4), P).ellipse(0, 4.4, .25).line(P, (0, .5), c="d")
    for X, s in ((-3.6, "A"), (4.8, "B")):
        f.line(P, (X, .9), c="a").rect(X - .7, .35, 1.4, .8, fill="g").text((X, .75), s)
    f.arrow((-4.6, 1.6), (-6.2, 1.6), c="b").arrow((5.8, 1.6), (4.4 - .8, 1.6), c="b")
    return f.text(P, "P", dx=-12, dy=-6).text((0, -.9), "Q").text((.8, 2.2), "4 m")


# ---------- Larson §2.6 ----------
register("lr_c4", lambda: radar_plane("6 mil"))
register("lr_c5", lambda: triangle("2000 ft", "s", ang="θ", top="roket", base="kamera",
                                   arrows=(((.5, 4.3), (.5, 5.6)),)))


@fig
def lr_c6():
    f = F(-4, 12, -4, 4, w=300)
    th = math.radians(60)
    A, B = (0, 0), (2.8 * cos(th), 2.8 * sin(th))
    C = (B[0] + sqrt(42 - B[1] ** 2), 0)
    f.ellipse(0, 0, 2.8, c="d").line(A, C, c="d").line(A, B, C, c="a").angle(A, 0, 60, .8, "θ")
    f.rect(C[0] - .3, -.8, 2.2, 1.6, fill="g")
    for p in (A, B, C):
        f.dot(p)
    return f.text((.2, 1.7), "3").text((5, 1.8), "7").dim((0, -3.3), (C[0], -3.3), "x", off=(0, 12))


@fig
def lr_p19():
    f = F(-2, 16, -5, 3, w=320, cap="penampang memanjang; lebar kolam 6 m")
    f.poly((0, -2), (0, -3), (6, -2), c=None, fill="f").line((0, -2), (6, -2), c="a")
    f.poly((0, 0), (12, 0), (12, -1), (0, -3))
    f.dim((-1, -3), (-1, 0), "3 m", off=(-18, 0)).dim((13, -1), (13, 0), "1 m", off=(18, 0))
    return f.dim((0, 1.2), (12, 1.2), "12 m", off=(0, -9))


@fig
def lr_p20():
    f = F(-2.6, 12.5, -.8, 8, w=290)
    d = (6, 2.6)
    A, B, C = (0, 4), (4, 4), (2, 0)
    A2, B2, C2 = [(p[0] + d[0], p[1] + d[1]) for p in (A, B, C)]
    f.poly((1, 2), (3, 2), (9, 4.6), (7, 4.6), c=None, fill="f").poly((1, 2), (C), (3, 2), c=None, fill="f")
    f.poly(A, B, C).line(A, A2, B2, B).line(B2, C2, C).line(A2, C2, c="d").line((1, 2), (3, 2), c="a")
    f.dim((-1, 0), (-1, 4), "3 ft", off=(-18, 0)).dim((0, 5), (4, 5), "3 ft", off=(0, -9))
    return f.text((9.4, 2.0), "12 ft").dim((4.6, 0), (4.6, 2), "h", off=(10, 0))


register("lr_p21", lambda: triangle("x", "y", "25 ft", arrows=(((6.2, .5), (7.8, .5)),)))
register("lr_p22", lambda: triangle("x", "y", "5 m", arrows=(((.5, 4.3), (.5, 5.8)),)))


@fig
def lr_p23():
    f = F(-4.5, 11, -1.4, 9, w=260)
    f.hatch(-.5, 10, 0, .3, .55).rect(-2.4, 0, 2.4, 7.2, fill="g")
    O, T, E = (0, 0), (0, 7.2), (6.24, 3.6)
    f.line(O, E, c="a").line(T, E, c="b").dot(T).dot(E).line(E, (6.24, 0), c="d")
    return (f.text(E, "(x, y)", anchor="start", dx=8).text((3.2, 6.2), "s").text((3.8, 1.4), "12 m")
            .dim((-3.2, 0), (-3.2, 7.2), "12 m", off=(-20, 0)).text((6.8, 1.8), "y").text((3.2, -.8), "x"))


register("lr_p24", lambda: boat("12 ft"))


@fig
def lr_p25():
    f = F(-2, 11, -1.8, 9, w=250)
    f.arrow((0, 0), (10, 0)).arrow((0, 0), (0, 8.4))
    A, B = (0, 6), (4.5, 0)
    f.line(A, B, c="a").dot(A, r=4.5).dot(B, r=4.5).arrow(A, (0, 4.2), c="b").arrow(B, (2.8, 0), c="b")
    return (f.text((2.8, 3.4), "s").text((-.9, 6), "300").text((4.5, -.8), "225")
            .text((6.8, -1.5), "jarak (mil)"))


register("lr_p26", lambda: radar_plane("5 mil"))


@fig
def lr_p27():
    f, P = diamond("90 ft", "23")
    return f.line((0, -5), P, c="a").text((-.6, 0), "d")


register("lr_p29", lambda: lamp_person("15 ft", "6 ft"))
register("lr_p30", lambda: lamp_person("20 ft", "6 ft", toward=True))


@fig
def lr_p31():
    f = F(-2.4, 9, -1.6, 8, w=230)
    f.arrow((-1, 0), (8, 0)).arrow((0, -.5), (0, 7.4))
    Y, X = (0, 4.8), (3.6, 0)
    f.line(Y, X, c="a").rect(-.45, 4.8, .9, 1.4, fill="g").rect(3.6, -.35, 1.8, .7, fill="g").dot(X).dot(Y)
    return (f.text(Y, "(0, y)", anchor="start", dx=12).text(X, "(x, 0)", dy=-14, anchor="start", dx=4)
            .text((2.4, 2.8), "1 m"))


def captioned(g, cap):
    g.cap = cap
    return g


register("lr_p34a", lambda: captioned(curve(lambda x: 3.6 / (x + .6) ** 1.0 * .75, .2, 4.4, 0, 4.2, "x", "y",
                                  xt=[1, 2, 3, 4], yt=[1, 2, 4], w=250), "(i)"))
register("lr_p34b", lambda: captioned(curve(lambda x: 2 * 1.45 ** x, -3, 3.1, 0, 6.4, "x", "y",
                                  xt=[-3, -1, 1, 3], yt=[2, 4, 6], w=250), "(ii)"))
register("lr_p41", lambda: triangle("permukaan air", "10 ft", "x", ang="θ", H=3.4, W=6.4, top="ujung joran",
                                    base="ikan"))
register("lr_p42", lambda: radar_plane("5 mil", ang="θ", st="pengamat"))


@fig
def lr_p43():
    f = F(-2, 12, -1.6, 7.6, w=270)
    f.rect(-1, -1, 12.5, 1, c=None, fill="g").line((-1, 0), (11.5, 0), c="a")
    L, Q, S = (2, 5.5), (2, 0), (7.5, 0)
    f.line(L, Q, c="d").line(L, S, c="b").rect(.9, 5.5, 2.2, 1.2, fill="f").dot(L).dot(S)
    f.angle(L, 270, 315, 1.5, "θ")
    return f.text((1, 2.7), "50 ft").text((4.7, -.5), "x").text((8.8, .6), "dinding").text((5.6, 6.2), "mobil patroli")


@fig
def lr_p44():
    f = F(-5.5, 7, -5, 5, w=240)
    f.ellipse(0, 0, 4).ellipse(0, 0, 2.7, c="thin", fill="f").arrow((-5, 0), (6.4, 0))
    P = (3.4 * cos(math.radians(130)), 3.4 * sin(math.radians(130)))
    f.line((0, 0), P, c="b").line(P, (P[0], 0), c="d").dot(P).dot((0, 0)).angle((0, 0), 130, 180, 1.0, "θ")
    return (f.text(P, "P", dy=-12).text((.5, 1.9), "30 cm").text((P[0] / 2, -.6), "x").text((6.6, .6), "x"))


register("lr_p44g", lambda: curve(lambda t: -600 * pi * sin(t), 0, 2 * pi, -2100, 2100, "θ", "dx/dt",
                                  xt=[(pi / 2, "π/2"), (pi, "π"), (2 * pi, "2π")], yt=[-1885, 1885]))


@fig
def lr_p46():
    f = F(-8, 8, -2, 8, w=290)
    f.hatch(-7, 7, 0, .3, .55)
    C, Q = (0, 6), (4.2, 0)
    f.line(C, (0, 0), c="d").line(C, Q, c="b").dot(C).dot(Q).angle(C, 270, 305, 1.8, "θ")
    return (f.text(C, "kamera", dy=-13).text((-1.2, 3), "50 ft").text((2.1, -.9), "x")
            .dim((-7, -1.7), (7, -1.7), "100 ft", off=(0, 12)))


# ---------- Larson §3.7 ----------
@fig
def lo_c1():
    f = F(0, 12, 0, 8, w=220)
    f.cuboid(1.5, 1.4, 5, 3.8, 2.6, 1.7, open_top=True)
    return f.text((4, .7), "x").text((8.6, 1.6), "x").text((9.8, 4.6), "h")


@fig
def lo_c2():
    f = F(-3.4, 3.8, -1.2, 5.2, w=250)
    f.axes(-3, 3.3, -.8, 4.7, xt=[-1, 1], yt=[1, 3])
    f.plot(lambda x: 4 - x * x, -2.15, 2.15)
    x = sqrt(1.5)
    for s in (-1, 1):
        f.line((0, 2), (s * x, 2.5), c="b").dot((s * x, 2.5))
    return f.dot((0, 2)).text((.2, 1.5), "(0, 2)", anchor="start").text((x, 2.5), "(x, y)", anchor="start", dx=8)


@fig
def lo_c3():
    f = F(-2, 11, -.6, 12.6, w=200)
    f.rect(1.5, .5, 7, 11, fill="g").rect(2.8, 2.2, 4.4, 7.6, fill="f")
    f.dim((9.4, 2.2), (9.4, 9.8), "x", off=(10, 0)).dim((2.8, 12), (7.2, 12), "y", off=(0, -8))
    f.dim((5, 9.8), (5, 11.5), "1½", off=(16, 0)).dim((5, .5), (5, 2.2), "1½", off=(16, 0))
    return f.dim((1.5, 6), (2.8, 6), "1", off=(0, -10)).dim((7.2, 6), (8.5, 6), "1", off=(0, -10))


@fig
def lo_c4():
    f = F(-2.4, 14, -2, 9.6, w=270)
    f.hatch(-.5, 12.5, 0, .3, .55)
    f.line((0, 0), (0, 3.4)).line((12, 0), (12, 8)).line((0, 3.4), (3.6, 0), (12, 8), c="a").dot((3.6, 0))
    f.text((-1.2, 1.7), "12 ft").text((13.2, 4), "28 ft").text((2.3, 2.2), "y").text((7, 4.6), "z")
    return f.dim((0, -1.1), (3.6, -1.1), "x", off=(0, 12)).dim((3.6, -1.1), (12, -1.1), "30 − x", off=(0, 12))


@fig
def lo_c5():
    f = F(0, 16, 0, 8, w=300, cap="kawat 4 ft: persegi dan lingkaran")
    f.rect(2, 2, 4, 4, fill="g").ellipse(11.5, 4, 2.4, fill="f").line((11.5, 4), (13.9, 4), c="b")
    return f.text((4, 6.6), "x").text((1.4, 4), "x").text((12.6, 4.6), "r")


register("lo_p4", lambda: box_net(24, 24, 3.5, "24", "24"))


@fig
def lo_p21():
    f = F(0, 10, 0, 6, w=240)
    f.rect(.3, 4.2, 9.4, 1.5, c=None, fill="f").text((5, 5), "sungai")
    f.rect(2, 1, 6, 3.2, c=None, fill="g").line((2, 4.2), (2, 1), (8, 1), (8, 4.2), c="b")
    return f.text((1.5, 2.6), "y").text((8.5, 2.6), "y").text((5, .4), "x")


@fig
def lo_p23():
    f = F(-5, 5.5, -1, 10.5, w=180)
    f.rect(-3.5, 0, 7, 5.5, fill="f").arc(0, 5.5, 3.5, 0, 180, fill="g")
    return f.line((-3.5, 5.5), (3.5, 5.5), c="thin").text((4.2, 2.7), "y").text((0, -.6), "x")


@fig
def lo_p24():
    f = F(-1, 7.4, -1.2, 4.6, w=260)
    f.rect(0, 0, 3, 1.5, fill="g").axes(-.6, 6.8, -.8, 4.1, xt=[3, 6], yt=[3])
    return f.line((-.6, 3.3), (6.6, -.3), c="a").dot((3, 1.5)).text((3, 1.5), "(x, y)", anchor="start", dx=6, dy=-8)


@fig
def lo_p25():
    f = F(-1, 4.8, -.8, 4.4, w=230)
    f.poly((0, 0), (2.6, 0), (0, 3.25), c=None, fill="g").axes(-.5, 4.3, -.5, 4)
    f.line((0, 3.25), (2.6, 0), c="a")
    for p in ((1, 2), (0, 3.25), (2.6, 0)):
        f.dot(p)
    return (f.text((1, 2), "(1, 2)", anchor="start", dx=8).text((0, 3.25), "(0, y)", anchor="start", dx=8, dy=-6)
            .text((2.6, 0), "(x, 0)", dy=15))


@fig
def lo_p26():
    f = F(-8, 8, -7.5, 7.5, w=220)
    f.ellipse(0, 0, 6, fill="g").poly((0, 6), (-5.2, -3), (5.2, -3), fill="f")
    f.line((0, 6), (0, -3), c="d").line((0, 0), (5.2, -3), c="b").dot((0, 0)).angle((0, 6), 270, 300, 2.0, "α")
    return f.text((3, -.9), "6").text((-.8, 2.2), "6").text((-.7, -1.6), "h")


register("lo_p27", lambda: semicircle_rect(5, 3.54, "(x, y)", "5"))


@fig
def lo_p29():
    f = F(-6, 20, -2.4, 9, w=300)
    f.rect(2, 1, 10, 5, fill="g").arc(2, 3.5, 2.5, 90, 270, c="a", fill="f").arc(12, 3.5, 2.5, -90, 90, c="a", fill="f")
    f.line((2, 6), (12, 6), c="a").line((2, 1), (12, 1), c="a")
    return f.dim((2, 7), (12, 7), "x", off=(0, -9)).dim((16, 1), (16, 6), "y", off=(10, 0))


register("lo_p37", lambda: circle_beam("20", "h", "w"))


@fig
def lo_p38():
    f = F(-5.5, 6.5, -1.4, 7.4, w=250)
    f.arrow((-5, 0), (5.6, 0)).arrow((0, -.5), (0, 6.8))
    A, B, J, S = (-3.5, 0), (3.5, 0), (0, 2.2), (0, 5.2)
    f.line(A, J, B, c="a").line(J, S, c="a")
    for p in (A, B, J, S):
        f.dot(p)
    return (f.text(A, "(−x, 0)", dy=15).text(B, "(x, 0)", dy=15).text(J, "(0, y)", anchor="start", dx=8, dy=-4)
            .text(S, "(0, h)", anchor="start", dx=8))


@fig
def lo_p39():
    f = F(-3.4, 3.4, -3, 3, w=200)
    f.ellipse(0, 0, 2.5, fill="f").poly((0, 2.5), (-2.1, -1.35), (2.1, -1.35), fill="g")
    f.line((0, 0), (0, -2.5), c="thin").dot((0, 0)).angle((0, 2.5), 242, 298, .6, "θ")
    return f.text((.4, -.7), "2")


@fig
def lo_p40():
    f = F(-1.6, 8, -3, 23, w=250, h=250)
    f.poly((0, 0), (5, 0), (0, 20), c=None, fill="g").axes(-.8, 7.4, -1.6, 21.5, xt=[2, 5], yt=[12, 20])
    f.plot(lambda x: 16 - x * x, -.5, 4.15).line((-.1, 20.4), (5.2, -.8), c="b").dot((2, 12))
    return f.text((2, 12), "(2, 12)", anchor="start", dx=10).text((4.4, 17), "y = 16 − x²")


register("lo_p41", lambda: shore("2 km", "x", "4 km", "sumur", "kilang"))


@fig
def lo_p42():
    f = F(-6, 6, -2.4, 8.2, w=220)
    f.ellipse(0, 0, 4, 1.1, fill="g")
    S = (0, 6.6)
    f.line((-4, 0), S, (4, 0), c="a").line(S, (0, 0), c="d").dot(S).angle((4, 0), 121, 180, 1.2, "α")
    return (f.text(S, "lampu", dy=-13).text((-.5, 3.2), "h").text((2.8, 3.4), "s")
            .dim((-4, -1.8), (4, -1.8), "4 ft", off=(0, 12)))


@fig
def lo_p43():
    f = F(-1.5, 12, -3.6, 6, w=300)
    f.rect(-1, 0, 12.5, 5.5, c=None, fill="f").line((-1, 0), (11.5, 0))
    A, P, Q = (1, 5), (4.2, 0), (10, -2.4)
    f.line(A, P, c="a").line(P, Q, c="b").line(A, (1, 0), c="d").line(Q, (10, 0), c="d")
    for p in (A, P, Q):
        f.dot(p)
    return (f.text(A, "perahu", anchor="start", dx=8).text(Q, "Q", dy=14).text((.4, 2.5), "2")
            .text((10.5, -1.2), "1").text((2.6, -.6), "x").text((7, .7), "3 − x"))


@fig
def lo_p46():
    f = F(-1, 12, -4.4, 5.4, w=290)
    f.rect(0, 0, 11, 4.8, c=None, fill="f").rect(0, -3.8, 11, 3.8, c=None, fill="g").line((0, 0), (11, 0))
    P, M, Q = (1.5, 4.2), (6, 0), (10, -3)
    f.line(P, M, Q, c="b").line((6, 3.6), (6, -3.4), c="d").line(P, (1.5, 0), c="thin").line(Q, (10, 0), c="thin")
    for p in (P, M, Q):
        f.dot(p)
    f.angle(M, 90, 137, 1.3, "θ₁").angle(M, 270, 323, 1.4, "θ₂")
    return (f.text(P, "P", dx=-11).text(Q, "Q", dx=11).text((.9, 2), "d₁").text((10.6, -1.5), "d₂")
            .text((3.6, -.5), "x").text((8.2, .6), "a − x").text((9.6, 4), "medium 1").text((2, -2.8), "medium 2"))


register("lo_p47", lambda: sector_cone("12", "θ", "12"))


@fig
def lo_p48():
    f = F(-2, 18, -3, 8.6, w=290)
    f.poly((0, 6.9), (4, 0), (12, 0), (16, 6.9), c=None, fill="f").line((0, 6.9), (4, 0), (12, 0), (16, 6.9), c="a")
    f.line((0, 0), (4, 0), c="d").line((12, 0), (16, 0), c="d").angle((4, 0), 120, 180, 1.4, "θ").angle((12, 0), 0, 60, 1.4, "θ")
    return f.text((.2, 3.2), "8 ft").text((15.8, 3.2), "8 ft").dim((4, -1.4), (12, -1.4), "8 ft", off=(0, 12))


@fig
def lo_p51():
    f = F(-1.6, 12.6, -1.4, 8.4, w=300)
    f.axes(-.8, 11.8, -.8, 7.6, xt=[4, 5, 10], yt=[3, 6])
    m = .45
    f.line((-.4, -.18), (11.2, 11.2 * m), c="a")
    for x, y in ((4, 1), (5, 6), (10, 3)):
        f.line((x, y), (x, m * x), c="b").dot((x, y)).text((x, y), f"({x}, {y})", anchor="start", dx=7, dy=-4)
    return f.text((11, 5.8), "y = mx")


@fig
def lo_p54():
    f = F(-6.4, 6.4, -6, 6, w=220)
    r, th = 5, math.radians(23)
    w, a = r * sin(th), r * cos(th)
    pts = [(w, a), (w, w), (a, w), (a, -w), (w, -w), (w, -a), (-w, -a), (-w, -w), (-a, -w), (-a, w), (-w, w), (-w, a)]
    f.ellipse(0, 0, r).poly(*pts, c="a", fill="g")
    f.line((0, 0), (w, a), c="d").line((0, 0), (0, a), c="d").angle((0, 0), 67, 90, 2.0, "θ")
    return f.dim((0, -.6), (a, -.6), "x", off=(0, 12)).dot((0, 0))


@fig
def lo_l1():
    f = F(-5, 5.4, -4.4, 4.4, w=240)
    f.ellipse(0, 0, 3.4, fill="f")
    t = math.radians(55)
    A, B, C = (3.4, 0), (3.4 * cos(t), 3.4 * sin(t)), (-3.4, 0)
    f.arc(0, 0, 3.4, 0, 55, c="b").line(B, C, c="a").line(C, A, c="d").line((0, 0), B, c="d").angle((0, 0), 0, 55, .8, "θ")
    for p in (A, B, C, (0, 0)):
        f.dot(p)
    return f.text(A, "A", dx=11).text(B, "B", dx=8, dy=-11).text(C, "C", dx=-11).text((1.7, -.6), "2 km")
