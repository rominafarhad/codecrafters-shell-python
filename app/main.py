import sys

def main():
    while True:
        # Display the prompt
        sys.stdout.write("$ ")
        sys.stdout.flush()
        
        # Read user input
        command_input = input()

        # Handle the 'exit 0' command to terminate the shell
        if command_input == "exit 0":
            sys.exit(0)
        
        # Handle the 'echo' command to print arguments
        elif command_input.startswith("echo "):
            # Extract everything after "echo " (5 characters)
            text_to_print = command_input[5:]
            print(text_to_print)
            
        else:
            # Handle unknown commands
            print(f"{command_input}: command not found")

if __name__ == "__main__":
    main()