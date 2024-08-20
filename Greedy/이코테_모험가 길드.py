import sys

input = sys.stdin.readline

N = int(input())
gongpo = list(map(int, input().split()))

gongpo.sort()

ans = 0

num = 0
i = 0
while i < N:
    num += 1   #현재 1명 추가

    if gongpo[i] >= num:
        ans += 1
        num = 0

    i += 1

print(ans)
