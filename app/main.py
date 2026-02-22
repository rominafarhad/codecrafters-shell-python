import sys

def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        try:
            command_input = input()
        except EOFError:
            break

        # Split the input into parts (command and arguments)
        # Example: "echo hello world" -> ["echo", "hello", "world"]
        parts = command_input.split()
        
        if not parts:
            continue

        command = parts[0]
        args = parts[1:]

        # Handle 'exit' command
        if command == "exit":
            sys.exit(0)
        
        # Handle 'echo' command
        elif command == "echo":
            # Print all arguments joined by a single space
            print(" ".join(args))
            
        # Handle unknown commands
        else:
            print(f"{command_input}: command not found")

if __name__ == "__main__":
    main()