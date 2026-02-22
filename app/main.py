import sys
import os

def main():
    # List of shell built-in commands
    builtins = ["exit", "echo", "type"]

    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        
        command_input = input()
        parts = command_input.split()
        if not parts:
            continue
            
        command = parts[0]
        args = parts[1:]

        # 1. Handle 'exit 0'
        if command == "exit" and args == ["0"]:
            sys.exit(0)
        
        # 2. Handle 'echo'
        elif command == "echo":
            print(" ".join(args))
            
        # 3. Handle 'type'
        elif command == "type":
            cmd_name = args[0]
            if cmd_name in builtins:
                print(f"{cmd_name} is a shell builtin")
            else:
                # Look for the command in the PATH environment variable
                path_env = os.environ.get("PATH", "")
                found = False
                for path in path_env.split(os.pathsep):
                    full_path = os.path.join(path, cmd_name)
                    if os.path.isfile(full_path) and os.access(full_path, os.X_OK):
                        print(f"{cmd_name} is {full_path}")
                        found = True
                        break
                if not found:
                    print(f"{cmd_name}: not found")
                
        else:
            # Handle unknown commands
            print(f"{command_input}: command not found")

if __name__ == "__main__":
    main()