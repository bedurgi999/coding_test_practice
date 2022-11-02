import sys
input = sys.stdin.readline

n = int(input())

dp = [0 for _ in range(100001)]
dp[1] = -1
dp[2] = 1
dp[3] = -1

if n < 4:
    print(dp[n])
    exit()
    
for i in range(4, n + 1):
    if i % 5 == 0:
        dp[i] = dp[i - 5] + 1
    else:
        if dp[i - 2] == -1:
            dp[i] = -1
        else:
            dp[i] = dp[i - 2] + 1

print(dp[n])