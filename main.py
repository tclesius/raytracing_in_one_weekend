import math

import numpy as np

from color import write_color
from hittable import hit_record, hittable
from hittable_list import hittable_list
from sphere import sphere
from vec3 import color, point3, vec3
from ray import ray
import utilitys
from camera import camera


# def hit_sphere(center: point3, radius: float, r: ray) -> float:
#     oc = r.origin - center
#     a = r.direction.length_squared()
#     half_b = oc.dot(r.direction)
#     c = oc.length_squared() - radius ** 2
#     discriminant = half_b ** 2 - a * c
#     if discriminant < 0:
#         return -1.0
#     else:
#         return (-half_b - math.sqrt(discriminant)) / a


# def ray_color(r: ray) -> color:
#     t = hit_sphere(point3(0, 0, -1), 0.5, r)
#     if t > 0.0:
#         N = (r.at(t) - vec3(0, 0, -1)).unit_vector()
#         return 0.5 * color(N.x() + 1, N.y() + 1, N.z() + 1)
#     unit_direction = r.direction.unit_vector()
#     t = 0.5 * (unit_direction.y() + 1.0)
#     return (1.0 - t) * color(1.0, 1.0, 1.0) + t * color(0.5, 0.7, 1.0)


def ray_color(r: ray, world: hittable) -> color:
    hit, record = world.hit(r, 0, utilitys.infinity)

    if hit:
        return 0.5 * (record.normal + color(1, 1, 1))
    unit_direction = r.direction.unit_vector()
    t = 0.5 * (unit_direction.y() + 1.0)
    return (1.0 - t) * color(1.0, 1.0, 1.0) + t * color(0.5, 0.7, 1.0)


def main():
    # image
    aspect_ratio = 16.0 / 9.0
    image_width = 400
    image_height = int(image_width / aspect_ratio)
    samples_per_pixel = 100

    # world
    world = hittable_list()
    world.add(sphere(point3(0, 0, -1), 0.5))
    world.add(sphere(point3(0, -100.5, -1), 100))

    # camera
    cam = camera()

    # render
    ppm_file = open("example.ppm", "w")
    ppm_file.write(F"P3\n{image_width} {image_height}\n255\n")

    for j in range(image_height - 1, -1, -1):
        print(f"\rScanlines remaining: {j} ", flush=True)
        for i in range(image_width):
            pixel_color = color(0, 0, 0)
            for s in range(samples_per_pixel):
                u = (i + utilitys.random_float()) / (image_width - 1)
                v = (j + utilitys.random_float()) / (image_height - 1)
                r = cam.get_ray(u, v)
                pixel_color += ray_color(r, world)
            write_color(ppm_file, pixel_color, samples_per_pixel)

    ppm_file.close()
    print("\nDone.\n")


if __name__ == '__main__':
    main()
