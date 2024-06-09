import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, s, d = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

depth = [0] * (n+1)

def dfs(now, prev):
    for nxt in graph[now]:
        if prev != nxt:
            depth[now] = max(depth[now], dfs(nxt, now) + 1) #여기서 헤맸다 가장 자식이 많은 애를 Return.

    return depth[now]

dfs(s, 0)
ans = 0
# print(depth)
for i in range(1, n+1):
    if depth[i] >= d and i != s:
        ans += 1

print(ans * 2)

'''
depth기본 값을 1로 두고 depth[now] += 로 하면
인접 노드를 살필 때마다 depth[now]값이 누적됨. 우리는 자식의 수가 가장 많은 노드를 구할 것이므로 누적해나가면 안됨!

그리고 depth 기본 값을 1로 두기도 애매한게 +=를 못 쓰므로 어짜피 누적이 안 됨. 굳이 1로 둘 필요 없음
'''
