import sys
import os
import subprocess
import shlex

def main():
    # Adding 'pwd' to builtins as we'll use it often
    builtins = ["exit", "echo", "type", "cd", "pwd"]

    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        
        try:
            command_input = input()
            # shlex.split handles single and double quotes automatically!
            parts = shlex.split(command_input)
        except EOFError:
            break
        except ValueError as e:
            # Handle cases where quotes are not closed
            print(f"shell: {e}")
            continue
            
        if not parts:
            continue
            
        command = parts[0]
        args = parts[1:]

        # 1. Exit command
        if command == "exit" and args == ["0"]:
            sys.exit(0)
        
        # 2. Echo command (shlex handles the quotes, we just join args)
        elif command == "echo":
            print(" ".join(args))
            
        # 3. PWD command
        elif command == "pwd":
            print(os.getcwd())

        # 4. Type command
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
        
        # 5. CD command
        elif command == "cd":
            path = args[0] if args else "~"
            if path == "~":
                path = os.path.expanduser("~")
            try:
                os.chdir(path)
            except Exception as e:
                print(f"cd: {args[0]}: No such file or directory")

        # 6. External Programs
        else:
            path_env = os.environ.get("PATH", "")
            found = False
            for path in path_env.split(os.pathsep):
                full_path = os.path.join(path, command)
                if os.path.isfile(full_path) and os.access(full_path, os.X_OK):
                    subprocess.run([full_path] + args)
                    found = True
                    break
            if not found:
                print(f"{command}: command not found")

if __name__ == "__main__":
    main()