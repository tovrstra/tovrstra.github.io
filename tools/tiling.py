#!/usr/bin/env python3
"""Generate a pinwheel tiling of the plane, to be used as a background pattern.

SVG Library: https://github.com/orsinium-labs/svg.py
Pinwheel tiling: https://en.wikipedia.org/wiki/Pinwheel_tiling
"""

from itertools import chain

import numpy as np
import svg

triangles = []


def recurse_triangle(origin, axis, sign, depth):
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
        recurse_triangle(origin1, axis1, -sign, depth - 1)
        origin2 = origin - 0.5 * axis1
        axis2 = 0.4 * (axis - ortho)
        recurse_triangle(origin2, axis2, sign, depth - 1)
        recurse_triangle(origin2, axis2, -sign, depth - 1)
        origin3 = origin - axis1 + axis2
        recurse_triangle(origin3, axis2, -sign, depth - 1)
        recurse_triangle(origin3, -axis2, sign, depth - 1)


recurse_triangle(np.array([0.0, 0.0]), np.array([2000.0, 0.0]), +1, 4)
recurse_triangle(np.array([2000.0, 1000.0]), np.array([-2000.0, 0.0]), +1, 4)

width = 2000
height = 1000
vbox = svg.ViewBoxSpec(0, 0, width, height)


def color(triangle, bgcolor, shift, sign):
    y = (triangle[1] + triangle[3] + triangle[5]) / 3 + rng.uniform(0, 80)
    c = np.exp(-y / 200)
    r = int(bgcolor[1:3], 16) + sign * round(int(shift[1:3], 16) * c)
    g = int(bgcolor[3:5], 16) + sign * round(int(shift[3:5], 16) * c)
    b = int(bgcolor[5:7], 16) + sign * round(int(shift[5:7], 16) * c)
    return f"#{r:02x}{g:02x}{b:02x}"


for scheme, bgcolor, shift in ("light", "#f0e0d0", "#406080"), ("dark", "#181210", "#705030"):
    rng = np.random.default_rng(0)
    sign = -1 if scheme == "light" else 1
    elements = [
        svg.Polygon(points=triangle, fill=color(triangle, bgcolor, shift, sign))
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
