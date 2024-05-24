import sys


def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        command, *args = input().split(" ")

        if command == "exit":
            exit_code = int(args[0]) if args else 0
            sys.exit(exit_code)
        elif command == "echo":
            print(" ".join(args))
        else:
            print(f"{command}: command not found")

        sys.stdout.flush()


if __name__ == "__main__":
    main()
