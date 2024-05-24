import os
import sys

from typing import Optional


def locate_executable(command) -> Optional[str]:
    path = os.environ.get("PATH", "")

    for directory in path.split(":"):
        file_path = os.path.join(directory, command)

        if os.path.isfile(file_path) and os.access(file_path, os.X_OK):
            return file_path


def handle_exit(args):
    sys.exit(int(args[0]) if args else 0)


def handle_echo(args):
    print(" ".join(args))


def handle_type(args):
    if args[0] in builtins:
        print(f"{args[0]} is a shell builtin")
    elif executable := locate_executable(args[0]):
        print(f"{args[0]} is {executable}")
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
