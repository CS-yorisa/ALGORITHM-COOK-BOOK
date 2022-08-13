"""
Title : 멀티탭 스캐줄링
Link : https://www.acmicpc.net/problem/1700
"""

from bisect import bisect_left
from sys import stdin

input = stdin.readline
MIIS = lambda: map(int, input().split())


if __name__ == "__main__":
    N, K = MIIS()
    devices = list(MIIS())
    devices.reverse()
    devices_pos = {x: [] for x in set(devices)}
    for idx, x in enumerate(devices):
        devices_pos[x].append(idx)
    multitab = set()
    count = 0
    ans = 0
    for i, x in enumerate(devices):
        if count <= N and x in multitab:
            continue
        if count < N:
            multitab.add(x)
            count += 1
            continue
        remove = idx = 0
        for y in multitab:
            _idx = bisect_left(devices_pos[y], i)
            if _idx == len(devices_pos[y]):
                remove = y
                break
            _idx = devices_pos[y][_idx]
            if idx < _idx:
                remove = y
                idx = _idx
        multitab.remove(remove)
        multitab.add(x)
        ans += 1
    print(ans)
