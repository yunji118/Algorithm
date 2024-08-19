import sys

input = sys.stdin.readline

N, K = map(int, input().split())

ans = int(1e9)
def bruteforce(num, cnt):
    global ans

    if num == 1:
        ans = min(ans, cnt)
        return

    if num < 1:
        return

    bruteforce(num - 1, cnt + 1)
    bruteforce(num // K, cnt + 1)

bruteforce(N, 0)
print(ans)


'''

while True:
    div = (N // K) * K    //K로 나눠 떨어지는 수
    ans += (N - div)   // K로 나눠 떨어지는 수를 만들기 위한 -1의 연산 횟수
    N = div
    
    if N < K:  //K로 나눌 수 없는 경우
        break
    
    //K로 나누기
    N //= K
    ans += 1
   
ans += (N - 1) //남은 수에 대해 1씩 빼기
 
'''
