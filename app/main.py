import sys

def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        # Wait for user input
        command = input()

        # Check if the command is 'exit 0'
        if command == "exit 0":
            sys.exit(0)
        # If it's any other command, show error
        elif command:
            print(f"{command}: command not found")

if __name__ == "__main__":
    main()