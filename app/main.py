import sys

def main():
    # List of commands that are built into our shell
    builtins = ["exit", "echo", "type"]

    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        try:
            user_input = input()
        except EOFError:
            break

        if not user_input:
            continue

        parts = user_input.split()
        command = parts[0]
        args = parts[1:]

        # Handle 'exit 0'
        if command == "exit" and args == ["0"]:
            sys.exit(0)
        
        # Handle 'echo'
        elif command == "echo":
            print(" ".join(args))

        # Handle 'type'
        elif command == "type":
            if args[0] in builtins:
                print(f"{args[0]} is a shell builtin")
            else:
                print(f"{args[0]}: not found")
            
        else:
            print(f"{user_input}: command not found")

if __name__ == "__main__":
    main()