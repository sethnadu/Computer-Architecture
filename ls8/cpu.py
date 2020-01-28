"""CPU functionality."""

import sys

# sys.argv[1] = 'examples/mult.ls8'


print( sys.argv[1])


class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256
        self.reg = [0] * 8

        self.pc = 0

    def load(self):
        """Load a program into memory."""

        address = 0
        binary_strings = []
        program = []
        # For now, we've just hardcoded a program:
        l = open(sys.argv[1], 'r')
        for line in l:
            if line.startswith('#'):
                None
            elif line == '\n':
                None
            elif line.startswith('\n'):
                None
            else:
                binary_strings.append(line)

        print(binary_strings)
        
        # program = [ 
        #     # From print8.ls8
        #     0b10000010, # LDI R0,8
        #     0b00000000,
        #     0b00001000,
        #     0b01000111, # PRN R0
        #     0b00000000,
        #     0b00000001, # HLT
        # ]
        for i in binary_strings:
            if "#" in i:
                for j in range(len(i)):
                    if i[j] is '#':
                        print("outcome", i[0:j])
                        x = int(i[0:j], 2)
                        program.append(x)
            else:
                x = int(i, 2)
                program.append(x)
            
        print('program', program)
        for instruction in program:
            self.ram[address] = instruction
            address += 1

    def ram_read(self, MAR):
        # print(self.ram[MAR])
        return self.ram[MAR]

    def ram_write(self, MAR, MDR):
        self.ram[MAR] = MDR


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        
        running = True
        # LOAD immediate
        LDI = 0b10000010 #10000010
        # Print
        PRN = 0b01000111 #1000111
        # Halt
        HTL = 0b00000001 #1

        while running:
            operand_a = self.ram_read(self.pc + 1)
            operand_b = self.ram_read(self.pc + 2)
            ir = self.ram_read(self.pc)
            if ir == LDI:
                # self.ram_write(operand_a, operand_b)
                self.reg[operand_a] = operand_b
                self.pc += 3
            elif ir == PRN:
                print("REG", self.reg[operand_a])
                self.pc += 2
            elif ir == HTL:
                running = False

        
