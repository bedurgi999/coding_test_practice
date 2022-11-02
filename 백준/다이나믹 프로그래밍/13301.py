import sys
input = sys.stdin.readline

n = int(input())

dp = [0 for _ in range(n + 1)]
dp[1] = 1

for i in range(2, n + 1):
    dp[i] = dp[i-2] + dp[i - 1]

print(((dp[n] + dp[n-1]) * 2) + ((dp[n-1] + dp[n-2]) * 2))