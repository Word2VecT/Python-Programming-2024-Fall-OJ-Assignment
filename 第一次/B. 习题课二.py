import heapq

n = int(input())
nums = list(map(int, input().split()))

heapq.heapify(nums)
print(sum([(heapq.heappop(nums) + 1) // 2 for _ in range((n + 1) // 2)]))
