import sys, heapq

input = sys.stdin.readline

N, K = map(int, input().split())  # N:수빈  K:동생


time = [int(1e9)] * 100001
def dijkstra(start):
    h = []

    time[start] = 0
    heapq.heappush(h, [0, start])  #[걸린 시간, 위치]
    while h:
        cost, now = heapq.heappop(h)

        if time[now] < cost:
            continue

        if 0 <= now - 1 <= 100000 and cost + 1 < time[now - 1]:
            time[now - 1] = cost + 1
            heapq.heappush(h, [cost + 1, now - 1])

        if 0 <= now + 1 <= 100000 and cost + 1 < time[now + 1]:
            time[now + 1] = cost + 1
            heapq.heappush(h, [cost + 1, now + 1])

        # print("now = ", now)
        if 0 <= now * 2 <= 100000 and cost < time[now * 2]:
            time[now * 2] = cost
            heapq.heappush(h, [cost, now * 2])


dijkstra(N)
print(time[K])
