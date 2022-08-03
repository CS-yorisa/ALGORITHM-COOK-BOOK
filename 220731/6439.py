t = int(input())


def ccw(a, b, c):
    S = (b[0] - a[0])*(c[1] - a[1]) - (b[1] - a[1])*(c[0] - a[0])
    if S > 0:
        return 1
    elif S < 0:
        return -1
    else:
        return 0


def cross_check(a, b, c, d):
    if ccw(a, b, c) * ccw(a, b, d) <=0 and \
       ccw(c, d, a) * ccw(c, d, b) <=0 :
        if (a[0] < c[0] and a[0] < d[0] and b[0] < c[0] and b[0] < d[0]) or \
           (c[0] < a[0] and c[0] < b[0] and d[0] < a[0] and d[0] < b[0]) :
            return False
        if (a[1] < c[1] and a[1] < d[1] and b[1] < c[1] and b[1] < d[1]) or \
           (c[1] < a[0] and c[1] < b[1] and d[1] < a[1] and d[1] < b[1]) :
            return False
        return True
    return False


for _ in range(t):
    xs, ys, xe, ye, xl, yt, xr, yb = map(int, input().strip().split())
    X, Y = [xs, ys], [xe, ye]
    if X > Y :
        X, Y = Y, X

    A = [min(xl, xr), min(yt, yb)]
    B = [min(xl, xr), max(yt, yb)]
    C = [max(xl, xr), min(yt, yb)]
    D = [max(xl, xr), max(yt, yb)]

    if cross_check(X, Y, A, B) or cross_check(X, Y, B, D) or cross_check(X, Y, D, C) or cross_check(X, Y, C, A):
        print('T')
    else:
        if (A[0] < xs and A[0] < xe and xs < C[0] and xe < C[0]) and (A[1] < ys and A[1] < ye and ys < D[1] and ye < D[1]):
            print('T')
        else:
            print('F')


