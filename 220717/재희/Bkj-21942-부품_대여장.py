import sys
from datetime import datetime

input = sys.stdin.readline
MSISS = lambda: map(str, input().strip().split())

N, L, F = MSISS()
N, F = int(N), int(F)
period: int = int(L[:3]) * 1440 + int(L[4:6]) * 60 + int(L[7:])  # 대여기간을 분으로 환산
data = dict()  # 대여 정보
penalty = dict()  # 벌금 정보

for _ in range(N):
    day, time, item, member = MSISS()
    key: str = item + '.' + member
    current_date: str = day + '.' + time
    # 이미 대여하고 반납하는 경우
    if data.get(key) and data[key] != '.':
        rent_date = datetime.strptime(data[key], "%Y-%m-%d.%H:%M")
        return_date = datetime.strptime(current_date, "%Y-%m-%d.%H:%M")
        diff = return_date - rent_date
        minute_diff = (diff.days * 1440 + diff.seconds / 60) - period
        # 대여기간을 초과한 경우
        if minute_diff > 0:
            if penalty.get(member):
                penalty[member] += minute_diff * F
            else:
                penalty[member] = minute_diff * F
        data[key] = '.'
    # 대여하는 경우
    else:
        data[key] = current_date

sorted_penalty = sorted(penalty.items())

if sorted_penalty:
    for member, value in sorted_penalty:
        print(member, int(value))
else:
    print(-1)