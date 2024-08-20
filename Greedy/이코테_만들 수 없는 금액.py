import sys

input = sys.stdin.readline

N = int(input())
coin = list(map(int, input().split()))
possible = set()

visited = [False] * N
def bruteforce(now, money):
    if now == N:
        possible.add(money)
        return

    for i in range(now, N):
        if not visited[i]:
            visited[i] = True
            possible.add(money + coin[i])
            bruteforce(i+1, money + coin[i])
            visited[i] = False


bruteforce(0, 0)

i = 1
while True:
    if i not in possible:
        print(i)
        exit(0)
    i += 1

'''
아이디어: 1 ~ target - 1원까지 만들 수 있다고 가정.
 화폐 단위가 작은 동전부터 하나씩 확인하면서 새로 추가되는 동전을 이용해 target 금액을 만들 수 있는지 확인하기
 

1. 동전을 오름차순으로 정렬
2. 동전을 1개씩 추가하면서 target값을 추가되는 동전 금액 만큼 더해주기. target += coin[i]
3. 추가된 동전 <= target -> 추가된 동전을 이용해서 target값을 만들 수 있음
4. 추가된 동전 > target -> 추가된 동전을 이용해서 target값을 만들 수 없음


  1      2              3               5               13
t=1    t=2 (0~1가능)     t=4 (0~3가능)    t=7 (0~6가능)    t=12 (0~11가능)
       2 만들 수 있음      4 만들 수 있음     7 만들 수 있음     13과 0~11을 조합해서 12를 만들 수 없음 


target = 1

for c in coin:
    if c > target:
        break
    target += c
    


'''
