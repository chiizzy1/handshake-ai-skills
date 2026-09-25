#!/usr/bin/env python3
"""Measure the rendered sheet back, the way a solver has to.

This is the fairness gate. If the computed truth cannot be recovered from the
raster within the rubric band, the task is unfair rather than hard, and no
amount of careful work by the model would reach the golden.

It is also the only check that catches geometry that is wrong in a way area
arithmetic hides — a self-intersecting ring sums to a believable total and
fills completely differently.
"""
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon, Rectangle

CAL_COLOUR = (1.0, 0.0, 0.0)


def mask_render(path, xlim, ylim, figsize, regions, bar, dpi=200):
    """Re-render the same transform with flat unique colours per region, plus a
    solid calibration strip standing in for the graphic scale bar.

    `regions` is [(key, ring, (r,g,b), zorder)]; `bar` is (x, y, length, h).
    """
    fig, ax = plt.subplots(figsize=figsize)
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_aspect("equal")
    ax.axis("off")
    fig.patch.set_facecolor("white")
    for _key, ring, colour, z in regions:
        ax.add_patch(Polygon(ring, closed=True, facecolor=colour,
                             edgecolor="none", zorder=z))
    bx, by, blen, bh = bar
    ax.add_patch(Rectangle((bx, by), blen, bh, facecolor=CAL_COLOUR,
                           edgecolor="none", zorder=20))
    fig.savefig(path, dpi=dpi, bbox_inches="tight", pad_inches=0.15,
                facecolor="white")
    plt.close(fig)


def load(path):
    return np.round(np.asarray(plt.imread(path))[:, :, :3] * 255).astype(int)


def calibrate(img, bar_len):
    """Units per pixel, taken from the calibration strip alone."""
    red = (img[:, :, 0] > 200) & (img[:, :, 1] < 60) & (img[:, :, 2] < 60)
    cols = np.where(red.any(axis=0))[0]
    if cols.size == 0:
        raise RuntimeError("calibration strip not found in the mask render")
    px = cols.max() - cols.min() + 1
    return bar_len / px, px


def count_px(img, colour, tol=2):
    t = np.round(np.array(colour) * 255).astype(int)
    return int(np.all(np.abs(img - t) <= tol, axis=2).sum())


def palette(n, channel=2):
    """n distinguishable flat colours in one channel, spaced 8 levels apart so
    a +/-2 tolerance cannot bleed between them."""
    out = []
    for i in range(n):
        c = [0.0, 0.0, 0.0]
        c[channel] = (i + 1) * 8 / 255.0
        out.append(tuple(c))
    return out


def compare(measured, truth, band_pct, label="region"):
    """Print a measured-vs-truth table and return the worst absolute error."""
    worst = 0.0
    width = max(len(str(k)) for k in truth)
    print(f"\n  {label:<{width}} {'measured':>12} {'truth':>11} {'error':>9}")
    for k in truth:
        m, t = measured[k], float(truth[k])
        err = 100.0 * (m - t) / t if t else 0.0
        worst = max(worst, abs(err))
        print(f"  {str(k):<{width}} {m:12.2f} {t:11.2f} {err:+8.2f} %")
    lim = band_pct * 100
    print(f"\n  worst error {worst:.2f} %   rubric band +/- {lim:.2f} %")
    print(f"  MEASURABLE WITHIN BAND: {worst < lim}")
    return worst


def area_check(xlim, ylim, figsize, groups, bar, truth, band_pct,
               scratch="_mask.png", dpi=200):
    """End-to-end: render the mask, calibrate, measure each group, compare.

    `groups` maps an output key to the list of rings that make it up, so a
    finish split across disconnected zones is summed before comparison.
    """
    rings = []
    colours = {}
    flat = [(k, r) for k, rs in groups.items() for r in rs]
    pal = palette(len(flat))
    for (k, ring), c in zip(flat, pal):
        rings.append((k, ring, c, 2))
        colours.setdefault(k, []).append(c)

    mask_render(scratch, xlim, ylim, figsize, rings, bar, dpi=dpi)
    img = load(scratch)
    upp, bar_px = calibrate(img, bar[2])
    print(f"  calibration strip {bar_px} px for {bar[2]:.0f} units "
          f"-> {1/upp:.2f} px/unit")

    measured = {}
    for k, cs in colours.items():
        measured[k] = sum(count_px(img, c) for c in cs) * upp * upp
    worst = compare(measured, truth, band_pct, label="region")
    os.remove(scratch)
    return worst < band_pct * 100
