"""
Title : 숫자구슬
Link : https://www.acmicpc.net/problem/2613
"""

from sys import stdin

input = stdin.readline
MIIS = lambda: map(int, input().split())


def search(M: int, beads: tuple[int]) -> int:
    left, right = 0, sum(beads)
    max_bead = max(beads)
    ans = right
    beads_count = []
    while left <= right:
        mid = (left + right) // 2
        if mid < max_bead:
            left = mid + 1
            continue
        counts = get_beads_counts(M, mid, beads)
        if counts:
            ans = mid
            beads_count = counts[::]
            right = mid - 1
        else:
            left = mid + 1
    print(ans)
    print(*beads_count)


def get_beads_counts(divide: int, max_sum: int, beads: tuple[int]) -> list[int]:
    counts = [0] * divide
    idx = count = 0
    sum_now = 0
    for x in beads:
        if sum_now + x > max_sum:
            counts[idx] = count
            idx += 1
            count = 0
            sum_now = 0
        if idx == divide:
            return []
        sum_now += x
        count += 1
    counts[idx] = count
    left = idx
    idx += 1
    while idx < divide:
        if counts[left] > 1:
            counts[left] -= 1
            counts[idx] += 1
            idx += 1
        else:
            left -= 1
    return counts


if __name__ == "__main__":
    N, M = MIIS()
    beads = tuple(MIIS())
    search(M, beads)

"""
4 4
3 1 1 1
"""
