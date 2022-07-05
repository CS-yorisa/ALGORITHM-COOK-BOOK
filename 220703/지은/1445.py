import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())
forest = [list(input().rstrip()) for _ in range(N)]
dist = [[float('inf')]*M for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
sy, sx, fy, fx = 0, 0, 0, 0
for i in range(N):
    for j in range(M):
        if forest[i][j] == "S":
            sy, sx = i, j
        elif forest[i][j] == "F":
            fy, fx = i, j
        # 쓰레기 주변은 '#' 으로 표시해주기
        elif forest[i][j] == "g":
            for k in range(4):
                ny = i + dy[k]
                nx = j + dx[k]
                if 0 <= ny < N and 0 <= nx < M and forest[ny][nx] == ".":
                    forest[ny][nx] = "#"

q = []
# 쓰레기 지나는 횟수, 쓰레기 옆을 지나는 횟수, 시작점
heapq.heappush(q, (0, 0, sy, sx))
visited = [[0] * M for _ in range(N)]
visited[sy][sx] = 1

while q:
    a, b, y, x = heapq.heappop(q)

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
            visited[ny][nx] = 1
            if forest[ny][nx] == ".":
                heapq.heappush(q, (a, b, ny, nx))
            elif forest[ny][nx] == "#":
                heapq.heappush(q, (a, b+1, ny, nx))
            elif forest[ny][nx] == "g":
                heapq.heappush(q, (a + 1, b, ny, nx))
            else:
                print(a, b)
                break
