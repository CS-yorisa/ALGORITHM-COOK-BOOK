"""
Title : 선분 교차 1
Link : https://www.acmicpc.net/problem/17386
"""


x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())


# 첫 직선 기준 가능한지 확인
d1 = (y1 - y2) * (x3 - x1) + (x2 - x1) * (y3 - y1)
d2 = (y1 - y2) * (x4 - x1) + (x2 - x1) * (y4 - y1)

# 두번째 직선 기준 가능한지 확인
d3 = (y4 - y3) * (x1 - x3) + (x3 - x4) * (y1 - y3)
d4 = (y4 - y3) * (x2 - x3) + (x3 - x4) * (y2 - y3)

# 두 직선 기준 교차하는 형태인지 확인
# 두 직선의 교점에 관한식을 한 직선의 x좌표를 사용
# 두 개 값을 비교
# e1 = (y2 - y1) * (y4 - y3) * (x1 - x1) + y1 * (y4 - y3) - (y4 - y3) * (x2 - x1) * (x1 - x2) - y3 * (x2 - x1)
# e2 = (y2 - y1) * (y4 - y3) * (x2 - x1) + y1 * (y4 - y3) - (y4 - y3) * (x2 - x1) * (x2 - x2) - y3 * (x2 - x1)
# 직선 기준 위 아래면 비교할 필요 없음


# 두 값이 모두 양수 / 음수인 경우 불가능
if (d1 < 0 and d2 < 0) or (d1 > 0 and d2 > 0):
    print(0)
elif (d3 < 0 and d4 < 0) or (d3 > 0 and d4 > 0):
    print(0)
# elif (e1 < 0 and e2 < 0) or (e1 > 0 and e2 > 0):
#     print(0)
else:
    print(1)
