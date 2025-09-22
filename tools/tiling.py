#!/usr/bin/env python3
"""Generate a pinwheel tiling of the plane, to be used as a background pattern.

SVG Library: https://github.com/orsinium-labs/svg.py
Pinwheel tiling: https://en.wikipedia.org/wiki/Pinwheel_tiling
"""

from itertools import chain

import numpy as np
import svg


def recurse_triangle(origin, axis, sign, triangles, depth):
    """Recursively subdivide a triangle into smaller triangles."""
    ortho = (0.5 * sign) * np.array([-axis[1], axis[0]])
    if depth == 0:
        p1 = origin
        p2 = origin + axis
        p3 = origin + ortho
        triangle = list(chain.from_iterable(p.round(6).tolist() for p in [p1, p2, p3, p1]))
        triangles.append(triangle)
    else:
        axis1 = -0.8 * ortho - 0.2 * axis
        origin1 = origin - axis1
        recurse_triangle(origin1, axis1, -sign, triangles, depth - 1)
        origin2 = origin - 0.5 * axis1
        axis2 = 0.4 * (axis - ortho)
        recurse_triangle(origin2, axis2, sign, triangles, depth - 1)
        recurse_triangle(origin2, axis2, -sign, triangles, depth - 1)
        origin3 = origin - axis1 + axis2
        recurse_triangle(origin3, axis2, -sign, triangles, depth - 1)
        recurse_triangle(origin3, -axis2, sign, triangles, depth - 1)


def color_exp(triangle, rng, bgcolor, shift, sign):
    y = (triangle[1] + triangle[3] + triangle[5]) / 3 + rng.uniform(0, 100)
    c = np.exp(-y / 200)
    r = int(bgcolor[1:3], 16) + sign * round(int(shift[1:3], 16) * c)
    g = int(bgcolor[3:5], 16) + sign * round(int(shift[3:5], 16) * c)
    b = int(bgcolor[5:7], 16) + sign * round(int(shift[5:7], 16) * c)
    return f"#{r:02x}{g:02x}{b:02x}"


def draw_backgrounds():
    width = 2000
    height = 1000
    vbox = svg.ViewBoxSpec(0, 0, width, height)

    triangles = []
    recurse_triangle(np.array([0.0, 0.0]), np.array([width, 0.0]), +1, triangles, 4)
    recurse_triangle(np.array([width, height]), np.array([-width, 0.0]), +1, triangles, 4)

    for scheme, bgcolor, shift in ("light", "#ffeedd", "#446688"), ("dark", "#181210", "#705030"):
        rng = np.random.default_rng(0)
        sign = -1 if scheme == "light" else 1
        elements = [
            svg.Polygon(points=triangle, fill=color_exp(triangle, rng, bgcolor, shift, sign))
            for triangle in triangles
        ]
        canvas = svg.SVG(
            width=width,
            height=height,
            viewBox=vbox,
            elements=elements,
        )
        with open(f"../static/tiling-{scheme}.svg", "w") as f:
            f.write(str(canvas))
            f.write("\n")


def color_opengraph(triangle, rng, color1, color2):
    umax = 300
    dmax = 1800 - umax
    d = sum(triangle) / 6 + rng.uniform(0, umax)
    c = (1 + np.tanh((d - dmax / 2) / 350)) / 2
    r = round(c * int(color1[1:3], 16) + (1 - c) * int(color2[1:3], 16))
    g = round(c * int(color1[3:5], 16) + (1 - c) * int(color2[3:5], 16))
    b = round(c * int(color1[5:7], 16) + (1 - c) * int(color2[5:7], 16))
    print(d, c)
    return f"#{r:02x}{g:02x}{b:02x}"


def draw_opengraph():
    width = 1200
    height = 600
    vbox = svg.ViewBoxSpec(0, 0, width, height)

    triangles = []
    recurse_triangle(np.array([0.0, 0.0]), np.array([width, 0.0]), +1, triangles, 2)
    recurse_triangle(np.array([width, height]), np.array([-width, 0.0]), +1, triangles, 2)

    rng = np.random.default_rng(0)
    color1 = "#503010"
    color2 = "#ffee99"
    elements = []
    for triangle in triangles:
        color = color_opengraph(triangle, rng, color1, color2)
        elements.append(svg.Polygon(points=triangle, fill=color, stroke=color, stroke_width=1))
    canvas = svg.SVG(
        width=width,
        height=height,
        viewBox=vbox,
        elements=elements,
    )
    with open("../static/og-tiling.svg", "w") as f:
        f.write(str(canvas))
        f.write("\n")


if __name__ == "__main__":
    draw_backgrounds()
    draw_opengraph()
