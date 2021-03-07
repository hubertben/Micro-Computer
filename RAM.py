from command import Command

class RAM:

    def __init__(self, stick_number):
        self.registers = []
        self.stick_number = stick_number

    def display_registers(self):
        print('\nRAM #', self.stick_number)
        for r in self.registers:
            print(r[0], '\t', r[1])
    
    def load_memory(self, memory):
        for index, item in enumerate(memory):
            self.registers.append((index,item))

    def return_command(self, index):
        return self.registers[index]
        
    def clean_memory(self):
        return