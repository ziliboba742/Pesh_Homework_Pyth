import math


def square(side):
    area = side * side
    return math.ceil(area) if not isinstance(side, int) else area


# Пимер.
print(square(5))   # 25
print(square(2.5))  # 7
print(square(3.0))  # 9.0
