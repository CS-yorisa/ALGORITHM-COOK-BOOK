
# 팰린드롬 체크
def is_palindrome(word):
    return word == word[::-1]

string = input()
length = len(string)
dp = [[5000] * length for _ in range(length)]
dp[0][0] = 1

for i in range(length):
    for j in range(i, length):
        # 직전 자리까지 만들어진 팰린드롬 개수의 최소부터 누적
        if i == j and i:
            dp[i][j] = min(d[j - 1] for d in dp[:i]) + 1
            continue
        if is_palindrome(string[i:j + 1]):
            dp[i][j] = dp[i][i]

# 마지막 문자까지 팰린드롬이 완성된 경우의 최솟값
print(min(d[-1] for d in dp))