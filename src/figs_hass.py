import math
from math import sin, cos, sqrt, pi

from svg import F, fig, register
from shapes import (curve, box_net, cyl_dims, semicircle_rect, circle_beam, sector_cone,
                    shore, beam_wall, two_lights, cone_in_sphere, rect_under)


@fig
def h_c1a():
    return box_net(12, 12, 2.2, "12", "12", cap="(a) lembaran")


@fig
def h_c1b():
    f = F(0, 13, 0, 7, w=240, cap="(b) kotak terlipat")
    f.cuboid(1, 1, 7, 2, 3.5, 2.5, open_top=True)
    f.dim((1, 0.3), (8, 0.3), "12 − 2x", off=(0, 12))
    f.dim((0.3, 1), (0.3, 3), "x", off=(-9, 0))
    return f.text((11.8, 2), "12 − 2x")


register("h_c1c", lambda: curve(lambda x: x * (12 - 2 * x) ** 2, 0, 6, 0, 145, "x", "V",
                                xt=[2, 6], yt=[128], mark=(2, 128), label="V = x(12 − 2x)²"))


@fig
def h_c2():
    return cyl_dims("r", "h", diameter="2r")


register("h_c2g", lambda: curve(lambda r: 2 * pi * r * r + 2000 / r, 1.4, 12, 0, 1500, "r", "A",
                                xt=[(5.42, "5,42")], yt=[500, 1000], mark=(5.42, 553.6)))


@fig
def h_c3():
    return semicircle_rect(2, sqrt(2), "(x, √(4−x²))", "2")


@fig
def h_c4():
    f = F(-1, 11, -5, 5, w=330)
    f.rect(0, 0, 10, 4.2, c=None, fill="f").rect(0, -4.2, 10, 4.2, c=None, fill="g")
    f.arrow((-0.5, 0), (10.8, 0)).arrow((0, -4.6), (0, 4.8))
    A, P, B = (0, 3), (5.5, 0), (8, -3.5)
    f.line(A, P, B, c="b").dot(A).dot(P).dot(B)
    f.line((5.5, 3), (5.5, -3.5), c="d")
    f.angle(P, 90, 151, 1.2, "θ₁").angle(P, 270, 306, 1.4, "θ₂")
    f.text(A, "A", dx=-12).text(B, "B", dx=12).text(P, "P", dx=10, dy=-10)
    f.text((-0.5, 1.5), "a").text((2.7, -0.5), "x").text((6.9, -3.9), "d − x").text((5, -1.8), "b")
    return f.text((8.3, 3.3), "medium 1 (c₁)").text((2.2, -3), "medium 2 (c₂)")


register("h_c6", lambda: curve(lambda x: 5000 / x + 25 * x, 3.2, 40, 0, 1700, "x (hari)", "c(x)",
                               xt=[(14.14, "14,14")], yt=[707], mark=(14.14, 707.1),
                               extra=[(lambda x: 25 * x, 0, 40, "b"), (lambda x: 5000 / x, 3.2, 40, "ad")]))


@fig
def h_p3():
    f = F(-1.4, 1.5, -0.2, 1.3, w=300)
    f.axes(-1.35, 1.35, -0.15, 1.2)
    f.rect(-0.6, 0, 1.2, 0.4, fill="f")
    f.line((-1, 0), (0, 1), (1.12, -0.12), c="a").dot((0.6, 0.4))
    f.text((0.6, 0.4), "P(x, ?)", anchor="start", dx=8, dy=-6)
    f.text((0, 1), "B", dx=12).text((1, 0), "A", dx=6, dy=-10)
    return f.text((-1, 0), "−1", dy=14).text((0.6, 0), "x", dy=14).text((1, 0), "1", dy=14)


register("h_p4", lambda: rect_under(lambda x: 12 - x * x, -3.7, 3.7, -1, 13.5, 2, "y = 12 − x²"))


@fig
def h_p5():
    return box_net(45, 24, 5, "45 cm", "24 cm")


