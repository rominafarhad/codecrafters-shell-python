import sys
import os

def main():
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

        if command == "exit" and args == ["0"]:
            sys.exit(0)
        
        elif command == "echo":
            print(" ".join(args))

        elif command == "type":
            cmd_to_check = args[0]
            if cmd_to_check in builtins:
                print(f"{cmd_to_check} is a shell builtin")
            else:
                # Search for the command in the PATH environment variable
                path_env = os.environ.get("PATH")
                found = False
                for path in path_env.split(":"):
                    full_path = os.path.join(path, cmd_to_check)
                    if os.path.isfile(full_path):
                        print(f"{cmd_to_check} is {full_path}")
                        found = True
                        break
                if not found:
                    print(f"{cmd_to_check}: not found")
            
        else:
            print(f"{user_input}: command not found")

if __name__ == "__main__":
    main()