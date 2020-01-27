import sys

PRINT_BEEJ = 1
HALT = 2
PRINT_NUM = 3
# 3 takes argument
SAVE = 4 #Saves value to register
PRINT_REGISTER = 5
ADD = 6

memory = [
    PRINT_BEEJ,
    SAVE, # Saves value 65 to register 2
    65,
    2,
    SAVE, # Saves value 20 to register 3
    20,
    3,
    ADD, # Add values r2 and r3, store it in r2
    2, 
    3,
    PRINT_REGISTER, #PRINt the value in r2
    2,
    HALT
]

register = [0] * 8

pc = 0
running = True

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