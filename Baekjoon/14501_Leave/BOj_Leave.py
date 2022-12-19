n = int(input())
list_table = [list(map(int,input().split())) for _ in range(n)]
length = len(list_table)
dp = [0] * 50
for i in range(len(list_table)-1, -1, -1):
    if length < i + list_table[i][0]:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(list_table[i][1] + dp[list_table[i][0] + i], dp[i+1])
print(dp[0])