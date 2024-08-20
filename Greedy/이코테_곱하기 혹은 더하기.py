import sys

input = sys.stdin.readline

number = list(map(int, input().rstrip()))

ans = 0
for i in range(len(number)):
    if number[i] <= 1 or ans <= 1:  #0일 때가 아니라 1일때!! 111의 경우 1+1+1이 유리하므로
        ans += number[i]
    else:
        ans *= number[i]

print(ans)
