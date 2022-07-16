import sys
input = sys.stdin.readline

months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]


def dayTime(D, T):
    _, new_m, new_d = map(int, D.split('-'))
    new_d += sum(months[:new_m])
    h, m = T.split(":")
    return new_d * 60 * 24 + int(h) * 60 + int(m)

N, L, F = input().strip().split()
N, F = int(N), int(F)

a, b = L.split('/')
c, d = b.split(':')

duration = int(a)*24*60 + int(c)*60 + int(d)

rent_list = {}
ans_list = {}
for _ in range(N):
    D, T, P, M = input().strip().split()
    time = dayTime(D, T)
    if (P, M) in rent_list:
        return_time = time - rent_list.pop((P, M))
        if return_time > duration:
            if M in ans_list :
                ans_list[M] += F*(return_time - duration)
            else :
                ans_list[M] = F*(return_time - duration)

    else:
        rent_list[(P, M)] = time

if ans_list:
    for k in sorted(ans_list.keys()):
        print(k, ans_list[k])
else:
    print(-1)