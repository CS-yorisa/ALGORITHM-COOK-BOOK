seq1 = input().strip()
seq2 = input().strip()
seq3 = input().strip()

l1 = len(seq1)
l2 = len(seq2)
l3 = len(seq3)

arr = [[[0] * (l3  + 1) for _ in range(l2 + 1)] for _ in range(l1+1)]

for i in range(1, l1+1):
    for j in range(1, l2+1):
        for k in range(1, l3+1):
            if seq1[i-1] == seq2[j-1] and seq2[j-1] == seq3[k-1]:
                arr[i][j][k] = arr[i-1][j-1][k-1] + 1
            else:
                arr[i][j][k] = max(arr[i-1][j][k], arr[i][j-1][k], arr[i][j][k-1])
ans = -1

for i in range(l1+1):
    for j in range(l2+1):
        ans = max(max(arr[i][j]), ans)

print(ans)