@fig
def h_p6():
    f = F(-0.5, 5.5, -0.5, 4.5, w=240)
    f.axes(-0.3, 5.1, -0.3, 4)
    f.poly((0, 0), (4, 0), (0, 3), c="a", fill="f")
    f.text((2.2, 1.8), "20").text((4, 0), "(a, 0)", dy=14)
    return f.text((0, 3), "(0, b)", anchor="end", dx=-4)


@fig
def h_p7():
    f = F(0, 10, 0, 6, w=260)
    f.rect(0.3, 0.4, 9.4, 1.4, c=None, fill="f").text((5, 1.1), "sungai")
    f.rect(2, 1.8, 6, 3.2, c=None, fill="g")
    f.line((2, 1.8), (2, 5), (8, 5), (8, 1.8), c="b")
    return f.text((1.5, 3.4), "x").text((8.5, 3.4), "x").text((5, 5.5), "800 − 2x")


@fig
def h_p8():
    f = F(0, 10, 0, 7, w=240)
    f.rect(1, 1, 8, 5, fill="g").line((5, 1), (5, 6), c="b")
    f.text((5, 6.5), "x").text((0.5, 3.5), "y")
    return f.text((3, 3.5), "½ lahan").text((7, 3.5), "½ lahan")


@fig
def h_p10():
    f = F(0, 10, 0, 7, w=240)
    f.hatch(0.2, 1.5, 5, .4, .45).hatch(7, 9.8, 5, .4, .45)
    f.cuboid(1.5, 1.5, 5.5, 3.5, 1.6, 1.1, open_top=True)
    return f.text((4.2, 0.9), "x").text((8.3, 1.6), "x").text((1, 3.2), "y")


@fig
def h_p11():
    f = F(0, 10, 0, 12, w=190)
    f.rect(1.5, 0.5, 7, 11, fill="g").rect(3, 3, 4, 6, fill="f")
    f.text((5, 6), "312,5 cm²")
    f.dim((5, 9), (5, 11.5), "10", off=(12, 0)).dim((5, 0.5), (5, 3), "10", off=(12, 0))
    return f.dim((1.5, 6), (3, 6), "5", off=(0, -10)).dim((7, 6.8), (8.5, 6.8), "5", off=(0, -10))


@fig
def h_p12():
    return cone_in_sphere("3", "y", "x")


@fig
def h_p13():
    f = F(0, 10, 0, 5, w=220)
    f.poly((1, 1), (9, 1), (6, 4.5), fill="f").angle((1, 1), 0, 35, 1.2, "θ")
    return f.text((5, 0.4), "a").text((3.2, 3.1), "b")


@fig
def h_p15():
    f = F(0, 9, 0, 5, w=220, cap="tutup/alas dari persegi 2r")
    for x in (0.3, 4.7):
        f.rect(x, 0.5, 4, 4, c="s", fill="g").ellipse(x + 2, 2.5, 2, fill="f")
        f.line((x + 2, 2.5), (x + 4, 2.5), c="thin").text((x + 3, 2.9), "r")
    return f


@fig
def h_p16():
    f = F(-4, 47, -4, 33, w=320)
    x, b = 6, 16.5
    pts = [(0, x), (x, x), (x, 0), (x + b, 0), (x + b, x), (45, x), (45, 30 - x), (x + b, 30 - x),
           (x + b, 30), (x, 30), (x, 30 - x), (0, 30 - x)]
    f.poly(*pts, fill="f")
    for X in (x, x + b, 2 * x + b):
        f.line((X, x), (X, 30 - x), c="d")
    f.line((x, x), (x + b, x), c="d").line((x, 30 - x), (x + b, 30 - x), c="d")
    f.text((x + b / 2, 15), "alas").text((2 * x + b + b / 2, 15), "tutup")
    f.dim((0, -2.5), (45, -2.5), "45 cm", off=(0, 12)).dim((-2.5, 0), (-2.5, 30), "30 cm", off=(-26, 0))
    f.dim((0, 32), (x, 32), "x", off=(0, -9)).dim((x + b, 32), (2 * x + b, 32), "x", off=(0, -9))
    return f.dim((47, 0), (47, x), "x", off=(10, 0))


