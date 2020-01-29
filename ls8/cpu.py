"""CPU functionality."""

import sys

running = True
# LOAD immediate
LDI = 0b10000010 
# Print
PRN = 0b01000111 
# Multiply
MUL = 0b10100010
# Halt
HTL = 0b00000001 
    

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256
        self.reg = [0] * 8
        self.pc = 0
        self.branchtable = {}
        self.branchtable[LDI] = self.handle_ldi
        self.branchtable[PRN] = self.handle_prn
        self.branchtable[MUL] = self.handle_mul

    def load(self):
        """Load a program into memory."""

        # Check for what arguement of files be ran
        if len(sys.argv) != 2:
            print("Usage: file.py filename", file=sys.stderr)
            sys.exit(1)
        else:
            fileName = sys.argv[1]

        address = 0
        binary_strings = []
        program = []

        #  If second arguement is valid
        try:
            # Open the file that contains the programs
            l = open(fileName, 'r')
            for line in l:
                if line.startswith('#'):
                    None
                elif line == '\n':
                    None
                elif line.startswith('\n'):
                    None
                else:
                    binary_strings.append(line)

            print("Array of Binary_strings", binary_strings)
            
            for i in binary_strings:
                comment_split = i.split('#')
                new_value = comment_split[0]
                x = int(new_value, 2)
                program.append(x)
                
            print('program', program)
            for instruction in program:
                # self.ram[address] = instruction
                self.ram_write(address, instruction)
                address += 1

        # If second arguement is invalid
        except FileNotFoundError:
            print(f'{sys.argv[0]} : {sys.argv[1]} Not found')
            sys.exit(2)

    def ram_read(self, MAR):
        # print(self.ram[MAR])
        return self.ram[MAR]

    def ram_write(self, MAR, MDR):
        self.ram[MAR] = MDR

    def handle_ldi(self, reg_a, reg_b):
        self.reg[reg_a] = reg_b
        # Skip current pc and its two arguements
        self.pc += 3

    def handle_prn(self, reg_a, reg_b):
        print("REG", self.reg[reg_a])
        # Skip current pc and it's single arguement
        self.pc += 2

    def handle_mul(self, reg_a, reg_b):
        self.alu("MUL", reg_a, reg_b)
        # Skip current pc and it's two arguements
        self.pc += 3
    

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""
        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        elif op == "MUL":
            
            self.reg[reg_a] *= self.reg[reg_b]
            print(self.reg[reg_a])
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
        while running:
            operand_a = self.ram_read(self.pc + 1)
            operand_b = self.ram_read(self.pc + 2)
            ir = self.ram_read(self.pc)

            if ir in self.branchtable:
                self.branchtable[ir](operand_a, operand_b)
            elif ir is HTL:
                running = False