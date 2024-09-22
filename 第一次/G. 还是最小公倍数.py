import math
from functools import reduce


def lcm(x, y):
    return x * y // math.gcd(x, y)


C = int(input())
for _ in range(C):
    nums = list(map(int, input().split()))
    print(reduce(lcm, nums[1:]))
