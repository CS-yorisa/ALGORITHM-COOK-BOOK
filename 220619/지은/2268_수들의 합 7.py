import sys
input = sys.stdin.readline


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

N, M = map(int, input().split())

a = [0 for _ in range(N+1)]
tree = [0 for _ in range(4*(N+1))]


for _ in range(M):
    f, i, j = map(int, input().split())
    if f == 0:
        if i > j :
            print(Sum(tree, 1, 1, N, j, i))
        else:
            print(Sum(tree, 1, 1, N, i, j))

    else:
        update(tree, 1, 1, N, i, j - a[i])
        a[i] = j

