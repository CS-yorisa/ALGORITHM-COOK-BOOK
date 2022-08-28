import sys, bisect

input = sys.stdin.readline

n = int(input())
ports: list[int] = list(map(int, input().split()))

dp: list[int] = [ports[0]]

for i in range(n):
    if ports[i] > dp[-1]:
        dp.append(ports[i])
    else:
        idx = bisect.bisect_left(dp, ports[i])
        dp[idx] = ports[i]

print(len(dp))