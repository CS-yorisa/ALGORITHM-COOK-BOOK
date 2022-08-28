import sys

input = sys.stdin.readline
Point = tuple[int]

def ccw(p1: Point, p2: Point, p3: Point) -> int:
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)


N = int(input())

slashs = [tuple(map(int, input().split())) for _ in range(N)]
slashs.sort(key=lambda x : x[4])
answer = 0

for i in range(len(slashs)):
    sx1, sy1, ex1, ey1, w1 = slashs[i]
    cnt = 1
    for j in range(i + 1, len(slashs)):
        sx2, sy2, ex2, ey2, w2 = slashs[j]
        p1, p2, p3, p4 = (sx1, sy1), (ex1, ey1), (sx2, sy2), (ex2, ey2)
        if ccw(p1, p2, p3) * ccw(p1, p2, p4) < 0 and ccw(p3, p4, p1) * ccw(p3, p4, p2) < 0:
            cnt += 1
    answer += (w1 * cnt)

print(answer)