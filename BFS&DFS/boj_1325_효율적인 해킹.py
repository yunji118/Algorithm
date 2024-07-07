import sys
##sys.setrecursionlimit(10**6) pypy3으로 통과함

input = sys.stdin.readline

N, M = map(int, input().split())  #컴퓨터의 수, 관계의 수

graph = [[] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())  #b를 해킹하면 a도 해킹할 수 있음
    graph[b].append(a)


def bfs(start):
    que = []
    que.append(start)
    visited = [False] * (N+1)
    cnt = 0
    visited[start] = True

    while que:
        now = que.pop()

        for nxt in graph[now]:
            if not visited[nxt]:
                visited[nxt] = True
                que.append(nxt)
                cnt += 1

    return cnt


count = [0] * (N+1)
max_cnt = 0

for i in range(1, N+1):
    count[i] = bfs(i)
    max_cnt = max(max_cnt, count[i])

for i in range(1, N+1):
    if max_cnt == count[i]:
        print(i, end=" ")


