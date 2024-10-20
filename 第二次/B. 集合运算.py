n = int(input())
A = set(map(int, input().split()))

m = int(input())
B = set(map(int, input().split()))

print(" ".join(map(str, sorted(A & B))))
print(" ".join(map(str, sorted(A | B))))
print(" ".join(map(str, sorted(A - B))))
