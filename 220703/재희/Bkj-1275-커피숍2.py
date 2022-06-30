import sys, math
from typing import List

input = sys.stdin.readline
MIIS = lambda: map(int, input().split())

class SegmentTree:
    def __init__(self, N: int, array: List[int]) -> None:
        self.N = N
        self.array = array
        h = math.ceil(math.log2(N))
        tree_size = 1 << (h + 1)
        self.tree = [0] * tree_size
        self.node_index = [0] * (N + 1)  # 수열의 노드 인덱스 저장
        self.find_node_index(1, 1, N)
    
    def find_node_index(self, node: int, start: int, end: int) -> None:
        if start == end:
            self.node_index[start] = node
            self.tree[node] = self.array[start]
            self.update(node // 2)
        else:
            mid = (start + end) // 2
            self.find_node_index(node * 2, start, mid)
            self.find_node_index(node * 2 + 1, mid + 1, end)
    
    def query(self, node: int, start: int, end: int, left: int, right: int) -> int:
        if left > end or right < start:
            return 0
        if left <= start and end <= right:
            return self.tree[node]
        mid = (start + end) // 2
        return self.query(node * 2, start, mid, left, right) + self.query(node * 2 + 1, mid + 1, end, left, right)
        
    def update(self, node: int) -> None:
        while node:
            self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]
            node //= 2

N, Q = MIIS()
array = [0] + list(MIIS())
segment_tree = SegmentTree(N, array)

for _ in range(Q):
    x, y, a, b = MIIS()
    if x > y:
        x, y = y, x
    # 구간 합을 출력한 뒤 수 변경
    print(segment_tree.query(1, 1, N, x, y))
    segment_tree.tree[segment_tree.node_index[a]] = b
    segment_tree.update(segment_tree.node_index[a] // 2)