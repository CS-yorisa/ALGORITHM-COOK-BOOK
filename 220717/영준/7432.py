"""
Title : 디스크 트리
Link : https://www.acmicpc.net/problem/7432
"""

from collections import defaultdict
from sys import stdin

input = stdin.readline


def search(depth: int, now: str) -> str:
    global directory
    if not directory[now]:
        return ""
    ans = ""
    for child, grand_child in sorted(directory[now]):
        ans += f"{' ' * depth}{child}\n"
        ans += search(depth + 1, grand_child)
    return ans


if __name__ == "__main__":
    N = int(input())
    directory = defaultdict(set)
    for _ in range(N):
        d = tuple(input().strip().split("\\"))
        now = d[0]
        directory[""].add((now, now))
        for i in range(1, len(d)):
            before = now
            _now = d[i]
            now += f" {_now}"
            directory[before].add((_now, now))
    print(search(0, ""))
