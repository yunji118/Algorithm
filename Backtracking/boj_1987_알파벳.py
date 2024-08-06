import sys
input = sys.stdin.readline

R, C = map(int, input().split())
board = [input().rstrip() for _ in range(R)]
# s = set(board[0][0])
alpha = [False] * 26
alpha[ord(board[0][0]) - ord('A')] = True
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
ans = 0

def backtracking(r, c, cnt):
    global ans
    ans = max(ans, cnt)

    for i in range(4):
        nr, nc = r + d[i][0], c + d[i][1]
        if nr < 0 or nr >= R or nc < 0 or nc >= C:
            continue
        if not alpha[ord(board[nr][nc]) - ord('A')]:
            # s.add(board[nr][nc])
            alpha[ord(board[nr][nc]) - ord('A')] = True
            backtracking(nr, nc, cnt + 1)
            alpha[ord(board[nr][nc]) - ord('A')] = False
            # s.remove(board[nr][nc])



backtracking(0, 0, 1)
print(ans)

''''
pypy3으로 통과
set은 best에 O(1)인데 worst일 경우 O(n)이라 시간초과가 날 수도 있다
그래서 alpha 배열을 통해 이전에 나왔었는지 체크함
'''
