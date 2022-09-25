import sys

input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


N, K = MIIS()
foods = list(MIIS()) + [0]
dp = [0] * (N + 1)

count = 0
l = r = 0
while r <= N:
    if count >= K:
        while count >= K:
            dp[r] = max(dp[r], dp[l] + count - K)
            count -= foods[l]
            l += 1
        continue
    dp[r] = max(dp[r], dp[r - 1])
    count += foods[r]
    r += 1

print(dp[-1])
