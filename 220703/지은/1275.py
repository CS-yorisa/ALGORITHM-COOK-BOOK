import sys
input = sys.stdin.readline


def init(start, end, node):
    if start == end:
        tree[node] = arr[start]
        return tree[node]
    mid = (start+end) // 2
    tree[node] = init(start, mid, node * 2) + init(mid + 1, end, node * 2 + 1)
    return tree[node]


def Sum(tree, node, start, end, left, right):
    # 범위를 벗어나는 경우 리턴 0
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    return Sum(tree, node*2, start, (start + end) // 2, left, right) + Sum(tree, node * 2 + 1, (start + end) // 2+1, end, left, right)


def update(tree, node, start, end, index, val):
    if index < start or index > end:
        return
    tree[node] += val
    if start != end :
        update(tree, node * 2, start, (start + end) // 2, index, val)
        update(tree, node * 2 + 1, (start + end) // 2 + 1, end, index, val)


N, Q = map(int, input().split())

arr = list(map(int, input().split()))
tree = [0 for _ in range(4*(N+1))]

init(0, N-1, 1)

for _ in range(Q):
    x, y, a, b = map(int, input().split())
    if x <= y:
        print(Sum(tree,1,0,N-1, x-1, y-1))
    else:
        print(Sum(tree,1,0,N-1, y-1, x-1))

    update(tree, 1, 1, N, a, b - arr[a-1])
    arr[a-1] = b



