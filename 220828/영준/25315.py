"""
Title : N수매화검법
Link : https://www.acmicpc.net/problem/25315
"""

from sys import stdin

input = stdin.readline
Point = tuple[int]


def get_ccw(A: Point, B: Point, C: Point) -> int:
    ccw = (B[0] - A[0]) * (C[1] - A[1]) - (B[1] - A[1]) * (C[0] - A[0])
    return 0 if not ccw else 1 if ccw > 0 else -1


if __name__ == "__main__":
    N = int(input())
    actions = []
    for _ in range(N):
        sx, sy, ex, ey, w = map(int, input().split())
        actions.append(((sx, sy), (ex, ey), w))
    actions.sort(key=lambda x: x[2])
    ans = 0
    for idx, (S1, E1, w1) in enumerate(actions):
        count = 1
        for i in range(idx + 1, N):
            S2, E2, _ = actions[i]
            tmp1 = get_ccw(S1, E1, S2) * get_ccw(S1, E1, E2)
            tmp2 = get_ccw(S2, E2, S1) * get_ccw(S2, E2, E1)
            if tmp1 < 0 and tmp2 < 0:
                count += 1
        ans += count * w1
    print(ans)
