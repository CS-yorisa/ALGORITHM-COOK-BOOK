import sys
from typing import List, Tuple

input = sys.stdin.readline
Point = Tuple[int]

# (x2 - x1)(y3 - y1) - (x3 - x1)(y2 - y1) = (x1y2 + x2y3 + x3y1) - (x2y1 + x3y2 + x1y3)
def ccw(p1: Point, p2: Point, p3: Point) -> int:
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return (x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3)

points: List[Point] = [tuple(map(int, input().split())) for _ in range(3)]

answer = ccw(*points)

if answer > 0:
    print(1)
elif answer < 0:
    print(-1)
else:
    print(0)