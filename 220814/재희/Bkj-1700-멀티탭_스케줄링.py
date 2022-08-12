import sys, heapq

input = sys.stdin.readline
MIIS = lambda: map(int, input().split())

N, K = MIIS()
items: list[int] = list(MIIS())
used: list[int] = [0] * (K + 1)
use_count: int = 0
min_heap = []
answer: int = 0

use_idx: list[int] = [0] * (K + 1)  # 전기용품의 다음 순서의 인덱스 저장
item_sequence_idx: list[list[int]] = [[] for _ in range(K + 1)]  # 전기용품의 순서를 배열로 입력
for i in range(K):
    item = items[i]
    item_sequence_idx[item].append(i)
# 전기용품의 순서 마지막에 최댓값으로 패딩 추가
for i in range(1, K + 1):
    item_sequence_idx[i].append(101)

for item in items:
    # 이미 꽂혀있음
    if used[item] == 1:
        use_idx[item] += 1
        heapq.heappush(min_heap, (-item_sequence_idx[item][use_idx[item]], item))
        continue
    # 남아있는 자리가 있음
    if use_count < N:
        used[item] = 1
        use_count += 1
        use_idx[item] += 1
        heapq.heappush(min_heap, (-item_sequence_idx[item][use_idx[item]], item))
        continue
    # 남아있는 자리가 없음
    while True:
        count, current_item = heapq.heappop(min_heap)
        # 데이터 유효성 확인
        if item_sequence_idx[current_item][use_idx[current_item]] == -count:
            break
    used[current_item] = 0
    answer += 1
    used[item] = 1
    use_idx[item] += 1
    heapq.heappush(min_heap, (-item_sequence_idx[item][use_idx[item]], item))

print(answer)