import sys

input = sys.stdin.readline

N = int(input())  #전제의 개수

graph = [[0] * 26 for _ in range(26)]
for i in range(N):
    a, isis, b = input().split()
    graph[ord(a) - ord('a')][ord(b) - ord('a')] = 1

M = int(input())

for i in range(26):
    for s in range(26):
        for e in range(26):
            if graph[s][i] == 1 and graph[i][e] == 1:
                graph[s][e] = 1


ans = []

for _ in range(M):
    a, isis, b = input().split()

    if graph[ord(a) - ord('a')][ord(b) - ord('a')] > 0:
        ans.append('T')
    else:
        ans.append('F')

for a in ans:
    print(a)
