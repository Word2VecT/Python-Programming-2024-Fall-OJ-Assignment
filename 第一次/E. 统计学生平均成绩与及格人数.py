import statistics

N = int(input())
scores = list(map(int, input().split()))

avg = statistics.mean(scores)
cnt = sum(1 for score in scores if score >= 60)

print(f"average = {avg:.1f}")
print(f"count = {cnt}")
