"""
Developer: Don Dang
Date: 3/13/24
Week: 8
Subject: Graph

References:
    1. A Common-Sense Guide to Data Structures and Algorithms, Second Edition, 2nd Edition,
    Chapter 18 - Dijkstra's Algorithm
    - https://learning.oreilly.com/library/view/a-common-sense-guide/9781680508048/f_0186.xhtml#sect.dijkstras-algorithm

Assignment Requirements:
    1. Use Dijkstra's Algorithm to find the shortest path



Date        Developer     Activities
3/13/24      Don D        Attempt to start assignment 8
"""

import collections  # special data structures


class Place:
    def __init__(self):
        """
        create dictionaries to hold graph, cheapest path and cheapest prior stopped locations
        """
        self.adjacency_list = {}  # adjacency list to hold vertices and their neighbors and weights
        self.cheapest_prices_table = {}  # hold the cheapest prices starting location
        self.cheapest_previous_stopped_station = {}  # hold the cheapest prior stopped location

    @staticmethod
    def create_graph(graph_config):
        """
        create graphs
        :param graph_config: map configuration
        :return: Place instance
        """
        g = Place()
        if graph_config == 1:  # create graph to find the shortest path from Atlanta to El Paso
            pass
        elif graph_config == 2:  # create graph to find the shortest path from South Center Mall to Seattle Center
            g.add_travel_route("SC_Mall", "Tukwila_LLR_Station", 0)
            g.add_travel_route("SC_Mall", "Intl_District", 4)
            g.add_travel_route("SC_Mall", "Renton_Park_Ride", 5)
            g.add_travel_route("Tukwila_LLR_Station", "Westlake_Center", 5)
            g.add_travel_route("Westlake_Center", "Seattle_Center", 4)
            g.add_travel_route("Intl_District", "Westlake_Center", 1)
            g.add_travel_route("Intl_District", "Seattle_Center", 3)
            g.add_travel_route("Renton_Park_Ride", "Seattle_Center", 3)
        elif graph_config == 3:  # create a graph to find the shortest path to locate a specific relative (blood/non-blood) starting from great-grandfather
            pass
        return g

    def add_travel_route(self, start_loc, destination, cost):
        """
        create the adjacency list that include start location, destination and travel cost
        :param start_loc: starting location
        :param destination: destination
        :param cost: travel cost
        :return: None
        """
        if start_loc not in self.adjacency_list:  # if start Location is not already in adjacency list
            self.adjacency_list[start_loc] = {}  # set start location value to be an empty dictionary
        self.adjacency_list[start_loc][destination] = cost  # update {start location: {destination: cost}}

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
        create visited set to locations that have visited
        create deque object to hold locations
        call visited_location to mark visited location
        call enqueue_unvisited_locations
        :param start_loc: starting vertex
        :return: None
        """
        visited = set()  # create empty set to hold visited locations
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
        if vertex not in visited:
            visited.add(vertex)
            print(f"{vertex}", end=" ")

        # if vertex not in visited or visited[vertex] is False:
        #     visited[vertex] = True
        #     print(f"{vertex}", end=" ")

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
            if destination not in visited:  # if destination is not marked visited
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
p.print_graph()
print()
p.bfs_traversal("SC_Mall")
