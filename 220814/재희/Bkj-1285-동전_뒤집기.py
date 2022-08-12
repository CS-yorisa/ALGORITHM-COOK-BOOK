import sys

input = sys.stdin.readline

N: int = int(input())
coins: list[str] = [input().rstrip() for _ in range(N)]
answer: int = N * N

for bit in range(1 << N):
    total: int = 0
    for j in range(N):
        cnt: int = 0
        for i in range(N):
            if coins[i][j] == ('T' if bit & (1 << i) else 'H'):
                cnt += 1
        total += min(cnt, N - cnt)
    answer = min(answer, total)

print(answer)