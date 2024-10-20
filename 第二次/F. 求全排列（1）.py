import itertools

while True:
    try:
        n = int(input())
    except EOFError:
        break

    permutations = itertools.permutations(range(1, n + 1))

    for p in permutations:
        print(" ".join(map(str, p)))
