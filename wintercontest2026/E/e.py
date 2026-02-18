def main():
    n, k = map(int, input().split())

    if n == 1:
        print("impossible")
        return

    first_points = 0
    other_points = 0

    # all players are right in all rounds except the last round
    # while right, they accumulate points
    for i in range(1, n):
        print(i, i, *([0, 0] * (k - 1)))
        first_points += 2 + i
        other_points += 2

    # now negate all gained points in one round
    print(n + first_points, n, *([other_points, 0] * (k - 1)))

if __name__ == "__main__":
    main()
