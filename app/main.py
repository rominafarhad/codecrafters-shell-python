import sys

def main():
    # List of built-in commands we have implemented so far
    builtins = ["exit", "echo", "type"]

    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        try:
            command_input = input()
        except EOFError:
            break

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
            print(" ".join(args))

        # Handle 'type' command
        elif command == "type":
            if args[0] in builtins:
                print(f"{args[0]} is a shell builtin")
            else:
                print(f"{args[0]}: not found")
            
        # Handle unknown commands
        else:
            print(f"{command_input}: command not found")

if __name__ == "__main__":
    main()