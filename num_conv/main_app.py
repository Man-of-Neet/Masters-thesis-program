import conection
import netlink
import rooting
import slot_ctrl
if __name__ == '__main__':
    d_c_num = 1000000
    Start = 0
    Goal = 0
    #set toporogy
    Topology = rooting.add_node_and_edge()
    av_suvtime = 50
    lam = 1.0
    times = 0
    FirstScore = 0.0
    while times < 3:
        while lam*av_suvtime <= 500:
            #SET_Condition
            call_loss = 0
            link = netlink.link_init()
            L_Stat, NumCore = netlink.SET_LinkStat()
            for outbreak in range(1, d_c_num+1):
                #start & goal -> test ok
                Start, Goal = conection.define_passroot()
                #Passing node & Path length　-> test ok
                Node_list, Distance = rooting.dijkstra_path(Topology, Start, Goal)
                #About-Path Slot & Survival -> test ok
                Slot, Survival = conection.slot_survival(Distance, av_suvtime)
                ##print(str(outbreak) + "," + str(Slot) + "," + str(Survival))
                #Node_list to PassEdge -> test ok
                PassEdge = rooting.choose_edge(Node_list, link)
                acom_bool = slot_ctrl.Search_Available_Slot(Slot, link, PassEdge, NumCore, L_Stat, Start, Goal, outbreak, Survival)
                call_loss = netlink.Loss_x_Foword(acom_bool, call_loss, lam, link)
            print(str(av_suvtime*lam)+","+str(call_loss/outbreak))
            if lam*av_suvtime <= 200:
                lam += 0.25
            elif lam*av_suvtime <= 250:
                lam += 0.5
            elif lam*av_suvtime <=500:
                lam += 1.0
        lam = 1.0
        times += 1
