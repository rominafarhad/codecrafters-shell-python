import sys

def main():
    # Infinite loop to keep the shell running
    while True:
        # Display the prompt symbol
        sys.stdout.write("$ ")
        sys.stdout.flush()

        # Wait for user input
        command = input()

        # Print error message for any command entered
        if command:
            print(f"{command}: command not found")

if __name__ == "__main__":
    main()