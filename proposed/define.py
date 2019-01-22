import random

class define_Start_Goal:
    def define_passroot(self):
        Start = random.randint(1, 12)
        while True:
           Goal = random.randint(1, 12)
           if Start != Goal:
                break
        return Start, Goal

SGdef = define_Start_Goal()
Start = SGdef.define_passroot
print(Start)