register("h_p16g", lambda: curve(lambda x: 2 * x ** 3 - 75 * x ** 2 + 675 * x, 0, 15, 0, 2000, "x", "V",
                                 xt=[(5.89, "5,89"), 15], yt=[(1782.5, "1.782,5")], mark=(5.886, 1782.5)))


@fig
def h_p17():
    f = F(-2, 100, -8, 66, w=330, cap="karton dibuka; garis putus-putus = lipatan")
    x = 12
    pts = [(0, x), (x, x), (x, 0), (45 - x, 0), (45 - x, x), (45 + x, x), (45 + x, 0), (90 - x, 0),
           (90 - x, x), (90, x), (90, 60 - x), (90 - x, 60 - x), (90 - x, 60), (45 + x, 60),
           (45 + x, 60 - x), (45 - x, 60 - x), (45 - x, 60), (x, 60), (x, 60 - x), (0, 60 - x)]
    f.poly(*pts, fill="f")
    for X in (x, 45 - x, 45 + x, 90 - x):
        f.line((X, x), (X, 60 - x), c="d")
    for X0, X1 in ((x, 45 - x), (45 + x, 90 - x)):
        f.line((X0, x), (X1, x), c="d").line((X0, 60 - x), (X1, 60 - x), c="d")
    f.line((45, x), (45, 60 - x), c="thin")
    f.text((6, 8), "x").text((6, 52), "x")
    f.dim((0, -4), (90, -4), "90 cm", off=(0, 12))
    return f.dim((96, 0), (96, 60), "60 cm", off=(26, 0))


register("h_p17g", lambda: curve(lambda x: 8 * x ** 3 - 420 * x ** 2 + 5400 * x, 0, 22.5, 0, 23000, "x", "V",
                                 xt=[5, (8.49, "8,49"), (12.5, "12,5")], yt=[17500, 20468],
                                 mark=(8.486, 20468), hline=17500))
register("h_p18", lambda: rect_under(lambda x: 4 * cos(x / 2), -pi, pi, -.6, 4.8, 1.72, "y = 4 cos(x/2)",
                                     xt=[(-pi, "−π"), (pi, "π")]))


@fig
def h_p19():
    f = F(-12, 12, -12, 12, w=210)
    f.ellipse(0, 0, 10, fill="g")
    f.cylinder(0, -5.8, 8.1, 11.6, ry=1.5)
    f.line((0, 0), (8.1, 5.8), c="b").text((3, 3.6), "10").dot((0, 0))
    return f.text((4, 6.6), "r").dim((-9.4, -5.8), (-9.4, 5.8), "h", off=(-10, 0))


@fig
def h_p20():
    f = F(0, 12, 0, 7, w=270)
    f.cuboid(1.5, 1.2, 6.5, 2.8, 2.5, 1.8)
    f.line((4.5, 1.2), (4.5, 4), (7, 5.8), c="b").line((4.5, 1.2), (7, 3), (7, 5.8), c="ad")
    f.dim((1.5, 0.5), (8, 0.5), "panjang L", off=(0, 12)).text((9.9, 2.2), "x")
    return f.text((0.9, 2.6), "x").text((6.2, 6.5), "lingkar")


register("h_p20g", lambda: curve(lambda L: L * ((276 - L) / 4) ** 2, 0, 276, 0, 220000, "L", "V",
                                 xt=[92, 276], yt=[(194672, "194.672")], mark=(92, 194672)))


@fig
def h_p21():
    f = F(0, 10, 0, 8, w=220)
    f.cuboid(1.2, 1.2, 4, 4, 2.6, 1.8)
    f.line((3.2, 1.2), (3.2, 5.2), (5.8, 7), c="b")
    return f.text((0.6, 3.2), "h").text((3.2, 0.6), "h").text((7.1, 1.6), "w").text((4.2, 7.4), "lingkar")


register("h_p21g", lambda: curve(lambda h: h * h * (138 - 1.5 * h), 0, 92, 0, 200000, "h", "V",
                                 xt=[(61.33, "61,3"), 92], yt=[(173042, "173.042")], mark=(61.33, 173042)))


