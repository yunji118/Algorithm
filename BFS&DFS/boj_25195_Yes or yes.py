import sys
from collections import deque

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N, M = map(int, input().split())  #정점의 개수, 간선의 개수

graph = [[] * (N+1) for _ in range(N+1)]

for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)

s = int(input())
gomgom = list(map(int, input().split()))

def bfs(now):
    que = deque()
    que.append(now)

    while que:
        now = que.popleft()

        if now in gomgom:
            continue

        for nxt in graph[now]:
            que.append(nxt)

        if len(graph[now]) == 0:
            print("yes")
            exit(0)


def dfs(now):
    if now in gomgom:
        return

    for nxt in graph[now]:
        dfs(nxt)

    if len(graph[now]) == 0:
        print("yes")
        exit(0)


# dfs(1)
bfs(1)
print("Yes")


