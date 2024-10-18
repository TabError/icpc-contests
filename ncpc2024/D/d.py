from math import ceil, log2

# ===== from reference =====
# Global functions for index calculations
def pa(x):
    return x // 2

def lc(x):
    return 2 * x

def rc(x):
    return 2 * x + 1

FUNC = lambda x, y: max(x,y)
NEUTRAL = -(1 << 30)

class TournamentTree:
  def __init__(self, a: list):
    self.N = 1 << ceil(log2(len(a)))
    self.t = [NEUTRAL] * self.N * 2
    self.t[self.N : self.N + len(a)] = a
    for i in reversed(range(1, self.N)):
      self.t[i] = FUNC(self.t[lc(i)], self.t[rc(i)])

  def get(self, l, r):
    l += self.N; r += self.N
    res = NEUTRAL
    while l <= r and (l != 1 or r != 1):
      if l % 2 == 1:
        res = FUNC(res, self.t[l])
        l += 1
      if r % 2 == 0:
        res = FUNC(res, self.t[r])
        r -= 1
      l = pa(l); r = pa(r)
    return res

  def set(self, p, val):
    p += self.N
    self.t[p] = val
    while p > 1:  # <=> while p != pa(p)
      p = pa(p)
      self.t[p] = FUNC(self.t[lc(p)], self.t[rc(p)])
# ===== from reference =====
# the get method here is inclusive
# i.e. get(l, r) gets [l, r]


# # Example usage
# if __name__ == '__main__':
#     array = [1, 3, 5, 7, 9, 11]
#     itree = TournamentTree(array)
#     print(itree.get(1, 4))  # Example query
#     itree.set(3, 0)          # Example update
#     print(itree.get(1, 4))  # Example query after update


# task spedific

N, K = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

from collections import defaultdict


def solve():
  # preps
  d = defaultdict(list)

  for i, v in enumerate(b):
    d[v].append(i + 1)

  matches = [ NEUTRAL ] * (N * K + 9)
  matches[0] = 0

  it = TournamentTree(matches)

  # solve loop
  for card in a:
    for matchpos in reversed(d[card]):
      matchno = it.get(0, matchpos - 1)
      it.set(matchpos, matchno + 1)

  return it.get(0, N*K + 5)


print(solve())

