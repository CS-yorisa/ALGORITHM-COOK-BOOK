"""
Title : 집배원 한상덕
Link : https://www.acmicpc.net/problem/2842
"""

from collections import deque
from sys import stdin

input = stdin.readline


def search(high: int, low: int) -> bool:
    queue = deque([post])
    houses_check = 0
    visited = [[False] * N for _ in range(N)]
    while queue:
        x, y = queue.popleft()
        if visited[x][y]:
            continue
        visited[x][y] = True
        if town[x][y] == "K":
            houses_check += 1
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny]:
                    continue
                if low <= heights_map[nx][ny] <= high:
                    queue.append((nx, ny))
    if houses_check == houses:
        return True
    return False


if __name__ == "__main__":
    N = int(input())
    town = [input().strip() for _ in range(N)]
    heights_map = [list(map(int, input().split())) for _ in range(N)]
    heights = sorted(set(sum(heights_map, [])))
    if len(heights) == 1:
        print(0)
        exit()

    post = tuple()
    houses = 0
    possible_heights = []
    for i, line in enumerate(town):
        for j, x in enumerate(line):
            h = heights_map[i][j]
            if x == "P":
                post = (i, j)
                possible_heights.append(h)
            elif x == "K":
                houses += 1
                possible_heights.append(h)
    house_min_index = heights.index(min(possible_heights))
    house_max_index = heights.index(max(possible_heights))

    left, right = 0, house_max_index
    ans = 1_000_000
    delta = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    while right < len(heights):
        while left <= house_min_index:
            high, low = heights[right], heights[left]
            if search(high, low):
                left += 1
                if ans > high - low:
                    ans = high - low
            else:
                break
        right += 1
    print(ans)

"""
5
P....
.....
.....
.....
K...K
5 0 4 5 4
5 0 5 8 5
5 0 5 0 5
6 0 5 0 5
6 5 4 0 5
"""
