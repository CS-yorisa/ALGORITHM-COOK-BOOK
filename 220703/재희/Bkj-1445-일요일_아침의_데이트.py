import sys, heapq
from typing import Tuple, List

input = sys.stdin.readline

# S, F 위치 파악 / g 주변은 h 로 변경
def check_map() -> Tuple[int]:
    global MAP
    sx = sy = ex = ey = 0
    for i in range(N):
        for j in range(M):
            block = MAP[i][j]
            if block == 'S':
                sx, sy = i, j
            elif block == 'F':
                ex, ey = i, j
            elif block == 'g':
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if 0 <= nx < N and 0 <= ny < M and MAP[nx][ny] == '.':
                        MAP[nx][ny] = 'h'
    return (sx, sy, ex, ey)

def dijkstra(MAP: List[List[int]], sx: int, sy: int, ex: int, ey: int) -> List[int]:
    distance = [[float('inf')] * M for _ in range(N)]
    distance[sx][sy] = 0
    queue = []
    heapq.heappush(queue, (0, sx, sy))

    while queue:
        now_dist, x, y = heapq.heappop(queue)

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < M:
                new_dist = now_dist
                block = MAP[nx][ny]
                # h 는 10000 번 이상 거치지 않기 때문에 10000 단위로 구분
                if block == 'g':
                    new_dist += 10000
                elif block == 'h':
                    new_dist += 1
                if new_dist < distance[nx][ny]:
                    distance[nx][ny] = new_dist
                    heapq.heappush(queue, (new_dist, nx, ny))
    return distance[ex][ey]

N, M = map(int, input().split())
MAP = [list(str(input().strip())) for _ in range(N)]
dx, dy = (1, 0, -1, 0), (0, 1, 0, -1)
sx, sy, ex, ey = check_map()

answer = dijkstra(MAP, sx, sy, ex, ey)
# 10000 단위로 구분하여 출력
print(answer // 10000, answer % 10000)