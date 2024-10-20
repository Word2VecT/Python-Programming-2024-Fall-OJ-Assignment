T = int(input())

cycles = {
    0: [0],
    1: [1],
    2: [2, 4, 8, 6],
    3: [3, 9, 7, 1],
    4: [4, 6],
    5: [5],
    6: [6],
    7: [7, 9, 3, 1],
    8: [8, 4, 2, 6],
    9: [9, 1],
}

for _ in range(T):
    N = int(input())
    last_digit = N % 10
    cycle = cycles[last_digit]
    print(cycle[N % len(cycles[last_digit]) - 1])
