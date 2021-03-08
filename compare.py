# Compares the value in the register index to the accumulator
# If they are equal, execute line under if
# If they are not equal, execute 2 lines under if

class Compare():

    def __init__(self, index):
        self.index = int(index)

    def __repr__(self):
        return 'COMPARE ' + str(self.index)

    def execute(self, cpu, ram):
        value_1 = ram.registers[self.index][1]
        value_2 = cpu.accumulator

        if(value_1 == value_2):
            cpu.program_counter += 1
        else: # Val2 is larger of the same
            cpu.program_counter += 2
        return 
        