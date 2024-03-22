import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
# maze = [[0] * M for _ in range(N)]
maze = []
# for i in range(N):
#     tmp = input().rstrip()
#     for j in range(len(tmp)):
#         maze[i][j] = int(tmp[j:j+1])
'''
입력이 붙어서 나와도 이렇게 처리하면 되는구나...!!!!!
'''
for i in range(N):
    maze.append(list(map(int, input().rstrip())))


move = [[0] * M for _ in range(N)]

def bfs():
    que = deque()
    que.append([0, 0])
    dr = [0, 0, -1, 1]
    dc = [1, -1, 0, 0]
    move[0][0] = 1 #시작칸과 끝칸을 모두 포함해서 계산하라고 했으니까

    while que:
        now = que.popleft()
        # print("now = ",now)
        for p in range(4):
            nr = now[0] + dr[p]
            nc = now[1] + dc[p]
            # print("nr = ", nr, "nc = ", nc)
            if nr >= 0 and nr < N and nc >= 0 and nc < M and maze[nr][nc] == 1 and move[nr][nc] == 0:
                # move[nr][nc] = min(move[nr][nc], move[now[0]][now[1]] + 1)
                move[nr][nc] = move[now[0]][now[1]] + 1
                que.append([nr, nc])

bfs()
print(move[N-1][M-1])

'''
굳이 move 배열을 두지 않아도 됨. 그냥 maze에 +1씩 하면서 카운트해도 됨!
'''
