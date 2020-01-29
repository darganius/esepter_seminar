import math
def rad():
    radius = int(input("Введите радиус: "))
    s = math.pi * (radius*radius)
    return s
print(rad())