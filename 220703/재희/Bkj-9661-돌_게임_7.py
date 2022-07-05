N = int(input()) % 5

# 4^x 이전 턴을 체크해서 모두 상근이가 이기는 경우 창영이가 승리
# 5 개씩 구간을 나누어 2, 5 번째 오는 경우
if N == 0 or N == 2:
    print('CY')
else:
    print('SK')