@fig
def h_p22():
    f = F(-5, 5, -1, 11, w=180)
    f.rect(-3.5, 0, 7, 5.5, fill="f")
    f.arc(0, 5.5, 3.5, 0, 180, fill="g")
    f.line((0, 5.5), (3.5, 5.5), c="b").text((1.7, 6.1), "r")
    return f.text((4.2, 2.7), "h").text((0, -0.6), "2r").text((0, 3), "bening").text((0, 7.6), "berwarna")


@fig
def h_p23():
    f = F(-6, 6, -2, 13, w=190)
    f.cylinder(0, 0, 3.5, 7, ry=0.9)
    f.arc(0, 7, 3.5, 0, 180, fill="g")
    f.line((0, 7), (3.5, 7), c="b").text((1.7, 7.7), "r")
    return f.dim((4.6, 0), (4.6, 7), "h", off=(11, 0))


@fig
def h_p24():
    f = F(-0.3, 5.6, -0.5, 2.3, w=340)
    f.poly((0, 1.5), (0.5, 0.64), (1.5, 0.64), (2.0, 1.5), c=None, fill="f")
    f.line((0, 1.5), (0.5, 0.64), (1.5, 0.64), (2.0, 1.5), c="a")
    f.line((0.5, 0.64), (0.5, 1.6), c="d").line((1.5, 0.64), (1.5, 1.6), c="d")
    f.text((1, 0.35), "1").text((0.02, 1.0), "1").text((2.0, 1.0), "1")
    f.text((0.33, 1.32), "θ").text((1.68, 1.32), "θ")
    a, b = (2.9, 0.2), (4.7, 1.3)
    for d in ((0, 0.45), (0.15, 0), (0.55, 0), (0.7, 0.45)):
        f.line((a[0] + d[0], a[1] + d[1]), (b[0] + d[0], b[1] + d[1]))
    for p in (a, b):
        f.poly((p[0], p[1] + .45), (p[0] + .15, p[1]), (p[0] + .55, p[1]), (p[0] + .7, p[1] + .45), fill="g")
    return f.text((4.7, 0.6), "20")


@fig
def h_p25():
    f = F(-4, 28, -3, 31, w=240)
    f.rect(0, 0, 21.6, 28)
    A, P, R, Q = (0, 0), (16.2, 0), (0, 22.9), (21.6, 15.3)
    f.poly(R, P, Q, c="b", fill="g").line(A, P, c="ad").line(A, R, c="ad")
    f.text(A, "A", dx=-10, dy=8).text(P, "P", dy=14).text(Q, "Q", dx=12).text(R, "R", dx=-10)
    f.text((21.6, 0), "B", dx=10, dy=8).text((21.6, 28), "C", dx=10, dy=-8).text((0, 28), "D", dx=-10, dy=-8)
    return f.text((8, -1.4), "x").text((20, 6.5), "x").text((9.5, 12.5), "L").text((-2.2, 11), "y")


@fig
def h_p26():
    f = F(0, 22, 0, 9, w=340)
    f.rect(0.5, 3, 6, 3.5, fill="f").text((3.5, 2.3), "x").text((7.1, 4.7), "y")
    f.cylinder(10, 1.5, 1.4, 4, ry=0.45).text((12, 3.5), "y").text((10, 6.7), "keliling = x")
    f.cylinder(17.5, 1.5, 3.8, 4, ry=1.0)
    f.rect(17.5, 1.5, 3.8, 4, c="b").text((19.4, 6.0), "x").text((17, 3.5), "y")
    return f.text((3.5, 0.3), "").text((10, 0.2), "(a)").text((17.5, -0.1), "(b)")


@fig
def h_p27():
    f = F(-6, 6, -2, 6, w=230)
    f.cone(0, 0, 4.5, 4.5, ry=1.2)
    f.poly((0, 0), (4.5, 0), (0, 4.5), c="b", fill="g").right_angle((0, 0), 0, 0.45)
    return f.text((-0.5, 2), "h").text((2.2, -0.45), "r").text((3.1, 2.6), "√3")


@fig
def h_p28():
    f = F(-0.8, 6, -0.8, 5, w=220)
    f.axes(-0.5, 5.5, -0.5, 4.4)
    f.line((-0.3, 3.225), (4.8, -0.6), c="a").line((0, 0), (1.44, 1.92), c="b").dot((1.44, 1.92))
    return f.text((4, 0), "a", dy=14).text((0, 3), "b", dx=-10).text((1.9, 2.3), "(x, y)")


