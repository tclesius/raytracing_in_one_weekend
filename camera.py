from dataclasses import dataclass

from ray import ray
from vec3 import point3, vec3


@dataclass
class camera:
    aspect_ratio = 16.0 / 9.0
    viewport_height = 2.0
    viewport_width = aspect_ratio * viewport_height
    focal_length = 1.0

    origin = point3(0, 0, 0)
    horizontal = vec3(viewport_width, 0.0, 0.0)
    vertical = vec3(0.0, viewport_height, 0.0)
    lower_left_corner = origin - horizontal / 2 - vertical / 2 - vec3(0, 0, focal_length)

    def get_ray(self, u: float, v: float) -> ray:
        return ray(self.origin, self.lower_left_corner + (u * self.horizontal) + (v * self.vertical) - self.origin)

