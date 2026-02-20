import heapq
n, k = map(int, input().split())
apples = sorted([tuple(map(int, input().split())) for _ in range(n * k)])
res, h = 0, []
for i in range(n * k):
    heapq.heappush(h, -apples[i][1])
    if i % n == 0:
        res -= heapq.heappop(h)
print(res)
