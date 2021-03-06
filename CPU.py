from instruction import Instruction
import sys

DNI_list = ['JUMP', 'COMPARE']

class CPU:

    def __init__(self):
        self.program_counter = 0
        self.instruction_register = None
        self.accumulator = 0

        self.ram_sticks = []
        self.current_ram_stick = 0

        self.last_command = None

    def display_cpu_stats(self):
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('Program Counter:', self.program_counter)
        print('Instruction Register:', self.instruction_register)
        print('Accumulator:', self.accumulator)

        for r in self.ram_sticks[self.current_ram_stick].registers:
            print(r)

    def load_ram(self, ram_stick):
        self.ram_sticks.append(ram_stick)

    def run(self):
        while(True):
            self.tick()
            self.display_cpu_stats()

    def tick(self):
        self.fetch()
        self.execute()
        if(self.last_command not in DNI_list):
            self.program_counter += 1
        
        
    def fetch(self):
        inst = self.ram_sticks[self.current_ram_stick].return_command(self.program_counter)
        self.instruction_register = Instruction(inst[0], inst[1])
        self.last_command = str(inst[1]).split(' ')[0] 
        
        if(self.last_command == 'END'):
            sys.exit()
        return

    def execute(self):
        self = self.instruction_register.command.execute(self, self.ram_sticks[self.current_ram_stick]) 
        return 

