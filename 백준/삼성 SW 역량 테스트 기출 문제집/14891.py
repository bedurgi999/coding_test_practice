import sys
input = sys.stdin.readline

# 12 1 3 4 6 8 9 11
gears = [[], [], [], [], []]

for i in range(1, 5):
    gears[i] = list(input().strip())

k = int(input())

rotations = []

prev = [[], [], [], [], []]

score = 0

for _ in range(k):
    rotations.append(list(map(int, input().split())))

for i, d in rotations:
    
    for j in range(1, 5):
        prev[j] = [gears[j][6], gears[j][2]]
    if d == 1:
        gears[i] = [gears[i][-1]] + gears[i][:7]
    elif d == -1:
        gears[i] = gears[i][1:] + [gears[i][0]]

    # 오른쪽 톱니바퀴
    if i != 4:
        next_d = d * -1
        for r in range(i+1, 5):
            if prev[r-1][1] != prev[r][0]:
                if next_d == 1:
                    gears[r] = [gears[r][-1]] + gears[r][:7]
                elif next_d == -1:
                    gears[r] = gears[r][1:] + [gears[r][0]]
                next_d = next_d * -1
            else:
                break
        
    # 왼쪽 톱니바퀴
    if i != 1:
        next_d = d * -1
        for l in range(i-1, 0, -1):
            if prev[l+1][0] != prev[l][1]:
                if next_d == 1:
                    gears[l] = [gears[l][-1]] + gears[l][:7]
                elif next_d == -1:
                    gears[l] = gears[l][1:] + [gears[l][0]]
                next_d = next_d * -1
            else:
                break
    

add = 1
for s in range(1, 5):
    if gears[s][0] == '1':
        score += add
    add *= 2
print(score)