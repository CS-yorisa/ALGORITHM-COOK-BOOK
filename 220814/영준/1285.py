"""
Title : 동전 뒤집기
Link : https://www.acmicpc.net/problem/1285
"""

from sys import stdin

input = stdin.readline


def reverse_line(N: int, line: list[int]) -> list[int]:
    new_line = [0] * N
    for idx, x in enumerate(line):
        if not x:
            new_line[idx] = 1
    return new_line


if __name__ == "__main__":
    N = int(input())
    coins = [[0] * N for _ in range(N)]
    for i in range(N):
        line = input().strip()
        for j, x in enumerate(line):
            if x == "H":
                coins[i][j] = 1
    ans = 500
    for bit in range(1 << N):
        tmp = [line[::] for line in coins]
        for x in range(N):
            if bit & (1 << x):
                tmp[x] = reverse_line(N, tmp[x])
        count = 0
        tmp = list(zip(*tmp))
        for line in tmp:
            c = sum(line)
            count += min(c, N - c)
        if ans > count:
            ans = count
    print(ans)
