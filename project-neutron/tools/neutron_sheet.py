#!/usr/bin/env python3
"""Drawing primitives shared by every Neutron task we author.

One rule governs this module: the sheet is drawn in real-world units with an
equal aspect ratio, and the graphic scale bar lives in those same units. That
is what makes a raster measurable — the bar and the geometry cannot drift
apart, because they are the same coordinate system.

Nothing here writes a dimension onto the drawing. Inputs are images, and the
whole point is that the solver must measure rather than read.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Rectangle

# Five hatch patterns that stay distinguishable at plan scale and after JPEG
# compression. Avoid pairs that differ only in angle.
HATCH = {
    "A": "o",      # circles
    "B": "xx",     # diagonal crosshatch
    "C": "--",     # horizontal lines
    "D": "//",     # diagonal lines
    "E": "..",     # stipple
}


class Sheet:
    """A drawing sheet in world units, with the usual furniture."""

    def __init__(self, x0, x1, y0, y1, figsize=(20.0, 12.0)):
        self.fig, self.ax = plt.subplots(figsize=figsize)
        self.x0, self.x1, self.y0, self.y1 = x0, x1, y0, y1
        self.ax.set_xlim(x0, x1)
        self.ax.set_ylim(y0, y1)
        self.ax.set_aspect("equal")
        self.ax.axis("off")

    # --- furniture ---------------------------------------------------------

    def frame(self, inset=0.8, lw=2.0):
        self.ax.add_patch(Rectangle(
            (self.x0 + inset, self.y0 + inset),
            (self.x1 - self.x0) - 2 * inset, (self.y1 - self.y0) - 2 * inset,
            fill=False, lw=lw, ec="black", zorder=1))
        return self

    def scale_bar(self, x, y, total=20.0, step=5.0, h=0.55, unit="m"):
        """Alternating graphic bar. `total` is in world units, so measuring the
        bar in pixels calibrates the whole sheet."""
        n = int(round(total / step))
        for i in range(n):
            self.ax.add_patch(Rectangle(
                (x + i * step, y), step, h,
                facecolor="black" if i % 2 == 0 else "white",
                edgecolor="black", lw=0.9, zorder=6))
        for i in range(n + 1):
            self.ax.text(x + i * step, y - 0.55, f"{int(i * step)}",
                         ha="center", va="top", fontsize=9, zorder=6)
        self.ax.text(x + total + 0.7, y + h / 2, unit, ha="left", va="center",
                     fontsize=9, zorder=6)
        self.ax.text(x + total / 2, y + h + 0.55, "GRAPHIC SCALE", ha="center",
                     va="bottom", fontsize=9, style="italic", zorder=6)
        return self

    def north(self, x, y, r=1.7):
        self.ax.add_patch(Polygon(
            [(x, y + r), (x - r * 0.42, y - r * 0.55), (x, y - r * 0.2)],
            closed=True, facecolor="black", edgecolor="black", lw=0.8, zorder=6))
        self.ax.add_patch(Polygon(
            [(x, y + r), (x + r * 0.42, y - r * 0.55), (x, y - r * 0.2)],
            closed=True, facecolor="white", edgecolor="black", lw=0.8, zorder=6))
        self.ax.text(x, y - r - 0.5, "N", ha="center", va="top", fontsize=11,
                     weight="bold", zorder=6)
        return self

    def title_block(self, x0, x1, y0, y1, rows):
        """`rows` is [(height, [(text, fontsize, bold), ...]), ...] laid out
        from the top down, each row from its own top edge, so nothing collides
        however long the strings get.

        Line spacing is expressed in world units, so it has to scale with the
        sheet: a site plan drawn at 200 m across needs leading roughly fifteen
        times a 14 m block's. The reference width is 14 units, which leaves the
        original sheets rendering unchanged.
        """
        u = (x1 - x0) / 14.0
        self.ax.add_patch(Rectangle((x0, y0), x1 - x0, y1 - y0, fill=False,
                                    lw=1.6, ec="black", zorder=6))
        y = y1
        for height, lines in rows:
            if y < y1:
                self.ax.plot([x0, x1], [y, y], color="black", lw=1.0, zorder=6)
            cursor = y - 0.95 * u
            for txt, fs, bold in lines:
                if txt:
                    self.ax.text(x0 + 0.55 * u, cursor, txt, ha="left",
                                 va="top", fontsize=fs, zorder=6,
                                 weight="bold" if bold else "normal")
                cursor -= ((fs / 9.0) * 1.05 + 0.18) * u
            y -= height
        return self

    def callout(self, text, tx, ty, px, py, fs=10):
        self.ax.annotate(text, xy=(px, py), xytext=(tx, ty), fontsize=fs,
                         zorder=7, ha="center", va="center",
                         arrowprops=dict(arrowstyle="-", lw=0.9, color="black",
                                         shrinkA=2, shrinkB=2))
        return self

    # --- content -----------------------------------------------------------

    def region(self, ring, hatch=None, lw=1.1, zorder=2, facecolor="white"):
        self.ax.add_patch(Polygon(ring, closed=True, facecolor=facecolor,
                                  edgecolor="black", lw=lw, hatch=hatch,
                                  zorder=zorder))
        return self

    def outline(self, ring, lw=2.4, zorder=5):
        self.ax.add_patch(Polygon(ring, closed=True, fill=False,
                                  edgecolor="black", lw=lw, zorder=zorder))
        return self

    def label(self, x, y, text, fs=8.5, zorder=4, **kw):
        self.ax.text(x, y, text, ha="center", va="center", fontsize=fs,
                     zorder=zorder, **kw)
        return self

    def save(self, path, dpi=300, quality=94):
        self.fig.savefig(path, dpi=dpi, pil_kwargs={"quality": quality},
                         bbox_inches="tight", pad_inches=0.15,
                         facecolor="white")
        plt.close(self.fig)
        return path


def centroid(ring):
    return (sum(p[0] for p in ring) / len(ring),
            sum(p[1] for p in ring) / len(ring))


def shoelace(ring):
    """Unsigned area of a closed vertex ring.

    Caution: this cancels signed lobes, so a self-intersecting ring can return
    a plausible number. Area alone never proves a polygon is well formed —
    check the winding, or measure the rendered fill.
    """
    a = 0.0
    n = len(ring)
    for i in range(n):
        x1, y1 = ring[i]
        x2, y2 = ring[(i + 1) % n]
        a += x1 * y2 - x2 * y1
    return abs(a) / 2.0


def is_simple(ring, samples=400):
    """Cheap self-intersection screen on a subsampled ring. Catches the bowtie
    winding bug that shoelace hides."""
    n = len(ring)
    step = max(1, n // samples)
    pts = ring[::step]
    m = len(pts)

    def seg_cross(p1, p2, p3, p4):
        def o(a, b, c):
            v = (b[1] - a[1]) * (c[0] - b[0]) - (b[0] - a[0]) * (c[1] - b[1])
            return 0 if abs(v) < 1e-12 else (1 if v > 0 else 2)
        o1, o2, o3, o4 = o(p1, p2, p3), o(p1, p2, p4), o(p3, p4, p1), o(p3, p4, p2)
        return o1 != o2 and o3 != o4

    for i in range(m):
        a1, a2 = pts[i], pts[(i + 1) % m]
        for j in range(i + 2, m):
            if i == 0 and j == m - 1:
                continue
            b1, b2 = pts[j], pts[(j + 1) % m]
            if seg_cross(a1, a2, b1, b2):
                return False
    return True
