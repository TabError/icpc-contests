N, P = map(int, input().split())

t = 0
n = N

# print(N, P)

if N % 2 == 0:
  N -= P
  t += 1

  N //= 2
  lps = N//P
  N -= lps * P
  t += 2 * lps

  # print(lps, t)
  # print("N", N)

  if 2 * N == P:
    t += 1

else:
  N -= P
  t += 1

  N //= 2
  lps = N//P
  N -= lps * P
  t += 2 * lps
  # print(lps, t)

print(n - P * t)

