import sys
import os
import subprocess
import shlex

def main():
    # Final list of core built-in commands
    builtins = ["exit", "echo", "type", "cd", "pwd"]

    while True:
        try:
            # Display prompt
            sys.stdout.write("$ ")
            sys.stdout.flush()
            
            # Read input
            command_input = input()
            if not command_input.strip():
                continue

            # Advanced parsing using shlex for all quote types and backslashes
            parts = shlex.split(command_input)
            if not parts:
                continue
                
            command = parts[0]
            args = parts[1:]

            # 1. Exit Logic
            if command == "exit":
                code = int(args[0]) if args else 0
                sys.exit(code)
            
            # 2. Echo Logic
            elif command == "echo":
                print(" ".join(args))
                
            # 3. PWD Logic
            elif command == "pwd":
                print(os.getcwd())

            # 4. Type Logic (Searching builtins and PATH)
            elif command == "type":
                cmd_name = args[0]
                if cmd_name in builtins:
                    print(f"{cmd_name} is a shell builtin")
                else:
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
            
            # 5. CD Logic
            elif command == "cd":
                path = args[0] if args else os.path.expanduser("~")
                if path == "~":
                    path = os.path.expanduser("~")
                try:
                    os.chdir(path)
                except Exception:
                    print(f"cd: {path}: No such file or directory")

            # 6. External Program Execution
            else:
                path_env = os.environ.get("PATH", "")
                executable_found = False
                for path in path_env.split(os.pathsep):
                    full_path = os.path.join(path, command)
                    if os.path.isfile(full_path) and os.access(full_path, os.X_OK):
                        subprocess.run([full_path] + args)
                        executable_found = True
                        break
                
                if not executable_found:
                    print(f"{command}: command not found")

        except EOFError:
            break
        except Exception as e:
            # Catch-all for any unexpected errors to keep the shell alive
            pass

if __name__ == "__main__":
    main()