import sys
input = sys.stdin.readline

def rolling(dir, dice):
    # 상, 후, 우, 좌, 정, 하
    a, b, c, d, e, f = dice[1:]
    
    # 동 서 북 남
    if dir == 1:
        dice = [0, d, b, a, f, e, c]
    elif dir == 2:
        dice = [0, c, b, f, a, e, d]
    elif dir == 3:
        dice = [0, e, a, c, d, f, b]
    elif dir == 4:
        dice = [0, b, f, c, d, a, e]
    
    return dice

              
    
# 상, 후, 우, 좌, 정, 하
dice = [0, 0, 0, 0, 0, 0, 0]
board = []

n, m, x, y, k = map(int, input().split())



for _ in range(n):
    board.append(list(map(int, input().split())))

command = list(map(int, input().split()))

# 동 서 북 남
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

for d in command:
    x += dx[d]
    y += dy[d]
    
    if x < 0 or x >= n or y < 0 or y >= m:
        x -= dx[d]
        y -= dy[d]
        continue
        
    dice = rolling(d, dice)
    if board[x][y] == 0:
        board[x][y] = dice[6]
    elif board[x][y] != 0:
        dice[6] = board[x][y]
        board[x][y] = 0
    print(dice[1])

