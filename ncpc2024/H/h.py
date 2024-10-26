s = input()

from collections import Counter

c = Counter(s)

for k, v in c.items():
  if not k.isspace(): 
    print(k, v)
