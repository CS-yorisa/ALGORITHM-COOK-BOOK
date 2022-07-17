"""
Title : 개미굴
Link : https://www.acmicpc.net/problem/14725
"""

from collections import defaultdict
from sys import stdin

input = stdin.readline


def search(depth: int, parent: str) -> str:
    global trie
    if not trie[parent]:
        return ""
    ans = ""
    for x in sorted(trie[parent]):
        ans += f"{'-' * (2 * depth)}{x}\n"
        child = f"{x}" if not parent else f"{parent} {x}"
        ans += f"{search(depth + 1, child)}"
    return ans


if __name__ == "__main__":
    N = int(input())
    trie = defaultdict(set)
    for _ in range(N):
        ants = input().strip().split()
        m = int(ants[0])
        parent = f"{ants[1]}"
        trie[""].add(parent)
        for i in range(m - 1):
            x, y = ants[1 + i], ants[2 + i]
            trie[parent].add(y)
            parent += f" {y}"
    ans = search(0, "")
    print(ans)
