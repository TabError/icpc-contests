import heapq

def main():
    n, k = map(int, input().split())
    apples = [tuple(map(int, input().split())) for _ in range(n * k)]
    apples.sort()

    res = 0
    h = []
    for i in range(n * k):
        heapq.heappush(h, -apples[i][1])
        if i % n == 0:
            res -= heapq.heappop(h)
    print(res)


if __name__ == "__main__":
    main()
