"""
Title : 부분배열 고르기
Link : https://www.acmicpc.net/problem/2104
"""

from math import log2, ceil
from sys import stdin, setrecursionlimit

input = stdin.readline
setrecursionlimit(10**6)


class SegmentTree:
    def __init__(self, N: int, seq: list) -> None:
        self.N = N
        self.seq = [0] + seq
        self.sum_tree = [0] * (1 << ceil(log2(N) + 1))
        self.min_tree = [0] * (1 << ceil(log2(N) + 1))
        self.init(1, 1, N)

    def init(self, node: int, start: int, end: int) -> None:
        if start == end:
            self.sum_tree[node] = self.seq[start]
            self.min_tree[node] = start
            return
        mid = (start + end) // 2
        self.init(node * 2, start, mid)
        self.init(node * 2 + 1, mid + 1, end)
        self.sum_tree[node] = self.sum_tree[node * 2] + self.sum_tree[node * 2 + 1]
        if self.seq[self.min_tree[node * 2]] < self.seq[self.min_tree[node * 2 + 1]]:
            self.min_tree[node] = self.min_tree[node * 2]
        else:
            self.min_tree[node] = self.min_tree[node * 2 + 1]

    def get_values(
        self, node: int, start: int, end: int, left: int, right: int
    ) -> tuple:
        if end < left or right < start:
            return (0, -1)
        if left <= start and end <= right:
            return (self.sum_tree[node], self.min_tree[node])
        mid = (start + end) // 2
        left_value, left_idx = self.get_values(node * 2, start, mid, left, right)
        right_value, right_idx = self.get_values(
            node * 2 + 1, mid + 1, end, left, right
        )
        sum_value = left_value + right_value
        if left_idx == -1 and right_idx == -1:
            return (0, -1)
        elif left_idx == -1:
            return (right_value, right_idx)
        elif right_idx == -1:
            return (left_value, left_idx)
        if self.seq[left_idx] < self.seq[right_idx]:
            return (sum_value, left_idx)
        else:
            return (sum_value, right_idx)

    def solve(self, start: int, end: int) -> int:
        if start == end:
            return self.seq[start] * self.seq[start]
        values = self.get_values(1, 1, self.N, start, end)
        if values[1] == -1:
            return 0
        sums = [
            values[0] * self.seq[values[1]],
            self.solve(start, values[1] - 1),
            self.solve(values[1] + 1, end),
        ]
        return max(sums)


if __name__ == "__main__":
    N = int(input())
    seq = list(map(int, input().split()))
    segment_tree = SegmentTree(N, seq)
    print(segment_tree.solve(1, N))

# ---------------------------------------

from sys import stdin

input = stdin.readline


def solution(seq: tuple) -> int:
    stack = []
    answer = 0
    now = 0
    for x in seq:
        left = now
        while stack and x < stack[-1][0]:
            y, left = stack.pop()
            answer = max(answer, y * (now - left))
        stack.append((x, left))
        now += x
    return max(answer, *(x * (now - left) for x, left in stack))


if __name__ == "__main__":
    N: int = int(input())
    seq: tuple = tuple(map(int, input().split()))
    print(solution(seq))
