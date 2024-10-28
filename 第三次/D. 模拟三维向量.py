import sys
import math


class Vector:
    def __init__(self, components):
        self.x, self.y, self.z = components

    def add(self, other):
        return Vector([self.x + other.x, self.y + other.y, self.z + other.z])

    def sub(self, other):
        return Vector([self.x - other.x, self.y - other.y, self.z - other.z])

    def mul(self, scalar):
        return Vector([self.x * scalar, self.y * scalar, self.z * scalar])

    def div(self, scalar):
        return Vector([self.x / scalar, self.y / scalar, self.z / scalar])

    def get_length(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)


lines = sys.stdin.read().splitlines()
while len(lines) < 4:
    lines.append("")
v1 = Vector(list(map(int, lines[0].split())))
v2 = Vector(list(map(int, lines[1].split())))
op = lines[2]
if op in ("mul", "div"):
    scalar = int(lines[3])
if op == "add":
    res = v1.add(v2)
    print(res.x, res.y, res.z)
elif op == "sub":
    res = v1.sub(v2)
    print(res.x, res.y, res.z)
elif op == "mul":
    res = v1.mul(scalar)
    print(res.x, res.y, res.z)
elif op == "div":
    res = v1.div(scalar)
    print("{0:.2f} {1:.2f} {2:.2f}".format(res.x, res.y, res.z))
elif op == "get_length":
    length = v1.get_length()
    print("{0:.2f}".format(length))
