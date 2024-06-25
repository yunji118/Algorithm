import sys

input = sys.stdin.readline

N, M = map(int, input().split())

time = list(map(int, input().split()))


if N < M:
    print(N)
else:
    start = 0  #여기서 틑림,,, min(time)이 아님!!
    end = int(2e9) * 10000

    NTime = 0  #N명을 태웠을 때의 시간
    while start <= end:
        mid = (start + end) // 2

        ## mid 분까지 탔던 사람의 수
        cnt = M
        for i in range(M):
            cnt += (mid // time[i])

        if cnt >= N: # N명 이상을 태웠을 경우
            NTime = mid
            end = mid - 1
        else:
            start = mid + 1

    # NTime - 1에 탑승한 아이들이 몇명인지 계산
    cnt = M  #처음에 M명 태우고 시작
    for i in range(M):
        cnt += (NTime - 1) // time[i]

    # 위의 연산으로 인해 현재 NTime - 1까지 놀이기구를 탄 아이들의 숫자가 cnt에 저장되어 있음
    # NTime에 마지막 아이가 탑승한 기구의 번호를 계산
    for i in range(M):
        if NTime % time[i] == 0:  #NTime에 현재 비어있는 놀이기구인가 확인. NTime을 나눴을 때 나머지가 0이면 현재 비어있음
            cnt += 1  #1명 태우기
        if cnt == N:  #N번째 아이면 번호 출력
            print(i+1)
            break
