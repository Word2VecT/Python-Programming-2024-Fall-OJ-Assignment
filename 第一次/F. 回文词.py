N = int(input())
S = input()

n = len(S)
rev_S = S[::-1]
dp = [0] * (n + 1)
for i in range(1, n + 1):
    prev = 0
    for j in range(1, n + 1):
        temp = dp[j]
        if S[i - 1] == rev_S[j - 1]:
            dp[j] = prev + 1
        else:
            dp[j] = max(dp[j], dp[j - 1])
        prev = temp
lps_length = dp[n]

print(n - lps_length)
