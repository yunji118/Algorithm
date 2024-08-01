import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

parent = [i for i in range(n)]
plan = list(map(int, input().split()))
def find_parent(x):
    if x != parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1: #길이 있으면 union
            union(i, j)

pa = parent[plan[0] - 1]
for i in range(1, m):
    if parent[plan[i] - 1] != pa:
        print("NO")
        exit(0)

print("YES")
