# Compares the value in the accumulator to the register index and stores the larger number in the accumulator

class Compare():

    def __init__(self, index):
        self.index = int(index)

    def __repr__(self):
        return 'COMPARE ' + str(self.index)

    def execute(self, cpu, ram):
        value_1 = ram.registers[self.index][1]
        value_2 = cpu.accumulator

        if(value_1 > value_2):
            cpu.accumulator = value_1
        else: # Val2 is larger of the same
            cpu.accumulator = value_2
        return 
        