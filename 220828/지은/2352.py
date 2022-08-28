import sys
from bisect import bisect_left
input = sys.stdin.readline

N = input()
data = list(map(int, input().split()))
link = []
for d in data:
    if not link or link[-1] < d:
        link.append(d)
    else:
        link[bisect_left(link, d)] = d
print(len(link))