"""
Title : 원 영역
Link : https://www.acmicpc.net/problem/10000
"""

from sys import stdin

input = stdin.readline


if __name__ == "__main__":
    N = int(input())
    circles = []
    for _ in range(N):
        x, r = map(int, input().split())
        circles.append((0, x + r))
        circles.append((1, x - r))
    circles.sort(key=lambda x: (x[1], x[0]))
    ans = 1
    stack = []
    for k, pos in circles:
        if k:
            stack.append((k, pos))
            continue
        total_width = 0
        while stack:
            _k, _pos = stack.pop()
            if _k:
                width = pos - _pos
                if width == total_width:
                    ans += 2
                else:
                    ans += 1
                stack.append((k, width))
                break
            else:
                total_width += _pos
    print(ans)
