import math
from dataclasses import dataclass


@dataclass
class vec3:
    e: list[float]

    def __init__(self, e0: float, e1: float, e2: float):
        self.e = [e0, e1, e2]

    def x(self):
        return self.e[0]

    def y(self):
        return self.e[1]

    def z(self):
        return self.e[2]

    def __eq__(self, other: 'vec3'):
        self.e = other.e

    def __neg__(self):
        return vec3(-self.e[0], -self.e[1], -self.e[2])

    def __getitem__(self, item):
        return self.e[item]

    def __iadd__(self, other: 'vec3'):
        self.e[0] += other.e[0]
        self.e[1] += other.e[1]
        self.e[2] += other.e[2]
        return self

    def __imul__(self, other: float):
        self.e[0] *= other
        self.e[1] *= other
        self.e[2] *= other
        return self

    def __itruediv__(self, other: float):
        self *= (1 / other)
        return self

    def __len__(self):
        return math.sqrt(self.length_squared())

    def length_squared(self):
        return self.e[0] ** 2 + self.e[1] ** 2 + self.e[2] ** 2

    # Utility functions
    def __repr__(self):
        return repr(f"{self.e[0]} {self.e[1]} {self.e[2]}")

    def __add__(self, other: 'vec3'):
        return vec3(self.e[0] + other.e[0], self.e[1] + other.e[1], self.e[2] + other.e[2])

    def __sub__(self, other: 'vec3'):
        return vec3(self.e[0] - other.e[0], self.e[1] - other.e[1], self.e[2] - other.e[2])

    def __mul__(self, other: [float, 'vec3']):
        if type(other) == vec3:
            return vec3(self.e[0] * other.e[0], self.e[1] * other.e[1], self.e[2] * other.e[2])
        elif type(other) == float:
            return vec3(self.e[0] * other, self.e[1] * other, self.e[2] * other)
        else:
            return ValueError(other)

    def __rmul__(self, other: [float, 'vec3']):
        return self * other

    def __truediv__(self, other: float):
        return self * (1 / other)

    def dot(self, other: 'vec3'):
        return self.e[0] * other.e[0] + self.e[1] * other.e[1] + self.e[2] * other.e[2]

    def cross(self, other: 'vec3'):
        return vec3(
            self.e[1] * other.e[2] - self.e[2] * other.e[1],
            self.e[2] * other.e[0] - self.e[0] * other.e[2],
            self.e[0] * other.e[1] - self.e[1] * other.e[0],
        )

    def unit_vector(self):
        return self / self.__len__()


# Type aliases for Vec3
point3 = vec3
color = vec3
