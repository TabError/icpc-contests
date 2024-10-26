
from collections import namedtuple

Point = namedtuple("Point", ['x', 'y'])

def readcomplex():
  return complex(*map(int, input().split()))

def printcomplex(c: complex):
  print(int(c.real), int(c.imag))

s = readcomplex()
t = readcomplex()
p = readcomplex()

bound = int(1e5)

A = complex(-bound, -bound)
B = complex(-bound, bound)
C = complex(bound, bound)
D = complex(bound, -bound)

diffx = s - p
if diffx.real > 0:
  if diffx.imag > 0:
    start = C
  else:
    start = D
else:
  if diffx.imag > 0:
    start = B
  else:
    start = A


difft = t - p
if difft.real > 0:
  if difft.imag > 0:
    end = C
  else:
    end = D
else:
  if difft.imag > 0:
    end = B
  else:
    end = A

rs = {
    (A, C): [B],
    (C, A): [B],
    (B, D): [A],
    (D, B): [A],
    }

if (start,end) in rs:
  inter = rs[(start, end)]
else:
  inter = []

route = [s + start, start, *inter, end, t + end]

# output
print(len(route))
for w in route:
  printcomplex(w)


