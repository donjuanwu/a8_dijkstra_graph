"""
Developer: Don Dang
Date: 3/13/24
Week: 8

Subject: Graph

References:

Notes:



Date        Developer     Activities
3/13/24      Don D        Attempt to start assignment 8
"""


class Place:
    def __init__(self):
        # create adjacency list
        self.adjacency_list = {}

    @staticmethod
    def create_graph(graph_config):
        """
        create graphs
        :param graph_config: map configuration
        :return: Place instance
        """
        g = Place()
        if graph_config == 1:
            pass
        elif graph_config == 2:  # build graph from South Center Mall to Seattle Center
            g.add_weighted_edge("SC_Mall", "Tukwila_LLR_Station", 0)
            g.add_weighted_edge("SC_Mall", "Intl_District", 4)
            g.add_weighted_edge("SC_Mall", "Renton_Park_Ride", 5)
            g.add_weighted_edge("Tukwila_LLR_Station", "Westlake_Center", 5)
            g.add_weighted_edge("Westlake_Center", "Seattle_Center", 4)
            g.add_weighted_edge("Intl_District", "Westlake_Center", 1)
            g.add_weighted_edge("Intl_District", "Seattle_Center", 3)
            g.add_weighted_edge("Renton_Park_Ride", "Seattle_Center", 3)
        elif graph_config == 3:
            pass
        return g

    def add_weighted_edge(self, vertex1, vertex2, weight):
        """
        create the adjacency list
        :param vertex1: starting location
        :param vertex2: destination
        :param weight: travel cost
        :return: None
        """







