import sys

def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        try:
            user_input = input()
        except EOFError:
            break

        if not user_input:
            continue

        # Split the input into command and arguments
        # Example: "echo hello world" -> ["echo", "hello", "world"]
        parts = user_input.split()
        command = parts[0]
        args = parts[1:]

        if command == "exit" and args == ["0"]:
            sys.exit(0)
        
        # New Feature: Handle the 'echo' command
        elif command == "echo":
            # Join the arguments back with a space and print
            print(" ".join(args))
            
        else:
            print(f"{user_input}: command not found")

if __name__ == "__main__":
    main()