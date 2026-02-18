INF = 10**18

def main():
    # read input
    n, x, r, d = map(int, input().split())
    winds =list(map(int, input().split()))

    # calculate prefix sum for sailing with the wind and only rowing if there is no wind
    prefix_rows = [0]
    for w in winds:
        prefix_rows.append(prefix_rows[-1] + (1 - w) * x)

    dp = [INF] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        # simple row from last step
        dp[i] = min(dp[i], dp[i - 1] + x)

        # use the sail until here
        start = max(0, i - d)
        dp[i] = min(dp[i], dp[start] + r + prefix_rows[i] - prefix_rows[start])

    # output result
    print(dp[-1])


if __name__ == "__main__":
    main()
