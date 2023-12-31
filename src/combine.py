import math
import numpy as np
from image_proc import Target

class Element:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.tan = b / a

def compute_target(resu, n):
    center = (1000, 1500)
    points = []
    for i in range(4):
        u = resu[i]
        for e in u:
            if i == 0:
                p = (center[0] + round(e.b/n), center[1] + round(e.a/n))
                points.append(p)
            elif i == 1:
                p = (center[0] - round(e.b/n), center[1] + round(e.a/n))
                points.append(p)
            elif i == 2:
                p = (center[0] - round(e.b/n), center[1] - round(e.a/n))
                points.append(p)
            elif i == 3:
                p = (center[0] + round(e.b/n), center[1] - round(e.a/n))
                points.append(p)
    p = (center[0] - round(resu[4]/n), center[1])
    points.append(p)
    p = (center[0], center[1] + round(resu[5]/n))
    points.append(p)
    p = (center[0] + round(resu[6]/n), center[1])
    points.append(p)
    p = (center[0], center[1] - round(resu[7]/n)) 
    points.append(p)
    return (center, points)

def compute_attr(target):
    u1, u2, u3, u4 = [], [], [], []
    N, E, S, W = 0, 0, 0, 0
    for i in target.borders:
        p = target.points[i]
        dy, dx = p[0] - target.center[0], p[1] - target.center[1]
        if  dx > 0:
            if dy > 0:
                e = Element(dx, dy)
                u1.append(e)
            elif dy == 0:
                E = dx
            else:
                e = Element(dx, -dy)
                u2.append(e)
        elif dx == 0:
            if dy > 0:
                N = dy
            else:
                S = -dy
        else:
            if dy > 0:
                e = Element(-dx, dy)
                u4.append(e)
            elif dy == 0:
                W = -dx
            else:
                e = Element(-dx, -dy)
                u3.append(e)
    u1.sort(key = lambda x: x.tan)
    u2.sort(key = lambda x: x.tan)
    u3.sort(key = lambda x: x.tan)
    u4.sort(key = lambda x: x.tan)
    return (u1, u2, u3, u4, N, E, S, W)

def combine(rs, tolerance=1e-4):
    def combine_u(ru1, ru2):
        pole = tolerance
        i1, i2 = 0, 0
        resu = []
        while i1 < len(ru1) and i2 < len(ru2):
            if ru1[i1].tan <= pole:
                if ru2[i2].tan <= pole:
                    a, b = (ru1[i1].a + ru2[i2].a), (ru1[i1].b + ru2[i2].b)
                    e = Element(a, b)
                    resu.append(e)
                    i1 += 1
                    i2 += 1
                else:
                    tmpi = i2 - 1
                    if tmpi < 0: tmpi = 0
                    a, b = (ru1[i1].a + ru2[tmpi].a), (ru1[i1].b + ru2[tmpi].b)
                    e = Element(a, b)
                    resu.append(e)
                    i1 += 1
            else:
                if ru2[i2].tan <= pole:
                    tmpi = i1 - 1
                    if tmpi < 0: tmpi = 0
                    a, b = (ru1[tmpi].a + ru2[i2].a), (ru1[tmpi].b + ru2[i2].b)
                    e = Element(a, b)
                    resu.append(e)
                    i2 += 1
                else:
                    pole += tolerance
        return resu
    if len(rs) == 2:
        r1 = rs[0]
        r2 = rs[1]
    else:
        r1 = rs[0]
        r2 = combine(rs[1:], tolerance)
    res_u, res_d = [], []
    for i in range(4):
        res_u.append(combine_u(r1[i], r2[i]))
    for i in range(4,8):
        res_d.append(r1[i] + r2[i])

    return (res_u[0], res_u[1], res_u[2], res_u[3], res_d[0], res_d[1], res_d[2], res_d[3])
