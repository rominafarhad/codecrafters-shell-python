import sys

def main():
    while True:
        # Display the prompt
        sys.stdout.write("$ ")
        sys.stdout.flush()

        try:
            # Read user input
            user_input = input()
        except EOFError:
            break

        # Stage: Implement exit builtin
        if user_input == "exit 0":
            sys.exit(0)
        
        # Handle invalid commands
        elif user_input:
            print(f"{user_input}: command not found")

if __name__ == "__main__":
    main()