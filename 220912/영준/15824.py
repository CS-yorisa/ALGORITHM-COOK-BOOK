"""
Titl : 너 봄에는 캡사이신이 맛있단다
Link : https://www.acmicpc.net/problem/15824
"""

from sys import stdin

input = stdin.readline


if __name__ == "__main__":
    N: int = int(input())
    menus: list[int] = list(map(int, input().split()))
    menus.sort()

    mod: int = 1_000_000_007
    combs: int = 1
    ans: int = 0

    for i in range(N):
        ans = (ans + (menus[i] - menus[-1 - i]) * (combs - 1)) % mod
        combs = (combs * 2) % mod
    print(ans)
