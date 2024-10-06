N = int(input())
A, B = map(int, input().split())

# dp = []

# dp[0] = [1 for _ in range(N)]


def solve():
  global A, B, N
  if A * B < N:
    return 0
  if A == 1 or B == 1:
    return 1

  # now we know: both are at least 2

  l = [A, B]
  A = min(l)
  B = max(l)

  dp = dict()

  tod = 2
  dp[1] = [0] * tod * (N + 1)
  dp[1][N-1] = 1

  # dp[2] = [0] * tod * (N + 1)
  # for i in range(N):
  #   dp[2][i] = sum(dp[1][1+i::1])

  # dp[3] = [0] * tod * (N + 1)
  # for i in range(N):
  #   dp[3][i] = sum(dp[2][1+i::2])

  for rowid in range(2, A+1):
    # the stuff ...
    dp[rowid] = [0] * tod * N
    for i in range(N):
      dp[rowid][i] = sum(dp[rowid-1][1+i::rowid-1])

  
  for k, l in dp.items():
    print(f"using {k} rows")
    for i in range(8):
      print(f"with {i} full cols:", dp[k][i*k])
    print("summing to:", sum(dp[k][0::k]))
    print(*l)


print(solve())

