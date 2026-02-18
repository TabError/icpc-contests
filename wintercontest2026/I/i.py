_, a, b = input(), input(), input()

wrongs = [i for i, (ac, bc) in enumerate(zip(a, b)) if ac != bc]
alts = (a[j] if i % 2 else b[j] for i, j in enumerate(wrongs))
res = [ac if ac == bc else next(alts) for ac, bc in zip(a, b)]
print("".join(res))
