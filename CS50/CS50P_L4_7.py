# Practice program building custom libraries (Part 1)

def main():
    hello("world")
    goodbye("world")

def hello(name):
    print(f"hello, {name}")

def goodbye(name):
    print(f"goodbye, {name}")

if __name__ == "__main__":
    main()