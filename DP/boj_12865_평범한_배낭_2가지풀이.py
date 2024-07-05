import sys

input = sys.stdin.readline

N, K = map(int, input().split()) #물품의 수, 버틸 수 있는 무게

W = []
V = []

for _ in range(N):
    w, v = map(int, input().split())
    W.append(w)
    V.append(v)

W = [0] + W
V = [0] + V

# dp = [[0] * (N+1) for _ in range(K+1)]
#
#
# for i in range(1, K+1): #무게
#     for j in range(1, N+1): #물품
#         dp[i][j] = dp[i][j-1] #기본 값은 현재 물품을 담지 않은 경우
#
#         if i - W[j] >= 0: #현재 무게에 물품을 담을 수 있으면
#             dp[i][j] = max(dp[i][j], dp[i - W[j]][j-1] + V[j])
#
# print(dp[K][N])
'''
    물품0 물품1 물품2
무게0
무게1
무게2

'''

dp = [[0] * (K+1) for _ in range(N+1)]

for i in range(1, N+1):  #물품
    for j in range(1, K+1):  #무게
        dp[i][j] = dp[i-1][j]

        if j >= W[i]:
            dp[i][j] = max(dp[i][j], dp[i-1][j-W[i]] + V[i])
        ## dp[i-1][j-W[i]] 에서 i-1을 간과함!! 이전 물품까지 고려했을 때를 해야함

print(dp[N][K])




'''
    무게0 무게1 무게2
물품0
물품1
물품2

'''
