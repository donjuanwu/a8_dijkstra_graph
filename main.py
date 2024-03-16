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
        if vertex1 not in self.adjacency_list:  # if vertex1 is not already in adjacency list
            self.adjacency_list[vertex1] = {}  # set vertex1 value to be an empty dictionary
        self.adjacency_list[vertex1][vertex2] = weight  # update {vertex1: {vertex2: weight}}

    def print_graph(self):
        """
        print graph including key and values
        :return: None
        """
        if self.adjacency_list:
            for start_loc in self.adjacency_list:  # get the key
                neighbors = self.adjacency_list[start_loc]  # retrieve the key value pair
                for destination in neighbors:  # get the neighbor
                    travel_fee = self.adjacency_list[start_loc][destination]
                    print(f"From {start_loc} going to {destination} cost ${travel_fee} ")


graph = 2
p = Place.create_graph(graph)
p.print_graph()
