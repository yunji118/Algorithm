import sys

input = sys.stdin.readline

N, M, K = map(int, input().split()) #N:배열의 크기 M:더하는 횟수 K:연속 가능

num = list(map(int, input().split()))

num.sort(reverse=True)

second = M // (K + 1)
first = M - second

print(num[0] * first + num[1] * second)
