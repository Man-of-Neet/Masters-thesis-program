import itertools
def Search_Available_Slot(Slot, link, PassEdge, NumCore, L_Stat, Start, Goal, outbreak, Survival):
    #Loop Number of Cores & Core Combination
    av_slots = [0] * Slot
    for com in itertools.product(NumCore, repeat=len(PassEdge)):
        #com is tuple
        L_Stat = [0 for i in range(len(L_Stat))]
        #Loop of hop
        #Confirmed -> len(PassEdge) == len(com)
        for hop in range(len(PassEdge)):
            #print(str(PassEdge[hop])+" : "+str(com[hop]))
            for sl in range(len(L_Stat)):
                #Correspondence between PassEdge and com has been confirmed
                L_Stat[sl] += link[PassEdge[hop]][com[hop]][sl].conection_number
        av_slots, acom_bool = Path_Acomodate_Process(Slot, L_Stat, av_slots)
        if acom_bool == False:
            continue
        elif acom_bool == True:
            for i in range(len(PassEdge)):
                for j in av_slots:
                    #print(i,j)
                    link[PassEdge[i]][com[i]][j].conection_number = outbreak
                    link[PassEdge[i]][com[i]][j].suvtime = Survival
                    link[PassEdge[i]][com[i]][j].start = Start
                    link[PassEdge[i]][com[i]][j].goal = Goal
            # for i in range(len(PassEdge)):
            #     for j in range(len(L_Stat)):
            #         print(link[PassEdge[i]][com[i]][j].conection_number, end="")
            #         print(",",end="")
            #     print("core" + str(com[i]) + ",topo" + str(PassEdge[i]) + ",out" + str(outbreak))
            return acom_bool
    return acom_bool


def Path_Acomodate_Process(Slot, L_Stat, av_slots):
    available = 0
    av_slots = [i*0 for i in av_slots]
    bool = False
    for i in range(len(L_Stat)):
        if L_Stat[i] == 0:
            av_slots[available] = i
            available += 1
            if available == Slot:
                bool = True
                break
        else:
            available = 0
            bool = False
    return av_slots, bool







#####
#下いらない適当に消す
#####
def link_release(link, l_num, s_num):
    #time foword
    foword = np.random.exponential(1/lam)
    edge_event -= foword
    for i in range(len(link)):
        for j in range(myfunc.link_size):
            if link[i][j].suvtime > 0.0:
                link[i][j].suvtime -= foword
                if link[i][j].suvtime < 0:
                    myfunc.link_release(link, i, j)
    #slot release
    link[l_num][s_num].conection_number = 0
    link[l_num][s_num].suvtime = 0
    link[l_num][s_num].start = 0
    link[l_num][s_num].goal = 0
    link[l_num][s_num].data_s = 0

def path_acomodate_process(link, slot, outbreak, surv_time, start, goal, data_size, edge_list):
    #使用リンクの連続性確認
    sum_link_status = [0 for i in range(len(link[0][0]))]
    for i in range(len(edge_list)):
        use_link = edge_list[i]
        for j in range(link_size):
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
