'''
레이지 프로퍼게이션 문제
Lazy 배열을 하나 더 선언하고 느리게 갱신해야 logN으로 해결 가능
'''

import sys
input = sys.stdin.readline


def init(index, start, end):
    if start == end:
        tree[index] = arr[start - 1]
        return
    mid = (start + end) // 2
    init(index * 2, start, mid)
    init(index*2+1, mid + 1, end)
    tree[index] = tree[index * 2] + tree[index * 2 + 1]


def Sum(index, start, end, left, right):
    update_lazy(index, start, end)
    # 범위를 벗어나는 경우 리턴 0
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[index]
    mid = (start + end)//2
    return Sum(index * 2, start, mid, left, right) + Sum(index * 2 + 1, mid + 1, end, left, right)


def update_seg(index, start, end, left, right, diff):
    update_lazy(index, start, end)
    if end < left or right < start :
        return

    if left <= start and end <= right :
        tree[index] += (end - start + 1)*diff
        if start != end:
            lazy[index * 2] += diff
            lazy[index * 2 + 1] += diff
        return

    mid = (start + end) // 2
    update_seg(index * 2, start, mid, left, right, diff)
    update_seg(index * 2 + 1, mid +1, end, left, right, diff)
    tree[index] = tree[index * 2] + tree[index * 2 +1]


def update_lazy(index, start, end):
    if lazy[index]:
        tree[index] += (end - start + 1) * lazy[index]

        if start != end:
            lazy[index * 2] += lazy[index]
            lazy[index * 2 + 1] += lazy[index]
        lazy[index] = 0


# M : 수의 변경이 일어나는 횟수
# K : 구간의 합을 구한느 횟수
N, M, K = map(int, input().split())

arr = [int(input()) for _ in range(N)]

# 배열 길이 4N
tree = [0 for _ in range(4*N)]
lazy = [0 for _ in range(4*N)]

init(1, 1, N)

for _ in range(M+K):
    data = list(map(int, input().split()))
    if data[0] == 1:
        _, b, c, d = data
        update_seg(1, 1, N, b, c, d)
    else:
        _, b, c = data
        print(Sum(1, 1, N, b, c))

