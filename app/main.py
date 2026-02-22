import sys

def main():
    # List of built-in commands supported by our shell
    builtins = ["exit", "echo", "type"]

    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        
        command_input = input()

        # Handle 'exit 0'
        if command_input == "exit 0":
            sys.exit(0)
        
        # Handle 'echo'
        elif command_input.startswith("echo "):
            print(command_input[5:])
            
        # Handle 'type' (New Stage)
        elif command_input.startswith("type "):
            cmd_name = command_input[5:]
            if cmd_name in builtins:
                print(f"{cmd_name} is a shell builtin")
            else:
                print(f"{cmd_name}: not found")
                
        else:
            print(f"{command_input}: command not found")

if __name__ == "__main__":
    main()