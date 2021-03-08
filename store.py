

class Store():

    def __init__(self, index):
        self.index = int(index)

    def __repr__(self):
        return 'STORE ' + str(self.index)

    def execute(self, cpu, ram):
        value = cpu.accumulator
        ram.registers[self.index] = (ram.registers[self.index][0], value)
        return 