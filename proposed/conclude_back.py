import random

def define_passroot():
    Start = random.randint(1, 12)
    while True:
       Goal = random.randint(1, 12)
       if Start != Goal:
            break
    print('Start = ' +str(Start))
    print('Goal = ' +str(Goal))
    
if __name__ == '__main__':
    for i in range(0, 10000000):
        define_passroot();
