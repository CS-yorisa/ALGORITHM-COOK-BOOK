"""
Title : 문자열 제곱
Link : https://www.acmicpc.net/problem/4354
"""

from sys import stdin

input = stdin.readline


# KMP
if __name__ == "__main__":
    while True:
        seq = input().strip()
        if seq == ".":
            break
        len_seq = len(seq)
        idx = 0
        check = [0] * len_seq
        for i in range(1, len_seq):
            while idx and seq[idx] != seq[i]:
                idx = check[idx - 1]
            if seq[idx] == seq[i]:
                idx += 1
                check[i] = idx
        max_len = len_seq - check[-1]
        if len_seq % max_len:
            print(1)
        else:
            print(len_seq // max_len)


# String matching
if __name__ == "__main__":
    while True:
        seq = input().strip()
        if seq == ".":
            break
        len_seq = len(seq)
        for i in range(1, len_seq + 1):
            if len_seq % i:
                continue
            target = seq[:i]
            if target * (len_seq // i) == seq:
                print(len_seq // i)
                break
