

class Jump:

    def __init__(self, index):
        self.index = index

    def execute(self):
        return 'JUMP', str(self.index)