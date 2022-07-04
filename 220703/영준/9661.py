"""
Title : 돌 게임 7
Link : https://www.acmicpc.net/problem/9661
"""

from sys import stdin

input = stdin.readline


if __name__ == "__main__":
    N = int(input())
    if not N % 5 or N % 5 == 2:
        print("CY")
    else:
        print("SK")
