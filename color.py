import typing

from utilitys import clamp
from vec3 import color


def write_color(file: typing.IO, pixel_color: color, samples_per_pixel: int):
    r = pixel_color.x()
    g = pixel_color.y()
    b = pixel_color.z()

    # Divide the color by the number of samples.
    scale = 1.0 / samples_per_pixel
    r *= scale
    g *= scale
    b *= scale

    # Write translated [0,255] value of each color component
    file.write(f"\
    {int(256 * clamp(r, 0.0, 0.999))} \
    {int(255.999 * clamp(g, 0.0, 0.999))} \
    {int(255.999 * clamp(b, 0.0, 0.999))} \
    \n")
