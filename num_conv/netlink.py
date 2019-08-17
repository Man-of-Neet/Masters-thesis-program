import random
import numpy as np
link_size = 128
s_core = 4
class Fiber(list):
    def __init__(self, conection_number: int, data_size: int, suvtime: float, start: int, goal: int, conection1: int, conection2: int) -> None:
        self.conection_number = conection_number
        self.suvtime = suvtime
        self.start = start
        self.goal = goal
        self.conection1 = conection1
        self.conection2 = conection2

def link_init():
    link = [[[i for i in range(link_size)] for j in range(s_core)] for k in range(18)]
    edge1 = [0, 1,1,2,3,3,4,5,5,6,7, 7,8, 9, 9,10,10,11]
    edge2 = [0, 2,4,3,4,7,5,6,7,8,8,10,9,10,11,11,12,12]
    for i in range(len(link)):
        for j in range(s_core):
            for k in range(link_size):
                link[i][j][k] = Fiber(0, 0, 0.0, 0, 0, edge1[i], edge2[i])
                link[i][j][k].conection_number = 0 #random.randrange(2)
    return link

def SET_LinkStat():
    L_Stat = [0 for i in range(link_size)]
    NumCore = [i for i in range(s_core)]
    return L_Stat, NumCore

def Loss_x_Foword(acom_bool, call_loss, lam, link):
    if acom_bool == False:
        call_loss += 1
    foword = np.random.exponential(1/lam)
    for i in range(len(link)):
        for j in range(len(link[i])):
            for k in range(len(link[i][j])):
                if link[i][j][k].conection_number == 0:
                    continue
                else:
                    link[i][j][k].suvtime -= foword
                    if link[i][j][k].suvtime <= 0:
                        link[i][j][k].conection_number = 0
                        link[i][j][k].suvtime = 0
                        link[i][j][k].start = 0
                        link[i][j][k].goal = 0
    return call_loss
