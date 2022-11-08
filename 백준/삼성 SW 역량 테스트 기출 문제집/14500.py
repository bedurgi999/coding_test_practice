import sys
input = sys.stdin.readline


def dfs(b, v, total, cnt, x, y):
    global ans
    
    if ans >= total + (max_val * (4 - cnt)):
        return
    
    if cnt == 4:
        ans = max(ans, total)
        return
    
    # 상 우 하 좌
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        
        if v[nx][ny] == False:
            if cnt == 2:
                v[nx][ny] = True
                dfs(b, v, total + b[nx][ny], cnt + 1, x, y)
                v[nx][ny] = False
            
            v[nx][ny] = True
            dfs(b, v, total + b[nx][ny], cnt + 1, nx, ny)
            v[nx][ny] = False

board = []
max_val = 0

n, m = map(int, input().split())
ans = 0

visited = [[False]*m for _ in range(n)]

for i in range(n):
    board.append(list(map(int, input().split())))
    max_val = max(max_val, *board[i])

for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(board, visited, board[i][j], 1, i, j)
        visited[i][j] = False

print(ans)