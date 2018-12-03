import time
import random
import math
import networkx as nx
import numpy as np
import numpy.random as rd
import matplotlib.pyplot as plt
from numpy.random import poisson #use_poisson

class Fiber(list):
    def __init__(self, sl_status: int, suvtime: float, conection1: int, conection2: int) -> None:
        self.sl_status = sl_status
        self.suvtime = suvtime
        self.conection1 = conection1
        self.conection2 = conection2

def define_passroot():
    Start = random.randint(1, 12)
    while True:
       Goal = random.randint(1, 12)
       if Start != Goal:
            break
    return Start, Goal

#リファクタリング必須
def define_pass_condition(length):
    band = 12.5
    if length <= 600:
        m_level = 10000
    elif length <=1200:
        m_level = 10000 / 2
    elif length <= 2400:
        m_level = 10000 / 4
    elif length <= 4800:
        m_level = 10000 / 8
    elif length <= 9600:
        m_level = 10000 / 16
    data_size = random.randint(1, 10000)
    sl = math.ceil(data_size / m_level)
    surv = np.random.poisson(lam=100.)
    return sl, surv

def break_node_all(node_event, estimate_time, restart_average):
    if node_event == -1:
        node = random.randint(1, 12)
        event_time = poisson(estimate_time, 1)
        restart = random.random() * restart_average
        print(str(node))
        print(str(event_time))
        print(str(restart))
        return node, event_time, restart

def next_node_event(lam):
    # 1分あたりlam回発生する。
    event = rd.exponential(1./lam)
    return event

def add_node_and_edge():
    graph = nx.Graph()
    # ノードを追加する
    graph.add_node('1')
    graph.add_node('2')
    graph.add_node('3')
    graph.add_node('4')
    graph.add_node('5')
    graph.add_node('6')
    graph.add_node('7')
    graph.add_node('8')
    graph.add_node('9')
    graph.add_node('10')
    graph.add_node('11')
    graph.add_node('12')
    # ノード間をエッジでつなぐ
    graph.add_edge('1', '2', len = 593, weight=593)#1
    graph.add_edge('1', '4', len = 1256, weight=1256)#2
    graph.add_edge('2', '3', len = 351, weight=351)#3
    graph.add_edge('3', '4', len = 47, weight=47)#4
    graph.add_edge('3', '7', len = 366, weight=366)#5
    graph.add_edge('4', '5', len = 250, weight=250)#6
    graph.add_edge('5', '6', len = 252, weight=252)#7
    graph.add_edge('5', '7', len = 250, weight=250)#8
    graph.add_edge('6', '8', len = 263, weight=263)#9
    graph.add_edge('7', '8', len = 186, weight=186)#10
    graph.add_edge('7', '10', len = 490, weight=490)#11
    graph.add_edge('8', '9', len = 341, weight=341)#12
    graph.add_edge('9', '10', len = 66, weight=66)#13
    graph.add_edge('9', '11', len = 280, weight=280)#14
    graph.add_edge('10', '11', len = 365, weight=365)#15
    graph.add_edge('10', '12', len = 1158, weight=1158)#16
    graph.add_edge('11', '12', len = 911, weight=911)#17
    return graph

def link_init():
    link = [[i for i in range(100)] for j in range(18)]
    edge1 = [0, 1,1,2,3,3,4,5,5,6,7, 7,8, 9, 9,10,10,11]
    edge2 = [0, 2,4,3,4,7,5,6,7,8,8,10,9,10,11,11,12,12]
    for i in range(len(link)):
        for j in range(100):
            link[i][j] = Fiber(0, 0.0 , edge1[i], edge2[i])
    print(len(link))
    return link
