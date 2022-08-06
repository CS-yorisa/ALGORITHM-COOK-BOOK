import sys

input = sys.stdin.readline
Point = tuple[int]

# (x2 - x1)(y3 - y1) - (x3 - x1)(y2 - y1) = (x1y2 + x2y3 + x3y1) - (x2y1 + x3y2 + x1y3)
def ccw(p1: Point, p2: Point, p3: Point) -> int:
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return (x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3)

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

p1, p2, p3, p4 = (x1, y1), (x2, y2), (x3, y3), (x4, y4)

# 세 점이 동일선상에 있는 경우는 없음 -> 값이 0 인 경우는 제외
if ccw(p1, p2, p3) * ccw(p1, p2, p4) < 0 and ccw(p3, p4, p1) * ccw(p3, p4, p2) < 0:
    print(1)
else:
    print(0)