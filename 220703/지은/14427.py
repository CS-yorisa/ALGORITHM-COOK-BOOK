import sys
input = sys.stdin.readline


def init(start, end, node):
    if start == end:
        tree[node] = start
        return tree[node]
    mid = (start+end) // 2
    tree[node] = min_index(init(start, mid, node * 2), init(mid + 1, end, node * 2 + 1))
    return tree[node]


def min_index(x, y):
    if a[x] == a[y]:
        return x if x < y else y
    return x if a[x] < a[y] else y


def update(start, end, node, index):
    if index < start or index > end or start == end:
        return tree[node]
    mid = (start+end) // 2
    tree[node] = min_index(update(start, mid, node*2, index), update(mid+1, end, node*2 + 1, index))
    return tree[node]


N = int(input())

a = list(map(int, input().split()))
tree = [0 for _ in range(4*(N+1))]

init(0, N-1, 1)

for _ in range(int(input())):
    query = list(input().split())
    if query[0] == '1':
        i, j = int(query[1]), int(query[2])
        a[i-1] = j
        update(0, N-1, 1, i-1)

    else:
        print(tree[1]+1)

