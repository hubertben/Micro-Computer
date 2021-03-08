

class Add():

    def __init__(self, index):
        self.index = int(index)

    def __repr__(self):
        return 'ADD ' + str(self.index)

    def execute(self, cpu, ram):
        value_1 = ram.registers[self.index][1]
        value_2 = cpu.accumulator
        cpu.accumulator = value_1 + value_2
        return 