import itertools as it
from queue import Queue

K = int(input())

from collections import namedtuple

Point = namedtuple("Point", ['x', 'y'])

def readcomplex():
  return complex(*map(int, input().split()))

def printcomplex(c: complex):
  print(int(c.real), int(c.imag))


ls = [Point(*map(int, input().split())) for _ in range(K)]




offset = 22
offset = 4
squash = 4

dim = 10000
dim = 40
s = dim // squash + 2 * offset

T = -5
N = -4
P = -3
W = -2


grid = [[0] * s for _ in range(s)]
toBig = lambda p: Point(p.x // squash + offset, p.y // squash + offset)

adjacents = lambda p: [Point(p.x + dx, p.y + dy) for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]]
neighbors = lambda p: [Point(p.x + dx, p.y + dy) for dx, dy in it.product([-1, 0, 1], repeat = 2) if not (dx == 0 and dy == 0)]

def init():
  for p in ls:
    cx, cy = p = toBig(p)
    
    grid[cy][cx] = P
    for nx, ny in neighbors(p):
      grid[ny][nx] = N

def bfs(start):
  q = Queue()
  q.put(start)
  while not q.empty():
    c = q.get()
    for a in adjacents(c):
      if grid[a.y][a.x] == 0:
        grid[a.y][a.x] = grid[c.y][c.x] + 1
        q.put(a)
      if grid[a.y][a.x] == T:
        return a


def routeBig(a, b):
  # update grid i.e. set target T
  grid[a.y][a.x] = T
  for nx, ny in neighbors(a):
    if nx==a.x+1 and ny == a.y + 1:
      continue
    grid[ny][nx] = T


  # bfs
  entry = bfs(a)

  # small routing
  routeClose(entry, ...)




  # backtrack
  # find way bfs got and set it to W
  # append to list

  # clean grid
  # remove target and mark nears as 0
  # but care for the other Ns

def routeClose():
  pass


def main():
  init()
  print(*reversed(grid),sep = "\n")
  # cur = Point(0, 0)
  # for p in ls:

  #   palt = Point(p.x // squash + offset, p.y // squash + offset)
  #   routeBig(cur, p)
  #   cur = p



main()



