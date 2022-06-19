import sys
import heapq

input = sys.stdin.readline

INF = float('inf')

N, M = map(int, input().split())
dist = [INF for _ in range(N+1)]
line = [[] for _ in range(N+1)]
ans = [0 for _ in range(N+1)]

for _ in range(M):
    A, B, C = map(int, input().split())
    line[A].append([B, C])
    line[B].append([A, C])

# 힙큐 이용 다익스트라 구현
q = []
dist[1] = 0
heapq.heappush(q, (0, 1))
while q:
    d, now = heapq.heappop(q)
    for next_comp, next_d in line[now]:
        cost = d + next_d
        if cost < dist[next_comp]:
            dist[next_comp] = cost
            ans[next_comp] = now
            heapq.heappush(q, (cost, next_comp))

print(N-1)
for i in range(N+1):
    if ans[i] != 0:
        print(i, ans[i])
