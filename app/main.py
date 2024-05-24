import sys


def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        command, *args = input().split(" ")

        if command == "exit":
            exit_code = int(args[0]) if args else 0
            sys.exit(exit_code)
        else:
            sys.stdout.write(f"{command}: command not found\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
