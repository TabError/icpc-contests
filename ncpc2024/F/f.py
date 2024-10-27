from collections import defaultdict
from cmath import phase

from math import isclose, tau

from bisect import bisect


def readfence() -> tuple([complex, complex]):
  x, y, xx, yy = map(int, input().split())
  return complex(x, y), complex(xx, yy)

def clockwise(ls: list) -> bool:
  conns = [b - a for a, b in zip(ls, ls[1:])]
  conns.append(ls[0] - ls[-1])

  phases = [phase(b / a) for a, b in zip(conns, conns[1:])]
  phases.append(phase(conns[0] / conns[-1]))
  s = sum(phases)

  assert isclose(abs(s), tau)
  return isclose(s, -tau)

def cross(a, b):
  return (a.conjugate() * b).imag

def area(ls: list) -> float:
  vals = [cross(ls[i - 1] - ls[0], ls[i] - ls[0]) for i in range(2, len(ls))]
  return abs(sum(vals)) / 2


def solve():
  f = int(input())
  fences = [readfence() for _ in range(f)]

  # corners = set(c for f in fences for c in f)

  usings = defaultdict(int)
  unused = defaultdict(set)
  for a, b in fences:
    usings[a] += 1
    usings[b] += 1
    unused[a].add(b)
    unused[b].add(a)

  # adj lists must be sorted to efficiently get next points
  adj = { p : list(sorted([(phase(e - p), e) for e in l])) for p, l in unused.items() }


  faces = []
  while len(usings) > 0:
    start = next(iter(usings))
    last = start

    curr = unused[last].pop()
    usings[curr] -= 1
    if usings[curr] == 0:
      del usings[curr]

    ls = [curr]
    while curr != start:
      dire = phase(last - curr)
      last = curr

      # print(adj[last], (dire, last))
      idx = bisect(adj[last], dire, key = lambda t: t[0])
      if idx == len(adj[last]):
        idx = 0

      _, curr = adj[last][idx]

      # update
      unused[last].remove(curr)
      usings[curr] -= 1
      if usings[curr] == 0:
        del usings[curr]
      ls.append(curr)

    # print("finished one area")
    if clockwise(ls):
      faces.append(ls)

  return sum(area(f) ** 2 for f in faces)


res = solve()
print(res)

