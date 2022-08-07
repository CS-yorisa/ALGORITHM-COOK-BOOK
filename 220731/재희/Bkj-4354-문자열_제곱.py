import sys
from typing import List

input = sys.stdin.readline
Table = List[int]

def KMP_table(pattern: str) -> Table:
    lp: int = len(pattern)
    tb: Table = [0] * lp

    pidx: int = 0
    for idx in range(1, lp):
        while pidx > 0 and pattern[idx] != pattern[pidx]:
            pidx = tb[pidx - 1]
        
        if pattern[idx] == pattern[pidx]:
            pidx += 1
            tb[idx] = pidx
        
    return tb


while True:
    s: str = input().strip()
    length: int = len(s)

    if s == '.':
        break

    table: Table = KMP_table(s)

    # 제곱으로 나타낼 수 있음
    if length % (length - table[-1]) == 0:
        print(length // (length - table[-1]))
    # 제곱으로 나타낼 수 없음
    else:
        print(1)