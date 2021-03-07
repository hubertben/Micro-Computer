

class Jump:

    def __init__(self, index):
        self.index = index

    def execute(self, cpu, ram):
        return 'JUMP', str(self.index)