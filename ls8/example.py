import sys

PRINT_BEEJ = 1
HALT = 2
PRINT_NUM = 3
# 3 takes argument
SAVE = 4 #Saves value to register
PRINT_REGISTER = 5
ADD = 6

memory = [0] * 256


register = [0] * 8

pc = 0
running = True


def load_memory(filename):
    if len(sys.argv) != 2:
    print("Usage: file.py filename", file=sys.stderr)
    sys.exit(1)

    try:
        with open(sys.argv[1]) as f:
            commands = []
            for line in f:
                # Ignore comments
                comment_split = line.split('#')
                val = comment_split[0]
                x = (val, 2)
                print(f'{x:08b}:{x:d}')
                commands.append(x)
            # print(commands)
            
    except FileNotFoundError:
        print(f'{sys.argv[0]} : {sys.argv[1]} Not found')
        sys.exit(2)

while running:
    # execute instruction sin memory

    command = memory[pc]

    if command == PRINT_BEEJ:
        print("BEEJ")
        pc +=1

    elif command == PRINT_NUM:
        num = memory[pc + 1]
        print(num)
        pc += 2

    elif command == HALT:
        running = False

    elif command == SAVE:
        num = memory[pc + 1]
        reg = memory[pc + 2]
        register[reg] = num
        pc += 3

    elif command == ADD:
        reg_a = memory[pc + 1]
        reg_b = memory[pc + 2]
        register[reg_a] += register[reg_b]
        pc +=3
    
    elif command == PRINT_REGISTER:
        reg = memory[pc + 1]
        print(register[reg])
        pc +=2

    else: 
        print(f"Error: Unknown command: {command}")
        sys.exit(1)