"""
Title : LCS 3
Link : https://www.acmicpc.net/problem/1958
"""

from sys import stdin

input = stdin.readline


if __name__ == "__main__":
    S1, S2, S3 = input().strip(), input().strip(), input().strip()
    l1, l2, l3 = len(S1), len(S2), len(S3)
    dp = [[[0] * (l3 + 1) for _ in range(l2 + 1)] for _ in range(l1 + 1)]
    for i, x in enumerate(S1):
        for j, y in enumerate(S2):
            for k, z in enumerate(S3):
                if x == y == z:
                    dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1
                else:
                    dp[i][j][k] = max(dp[i - 1][j][k], dp[i][j - 1][k], dp[i][j][k - 1])
    print(dp[l1 - 1][l2 - 1][l3 - 1])
