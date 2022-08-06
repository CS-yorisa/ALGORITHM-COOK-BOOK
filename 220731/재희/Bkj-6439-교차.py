import sys

input = sys.stdin.readline
Point = tuple[int]

def ccw(p1: Point, p2: Point, p3: Point) -> int:
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return (x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3)

def is_intersection(p1: Point, p2: Point, plt: Point, plb: Point, prt: Point, prb: Point) -> bool:
    # 직사각형의 모든 변을 체크
    for p3, p4 in ((plt, plb), (plt, prt), (prt, prb), (plb, prb)):
        ccw1, ccw2, ccw3, ccw4 = ccw(p1, p2, p3), ccw(p1, p2, p4), ccw(p3, p4, p1), ccw(p3, p4, p2)
        if ccw1 * ccw2 <= 0 and ccw3 * ccw4 <= 0:
            # 일직선 상에 있는 경우 포개진 상태인지 확인
            if ccw1 * ccw2 == 0 and ccw3 * ccw4 == 0:
                if (max(p1[0], p2[0]) >= min(p3[0], p4[0]) and max(p3[0], p4[0]) >= min(p1[0], p2[0]))\
                    and (max(p1[1], p2[1]) >= min(p3[1], p4[1]) and max(p3[1], p4[1]) >= min(p1[1], p2[1])):
                    return True
            else:
                return True
    return False


T = int(input())

for _ in range(T):
    lxs, lys, lxe, lye, x1, y1, x2, y2 = map(int, input().split())
    xl, xr = min(x1, x2), max(x1, x2)
    yb, yt = min(y1, y2), max(y1, y2)

    # 직사각형 내부에 선분의 점이 하나라도 포함
    if ((xl <= lxs <= xr) and (yb <= lys <= yt)) or ((xl <= lxe <= xr) and (yb <= lye <= yt)):
        print('T')
        continue

    if is_intersection((lxs, lys), (lxe, lye), (xl, yt), (xl, yb), (xr, yt), (xr, yb)):
        print('T')
    else:
        print('F')