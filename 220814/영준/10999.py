"""
Title : 구간 합 구하기 2
Link : https://www.acmicpc.net/problem/10999
"""

from math import ceil, log2
from sys import stdin

input = stdin.readline
II = lambda: int(input())
MIIS = lambda: map(int, input().split())


class SegmentTree:
    def __init__(self, N: int, seq: list[int]) -> None:
        self.N = N
        self.seq = [0] + seq
        self.tree = [0] * (1 << (ceil(log2(N)) + 1))
        self.lazy = [0] * (1 << (ceil(log2(N)) + 1))
        self.init_tree(1, 1, N)

    def mid(self, start: int, end: int) -> int:
        return (start + end) // 2

    def init_tree(self, node: int, start: int, end: int) -> None:
        if start >= end:
            self.tree[node] = self.seq[start]
            return
        mid = self.mid(start, end)
        self.init_tree(node * 2, start, mid)
        self.init_tree(node * 2 + 1, mid + 1, end)
        self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]

    def update_lazy(self, node: int, start: int, end: int) -> None:
        if self.lazy[node]:
            self.tree[node] += (end - start + 1) * self.lazy[node]
            if start != end:
                self.lazy[node * 2] += self.lazy[node]
                self.lazy[node * 2 + 1] += self.lazy[node]
            self.lazy[node] = 0

    def update_range(
        self, node: int, start: int, end: int, left: int, right: int, diff: int
    ) -> None:
        self.update_lazy(node, start, end)
        if right < start or end < left:
            return
        if left <= start and end <= right:
            self.tree[node] += (end - start + 1) * diff
            if start != end:
                self.lazy[node * 2] += diff
                self.lazy[node * 2 + 1] += diff
            return
        mid = self.mid(start, end)
        self.update_range(node * 2, start, mid, left, right, diff)
        self.update_range(node * 2 + 1, mid + 1, end, left, right, diff)
        self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]

    def query(self, node: int, start: int, end: int, left: int, right: int) -> int:
        self.update_lazy(node, start, end)
        if right < start or end < left:
            return 0
        if left <= start and end <= right:
            return self.tree[node]
        mid = self.mid(start, end)
        left_sum = self.query(node * 2, start, mid, left, right)
        right_sum = self.query(node * 2 + 1, mid + 1, end, left, right)
        return left_sum + right_sum


if __name__ == "__main__":
    N, M, K = MIIS()
    seq = [II() for _ in range(N)]
    segment_tree = SegmentTree(N, seq)
    for _ in range(M + K):
        cmd, *nums = MIIS()
        if cmd == 1:
            b, c, d = nums
            segment_tree.update_range(1, 1, N, b, c, d)
        else:
            b, c = nums
            print(segment_tree.query(1, 1, N, b, c))
