import numpy as np
from PIL import ImageColor

def rgb2hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def hex2rgb(hexColor):
    r, g, b = ImageColor.getcolor(hexColor, 'RGB')
    return r, g, b

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

def createColorsRGB(r, g, b, r2, g2, b2, n):
    reds = np.linspace(r, r2, n)
    greens = np.linspace(g, g2, n)
    blues = np.linspace(b, b2, n)

    color = []

    for i, c in enumerate(reds):
        c = (reds[i].tolist(), greens[i].tolist(), blues[i].tolist())
        color.append(c)

    return color

