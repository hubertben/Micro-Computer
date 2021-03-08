from file_reader import FileReader as fr
from CPU import CPU
from RAM import RAM

r = RAM(0)
r.load_memory(fr.read_commands())
r.display_registers()

c = CPU()
c.load_ram(r)

'''
load 6
add 7 
store 6
jump 1
0
0
1
1
'''



c.loop(100)
