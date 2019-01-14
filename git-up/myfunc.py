import time
import random
import math
import networkx as nx
import numpy as np
import numpy.random as rd
from numpy.random import poisson #use_poisson

class Fiber(list):
    def __init__(self, conection_number: int, data_size: int, suvtime: float, start: int, goal: int, conection1: int, conection2: int) -> None:
        self.conection_number = conection_number
        self.data_s = data_size
        self.suvtime = suvtime
        self.start = start
        self.goal = goal
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
def define_pass_condition(length, av_suvtime, data_size):
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
    sl = math.ceil(data_size / m_level)
    surv = np.random.exponential(av_suvtime)
    if surv < 0:
        surv *= -1
    return sl, surv

def break_node_all(node_event, estimate_time, restart_average):
    if node_event == -1:
        node = random.randint(1, 12)
        event_time = poisson(estimate_time, 1)
        restart = random.random() * restart_average
        '''
        print(str(node))
        print(str(event_time))
        print(str(restart))
        '''
        return node, event_time, restart

def next_edge_event(lam):
    # 1分あたりlam回発生する。
    event = rd.exponential(1./lam)
    return event

def add_node_and_edge():
    graph = nx.Graph()
    graph.clear()
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
    #print(graph.edges())
    return graph

def link_init():
    link = [[i for i in range(200)] for j in range(18)]
    edge1 = [0, 1,1,2,3,3,4,5,5,6,7, 7,8, 9, 9,10,10,11]
    edge2 = [0, 2,4,3,4,7,5,6,7,8,8,10,9,10,11,11,12,12]
    for i in range(len(link)):
        for j in range(200):
            link[i][j] = Fiber(0, 0, 0.0 , 0, 0, edge1[i], edge2[i])
    #print(len(link))
    return link

def tmp_init():
    tmp = [0 for i in range(200)]
    for i in range(len(tmp)):
        tmp[i] = Fiber(0, 0, 0.0 , 0, 0, 0, 0)
    #print(len(link))
    return tmp

def choose_edge(passnode, link):
    edge_list = [0 for i in range(len(passnode)-1)]
    for i in range(len(passnode)-1):
        for j in range(len(link)):
            if (link[j][0].conection1 == int(passnode[i]) and link[j][0].conection2 == int(passnode[i + 1])):
                edge_list[i] = j
                continue
            elif(link[j][0].conection1 == int(passnode[i + 1]) and link[j][0].conection2 == int(passnode[i])):
                edge_list[i] = j
                continue
    return edge_list

def break_edge(link, graph):
    choose = random.randint(1, 17)
    #print(choose)
    S = link[choose][0].conection1
    G = link[choose][0].conection2
    graph.remove_edge(str(S), str(G))
    #print("remove_edge = " + str(choose))
    #print(graph.edges())
    return choose

def link_release(link, l_num, s_num):
    link[l_num][s_num].conection_number = 0
    link[l_num][s_num].suvtime = 0
    link[l_num][s_num].start = 0
    link[l_num][s_num].goal = 0
    link[l_num][s_num].data_s = 0

def path_acomodate_process(link, slot, outbreak, surv_time, start, goal, data_size, edge_list):
    #使用リンクの連続性確認
    sum_link_status = [0 for i in range(200)]
    for i in range(len(edge_list)):
        use_link = edge_list[i]
        for j in range(200):
            sum_link_status[j] += link[use_link][j].conection_number

    #収容可否確認
    available_slot = 0
    avoid = [0 for i in range(slot)]
    for i in range(len(sum_link_status)):
        if sum_link_status[i] == 0:
            #print("avoid:" + str(avoid))
            #print(i)
            avoid[available_slot] = i
            available_slot +=1
            if available_slot == slot:
                available = 1
                break
        else:
            available_slot = 0
            available = 0

    if available == 1:
        for i in range(len(edge_list)):
            for j in range(len(avoid)):
                link[int(edge_list[i])][avoid[j]].conection_number = outbreak
                link[int(edge_list[i])][avoid[j]].suvtime = surv_time
                link[int(edge_list[i])][avoid[j]].start = start
                link[int(edge_list[i])][avoid[j]].goal = goal
                link[int(edge_list[i])][avoid[j]].data_s = data_size
        return True

    else:
        return False
