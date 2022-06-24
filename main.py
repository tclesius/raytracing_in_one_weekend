
from color import write_color
from hittable import hittable
from hittable_list import hittable_list
from sphere import sphere
from vec3 import color, point3, vec3
from ray import ray
import utilitys
from camera import camera


def ray_color(r: ray, world: hittable, depth: int) -> color:
    hit, record = world.hit(r, 0, utilitys.infinity)
    # if we've exceeded the ray bounce limit, no more light is gathered
    if depth <= 0:
        return color(0, 0, 0)

    if hit:
        target = record.p + record.normal + vec3.random_in_unit_sphere()
        return 0.5 * ray_color(ray(record.p, target - record.p), world, depth-1)

    unit_direction = r.direction.unit_vector()
    t = 0.5 * (unit_direction.y() + 1.0)
    return (1.0 - t) * color(1.0, 1.0, 1.0) + t * color(0.5, 0.7, 1.0)


def main():
    # image
    aspect_ratio = 16.0 / 9.0
    image_width = 400
    image_height = int(image_width / aspect_ratio)
    samples_per_pixel = 100
    max_depth = 50

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
                pixel_color += ray_color(r, world, max_depth)
            write_color(ppm_file, pixel_color, samples_per_pixel)

    ppm_file.close()
    print("\nDone.\n")


if __name__ == '__main__':
    main()
