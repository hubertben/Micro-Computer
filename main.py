
from CPU import CPU
from RAM import RAM

c = CPU()
r = RAM()
r.load_memory(['Load 6', 'Add 7', 'Store 6', 'Jump 1', 0, 0, 1, 1])
r.display_registers()

#c.loop(10000)
