import networkx as nx
def dijkstra_path(Topology, Start, Goal):
    if Start > Goal:
        Start, Goal = Goal, Start
    Node_list = nx.dijkstra_path(Topology, str(Start), str(Goal))
    Distance = nx.dijkstra_path_length(Topology, str(Start), str(Goal))
    return Node_list, Distance

def choose_edge(Node_list, link):
    edge_list = [0 for i in range(len(Node_list)-1)]
    for i in range(len(Node_list)-1):
        for j in range(len(link)):
            if (link[j][0][0].conection1 == int(Node_list[i]) and link[j][0][0].conection2 == int(Node_list[i + 1])):
                edge_list[i] = j
                continue
            elif(link[j][0][0].conection1 == int(Node_list[i + 1]) and link[j][0][0].conection2 == int(Node_list[i])):
                edge_list[i] = j
                continue
    #print(edge_list)
    return edge_list

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
    graph.add_edge('1', '2', weight=593)#1
    graph.add_edge('1', '4', weight=1256)#2
    graph.add_edge('2', '3', weight=351)#3
    graph.add_edge('3', '4', weight=47)#4
    graph.add_edge('3', '7', weight=366)#5
    graph.add_edge('4', '5', weight=250)#6
    graph.add_edge('5', '6', weight=252)#7
    graph.add_edge('5', '7', weight=250)#8
    graph.add_edge('6', '8', weight=263)#9
    graph.add_edge('7', '8', weight=186)#10
    graph.add_edge('7', '10', weight=490)#11
    graph.add_edge('8', '9', weight=341)#12
    graph.add_edge('9', '10', weight=66)#13
    graph.add_edge('9', '11', weight=280)#14
    graph.add_edge('10', '11', weight=365)#15
    graph.add_edge('10', '12', weight=1158)#16
    graph.add_edge('11', '12', weight=911)#17
    return graph
