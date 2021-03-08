from commands.Template import Template

class Jump(Template):

    def __init__(self, indecies):
        self.indecies = indecies

    def __repr__(self):
        t = Template.__repr__(self, 'JUMP')
        return t

    def execute(self, cpu, ram):
        index = int(self.indecies[0])
        cpu.program_counter = index
        return