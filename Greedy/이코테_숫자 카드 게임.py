import sys

input = sys.stdin.readline

N, M = map(int, input().split())
card = [list(map(int, input().split())) for _ in range(N)]

maximum = 1

for i in range(N):
    m = min(card[i])
    if m > maximum:
        maximum = m

print(maximum)
