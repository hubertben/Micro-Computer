

class RAM:

    def __init__(self):
        self.registers = []

    def display_registers(self):
        for r in self.registers:
            print(r[0], '\t', r[1])
    
    def load_memory(self, memory):
        for index, item in enumerate(memory):
            self.registers.append((index,item))