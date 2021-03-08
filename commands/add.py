
from commands.Template import Template

class Add(Template):

    def __init__(self, indecies):
        self.indecies = indecies

    def __repr__(self):
        t = Template.__repr__(self, 'ADD')
        return t

    def execute(self, cpu, ram):
        s = 0
        for i in self.indecies:
            s += ram.registers[int(i)][1]

        if(len(self.indecies) == 1):
            cpu.accumulator += s
        else:
            cpu.accumulator = s
        return 