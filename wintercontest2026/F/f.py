# OMG solving this problem with python was so incredibly painful.
# python not only has its recursion limit at ~1000. But the stack for recursion has probably overflown with the initial recursive approach. So just sys.setrecursionlimit(10**7) doesn't suffice. (btw setrecursionlimit is also capped internally. docs say it is platform dependent.) In python stack is kinda huge and not very well optimized, so i transformed the recursion into an iterative function ...

# import sys
# sys.setrecursionlimit(3 * 10 ** 5)

seen = set()
adj = dict()
min_element = dict()


def dfs(node):
    seen.add(node)
    for child in adj[node]:
        if child in seen:
            continue
        dfs(child)
        min_element[node] = min(min_element[node], child, min_element[child])


def dfs_iterative(root):
    stack = [(root, 0)]  # (node, parent)
    order = []

    while stack:
        node, parent = stack.pop()
        order.append((node, parent))
        for child in adj[node]:
            if child != parent:
                stack.append((child, node))

    # postorder processing
    for node, parent in reversed(order):
        for child in adj[node]:
            if child != parent:
                min_element[node] = min(min_element[node], child, min_element[child])


def main():
    n = int(input())
    nodelist = list(range(1, n + 1))
    for v in nodelist:
        adj[v] = []
        min_element[v] = n + 1

    for _ in range(n - 1):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)

    # dfs(1)
    dfs_iterative(1)

    # results
    results = []
    for v in nodelist:
        if v == 1:
            min_value = n + 1
            for child in adj[v]:
                if min(min_element[child], child) != 2:
                    min_value = min(min_value, child, min_element[child])
        else:
            min_value = min_element[v]
        results.append(min_value - 1)

    print(*results)


if __name__ == "__main__":
    main()
