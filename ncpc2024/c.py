n = int(input())

l = []
if n % 2:
  l.append(3)
  n -= 3
while n > 0:
  l.append(2)
  n -= 2

print(len(l))
print(*l)
