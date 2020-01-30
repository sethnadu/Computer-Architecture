import sys

PRINT_BEEJ = 1
HALT = 2
PRINT_NUM = 3
# 3 takes argument
SAVE = 4 #Saves value to register
PRINT_REGISTER = 5
ADD = 6
PUSH = 7
POP = 8
CALL = 9
RET = 10


memory = [0] * 256
register = [0] * 8
pc = 0
# Register at index 7 (8)
sp = 7

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

    elif command == PUSH:
        reg = memory[pc + 1]
        value = register[reg]
        register[SP] -= 1
        memory[register[SP]] = val
        pc +=2
    
    elif command == POP:
        reg = memory[pc + 1]
        value = memory[register[sp]]
        register[reg] = value
        pc +=2
    
    elif command = CALL:
        # The address of the instruction directly after CALL is pushed onto the stack
        value = pc + 2
        register[SP] -= 1
        memory[register[SP]] = val
        # The PC is set to the address stored in the given register
        reg = memory[pc + 1]
        subroutine_address = register[reg]
        # We jump to that location in Ram and execute the first instruction
        # The PC can move forward or backwards from it's current location
        pc = subroutine_address

    elif command = RET:
        # Return from the subroutine
        # Pop the value form the top of the stack and sotre it in the PC.
        return_address = register[SP]
        pc = memory[registers[SP]]
        # Increment the SP by 1
        registers[SP] += 1


    else: 
        print(f"Error: Unknown command: {command}")
        sys.exit(1)