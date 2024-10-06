
s = int(input(), 2)
d = int(input(), 2)
# m = list(input())
m = int(input(), 2)

# print(s, d, m)

# def add(a: list, b: list):
#   A = "".join(a)
#   B = "".join(b)
#   r = int(A, 2) + int(B, 2)
#   return list(bin(r)[2:])

r = None
for i in range(10024):
  if m == 0:
    r = i
    break

  # m.pop()
  m //= 2

  if (i + 1) % d == 0:
    # print("get money on", i)
    # print(M)

    # m = add(m, s)
    m += s
    # print(M)

if r is None:
  print("Infinite money!")
else:
  print(bin(r)[2:])


