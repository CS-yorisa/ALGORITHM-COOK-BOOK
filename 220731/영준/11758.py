"""
Title : CCW
Link : https://www.acmicpc.net/problem/11758
"""

from sys import stdin

input = stdin.readline
MIIS = lambda: map(int, input().split())


if __name__ == "__main__":
    x1, y1 = MIIS()
    x2, y2 = MIIS()
    x3, y3 = MIIS()
    CCW = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
    print(0 if not CCW else 1 if CCW > 0 else -1)
