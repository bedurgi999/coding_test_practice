import sys
input = sys.stdin.readline

# def dfs(b, v, x, y, d):
#     global answer
    
#     answer += 1
#     v[x][y] = True
#     # 북 동 남 서
#     dx = [-1, 0, 1, 0]
#     dy = [0, 1, 0, -1]
#     nd = 0
#     nx = 0
#     ny = 0
#     for i in range(4):
#         nd = (d - i) % 4
#         nx = x + dx[nd]
#         ny = y + dy[nd]
        
#         if b[nx][ny] == 0 and v[nx][ny] == False:
#             dfs(b, v, nx, ny, nd)
#             return
#         elif b[nx][ny] == 0 and v[nx][ny] == True:
#             continue
#         elif b[nx][ny] == 1:
#             nx = x - dx[nd]
#             ny = y - dy[nd]
#             dfs(b, v, nx, ny, nd)
#             return
#     if 
        
        

n, m = map(int, input().split())
r, c, d = map(int, input().split())
board = []
answer = 1
for _ in range(n):
    board.append(list(map(int, input().split())))

visited = [[False]*m for _ in range(n)]

visited[r][c] = True


    # 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
nd = 0
nx = 0
ny = 0

while True:
    flag = True
    
    for i in range(1, 5):
        nd = (d - i) % 4
        nx = r + dx[nd]
        ny = c + dy[nd]
        
        if 0 <= nx < n and 0 <= ny < m:    
            if board[nx][ny] == 0 and visited[nx][ny] == False:
                r = nx
                c = ny
                visited[r][c] = True
                answer += 1
                flag = False
                d = nd
                break
        
    if flag:
        nx = r - dx[nd]
        ny = c - dy[nd]
        
        if board[nx][ny] == 1:
            break
        else:
            r = nx
            c = ny
            d = nd

print(answer)