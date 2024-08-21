import heapq

def solution(food_times, k):
    if sum(food_times) <= k:  #전체 음식 먹는데 걸리는 시간이 k보다 작은 경우 (=모든 음식 다 먹음)
        return -1
    
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1))
    
    total_eat_time = 0 #먹는데 총 사용한 시간
    prev = 0 #직전 음식을 먹는데 걸린 시간
    
    length = len(food_times) #남은 음식의 개수
    
    #현재까지 음식 먹는데 소요한 시간 + (현재 음식 먹는데 걸리는 총 시간 - 이전에 먹은 시간) * 현재 음식 개수 <= K
    #만약 > k 라면 현재 음식을 다 먹을 수 없음!
    while total_eat_time + ((q[0][0] - prev) * length) <= k:
        now = heapq.heappop(q)[0]  #현재 음식 먹는데 걸리는 총 시간
        total_eat_time += ((now - prev) * length)
        length -= 1 #현재 음식 다 먹었으므로 남은 음식 개수에서 빼주기
        prev = now   #이전 음식 시간 재설정
        
    
    #현재 음식을 다 먹지 못하고 남은 음식 중에 몇 번째를 먹어야하는지 계산하기
    food = sorted(q, key=lambda x: x[1]) #음식 번호 기준으로 정렬
    answer = food[(k - total_eat_time) % length][1]
    
    
    return answer
