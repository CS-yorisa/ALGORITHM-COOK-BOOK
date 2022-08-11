N, K = map(int, input().strip().split())
data = list(map(int, input().strip().split()))
multitap = [0] * N
ans = remove_plug = remove_idx = 0

for i, d in enumerate(data):
    if d in multitap:
        continue
    elif 0 in multitap:
        multitap[multitap.index(0)] = d
    else:
        for j in multitap:
            # 전기 용품이 더 이상 사용 되지 않을 때
            if j not in data[i:]:
                remove_plug = j
                break
            # 가장 마지막에 사용되는 전기 플러그를 뽑아야 함
            elif data[i:].index(j) > remove_idx:
                remove_idx = data[i:].index(j)
                remove_plug = j

        multitap[multitap.index(remove_plug)] = d
        remove_idx = remove_plug = 0
        ans += 1

print(ans)

