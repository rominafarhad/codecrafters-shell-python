import sys

def main():
    # REPL: Read-Eval-Print Loop
    while True:
        # 1. READ: Display prompt and wait for input
        # Using write and flush to ensure '$ ' appears without a newline
        sys.stdout.write("$ ")
        sys.stdout.flush()

        try:
            command = input()
        except EOFError:
            break # Exit if the input stream is closed

        # 2. EVAL & 3. PRINT:
        # Since we are in the early stages, every command is "not found"
        if command:
            print(f"{command}: command not found")
        
        # 4. LOOP: The 'while True' handles the looping back to Step 1
        
if __name__ == "__main__":
    main()