@fig
def h_p31():
    f = F(0, 14, 0, 6, w=300)
    f.line((0.5, 5), (13.5, 5), c="a").dot((7.5, 5)).text((4, 5.6), "x").text((10.5, 5.6), "b − x")
    f.poly((2, 1), (6, 1), (4, 4.46), fill="f")
    return f.ellipse(10.5, 2.5, 1.8, fill="g")


@fig
def h_p33():
    f = F(-3.5, 3.8, -6, 0.8, w=210)
    A, B, C, D = (-2, 0), (2, 0), (0, -1.9), (0, -5)
    f.line(A, B, c="d").line((0, 0), C, c="d").line(A, C, B, c="b").line(C, D, c="b")
    f.dot(A).dot(B).rect(-0.45, -5.7, 0.9, 0.7, fill="g").text((0, -5.35), "D")
    f.text(A, "A", dx=-10).text(B, "B", dx=10).text(C, "C", dx=-12)
    f.text((-1, 0.4), "2 m").text((1, 0.4), "2 m")
    return f.dim((3, 0), (3, -5), "5 m", off=(18, 0))


@fig
def h_p35():
    f = F(-0.5, 4.2, -0.6, 4.6, w=200)
    f.poly((0, 0), (3, 0), (3, 4), fill="f").rect(1.5, 0, 1.5, 2, c="b", fill="g")
    f.right_angle((3, 0), 90, 0.25)
    return f.text((1.5, -0.35), "3").text((3.3, 2.2), "4").text((1.2, 2.2), "5").text((2.25, 2.25), "w").text((1.3, 1), "h")


@fig
def h_p36():
    return semicircle_rect(3, 3 / sqrt(2), None, "r = 3", wh=True)


@fig
def h_p39():
    return cone_in_sphere("1", "h − 1", "r")


register("h_p40", lambda: rect_under(lambda x: math.exp(-x), -.4, 3.5, -.15, 1.5, 1, "y = e⁻ˣ",
                                     half=True, xt=[], yt=[1]))


@fig
def h_p41():
    f = F(-2.6, 4.2, -2.4, 7.5, w=270, h=300)
    f.axes(-2.5, 3.8, -2.2, 6.9, yt=[3], xt=[1])
    f.plot(lambda x: 2 * x + 3, -2.4, 1.7).plot(math.log, 0.11, 3.7, c="b")
    f.line((0.5, 4), (0.5, math.log(.5)), c="d").line((-1.85, -0.69), (0.5, -0.69), c="d")
    for p in ((0.5, 4), (0.5, math.log(.5)), (-1.85, -.69), (.5, -.69)):
        f.dot(p)
    return f.text((2.4, 6.4), "y = 2x + 3").text((3, 1.8), "y = ln x")


@fig
def h_p43():
    f = F(-1, 5, -1.2, 4.8, w=260)
    f.poly((0, 0), (4, 0), (0, 4), c=None, fill="g")
    f.axes(-.7, 4.6, -1, 4.6)
    f.plot(lambda x: 3 * x - x * x, -.3, 3.3).line((-.3, 4.3), (4.4, -.4), c="ad").dot((2, 2))
    return f.text((2, 2), "(a, 3a − a²)", anchor="start", dx=6, dy=-8).text((3, 0), "3", dy=14).text((3.9, -.9), "y = 3x − x²")


@fig
def h_p44():
    return sector_cone("1", "θ", "1")


@fig
def h_p46():
    return shore("2 km", "x", "6 km", "perahu", "desa")


@fig
def h_p47():
    return beam_wall(2, 5, "2 m", "5 m", "balok", "gedung")


@fig
def h_p49():
    return two_lights("x", "6 − x", "8I", "I")


@fig
def h_p50():
    f = F(-0.5, 11, -0.8, 4.5, w=270)
    f.axes(-.3, 10.5, -.5, 4)
    f.plot(lambda x: x - x * x / 9, 0, 9).arrow((0, 0), (2, 2), c="b").angle((0, 0), 0, 45, 0.9, "α")
    return f.dim((0, -0.45), (9, -0.45), "R", off=(0, 12))


