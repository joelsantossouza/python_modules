import sys

if __name__ == "__main__":
    print("=== Command Quest ===")
    argc: int = len(sys.argv)
    if argc < 2:
        print("No arguments provided!")
    print(f"Program name: {sys.argv[0]}")
    if argc >= 2:
        print(f"Arguments received: {argc - 1}")
        i: int = 1
        while (i < argc):
            print(f"Argument {i}: {sys.argv[i]}")
            i += 1
    print(f"Total arguments: {argc}")
