

class CPU:

    def __init__(self):
        self.program_counter = 0
        self.instruction_register = None
        self.accumulator = 0

        self.ram_sticks = []
        self.current_ram_stick = 0

    def display_cpu_stats(self):
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('Program Counter:', self.program_counter)
        print('Instruction Register:', self.instruction_register)
        print('Accumulator:', self.accumulator)

    
    def load_ram(self, ram_stick):
        self.ram_sticks.append(ram_stick)

    def loop(self, iterator):
        for cycle in iterator:
            self.tick()

    def tick(self):
        self.fetch()
        self.execute()

        self.program_counter += 1
        self.display_cpu_stats()

    def fetch(self):
        self.instruction_register = self.ram_sticks[self.current_ram_stick].return_command(self.program_counter)
        return

    def execute(self):
        print(self.instruction_register[1].execute())
        return 

