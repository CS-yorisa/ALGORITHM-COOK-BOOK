import sys
input = sys.stdin.readline


def ccw(x1, y1, x2, y2, x3, y3):
    result = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
    if result == 0:
        return 0
    elif result < 0:
        return - 1
    elif result > 0:
        return 1


def isCcw(x1, y1, x2, y2, x3, y3, x4, y4):
    ab = ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4)
    cd = ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2)

    if ab == 0 and cd == 0:
        if x1 + y1 > x2 + y2 :
            x1, y1, x2, y2 = x2, y2, x1, y1
        if x3 + y3 > x4 + y4 :
            x3, y3, x4, y4 = x4, y4, x3, y3

        return x1 + y1 <= x4 + y4 and x3 + y3 <= x2 + y2

    return ab <= 0 and cd <= 0


N = int(input())
data = []
for _ in range(N):
    a,b,c,d,e = map(int, input().split())
    data.append([e, a, b, c, d])

data.sort()
ans = 0

for i in range(N):
    cnt = 1
    for j in range(i+1, N):
        x1, y1, x2, y2 = data[i][1], data[i][2], data[i][3], data[i][4]
        x3, y3, x4, y4 = data[j][1], data[j][2], data[j][3], data[j][4]

        if isCcw(x1, y1, x2, y2, x3, y3, x4, y4):
            cnt += 1

    ans += data[i][0] * cnt

print(ans)