@fig
def h_p51():
    return circle_beam("30 cm")


register("h_p51g", lambda: curve(lambda w: w * (900 - w * w), 0, 30, 0, 12000, "w", "S",
                                 xt=[(17.32, "17,3"), 30], yt=[10392], mark=(17.32, 10392), w=250))
register("h_p51h", lambda: curve(lambda d: d * d * sqrt(max(900 - d * d, 0)), 0, 30, 0, 12000, "d", "S",
                                 xt=[(24.49, "24,5"), 30], yt=[10392], mark=(24.49, 10392), w=250))
register("h_p52g", lambda: curve(lambda w: w * max(900 - w * w, 0) ** 1.5, 0, 30, 0, 300000, "w", "S",
                                 xt=[15, 30], yt=[(263100, "263.100")], mark=(15, 263083), w=250))
register("h_p52h", lambda: curve(lambda d: d ** 3 * sqrt(max(900 - d * d, 0)), 0, 30, 0, 300000, "d", "S",
                                 xt=[(25.98, "26"), 30], yt=[(263100, "263.100")], mark=(25.98, 263083), w=250))


@fig
def h_p53():
    f = F(0, 16, 0, 5, w=320)
    f.hatch(1, 15, 1, .3, .6).line((1, 1), (1, 4.2))
    f.spring((1, 2.2), (10.5, 2.2), coils=10, amp=0.55)
    f.rect(10.5, 1.6, 2.6, 1.3, fill="g").ellipse(11.1, 1.3, .3).ellipse(12.5, 1.3, .3)
    return f.text((7, 0.2), "0").text((11.8, 0.2), "10").text((15.5, 1), "s")


@fig
def h_p54():
    f = F(0, 12, 0, 10, w=220)
    f.line((1, 9), (11, 9)).line((6, 8.5), (6, 0.8), c="thin")
    f.spring((3, 9), (3, 5), coils=8, amp=.45).spring((9, 9), (9, 3), coils=8, amp=.45)
    f.rect(2.2, 3.8, 1.6, 1.2, fill="f").rect(8.2, 1.8, 1.6, 1.2, fill="g")
    f.line((3.8, 5), (6, 5), c="d").line((8.2, 3), (6, 3), c="d").dot((6, 5)).dot((6, 3))
    f.text((3, 4.4), "m₁").text((9, 2.4), "m₂").text((6.5, 5), "s₁").text((5.5, 3), "s₂")
    return f.text((6.5, 4), "0").text((6, 0.3), "s")


@fig
def h_p55():
    f = F(-2, 10, -1.5, 14, w=210)
    f.arrow((0, 0), (9.5, 0)).arrow((0, -1), (0, 13.5))
    f.dot((0, 12)).dot((0, 0)).dot((0, 6)).dot((4.5, 0))
    f.arrow((-.6, 11), (-.6, 8), c="b").line((0, 6), (4.5, 0), c="a")
    f.text((0, 12), "A (siang)", anchor="start", dx=8).text((0, 0), "B", dx=-10, dy=10)
    f.text((0, 6), "A(t)", anchor="start", dx=8, dy=-4).text((4.5, 0), "B(t)", dy=14)
    return f.text((3.1, 3.6), "s(t)").text((9.3, 0), "timur", dy=-10).text((-1.4, 9.5), "12")


register("h_p55g", lambda: curve(lambda t: sqrt((12 - 12 * t) ** 2 + 64 * t * t), -1, 3, -20, 30, "t", "",
                                 xt=[(0.692, "9/13"), 3], yt=[-10, 10, 20], label="s (biru), ds/dt (jingga)",
                                 extra=[(lambda t: (208 * t - 144) / sqrt((12 - 12 * t) ** 2 + 64 * t * t), -1, 3, "b")]))


