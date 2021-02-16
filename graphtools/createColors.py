import numpy as np
import pandas as pd
from PIL import ImageColor

def rgb2hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def createColors(inicial, final, n):
    ri, gi, bi = ImageColor.getcolor(inicial, 'RGB')
    rf, gf, bf = ImageColor.getcolor(final, 'RGB')
    reds = np.linspace(ri, rf, n)
    greens = np.linspace(gi, gf, n)
    blues = np.linspace(bi, bf, n)

    color = []

    for i, c in enumerate(reds):
        c = rgb2hex(int(round(reds[i].tolist(), 0)), int(round(greens[i].tolist(), 0)), int(round(blues[i].tolist(), 0)))
        color.append(c)

    return color

