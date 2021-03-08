from commands.Template import Template

class Store(Template):

    def __init__(self, indecies):
        self.indecies = indecies

    def __repr__(self):
        t = Template.__repr__(self, 'STORE')
        return t

    def execute(self, cpu, ram):
        value = cpu.accumulator

        for i in self.indecies:
            index = int(i)
            ram.registers[index] = (ram.registers[index][0], value)
        return 