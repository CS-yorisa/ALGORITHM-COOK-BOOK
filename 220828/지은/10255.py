import sys

input = sys.stdin.readline


def ccw(x1, y1, x2, y2, x3, y3):
    result = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
    if result == 0:
        return 0
    elif result < 0:
        return -1
    elif result > 0:
        return 1


def isCcw(x1, y1, x2, y2, x3, y3, x4, y4):
    ab = ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4)
    cd = ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2)

    if ab <= 0 and cd <= 0:
        if (x1 < x3 and x1 < x4 and x2 < x3 and x2 < x4) or (x3 < x1 and x3 < x2 and x4 < x1 and x4 < x2):
            return False
        if (y1 < y3 and y1 < y4 and y2 < y3 and y2 < y4) or (y3 < y1 and y3 < y2 and y4 < y1 and y4 < y2):
            return False
        return True
    return False



def isCcs_point(x1, y1, x2, y2, x3, y3, x4, y4):
    ab = ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4)
    cd = ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2)
    if ab == 0 and cd <= 0:
        return True
    return False


def isCcw_line(x1, y1, x2, y2, x3, y3, x4, y4):
    ab = ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4)
    cd = ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2)
    if ab < 0 and cd <= 0:
        return True
    return False


for dg in range(int(input())):
    xmin, ymin, xmax, ymax = map(int, input().split())
    r1 = xmin, ymin
    r2 = xmin, ymax
    r3 = xmax, ymin
    r4 = xmax, ymax

    x1, y1, x2, y2 = map(int, input().split())
    if x1 > x2:
        x1, y1, x2, y2 = x2, y2, x1, y1

    # 교점 없음
    isNone = True
    if isCcw(x1, y1, x2, y2, r1[0], r1[1], r2[0], r2[1]) or isCcw(x1, y1, x2, y2, r2[0], r2[1], r4[0], r4[1]) or isCcw(x1, y1, x2, y2, r4[0], r4[1], r3[0], r3[1]) or isCcw(x1, y1, x2, y2, r3[0], r3[1], r1[0], r1[1]):
        isNone = False

    if isNone:
        print(0)
        continue

    if x1 == x2 == xmin:
        if ((y1 < ymax) and (y2 > ymin)) or ((y2 < ymax) and (y1 > ymin)):
            print(4)
            continue

    elif x1 == x2 == xmax:
        if ((y1 < ymax) and (y2 > ymin)) or ((y2 < ymax) and (y1 > ymin)):
            print(4)
            continue

    elif y1 == y2 == ymin:
        if ((x1 < xmax) and (x2 > xmin)) or ((x2 < xmax) and (x1 > xmin)):
            print(4)
            continue

    elif y1 == y2 == ymax:
        if ((x1 < xmax) and (x2 > xmin)) or ((x2 < xmax) and (x1 > xmin)):
            print(4)
            continue

    line = point = 0

    if isCcw_line(x1, y1, x2, y2, r1[0], r1[1], r2[0], r2[1]):
        line += 1
    if isCcw_line(x1, y1, x2, y2, r2[0], r2[1], r4[0], r4[1]):
        line += 1
    if isCcw_line(x1, y1, x2, y2, r4[0], r4[1], r3[0], r3[1]):
        line += 1
    if isCcw_line(x1, y1, x2, y2, r3[0], r3[1], r1[0], r1[1]):
        line += 1

    if isCcs_point(x1, y1, x2, y2, r1[0], r1[1], r2[0], r2[1]):
        point += 1
    if isCcs_point(x1, y1, x2, y2, r2[0], r2[1], r4[0], r4[1]) :
        point += 1
    if isCcs_point(x1, y1, x2, y2, r4[0], r4[1], r3[0], r3[1]):
        point += 1
    if isCcs_point(x1, y1, x2, y2, r3[0], r3[1], r1[0], r1[1]):
        point += 1

    print(line + point//2)