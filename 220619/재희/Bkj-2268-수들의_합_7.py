import sys, math
input = sys.stdin.readline

# 리프 노드의 index 저장
def find_index(node: int, start: int, end: int) -> None:
    global node_index
    if start == end:
        node_index[start] = node
    else:
        find_index(node * 2, start, (start + end) // 2)
        find_index(node * 2 + 1, (start + end) // 2 + 1, end)

# 구간 합 (Sum 함수)
def query(node: int, start: int, end: int, left: int, right: int) -> int:
    global tree
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    return query(node * 2, start, (start + end) // 2, left, right) + query(node * 2 + 1, (start + end) // 2 + 1, end, left, right)

# 숫자 변경 (Modify 함수)
def update(node: int) -> None:
    global tree
    while node:
        tree[node] = tree[node * 2] + tree[node * 2 + 1]
        node //= 2

N, M = map(int, input().split())
# 높이 H = log2 N
h = math.ceil(math.log2(N))
# 배열의 크기 = (2 ** (H + 1)) - 1
tree_size = 1 << (h + 1)
tree = [0] * tree_size
node_index = [0] * (N + 1)

find_index(1, 1, N)

for _ in range(M):
    f, a, b = map(int, input().split())
    if f == 0:
        # 
        if a > b:
            a, b = b, a
        print(query(1, 1, N, a, b))
    else:
        tree[node_index[a]] = b
        update(node_index[a] // 2)