import sys

input = sys.stdin.readline

string1: str = input().strip()
string2: str = input().strip()
string3: str = input().strip()
length1: int = len(string1)
length2: int = len(string2)
length3: int = len(string3)
lcs: list[list[list[int]]] = [[[0] * (length1 + 1) for _ in range(length2 + 1)] for _ in range(length3 + 1)]

for i in range(1, length3 + 1):
    for j in range(1, length2 + 1):
        for k in range(1, length1 + 1):
            if string1[k - 1] == string2[j - 1] == string3[i - 1]:
                lcs[i][j][k] = lcs[i - 1][j - 1][k - 1] + 1
            else:
                lcs[i][j][k] = max(lcs[i - 1][j][k], lcs[i][j - 1][k], lcs[i][j][k - 1])

print(lcs[-1][-1][-1])