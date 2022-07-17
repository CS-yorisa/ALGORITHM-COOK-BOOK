"""
Title : 부품 대여장
Link : https://www.acmicpc.net/problem/21942
"""

from sys import stdin

input = stdin.readline
ISS = lambda: input().strip().split()


def get_duration(time: str) -> int:
    day, time = time.split("/")
    hour, minute = map(int, time.split(":"))
    duration = int(day) * 24 * 60 + hour * 60 + minute
    return duration


def get_time(day: str, time: str) -> int:
    global months
    _, month, day = map(int, day.split("-"))
    day += months[month - 1]
    hour, minute = map(int, time.split(":"))
    t = minute + hour * 60 + day * 60 * 24
    return t


if __name__ == "__main__":
    N, L, F = ISS()
    N, F = int(N), int(F)
    maximum_duration = get_duration(L)
    ans = {}
    borrow = {}
    months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for i in range(12):
        months[i + 1] += months[i]
    for _ in range(N):
        day, time, P, M = ISS()
        t = get_time(day, time)
        if (P, M) in borrow:
            borrow_duration = t - borrow[(P, M)]
            borrow.pop((P, M))
            if borrow_duration > maximum_duration:
                if M in ans:
                    ans[M] += F * (borrow_duration - maximum_duration)
                else:
                    ans[M] = F * (borrow_duration - maximum_duration)
        else:
            borrow[(P, M)] = t
    if not ans:
        print(-1)
    else:
        output = ""
        for key in sorted(ans.keys()):
            output += f"{key} {ans[key]}\n"
        print(output)
