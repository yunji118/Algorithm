import sys

N, K = map(int, sys.stdin.readline().rstrip().split())

dp = [[0] * (K+1) for _ in range(N+1)] #dp[i][j] = i번째 물건까지 고려하고 허용 용량이 j일 때의 최대 가치

for i in range(1, N+1):
    W, V = map(int, sys.stdin.readline().rstrip().split())
    for j in range(1, K+1):
        if j >= W: #허용용량 >= 물건의 무게
            #Max(현재 물건을 담기 전의 최대 가치, 현재 물건을 담았을 때의 최대 가치(현재 물건 담기 전 + 현재 물건의 가치))
            #현재 물건을 담기 전의 최대 가치 = 이전 행의 값
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-W] + V)
        else: #허용용량 < 물건의 무게 -> 현재 보고있는 물건을 담지 못하는 경우
            dp[i][j] = dp[i-1][j] #이전 행의 값 저장

print(dp[N][K])
