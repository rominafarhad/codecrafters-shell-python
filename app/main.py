import sys

def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        try:
            command = input()
        except EOFError:
            break

        # Check if the command starts with 'exit'
        if command == "exit 0" or command == "exit":
            sys.exit(0)

        # Check if the command starts with 'echo '
        elif command.startswith("echo "):
            # We take everything after the first 5 characters ('echo ')
            message = command[5:]
            print(message)

        # For any other unknown command
        elif command:
            print(f"{command}: command not found")

if __name__ == "__main__":
    main()