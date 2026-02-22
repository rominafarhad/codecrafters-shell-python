import sys

def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        try:
            command = input()
        except EOFError:
            break

        # Handle the 'exit' command
        # This will catch both 'exit' and 'exit 0'
        if command == "exit 0" or command == "exit":
            sys.exit(0)
            
        elif command:
            print(f"{command}: command not found")

if __name__ == "__main__":
    main()