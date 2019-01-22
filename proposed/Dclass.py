import networkx as nx
import matplotlib.pyplot as plt
import time

class dijkstra:
    def __init__(self, Start, Goal):
        self.Start = Start
        self.Goal = Goal
    def out_root(self):
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
        graph.add_edge('1', '2', weight=593)
        graph.add_edge('1', '4', weight=1256)
        graph.add_edge('2', '3', weight=351)
        graph.add_edge('3', '4', weight=47)
        graph.add_edge('3', '7', weight=366)
        graph.add_edge('4', '5', weight=250)
        graph.add_edge('5', '6', weight=252)
        graph.add_edge('5', '7', weight=250)
        graph.add_edge('6', '8', weight=263)
        graph.add_edge('7', '8', weight=186)
        graph.add_edge('7', '10', weight=490)
        graph.add_edge('8', '9', weight=341)
        graph.add_edge('9', '10', weight=66)
        graph.add_edge('9', '11', weight=280)
        graph.add_edge('10', '11', weight=365)
        graph.add_edge('10', '12', weight=1158)
        graph.add_edge('11', '12', weight=911)

        # ダイクストラ法で最短経路を探す
        return nx.dijkstra_path(graph, self.Start, self.Goal)
