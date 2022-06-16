import sys, math, heapq
from typing import List, Tuple
input = sys.stdin.readline

# 다익스트라를 통해 노드가 어느 회선으로 연결되는지 탐색
def dijkstra(graph: List[List[Tuple[int, int]]], start: int) -> None:
    global pre_nodes
    distance = [math.inf] * (N + 1)
    distance[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
        now_dist, now_node = heapq.heappop(queue)

        if distance[now_node] < now_dist:
            continue

        for new_node, new_dist in graph[now_node]:
            dist = distance[now_node] + new_dist
            if dist < distance[new_node]:
                distance[new_node] = dist
                pre_nodes[new_node] = now_node  # 연결된 노드 갱신
                heapq.heappush(queue, (dist, new_node))


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
pre_nodes = [0] * (N + 1)  # 연결된 이전 노드
for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))
    graph[B].append((A, C))

dijkstra(graph, 1)

print(N - 1)  # 무조건 N-1 개 필요
for i in range(2, N + 1):
    print(i, pre_nodes[i])