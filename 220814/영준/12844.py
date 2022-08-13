"""
Title : XOR
Link : https://www.acmicpc.net/problem/12844
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
        self.tree[node] = self.tree[node * 2] ^ self.tree[node * 2 + 1]

    def update_lazy(self, node: int, start: int, end: int) -> None:
        if self.lazy[node]:
            if (end - start + 1) % 2:
                self.tree[node] ^= self.lazy[node]
            if start != end:
                self.lazy[node * 2] ^= self.lazy[node]
                self.lazy[node * 2 + 1] ^= self.lazy[node]
            self.lazy[node] = 0

    def update_range(
        self, node: int, start: int, end: int, left: int, right: int, k: int
    ) -> None:
        self.update_lazy(node, start, end)
        if right < start or end < left:
            return
        if left <= start and end <= right:
            if (end - start + 1) % 2:
                self.tree[node] ^= k
            if start != end:
                self.lazy[node * 2] ^= k
                self.lazy[node * 2 + 1] ^= k
            return
        mid = self.mid(start, end)
        self.update_range(node * 2, start, mid, left, right, k)
        self.update_range(node * 2 + 1, mid + 1, end, left, right, k)
        self.tree[node] = self.tree[node * 2] ^ self.tree[node * 2 + 1]

    def query(self, node: int, start: int, end: int, left: int, right: int) -> int:
        self.update_lazy(node, start, end)
        if right < start or end < left:
            return 0
        if left <= start and end <= right:
            return self.tree[node]
        mid = (start + end) // 2
        left_xor = self.query(node * 2, start, mid, left, right)
        right_xor = self.query(node * 2 + 1, mid + 1, end, left, right)
        return left_xor ^ right_xor


if __name__ == "__main__":
    N = II()
    seq = list(MIIS())
    segment_tree = SegmentTree(N, seq)
    for _ in range(II()):
        cmd, *query = MIIS()
        if cmd == 1:
            i, j, k = query
            segment_tree.update_range(1, 1, N, i + 1, j + 1, k)
        else:
            i, j = query
            print(segment_tree.query(1, 1, N, i + 1, j + 1))
