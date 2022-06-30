import sys, math, collections
from typing import List
sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline
MIIS = lambda: map(int, input().split())

class SegmentTree:
    def __init__(self, N: int, A: List[int]) -> None:
        self.N = N
        self.A = A
        h = math.ceil(math.log2(N))
        tree_size = 1 << (h + 1)
        self.tree = [[0, 0] for _ in range(tree_size)]  # [구간 합, 최솟값 인덱스] 저장
        self.max_score = 0
        self.find_node(1, 1, N)
    
    def find_node(self, node: int, start: int, end: int) -> None:
        if start == end:
            self.tree[node][0] = self.A[start]
            self.tree[node][1] = start  # 최솟값의 인덱스 저장
            self.update(node // 2)
        else:
            mid = (start + end) // 2
            self.find_node(node * 2, start, mid)
            self.find_node(node * 2 + 1, mid + 1, end)
    
    def update(self, node: int) -> None:
        while node:
            # 구간 합 갱신
            self.tree[node][0] = self.tree[node * 2][0] + self.tree[node * 2 + 1][0]
            # 최솟값 인덱스 갱신
            left, right = self.tree[node * 2][1], self.tree[node * 2 + 1][1]
            if self.A[left] <= self.A[right]:
                self.tree[node][1] = left
            else:
                self.tree[node][1] = right
            node //= 2

    def query(self, node: int, start: int, end: int, left: int, right: int) -> int:
        if left > end or right < start:
            return [0, 0]
        if left <= start and end <= right:
            return self.tree[node]
        mid = (start + end) // 2
        left_query = self.query(node * 2, start, mid, left, right)
        right_query = self.query(node * 2 + 1, mid + 1, end, left, right)
        # 구간의 최솟값 인덱스 산출
        if self.A[left_query[1]] <= self.A[right_query[1]]:
            min_idx = left_query[1]
        else:
            min_idx = right_query[1]
        return [left_query[0] + right_query[0], min_idx]
    
    def divide(self, left: int, right: int) -> None:
        deq = collections.deque()
        deq.append((left, right))

        # 분할만 진행하며 구간 최댓값 갱신
        while deq:
            l, r = deq.popleft()
            if l > r:
                continue
            score, idx = self.query(1, 1, N, l, r)
            self.max_score = max(self.max_score, score * self.A[idx])
            deq.append((l, idx - 1))
            deq.append((idx + 1, r))


N = int(input())
A = [float('inf')] + list(MIIS())  # 더미로 최댓값 입력 (query 에서 예외처리)
segment_tree = SegmentTree(N, A)

segment_tree.divide(1, N)

print(segment_tree.max_score)