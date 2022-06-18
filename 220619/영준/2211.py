"""
Title : 네트워크 복구
Link : https://www.acmicpc.net/problem/2211
"""

import heapq
from sys import stdin

input = stdin.readline
MIIS = lambda: map(int, input().split())
graph = list[list[tuple[int]]]


def djikstra(N: int, lines: graph) -> None:
    heap = [(0, 1)]
    INF = 10**10
    visited = [INF] * (N + 1)
    visited[1] = 0
    parents = list(range(N + 1))
    while heap:
        dist, pos = heapq.heappop(heap)
        if visited[pos] < dist:
            continue
        for next_pos, add_dist in lines[pos]:
            next_dist = dist + add_dist
            if visited[next_pos] <= next_dist:
                continue
            visited[next_pos] = next_dist
            parents[next_pos] = pos
            heapq.heappush(heap, (next_dist, next_pos))
    ans = f"{N - 1}"
    for idx, x in enumerate(parents[2:]):
        ans += f"\n{idx + 2} {x}"
    print(ans)
    return


if __name__ == "__main__":
    N, M = MIIS()
    lines: graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        A, B, C = MIIS()
        lines[A].append((B, C))
        lines[B].append((A, C))
    djikstra(N, lines)
