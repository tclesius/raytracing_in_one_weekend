from vec3 import *


@dataclass
class ray:
    origin: point3
    direction: vec3

    def __init__(self, origin: point3 = None, direction: vec3 = None):
        self.origin = origin
        self.direction = direction

    def at(self, t: float):
        if self.origin is not None and self.direction is not None:
            return self.origin + t * self.direction
        else:
            return ValueError(f"Origin:{self.origin} Direction:{self.direction}")
