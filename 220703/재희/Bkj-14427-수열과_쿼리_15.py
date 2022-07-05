import sys, math
from typing import List

input = sys.stdin.readline
MIIS = lambda: map(int, input().split())

class SegmentTree:
    def __init__(self, N: int, A: List[int]) -> None:
        self.N = N
        self.A = A
        h = math.ceil(math.log2(N))
        tree_size = 1 << (h + 1)
        self.tree = [0] * tree_size
        self.node_index = [0] * (N + 1)  # 수열의 노드 인덱스 저장
        self.find_node_index(1, 1, N)
    
    def find_node_index(self, node: int, start: int, end: int) -> None:
        if start == end:
            self.node_index[start] = node
            self.tree[node] = start
            self.update(node // 2)  # 리프노드부터 트리 수정
        else:
            mid = (start + end) // 2
            self.find_node_index(node * 2, start, mid)
            self.find_node_index(node * 2 + 1, mid + 1, end)
    
    def update(self, node: int) -> None:
        while node:
            left, right = self.A[self.tree[node * 2]], self.A[self.tree[node * 2 + 1]]
            if left > right:
                self.tree[node] = self.tree[node * 2 + 1]
            elif left < right:
                self.tree[node] = self.tree[node * 2]
            # 값이 같은 경우 인덱스가 작은 것 저장
            else:
                self.tree[node] = min(self.tree[node * 2], self.tree[node * 2 + 1])
            node //= 2


N = int(input())
A = [0] + list(MIIS())
segment_tree = SegmentTree(N, A)
M = int(input())

for _ in range(M):
    query = list(MIIS())
    if query[0] == 1:
        q, i, v = query
        segment_tree.A[i] = v
        segment_tree.update(segment_tree.node_index[i] // 2)
    else:
        print(segment_tree.tree[1])