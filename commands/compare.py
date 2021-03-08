from commands.Template import Template

# Compares the value in the register index to the accumulator
# If they are equal, execute line under if
# If they are not equal, execute 2 lines under if

class Compare(Template):

    def __init__(self, indecies):
        self.indecies = indecies

    def __repr__(self):
        t = Template.__repr__(self, 'COMPARE')
        return t

    def execute(self, cpu, ram):
        index = int(self.indecies[0])
        value_1 = ram.registers[index][1]
        value_2 = cpu.accumulator

        if(value_1 == value_2):
            cpu.program_counter += 1
        else: # Val2 is larger of the same
            cpu.program_counter += 2
        return 
        