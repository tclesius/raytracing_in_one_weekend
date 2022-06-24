from abc import ABC
from typing import Tuple

from hittable import hittable, hit_record
import numpy as np

from ray import ray


class hittable_list(hittable, ABC):
    objects: np.array

    # TODO shared memory
    def __init__(self, object=None):
        self.objects = np.array([])
        if object is not None:
            self.add(object)

    def clear(self):
        self.objects = np.array([])

    def add(self, object: hittable):
        self.objects = np.append(self.objects, object)

    def hit(self, r: ray, tmin: float, tmax: float) -> tuple[bool, hit_record]:
        temp_record = hit_record()
        hit_anything = False
        closest_so_far = tmax

        for object in self.objects:
            if object.hit(r, tmin, closest_so_far, temp_record):
                hit_anything = True
                closest_so_far = temp_record.t
        return hit_anything, temp_record
