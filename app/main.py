import sys

def main():
    # Loop forever to keep the shell active
    while True:
        # Display the prompt for the user
        sys.stdout.write("$ ")
        sys.stdout.flush()

        # Wait for user input
        command = input()

        # Handle the 'exit 0' command specifically
        if command == "exit 0":
            sys.exit(0)
        # For any other command, show the 'not found' message
        elif command:
            print(f"{command}: command not found")

if __name__ == "__main__":
    main()