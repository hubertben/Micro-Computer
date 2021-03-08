
from commands.Template import Template

class Display(Template):

    def __init__(self, indecies):
        self.indecies = indecies

    def __repr__(self):
        t = Template.__repr__(self, 'DISPLAY')
        return t

    def execute(self, cpu, ram):

        for i in self.indecies:
            index = int(i)
            print('DISPLAY |', ram.registers[index])
        
        return 