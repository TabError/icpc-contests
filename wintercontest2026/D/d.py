#!/usr/bin/env python3

import sys

def query_in(x):
    print("?", x, 0)
    sys.stdout.flush()
    return input() == "in"

def main():
    x = 0

    while query_in(x):
        x += 1000

    while not query_in(x):
        pass

    print("!", x)
    sys.stdout.flush()

if __name__ == "__main__":
    main()
