

class Jump:

    def __init__(self, index):
        self.index = int(index)

    def __repr__(self):
        return 'JUMP ' + str(self.index)

    def execute(self, cpu, ram):
        cpu.program_counter = self.index
        return