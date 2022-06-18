"""
Title : 수들의 합 7
Link : https://www.acmicpc.net/problem/2268
"""

from math import ceil, log2
from sys import stdin

input = stdin.readline
MIIS = lambda: map(int, input().split())


class SegmentTree:
    def __init__(self, N: int) -> None:
        self.N = N
        self.seq = [0] * (N + 1)
        self.tree = [0] * (1 << (ceil(log2(N)) + 1))
        self.seq_to_tree = [0] * (N + 1)
        self.make_link_list(1, 1, self.N)

    def make_link_list(self, node: int, left: int, right: int):
        if left >= right:
            self.seq_to_tree[left] = node
            return
        mid = (left + right) // 2
        self.make_link_list(node * 2, left, mid)
        self.make_link_list(node * 2 + 1, mid + 1, right)

    def find_sum(self, node: int, start: int, end: int, left: int, right: int) -> int:
        if right < start or end < left:
            return 0
        if left <= start and end <= right:
            return self.tree[node]
        mid = (start + end) // 2
        return self.find_sum(node * 2, start, mid, left, right) + self.find_sum(
            node * 2 + 1, mid + 1, end, left, right
        )

    def update(self, node: int, value: int) -> None:
        node = self.seq_to_tree[node]
        self.tree[node] = value
        node //= 2
        while node:
            self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]
            node //= 2


if __name__ == "__main__":
    N, M = MIIS()
    segment_tree = SegmentTree(N)
    for _ in range(M):
        cmd, x, y = MIIS()
        if not cmd:
            if x > y:
                x, y = y, x
            print(segment_tree.find_sum(1, 1, N, x, y))
        else:
            segment_tree.update(x, y)
