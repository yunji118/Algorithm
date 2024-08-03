import sys
import heapq

input = sys.stdin.readline

N = int(input())
h = []

for _ in range(N):
    heapq.heappush(h, int(input()))

cnt = 0
while len(h) > 1:
    a = heapq.heappop(h)
    b = heapq.heappop(h)

    sum = a + b
    cnt += sum

    heapq.heappush(h, sum)

print(cnt)



'''
적은 애들부터 묶어야하는거 아닌가?
처음 2개 앞에서 pop해서 묶고
다시 넣고 
정렬
앞에서 2개 pop해서 묶고
다시 넣고
정렬



'''
