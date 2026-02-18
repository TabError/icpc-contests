from collections import defaultdict


def read_input():
    n, m = map(int, input().split())

    adj = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)

    nodes = set(range(1, n + 1))
    nodes_of_deg = defaultdict(list)
    for node in nodes:
        deg = len(adj[node])
        nodes_of_deg[deg].append(node)

    return n, nodes_of_deg


def solve1():
    n, degs = read_input()

    if len(degs[0]) > 0:
        print(n)
        print(*range(1, n + 1))
    else:
        print(0)


def solve2():
    n, degs = read_input()

    if len(degs[n - 1]) > 0:
        assert len(degs[n - 1]) == 1
        print(degs[n - 1][0])
    else:
        assert len(degs[0]) == 1
        print(degs[0][0])


def main():
    mode = input()

    if mode == "1":
        solve1()
    elif mode == "2":
        solve2()
    else:
        raise ValueError("Invalid mode")


if __name__ == "__main__":
    main()
