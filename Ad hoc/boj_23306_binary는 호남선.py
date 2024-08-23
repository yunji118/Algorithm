import sys

input = sys.stdin.readline

N = int(input())  #철로의 길이


#질문출력
print("? 1")
sys.stdout.flush()
a = int(input())

print(f"? {N}")   #f를 이용해서 위에 입력받은 N을 숫자로 출력하기 
sys.stdout.flush()
b = int(input())

if a == 1 and b == 0:
    print("! -1")
elif a == 0 and  b == 1:
    print("! 1")
else:
    print("! 0")

sys.stdout.flush()
