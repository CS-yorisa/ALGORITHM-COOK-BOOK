"""
Title : 교차
Linke : https://www.acmicpc.net/problem/6439
"""

from sys import stdin

input = stdin.readline


Point = tuple[int]


def check_inside(A: Point, B: Point, LB: Point, RT: Point) -> bool:
    xl, xr = min(LB[0], RT[0]), max(LB[0], RT[0])
    yb, yt = min(LB[1], RT[1]), max(LB[1], RT[1])
    if xl <= A[0] <= xr and yb <= A[1] <= yt:
        if xl <= B[0] <= xr and yb <= B[1] <= yt:
            return True
    return False


def chceck_line(A: Point, B: Point, C: Point, D: Point) -> bool:
    tmp1 = get_ccw(A, B, C) * get_ccw(A, B, D)
    tmp2 = get_ccw(C, D, A) * get_ccw(C, D, B)
    if not tmp1 and not tmp2:
        if A <= D and B >= C:
            return True
        return False
    if tmp1 <= 0 and tmp2 <= 0:
        return True
    return False


def get_ccw(A: Point, B: Point, C: Point) -> int:
    ccw = (B[0] - A[0]) * (C[1] - A[1]) - (B[1] - A[1]) * (C[0] - A[0])
    return 0 if not ccw else 1 if ccw > 0 else -1


if __name__ == "__main__":
    for _ in range(int(input())):
        x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
        A, B = (x1, y1), (x2, y2)
        if A > B:
            A, B = B, A
        X, Y, Z, W = (x3, y3), (x3, y4), (x4, y4), (x4, y3)
        if check_inside(A, B, Y, W):
            print("T")
            continue
        for C, D in ((Y, X), (Y, Z), (Z, W), (X, W)):
            if C > D:
                C, D = D, C
            if chceck_line(A, B, C, D):
                print("T")
                break
        else:
            print("F")
