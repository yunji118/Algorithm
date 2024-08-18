import sys

input = sys.stdin.readline

N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

ans = int(1e9)
dc = [-1, 0, 1]
def bruteforce(prev, cost, r, c):
    global ans

    if r == N-1:
        ans = min(ans, cost)
        return

    for i in range(3):
        if i == prev:
            continue
        if r + 1 < N and c + dc[i] < M and c + dc[i] >= 0:
            bruteforce(i, cost + board[r+1][c+dc[i]], r + 1, c + dc[i])


for i in range(M):  #이걸 M이 아니라 4라고 해서 틀렸었음^^;
    bruteforce(-1, board[0][i], 0, i)

print(ans)


