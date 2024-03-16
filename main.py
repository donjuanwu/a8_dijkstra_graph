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

import collections  # special data structures


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
        create the adjacency list with weight edged (travel cost)
        :param vertex1: starting location
        :param vertex2: destination
        :param weight: travel cost
        :return: None
        """
        if vertex1 not in self.adjacency_list:  # if vertex1 is not already in adjacency list
            self.adjacency_list[vertex1] = {}  # set vertex1 value to be an empty dictionary
        self.adjacency_list[vertex1][vertex2] = weight  # update {vertex1: {vertex2: weight}}

    def bfs_traversal(self, start_loc):
        """
        traverse graph using Breadth-first search
        print starting location
        mark visited vertex
        printed visited vertex
        add unvisited neighbors
        :param start_loc: starting location
        :return: None
        """
        print(f"Starting location {start_loc}: ", end="")
        self.bfs(start_loc)

    def bfs(self, start_loc):
        """
        create visited dictionary to locations that have visited
        create deque object to hold locations
        call visited_location to mark visited location
        call enqueue_unvisited_locations
        :param start_loc: starting vertex
        :return: None
        """
        visited = {}  # empty dictionary to hold visited locations
        q = collections.deque()  # create a double-ended queue
        q.appendleft(start_loc)  # add starting location to queue
        while q:
            current_loc = q.pop()  # pop queue and make starting location as current location
            self.visited_location(current_loc, visited)  # mark current location as visited
            self.enqueue_unvisited_locations(current_loc, visited, q)

    def visited_location(self, vertex, visited):
        """
        mark location as visited
        print places that have visited
        :param vertex: location
        :param visited: dictionary that hold visited locations
        :return: None
        """
        if vertex not in visited or visited[vertex] is False:
            visited[vertex] = True
            print(f"{vertex}", end=" ")

    def enqueue_unvisited_locations(self, current_loc, visited, que):
        """
        look for destination that is connected to current location
        determine if those locations have been visited
        If not, add to queue
        :param current_loc: current location
        :param visited: dictionary that hold visited locations
        :param que: places that need to be visited
        :return: None
        """
        if current_loc not in self.adjacency_list:  # if current location is not found in adjacency list, return ""
            return
        destinations = self.adjacency_list[current_loc]  # get neighbors value list from current location (key)
        for destination in destinations:  # get destination from destinations value list
            # print(f"destination: {destination}")
            if destination not in visited or visited[destination] is False:  # if destination is not marked visited
                que.appendleft(destination)  # add to queue

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
# p.print_graph()
p.bfs_traversal("SC_Mall")