@fig
def h_p56():
    f = F(0, 12, -1.2, 6, w=300)
    f.line((0.5, 0), (11.5, 0)).text((6, -0.7), "cermin datar")
    A, B, P = (2, 2.6), (10, 3.9), (5.2, 0)
    f.line(A, P, B, c="b").line(P, (5.2, 5), c="d").dot(A).dot(B)
    f.angle(P, 90, 141, 1.2, "θ₁").angle(P, 39, 90, 1.5, "θ₂")
    return f.text(A, "A", dx=-10).text(B, "B", dx=10).text((5.2, 5.4), "normal")


@fig
def h_p58():
    f = F(-11, 1.8, -1, 5, w=340)
    f.arrow((-11, 0), (1.2, 0)).arrow((0, -.5), (0, 4.5))
    f.plot(lambda x: 3 * (2 * (x / 10) ** 3 + 3 * (x / 10) ** 2), -10, 0)
    f.dim((-9.8, 0), (-9.8, 3), "H", off=(12, 0)).dim((-10, -.6), (0, -.6), "L", off=(0, 12))
    return f.text((-6.5, 3.2), "lintasan pendaratan").text((-1, .6), "bandara").text((1.4, 0), "x")


@fig
def h_p71():
    f = F(-.6, 6, -.6, 5, w=260)
    f.axes(-.4, 5.6, -.4, 4.6, xt=[(1, "a"), (2.75, "c"), (4.5, "b")])
    g = lambda x: .3 * (x - 1.8) ** 2 + 1.2
    top = lambda x: g(x) + .45 * (x - 1) * (4.5 - x)
    f.plot(top, .5, 5).plot(g, .3, 5, c="b")
    for X in (1, 2.75, 4.5):
        f.line((X, 0), (X, top(X)), c="d")
    return f.text((1.4, 3.1), "y = f(x)").text((4.6, 1.5), "y = g(x)")


register("h_p73", lambda: curve(lambda x: 1 / math.tan(x) - sqrt(2) / sin(x), .12, 3.02, -9, 1, "x", "y",
                                xt=[(pi / 4, "π/4"), (pi, "π")], yt=[-1, -5], mark=(pi / 4, -1)))
register("h_p74", lambda: curve(lambda x: math.tan(x) + 3 / math.tan(x), .22, 1.48, 0, 14, "x", "y",
                                xt=[(pi / 3, "π/3"), (pi / 2, "π/2")], yt=[(3.464, "2√3"), 10],
                                mark=(pi / 3, 3.464)))


@fig
def h_p75():
    f = F(-.6, 4.8, -.8, 2.8, w=280)
    f.axes(-.4, 4.4, -.5, 2.4)
    f.plot(sqrt, 0, 4.2, n=300).line((1.5, 0), (2.6, sqrt(2.6)), c="b")
    f.dot((1.5, 0)).dot((2.6, sqrt(2.6)))
    return f.text((1.5, 0), "(3/2, 0)", dy=15).text((2.4, 2.05), "(x, √x)").text((4.1, 1.7), "y = √x")


register("h_p75g", lambda: curve(lambda x: sqrt((x - 1.5) ** 2 + x), 0, 4, 0, 4, "x", "D",
                                 xt=[1, 4], yt=[(1.118, "√5/2")], mark=(1, 1.118),
                                 extra=[(sqrt, 0, 4, "b")]))


@fig
def h_p76():
    f = F(-4.8, 5.2, -.8, 5, w=280)
    f.axes(-4.6, 4.8, -.5, 4.6, xt=[-4, 4])
    f.arc(0, 0, 4, 0, 180, c="a").dot((1, sqrt(3))).line((1, sqrt(3)), (2, 2 * sqrt(3)), c="b").dot((2, 2 * sqrt(3)))
    return f.text((1, sqrt(3)), "(1, √3)", dy=14).text((3.3, 3.8), "(2, 2√3)")


register("h_p76g", lambda: curve(lambda x: sqrt(max(20 - 2 * x - 2 * sqrt(3 * max(16 - x * x, 0)), 0)),
                                 -4, 4, 0, 7, "x", "", xt=[-4, 2, 4], yt=[2, 4], mark=(2, 2),
                                 label="D (biru), y (jingga)",
                                 extra=[(lambda x: sqrt(max(16 - x * x, 0)), -4, 4, "b")]))
