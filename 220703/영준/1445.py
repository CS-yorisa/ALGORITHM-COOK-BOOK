"""
Title : 일요일 아침의 데이트
Link : https://www.acmicpc.net/problem/1445
"""

import heapq
from sys import stdin

input = stdin.readline


if __name__ == "__main__":
    N, M = map(int, input().split())
    forest_map = [input().strip() for _ in range(N)]
    is_garbage_next = [[False] * M for _ in range(N)]
    st, end = [], []
    dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
    for i in range(N):
        for j in range(M):
            if forest_map[i][j] == "S":
                st = [i, j]
            elif forest_map[i][j] == "F":
                end = [i, j]
            elif forest_map[i][j] == "g":
                for d in range(4):
                    nx, ny = i + dx[d], j + dy[d]
                    if 0 <= nx < N and 0 <= ny < M:
                        is_garbage_next[nx][ny] = True
    heap = [(0, 0, st[0], st[1])]
    visited = [[[10000, 10000] for _ in range(M)] for _ in range(N)]
    while heap:
        g, gn, x, y = heapq.heappop(heap)
        if [x, y] == end:
            print(g, gn)
            break
        if [g, gn] >= visited[x][y]:
            continue
        visited[x][y] = [g, gn]
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < N and 0 <= ny < M:
                if forest_map[nx][ny] == "F":
                    heapq.heappush(heap, (g, gn, nx, ny))
                elif forest_map[nx][ny] == "g":
                    heapq.heappush(heap, (g + 1, gn, nx, ny))
                elif is_garbage_next[nx][ny]:
                    heapq.heappush(heap, (g, gn + 1, nx, ny))
                else:
                    heapq.heappush(heap, (g, gn, nx, ny))


"""
형택 : 쓰레기가 어디있는지 조사 완료,
    쓰래기를 통과하기 싫어하고, 옆을 지나가기 불편
S에서 시작, F 꽃, g 쓰레기
S --> F 목표, 쓰레기 칸을 되도록 적게
    경우의 수가 여러개라면 쓰레기 옆을 지나가는 칸을 최소로
한 번에 가로 or 세로 한 칸

쓰레이 있는칸 or 칸이 비어 있는데 인접한 칸에 쓰레기 있으면 쓰레기 옆

시작칸 S, 종료칸 F는 아무런 횟수 세기 ㄴㄴ
"""
