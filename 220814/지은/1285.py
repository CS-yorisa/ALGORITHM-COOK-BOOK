import sys
input = sys.stdin.readline

N = int(input())
ans = N * N + 1
maps = [list(input()) for _ in range(N)]

# 모든 행 경우의 수 다 뒤집어 보기...
for bit in range(1 << N):
    tmp = [maps[i][:] for i in range(N)]
    # 행 뒤집기
    for i in range(N):
        if bit & (1 << i):
            for j in range(N):
                if tmp[i][j] == 'H':
                    tmp[i][j] = 'T'
                else:
                    tmp[i][j] = 'H'
    # 열 뒤집기
    sum_t = 0
    for i in range(N):
        cnt = 0
        for j in range(N):
            if tmp[j][i] == 'T':
                cnt += 1

        # T가 더 많을 경우 뒤집음
        sum_t += min(cnt, N-cnt)
    ans = min(sum_t, ans)

print(ans)
