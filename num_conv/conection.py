import math
import numpy
import numpy.random
import random
def define_passroot():
    Start = random.randint(1, 12)
    while True:
       Goal = random.randint(1, 12)
       if Start != Goal:
            break
    return Start, Goal

def slot_survival(Distance, av_suvtime):
    data_size = random.randint(1, 100)#1~10Gbps
    if Distance <= 600:
        #print("16QAM")
        if data_size <= 10:
            slot = 1
        elif data_size <= 40:
            slot = 3
        else:
            slot = 7

    elif Distance > 600:
        #print("QPSK")
        if data_size <= 10:
            slot = 2
        elif data_size <= 40:
            slot = 6
        else:
            slot = 14

    surv = numpy.random.exponential(av_suvtime)
    if surv < 0:
        surv *= -1
    return slot, surv
