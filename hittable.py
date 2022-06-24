from abc import abstractmethod, ABC
from dataclasses import dataclass

from ray import ray
from vec3 import point3, vec3


@dataclass(init=False)
class hit_record:
    p: point3
    normal: vec3
    t: float
    front_face: bool

    def set_face_normal(self, r: ray, outward_normal: vec3) -> None:
        self.front_face = r.direction.dot(outward_normal) < 0
        self.normal = outward_normal if self.front_face else -outward_normal


class hittable(ABC):
    @abstractmethod
    def hit(self, r: ray, tmin: float, tmax: float) -> [bool, hit_record]:
        pass
