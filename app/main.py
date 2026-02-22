import sys
import os

def main():
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

        if command == "exit":
            sys.exit(0)
        
        elif command == "echo":
            print(" ".join(args))

        elif command == "type":
            target = args[0]
            
            # 1. Check if it's a builtin
            if target in builtins:
                print(f"{target} is a shell builtin")
            else:
                # 2. Search in PATH
                path_env = os.environ.get("PATH")
                found = False
                
                if path_env:
                    # Split PATH by the OS-specific separator (usually ':')
                    directories = path_env.split(os.pathsep)
                    for directory in directories:
                        full_path = os.path.join(directory, target)
                        # Check if file exists and is executable
                        if os.path.isfile(full_path) and os.access(full_path, os.X_OK):
                            print(f"{target} is {full_path}")
                            found = True
                            break
                
                if not found:
                    print(f"{target}: not found")
            
        else:
            print(f"{command_input}: command not found")

if __name__ == "__main__":
    main()