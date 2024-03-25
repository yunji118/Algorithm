import sys

input = sys.stdin.readline

N, M = map(int, input().split()) #세로:N  가로:M
board = []

for _ in range(N):
    tmp = list(map(int, input().split()))
    board.append(tmp)

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]
que = []
def bfs(sr, sc):
    que.append([sr, sc])
    board[sr][sc] = 2
    size = 1

    while que:
        now = que.pop()

        for d in range(4):
            nr = now[0] + dr[d]
            nc = now[1] + dc[d]
            if 0 <= nr < N and 0 <= nc < M and board[nr][nc] == 1: #범위 내에 있고 그림이면
                board[nr][nc] = 2 #방문표시
                que.append([nr, nc])
                size += 1

    return size


numOfPics = 0
maxSize = 0

for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            maxSize = max(maxSize, bfs(i, j))
            numOfPics += 1


print(numOfPics)
print(maxSize)




