import sys

input = sys.stdin.readline

N, M = map(int, input().split())  #N:공의 개수  M:공의 최대 무게
weight = list(map(int, input().split()))

weight.sort()

ans = 0
for i in range(N):
    for j in range(i+1, N):
        if weight[j] > weight[i]: #나보다 무거운 애 등장. 즉, j는 i랑 무게가 같거나 가벼운 애들의 개수가 됨
            ans += (N-j)
            break

print(ans)


'''
array = [0] * 11   //무게별 개수 저장
for x in data:
    array[x] += 1

ans = 0
for i in range(1, M+1):
    N -= array[i]   //나보다 무거운 애들의 개수
    ans += (array[i] * N)   //i무게를 선택하는 경우의 수 * 걔보다 무거운 애들

'''
