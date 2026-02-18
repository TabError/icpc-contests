import sys

def exit():
    print("impossible")
    sys.exit()

def main():
    n = int(input())
    distances = list()
    for i in range(n):
        distances.append(list(map(int, input().split())))

    flowers = [None] * n

    flowers[0] = int(2e9)
    flowers[1] = flowers[0] + distances[0][1]

    for i in range(2, n):
        la = flowers[0] - distances[0][i]
        ra = flowers[0] + distances[0][i]

        lb = flowers[1] - distances[1][i]
        rb = flowers[1] + distances[1][i]

        if la == lb or la == rb:
            flowers[i] = la
        elif ra == lb or ra == rb:
            flowers[i] = ra
        else:
            exit()

        for j in range(2, i):
            if abs(flowers[i] - flowers[j]) != distances[i][j]:
                exit()

    print(*flowers)

if __name__ == "__main__":
    main()

