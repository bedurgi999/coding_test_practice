import sys
input = sys.stdin.readline

n, k = map(int, input().split())

if n <= 2:
    print(1)
    exit()
    
dp = [1, 1]

for i in range(3, n + 1):
    temp = []
    
    for j in range(i - 2):
        temp.append(dp[j] + dp[j+1])
    
    dp = [1] + temp[:] + [1]

print(dp[k-1])