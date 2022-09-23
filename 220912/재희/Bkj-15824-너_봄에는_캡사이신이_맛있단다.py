import sys

input = sys.stdin.readline


def in_cache(func):
    cache = {}

    def wrapper(n: int) -> int:
        if n in cache:
            return cache[n]
        else:
            cache[n] = func(n)
            return cache[n]

    return wrapper


@in_cache
def power(n: int) -> int:
    if n == 0:
        return 1

    x: int = power(n // 2)

    if n % 2 == 0:
        return (x * x) % 1000000007
    else:
        return (x * x * 2) % 1000000007


N: int = int(input())
foods: list[int] = sorted(list(map(int, input().split())))
answer: int = 0

for i in range(N):
    answer += (power(i) - power(N - i - 1)) * foods[i]

print(answer % 1000000007)
