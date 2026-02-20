def query_in(x):
    print("?", x, 0, flush=True)
    return input() == "in"

def main():
    x = 0

    while query_in(x):
        x += 1000

    while not query_in(x):
        pass

    print("!", x, flush=True)

if __name__ == "__main__":
    main()
