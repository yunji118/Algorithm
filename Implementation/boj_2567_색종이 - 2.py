import sys

input = sys.stdin.readline

N = int(input())
board = [[0] * 102 for _ in range(102)] #모서리에 패딩 1씩 넣기


while N > 0:
    N -= 1
    c, r = map(int, input().split())

    for i in range(r+1, r+11):
        for j in range(c+1, c+11):
            board[i][j] = 1

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

ans = 0
for r in range(1, 101):
    for c in range(1, 101):
        if board[r][c] == 1:
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                if board[nr][nc] == 0:
                    ans += 1

print(ans)
