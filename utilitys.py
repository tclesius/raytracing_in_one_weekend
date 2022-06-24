import math
import random

infinity = float('inf')
pi = math.pi
RAND_MAX = 1.0


def degrees_to_radiants(degrees: float):
    return degrees * pi / 180.0


def random_float(min: float = None, max: float = None) -> float:
    if min and max:
        return random.uniform(min, max)
    else:
        return random.uniform(0.0, 1.0)


def clamp(x: float, min: float, max: float) -> float:
    if x < min:
        return min
    elif x > max:
        return max
    else:
        return x
