import time
import random
import math
import networkx as nx
import numpy as np
import numpy.random as rd
import matplotlib.pyplot as plt
from numpy.random import poisson #use_poisson
import myfunc

if __name__ == '__main__':

    t1 = time.time()
    graph = myfunc.add_node_and_edge()
    t2 = time.time()
    lam = 1
    av_suvtime = 10.0
    edge_break = 0
    edge_event = 0.0
    restart_average = 300
    incount = 0
    #以下、ループ処理
    #ループ1,負荷変更
    while lam * av_suvtime <= 300:
        outbreak = 0
        call_loss = 0
        link = myfunc.link_init()
        #ループ2,100000呼発生
        while outbreak <= 100000:
            outbreak +=1
            start, goal = myfunc.define_passroot()
            if edge_event <= 0:
                #故障ノードがなければ edge_break = 0
                if edge_break == 0:
                    myfunc.break_edge(link)
                    edge_break = 1
                    edge_event = np.random.normal() * restart_average
                    if edge_event < 0:
                        edge_event *= -1
                    #print("break," + str(outbreak) + "," + str(edge_event))

                elif edge_break == 1:
                    #print("reset," + str(outbreak))
                    graph = myfunc.add_node_and_edge()
                    edge_break = 0
                    #1秒に平均何回発生する事象か？
                    edge_event = myfunc.next_edge_event(1/100)

            passnode = nx.dijkstra_path(graph, str(start), str(goal))

            edge_list = myfunc.choose_edge(passnode, link)
            slot, surv_time = myfunc.define_pass_condition(nx.dijkstra_path_length(graph, str(start), str(goal)), av_suvtime)
            #print('seizon' + str(surv_time))
            #収容可否確認
            sum_link_status = [0 for i in range(100)]
            for i in range(len(edge_list)):
                use_link = edge_list[i]
                for j in range(100):
                    sum_link_status[j] += link[use_link][j].conection_number
            #呼損
            #パス収容
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

            #print (available_slot)
            #print (avoid)
            if available == 1:
                for i in range(len(edge_list)):
                    for j in range(len(avoid)):
                        link[int(edge_list[i])][avoid[j]].conection_number = outbreak
                        link[int(edge_list[i])][avoid[j]].suvtime = surv_time
                        link[int(edge_list[i])][avoid[j]].start = start
                        link[int(edge_list[i])][avoid[j]].goal = goal
            else:
                #print(outbreak)
                call_loss += 1
                #print("call_loss:" + str(call_loss))

            #時間を進める
            foword = np.random.exponential(1/lam)
            edge_event -= foword
            for i in range(len(link)):
                for j in range(100):
                    if link[i][j].suvtime > 0.0:
                        link[i][j].suvtime -= foword
                        if link[i][j].suvtime < 0:
                            #print("syokika")
                            link[i][j].conection_number = 0
                            link[i][j].suvtime = 0
                            link[i][j].start = 0.0
                            link[i][j].goal = 0
            #print(foword)
            #表示がヤバイデバッグ用
            # if available == 1:
            #     for i in range(len(edge_list)):
            #         print('conection_number:' + str(outbreak))
            #         print('link' + str(edge_list[i]))
            #         for j in range(100):
            #             print("(" + str(link[edge_list[i]][j].start) + ", " + str(link[edge_list[i]][j].goal) + ", " + str(link[edge_list[i]][j].conection_number) + ")", end=", ")

            #print("slot = " + str(slot) + ", survival = " + str(surv_time) + ", next_breaktime = " + str(myfunc.next_node_event(0.01)))
        print (str(incount) +",,"+ str(lam * av_suvtime) + ", " + str(float(call_loss / outbreak)))
        incount += 1
        lam += 1
    t3 = time.time()

    elapsed_time = t2-t1
    print(f"経過時間：{elapsed_time}")
    elapsed_time = t3-t2
    print(f"経過時間：{elapsed_time}")

    # レイアウトの取得

    pos = nx.spring_layout(graph)

    # 可視化

    plt.figure(figsize=(12, 12))
    nx.draw_networkx_edges(graph, pos)
    nx.draw_networkx_nodes(graph, pos, font_size=16)
    nx.draw_networkx_labels(graph, pos, font_size=16, font_color="b")
    plt.axis('off')
    plt.show()
