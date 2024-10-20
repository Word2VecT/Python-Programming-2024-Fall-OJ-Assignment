a, b = map(lambda x: str(int(x)), input().split())

res = [char for pair in zip(a, b) for char in pair]
res.extend(a[len(b) :] or b[len(a) :])

# 输出结果
print("".join(res))
