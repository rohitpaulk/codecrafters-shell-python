import sys


def main():
    sys.stdout.write("$ ")
    sys.stdout.flush()

    command = input()
    sys.stdout.write(f"{command}: command not found\n")
    sys.stdout.flush()


if __name__ == "__main__":
    main()
