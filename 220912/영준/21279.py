"""
Title : 광부 호석
Link : https://www.acmicpc.net/problem/21279
"""

from sys import stdin

input = stdin.readline
MIIS = lambda: map(int, input().split())

Mineral = dict[int, list[tuple[int]]]
Coordinate = list[int]


if __name__ == "__main__":
    N: int
    C: int
    N, C = MIIS()
    minerals_x: Mineral = dict()
    minerals_y: Mineral = dict()
    for _ in range(N):
        x, y, v = MIIS()
        if x in minerals_x:
            minerals_x[x].append((y, v))
        else:
            minerals_x[x] = [(y, v)]
        if y in minerals_y:
            minerals_y[y].append((x, v))
        else:
            minerals_y[y] = [(x, v)]

    x: int = 100_000
    y: int = 0

    mineral_value: int = 0
    mineral_count: int = 0
    ans: int = 0

    while x >= 0 and y <= 100_000:
        if mineral_count <= C:
            if y in minerals_y:
                for _x, _v in minerals_y[y]:
                    if _x <= x:
                        mineral_value += _v
                        mineral_count += 1
            y += 1
        else:
            if x in minerals_x:
                for _y, _v in minerals_x[x]:
                    if _y <= y - 1:
                        mineral_value -= _v
                        mineral_count -= 1
            x -= 1
        if mineral_count <= C:
            if ans < mineral_value:
                ans = mineral_value

    print(ans)
