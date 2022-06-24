import math
from abc import ABC

from hittable import hittable, hit_record
from ray import ray
from vec3 import point3


class sphere(hittable, ABC):
    center: point3
    radius: float

    def __init__(self, center: point3, radius: float):
        self.center = center
        self.radius = radius

    def hit(self, r: ray, tmin: float, tmax: float, record: hit_record) -> bool:
        oc = r.origin - self.center
        a = r.direction.length_squared()
        half_b = oc.dot(r.direction)
        c = oc.length_squared() - self.radius ** 2
        discriminant = half_b ** 2 - a * c
        if discriminant < 0: return False

        sqrtd = math.sqrt(discriminant)
        root = (-half_b - sqrtd) / a
        if (root < tmin) or (tmax < root):
            root = (-half_b + sqrtd) / a
            if (root < tmin) or (tmax < root):
                return False

        record.t = root
        record.p = r.at(record.t)
        outward_normal = (record.p - self.center) / self.radius
        record.set_face_normal(r, outward_normal)

        return True
