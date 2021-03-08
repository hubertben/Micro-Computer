from commands.Template import Template

class Load(Template):

    def __init__(self, indecies):
        self.indecies = indecies

    def __repr__(self):
        t = Template.__repr__(self, 'LOAD')
        return t

    def execute(self, cpu, ram):
        index = int(self.indecies[0])
        value = ram.registers[index][1]
        cpu.accumulator = value
        return 
        