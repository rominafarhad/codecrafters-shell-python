import sys
import os
import subprocess
import shlex

def main():
    builtins = ["exit", "echo", "type", "cd", "pwd"]

    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        
        try:
            command_input = input()
            # Use shlex.split to handle complex quoting and backslashes
            parts = shlex.split(command_input)
        except EOFError:
            break
        except ValueError as e:
            print(f"shell: {e}")
            continue
            
        if not parts:
            continue
            
        command = parts[0]
        args = parts[1:]

        # Handle 'exit'
        if command == "exit" and args == ["0"]:
            sys.exit(0)
        
        # Handle 'echo'
        elif command == "echo":
            # shlex handles the parsing, we just join with single space
            print(" ".join(args))
            
        # Handle 'pwd'
        elif command == "pwd":
            print(os.getcwd())

        # Handle 'type'
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
        
        # Handle 'cd'
        elif command == "cd":
            path = args[0] if args else "~"
            if path == "~":
                path = os.path.expanduser("~")
            try:
                os.chdir(path)
            except Exception:
                print(f"cd: {args[0]}: No such file or directory")

        # Handle External Programs
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