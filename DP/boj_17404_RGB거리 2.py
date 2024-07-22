import sys

input = sys.stdin.readline

N = int(input()) #집의 수

cost = []

for _ in range(N):
    cost.append(list(map(int, input().split())))

ans = int(1e9)

for i in range(3):
    dp = [[int(1e9)] * 3 for _ in range(N)]
    dp[0][i] = cost[0][i]  #첫번째 집의 색을 고정시키고 출발
    for j in range(1, N):
        dp[j][0] = min(dp[j-1][1], dp[j-1][2]) + cost[j][0]  #현재 집을 빨간색으로 칠하기
        dp[j][1] = min(dp[j-1][0], dp[j-1][2]) + cost[j][1]  #현재 집을 초록색으로 칠하기
        dp[j][2] = min(dp[j-1][0], dp[j-1][1]) + cost[j][2]  #현재 집을 파랑색으로 칠하기

    dp[N-1][i] = int(1e9)  #첫번째집과 N번째집이 같은 색상인 경우 -> 큰 수 넣어서 무효화시키기
    ans = min(ans, dp[N-1][0], dp[N-1][1], dp[N-1][2])

print(ans)



