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
    lam = 0.1
    av_suvtime = 180.0
    edge_break = 0
    edge_event = 0.0
    restart_average = 1000
    average_edge_breakforward = 1000
    #以下、ループ処理
    #ループ1,負荷変更
    while average_edge_breakforward >= 0:
        restart_average = 1000
        while restart_average >= 0:
            lam = 0.1
            while lam * av_suvtime <= 300:
                outbreak = 0
                call_loss = 0
                call_succes = 0
                conection_bool = False
                link = myfunc.link_init()
                #ループ2,100000呼発生
                while outbreak <= 100000:
                    outbreak += 1
                    start, goal = myfunc.define_passroot()
                    if edge_event <= 0:
                        #故障ノードがなければ edge_break = 0
                        if edge_break == 0:
                            choose = myfunc.break_edge(link, graph)
                            edge_break = 1
                            edge_event = np.random.exponential(restart_average)
                            tmp_link = myfunc.tmp_init()
                            #エッジ故障時、再配置するコネクションを格納
                            for i in range(len(tmp_link)):
                                tmp_link[i].conection_number = link[choose][i].conection_number
                                tmp_link[i].start = link[choose][i].start
                                tmp_link[i].goal = link[choose][i].goal
                                tmp_link[i].suvtime = link[choose][i].suvtime
                                tmp_link[i].data_s = link[choose][i].data_s
                                #print(str(tmp_link[i].data_s) + "," , end=" " )
                            #print("")

                            #エッジ故障によるコネクションの瞬断
                            for i in range(len(link)):
                                for j in range(len(link[i])):
                                    if tmp_link[j].conection_number == link[i][j].conection_number:
                                        myfunc.link_release(link, i, j)

                            #コネクション再配置
                            tmp_conection = 0
                            for i in range(len(tmp_link)):
                                if tmp_link[i].conection_number != 0 and tmp_conection != tmp_link[i].conection_number:
                                    tmp_conection = tmp_link[i].conection_number
                                    if tmp_link[i].conection_number != 0 and tmp_conection == tmp_link[i].conection_number:
                                        passnode = nx.dijkstra_path(graph, str(tmp_link[i].start), str(tmp_link[i].goal))
                                        edge_list = myfunc.choose_edge(passnode, link)
                                        data_size = tmp_link[i].data_s
                                        slot, surv_time = myfunc.define_pass_condition(nx.dijkstra_path_length(graph, str(tmp_link[i].start), str(tmp_link[i].goal)), av_suvtime, tmp_link[i].data_s)
                                        surv_time = tmp_link[i].suvtime

                                        #print(edge_list)
                                        #print(slot, end=",")
                                        # print(surv_time, end=",")
                                        # print(data_size, end=",")
                                        # print(tmp_link[i].conection_number, end=",")
                                        # conection_bool = myfunc.path_acomodate_process(link, slot, tmp_link[i].conection_number, surv_time, start, goal, data_size, edge_list)
                                        # print(conection_bool)
                                        if conection_bool == False:
                                            call_loss += 1

                            if edge_event < 0:
                                edge_event *= -1
                            #print("break," + str(outbreak) + "," + str(edge_event))

                        elif edge_break == 1:
                            #print("reset," + str(outbreak))
                            graph = myfunc.add_node_and_edge()
                            edge_break = 0
                            #1秒に平均何回発生する事象か？
                            edge_event = myfunc.next_edge_event(1/average_edge_breakforward)

                    passnode = nx.dijkstra_path(graph, str(start), str(goal))
                    edge_list = myfunc.choose_edge(passnode, link)
                    data_size = random.randint(1, 10000)
                    slot, surv_time = myfunc.define_pass_condition(nx.dijkstra_path_length(graph, str(start), str(goal)), av_suvtime, data_size)
                    #print('seizon' + str(surv_time))

                    #パス収容
                    conection_bool = myfunc.path_acomodate_process(link, slot, outbreak, surv_time, start, goal, data_size, edge_list)

                    #呼損の有無
                    if conection_bool == False:
                        call_loss += 1
                    else:
                        call_succes += 1

                    #呼損がちゃんとカウントできているか？
                    #print(str(call_loss) + "+" + str(call_succes) + "/" + str(outbreak))
                    #時間を進める
                    foword = np.random.exponential(1/lam)
                    edge_event -= foword
                    for i in range(len(link)):
                        for j in range(200):
                            if link[i][j].suvtime > 0.0:
                                link[i][j].suvtime -= foword
                                if link[i][j].suvtime < 0:
                                    #print("syokika")
                                    myfunc.link_release(link, i, j)
                    #print(foword)
                    #表示がヤバイデバッグ用
                    # if available == 1:
                    #     for i in range(len(edge_list)):
                    #         print('conection_number:' + str(outbreak))
                    #         print('link' + str(edge_list[i]))
                    #         for j in range(100):
                    #             print("(" + str(link[edge_list[i]][j].start) + ", " + str(link[edge_list[i]][j].goal) + ", " + str(link[edge_list[i]][j].conection_number) + ")", end=", ")

                    #print("slot = " + str(slot) + ", survival = " + str(surv_time) + ", next_breaktime = " + str(myfunc.next_node_event(0.01)))
                print (str(average_edge_breakforward) +","+ str(restart_average) +","+ str(lam * av_suvtime) +","+ str(float(call_loss / outbreak)))
                lam += 0.1
            restart_average -= 50
        average_edge_breakforward -= 50

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
