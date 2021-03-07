

class Load():

    def __init__(self, index):
        self.index = index

    def execute(self, cpu, ram):
        return 'LOAD', str(self.index)
        