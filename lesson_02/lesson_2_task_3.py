import math

def square(side):
    area = side ** 2

    if isinstance(side, float):
        return math.ceil(area)
    return area

#print(square(7.3))