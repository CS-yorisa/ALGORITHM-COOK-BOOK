"""
Title : 꿈틀꿈틀 호석 애벌레 - 효율성
Link : https://www.acmicpc.net/problem/20181
"""

from sys import stdin

input = stdin.readline
MIIS = lambda: map(int, input().split())


if __name__ == "__main__":
    N, K = MIIS()
    feeds = list(MIIS()) + [0]
    feeds_status = [[0, 0] for _ in range(N)]
    left = right = 0
    feed_sum = feeds[0]
    while right < N:
        if feed_sum >= K:
            feeds_status[left] = [right, feed_sum]
            feed_sum -= feeds[left]
            left += 1
            if right < left:
                right = left
                feed_sum += feeds[right]
        else:
            right += 1
            feed_sum += feeds[right]
    dp = [0] * (N + 1)
    for i in range(N - 1, -1, -1):
        if feeds_status == [0, 0]:
            continue
        idx, s = feeds_status[i]
        dp[i] = max(dp[i + 1], dp[idx + 1] + s - K)
    print(dp[0])
