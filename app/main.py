import sys
import os
import subprocess

def find_in_path(command):
    path_env = os.environ.get("PATH")
    if path_env:
        directories = path_env.split(os.pathsep)
        for directory in directories:
            full_path = os.path.join(directory, command)
            if os.path.isfile(full_path) and os.access(full_path, os.X_OK):
                return full_path
    return None

def main():
    builtins = ["exit", "echo", "type", "pwd", "cd"]

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

        elif command == "pwd":
            print(os.getcwd())

        elif command == "cd":
            if args:
                path = args[0]
                # Handle relative and absolute paths
                try:
                    # os.chdir naturally understands '.', '..', and relative names
                    os.chdir(path)
                except (FileNotFoundError, NotADirectoryError):
                    print(f"cd: {path}: No such file or directory")
            
        elif command == "type":
            target = args[0]
            if target in builtins:
                print(f"{target} is a shell builtin")
            else:
                full_path = find_in_path(target)
                if full_path:
                    print(f"{target} is {full_path}")
                else:
                    print(f"{target}: not found")
        
        else:
            full_path = find_in_path(command)
            if full_path:
                subprocess.run([command] + args)
            else:
                print(f"{command}: command not found")

if __name__ == "__main__":
    main()