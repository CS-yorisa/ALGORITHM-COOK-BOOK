import sys

input = sys.stdin.readline
MIIS = lambda: map(int, input().split())
Point = tuple[int]

def ccw(p1: Point, p2: Point, p3: Point) -> int:
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)

def is_intersection(p1: Point, p2: Point, plt: Point, plb: Point, prt: Point, prb: Point) -> bool:
    cnt: int = 0
    # 직사각형의 모든 변을 체크
    for p3, p4 in ((plt, plb), (plt, prt), (prt, prb), (plb, prb)):
        ccw1, ccw2, ccw3, ccw4 = ccw(p1, p2, p3), ccw(p1, p2, p4), ccw(p3, p4, p1), ccw(p3, p4, p2)
        if ccw1 * ccw2 <= 0 and ccw3 * ccw4 <= 0:
            # 일직선 상에 있는 경우 포개진 상태인지 확인
            if (p1[0] == p2[0] == p3[0] == p4[0]) or (p1[1] == p2[1] == p3[1] == p4[1]):
                if (max(p1[0], p2[0]) >= min(p3[0], p4[0]) and max(p3[0], p4[0]) >= min(p1[0], p2[0]))\
                    and (max(p1[1], p2[1]) >= min(p3[1], p4[1]) and max(p3[1], p4[1]) >= min(p1[1], p2[1])):
                    # 점 하나만 접하는 경우
                    if (max(p1[0], p2[0]) == min(p3[0], p4[0]) or max(p3[0], p4[0]) == min(p1[0], p2[0]))\
                        and (max(p1[1], p2[1]) == min(p3[1], p4[1]) or max(p3[1], p4[1]) == min(p1[1], p2[1])):
                        return 1
                    else:
                        return 4
            else:
                cnt += 1
    for p in (plt, plb, prt, prb):
        # 직사각형의 꼭짓점에 점이 위치
        if p in (p1, p2):
            cnt -= 1
            continue
        # 선분이 직사각형의 꼭짓점을 지나는 경우
        if ((min(p1[0], p2[0]) <= p[0]) and (max(p1[0], p2[0]) >= p[0])) and ((min(p1[1], p2[1]) <= p[1]) and (max(p1[1], p2[1]) >= p[1])):
            if (p[1] - p1[1]) != 0 and (p2[1] - p1[1]) != 0:
                slope1 = (p[0] - p1[0]) / (p[1] - p1[1])
                slope2 = (p2[0] - p1[0]) / (p2[1] - p1[1])
                if slope1 == slope2:
                    cnt -= 1
    if cnt >= 2:
        return 2
    else:
        return cnt


T: int = int(input())

for _ in range(T):
    xl, yb, xr, yt = MIIS()
    x1, y1, x2, y2 = MIIS()

    # 직사각형 내부에 선분의 점이 전부 포함
    if ((xl < x1 < xr) and (yb < y1 < yt)) and ((xl < x2 < xr) and (yb < y2 < yt)):
        print(0)
        continue

    # 직사각형 내부, 직사각형 경계에 각각 점 위치
    if ((xl < x1 < xr) and (yb < y1 < yt)) and ((xl <= x2 <= xr) and (yb <= y2 <= yt)):
        print(1)
        continue
    if ((xl <= x1 <= xr) and (yb <= y1 <= yt)) and ((xl < x2 < xr) and (yb < y2 < yt)):
        print(1)
        continue

    # 직사각형 내부, 직사각형 외부에 각각 점 위치
    if ((xl < x1 < xr) and (yb < y1 < yt)) or ((xl < x2 < xr) and (yb < y2 < yt)):
        print(1)
        continue

    # 직사각형 경계에 점 2개 위치
    if ((xl <= x1 <= xr) and (yb <= y1 <= yt)) and ((xl <= x2 <= xr) and (yb <= y2 <= yt)):
        # 직선이 평행한 경우
        if (x1 == x2) or (y1 == y2):
            print(4)
        else:
            print(2)
        continue

    print(is_intersection((x1, y1), (x2, y2), (xl, yt), (xl, yb), (xr, yt), (xr, yb)))