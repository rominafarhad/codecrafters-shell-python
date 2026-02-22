import sys

def main():
    # REPL: Read-Eval-Print Loop
    while True:
        # Display prompt
        sys.stdout.write("$ ")
        sys.stdout.flush()

        try:
            command = input()
        except EOFError:
            break

        # Check if the command is 'exit 0'
        if command == "exit 0":
            sys.exit(0)
        # For any other command, show the 'not found' message
        elif command:
            print(f"{command}: command not found")

if __name__ == "__main__":
    main()