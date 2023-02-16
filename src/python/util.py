from random import random
from colorsys import hls_to_rgb

def rand_color() -> str:
    hue = random()
    luminosity = 0.5
    saturation = 0.5 + random()/2.0
    r,g,b = [int(256*i) for i in hls_to_rgb(hue, luminosity, saturation)]
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def generate_unique_color(taken_colors:list[str]) -> str:
    colors = set(taken_colors)
    while True:
        new_color = rand_color()
        if new_color not in colors:
            return new_color
