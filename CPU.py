

class CPU:

    def __init__(self):
        self.program_counter = 0
        self.instruction_register = None
        self.accumulator = 0

    def loop(self, iterator):
        for cycle in iterator:
            tick()

    def tick(self):
        fetch()
        decode()
        execute

    def fetch(self):
        return

    def decode(self):
        return

    def execute(self):
        return 