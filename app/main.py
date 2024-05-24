import sys


def handle_exit(args):
    sys.exit(int(args[0]) if args else 0)


def handle_echo(args):
    print(" ".join(args))


def handle_type(args):
    if args[0] in builtins:
        print(f"{args[0]} is a shell builtin")
    else:
        print(f"{args[0]} not found")


builtins = {
    "exit": handle_exit,
    "echo": handle_echo,
    "type": handle_type,
}


def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        command, *args = input().split(" ")

        if command in builtins:
            builtins[command](args)
            continue
        else:
            print(f"{command}: command not found")

        sys.stdout.flush()


if __name__ == "__main__":
    main()
