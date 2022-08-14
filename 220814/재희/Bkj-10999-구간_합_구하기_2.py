import sys, math

input = sys.stdin.readline
MIIS = lambda: map(int, input().split())

class SegmentTree:
    def __init__(self, N: int, A: list[int]) -> None:
        self.array = A
        h = math.ceil(math.log2(N))
        tree_size = 1 << (h + 1)
        self.tree = [0] * tree_size
        self.lazy = [0] * tree_size
        self.node_init(1, 1, N)
    
    def node_init(self, node: int, start: int, end: int) -> int:
        if start == end:
            self.tree[node] = self.array[start]
            return self.tree[node]
        mid = (start + end) // 2
        self.tree[node] = self.node_init(node * 2, start, mid) + self.node_init(node * 2 + 1, mid + 1, end)
        return self.tree[node]
    
    def update_lazy(self, node: int, start: int, end: int) -> None:
        if self.lazy[node] != 0:
            self.tree[node] += (end - start + 1) * self.lazy[node]
            if start != end:
                self.lazy[node * 2] += self.lazy[node]
                self.lazy[node * 2 + 1] += self.lazy[node]
            self.lazy[node] = 0
    
    def update_range(self, node: int, start: int, end: int, left: int, right: int, d: int) -> None:
        self.update_lazy(node, start, end)
        if left > end or right < start:
            return
        if left <= start and end <= right:
            self.tree[node] += (end - start + 1) * d
            if start != end:
                self.lazy[node * 2] += d
                self.lazy[node * 2 + 1] += d
            return
        mid = (start + end) // 2
        self.update_range(node * 2, start, mid, left, right, d)
        self.update_range(node * 2 + 1, mid + 1, end, left, right, d)
        self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]
    
    def query(self, node: int, start: int, end: int, left: int, right: int) -> int:
        self.update_lazy(node, start, end)
        if left > end or right < start:
            return 0
        if left <= start and end <= right:
            return self.tree[node]
        mid = (start + end) // 2
        return self.query(node * 2, start, mid, left, right) + self.query(node * 2 + 1, mid + 1, end, left, right)


N, M, K = MIIS()
A: list[int] = [0] + [int(input()) for _ in range(N)]
segment_tree = SegmentTree(N, A)

for _ in range(M + K):
    query, *q = map(int, input().split())
    if query == 1:
        left, right, d = q
        if d:
            segment_tree.update_range(1, 1, N, left, right, d)
    else:
        left, right = q
        print(segment_tree.query(1, 1, N, left, right))