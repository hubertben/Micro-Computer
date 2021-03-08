from command import Command as com

class RAM:

    def __init__(self, stick_number):
        self.registers = []
        self.stick_number = stick_number

    def display_registers(self):
        print('\nRAM #', self.stick_number)
        for r in self.registers:
            print(r[0], '\t', r[1])
    
    def load_memory(self, memory):
        for index, item in enumerate(memory):    
            item = item.strip()       
            if(self.is_digit(item)):
                item = int(item)

            print((index, item))
            self.registers.append((index, item))
        self.clean_memory()

    def return_command(self, index):
        return self.registers[index]
        
    def clean_memory(self):
        registers = []
        for command in self.registers:
            if(type(command[1]) == str):
                c = command[1].split(' ')
                attr = getattr(com, c[0])(c[1])
                concat = (command[0], attr)
                registers.append(concat)
            else:
                print(command)
                registers.append(command)
        self.registers = registers[:]

    def is_digit(self, n):
        try:
            int(n)
            return True
        except ValueError:
            return  False