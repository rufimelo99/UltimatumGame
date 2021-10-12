import networkx as nx
import matplotlib.pyplot as plt
"""
TODO
setup game first with random
we want a random generated graphs
we want to train individuals

"""
class ultimatumGame:
    def __init__(self, Nplayers) -> None:
        self.graph = nx.erdos_renyi_graph(Nplayers, 0.15)
        self.Players = []

    def printGraph(self):
        nx.draw_shell(self.graph)
        plt.show()

    