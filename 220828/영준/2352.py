"""
Title : 반도체 설계
Link : https://www.acmicpc.net/problem/2352
"""

from bisect import bisect_left
from sys import stdin

input = stdin.readline


if __name__ == "__main__":
    N = int(input())
    ports = map(int, input().split())

    LIS = [next(ports)]
    for x in ports:
        if LIS[-1] < x:
            LIS.append(x)
        else:
            LIS[bisect_left(LIS, x)] = x
    print(len(LIS))
