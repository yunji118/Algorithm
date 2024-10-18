import sys

input = sys.stdin.readline

N = int(input())

board = [[0] * 100 for _ in range(100)]

while N > 0:
    N -= 1
    c, r = map(int, input().split())

    for i in range(r, r+10):
        for j in range(c, c+10):
            board[i][j] = 1

ans = 0
for i in range(100):
    for j in range(100):
        if board[i][j] == 1:
            ans += 1

print(ans)
