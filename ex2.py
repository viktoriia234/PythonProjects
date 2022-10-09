from math import ceil


def oplata(d):
    return base + ceil(d / 140) * add


base = 4
add = 0.25
print(oplata(100))
print(oplata(1400))
