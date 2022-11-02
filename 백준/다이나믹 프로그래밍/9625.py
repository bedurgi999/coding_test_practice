import sys
input = sys.stdin.readline

n = int(input())

a = [0 for _ in range(n+1)]
b = [0 for _ in range(n+1)]

a[0] = 1
b[1] = 1

for i in range(2, n+1):
    a[i] = a[i-2] + a[i-1]
    b[i] = b[i-2] + b[i-1]
    
print(a[n], b[n])


"""
0 => A
1 => B
2 => BA 1
3 => BAB 1
4 => BABBA 2
5 => BABBABAB 3
6 => BABBABABBABBA 5
7 => BABBABABBABBABABBABAB 8
8 => BABBABABBABBABABBABABBABBABABBABBA 12

문자열 기준으로
i번째 문자 = i-1번째 문자 + i-2번째 문자 가된다.
"""