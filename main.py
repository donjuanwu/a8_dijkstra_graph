"""
Developer: Don Dang
Date: 3/13/24
Week: 8
Subject: Graph

References:
    1. A Common-Sense Guide to Data Structures and Algorithms, Second Edition, 2nd Edition,
    Chapter 18 - Dijkstra's Algorithm
    - https://learning.oreilly.com/library/view/a-common-sense-guide/9781680508048/f_0186.xhtml#sect.dijkstras-algorithm
    2. What is ternary operator in Python?
    - https://www.educative.io/answers/what-is-the-ternary-operator-in-python

Assignment Requirements:
    1. Use Dijkstra's Algorithm to find the shortest path



Date        Developer     Activities
3/13/24      Don D        Attempt to start assignment 8
"""

import collections  # special data structures


class Place:
    def __init__(self):
        """
        create dictionary to hold starting location to its neighbors
        create dictionary to hold cheapest path from starting location to adjacent station
        create dictionary to hold cheapest previous stopped locations
        """
        self.adjacency_list = {}  # adjacency list to hold starting location and their neighbors and travel cost
        self.cheapest_prices_table = {}  # hold the cheapest prices from starting location to adjacent station
        self.cheapest_previous_stopped_station = {}  # hold the cheapest previous stopped location

    @staticmethod
    def create_graph(graph_config):
        """
        create graphs
        :param graph_config: map configuration
        :return: Place instance
        """
        g = Place()
        # A Common-Sense Guide to Data Structures and Algorithms, Second Edition, 2nd Edition. Chapter 18
        # https://learning.oreilly.com/library/view/a-common-sense-guide/9781680508048/
        if graph_config == 1:  # Flight shortest path from Atlanta to El Paso
            g.add_travel_route("Atlanta", "Boston", 100)
            g.add_travel_route("Atlanta", "Denver", 160)
            g.add_travel_route("Boston", "Chicago", 120)
            g.add_travel_route("Boston", "Denver", 180)
            g.add_travel_route("Chicago", "El Paso", 80)
            g.add_travel_route("Denver", "Chicago", 40)
            g.add_travel_route("Denver", "El Paso", 140)
        elif graph_config == 2:  # Buses and Link Light Rail shortest path from South Center Mall to Seattle Center
            g.add_travel_route("Southcenter Mall", "Tukwila Station", 0)
            g.add_travel_route("Southcenter Mall", "Intl District", 4)
            g.add_travel_route("Southcenter Mall", "Renton Park Ride", 5)
            g.add_travel_route("Tukwila Station", "Westlake Center", 5)
            g.add_travel_route("Westlake Center", "Seattle Center", 4)
            g.add_travel_route("Intl District", "Westlake Center", 1)
            g.add_travel_route("Intl District", "Seattle Center", 3)
            g.add_travel_route("Renton Park Ride", "Seattle Center", 3)
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
        print(f"Starting Location: {start_loc}")
        print(f"Visited locations: ", end=" ")
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
        self.cheapest_prices_table[start_loc] = 0  # set starting location as first key and set travel cost to itself $0
        while q:
            current_loc = q.pop()  # pop queue and make starting location as current location
            self.visited_location(current_loc, visited)  # mark current location as visited
            self.enqueue_unvisited_locations(current_loc, visited, q)

    def visited_location(self, location, visited):
        """
        mark location as visited
        print places that have visited
        :param location: location
        :param visited: dictionary that hold visited locations
        :return: None
        """
        if location not in visited:
            visited.add(location)
            print(location, end=" ")

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
        # get neighbors locations as a value list (contains adjacent location & its travel cost) from current location
        travel_routes = self.adjacency_list[current_loc]
        unvisited_stations = []  # list to hold unvisited/adjacent stations
        for destination in travel_routes:  # get destination from travel routes
            if destination not in visited:  # if next destination/adjacent is not marked visited
                unvisited_stations.append(destination)  # add unvisited destination to list
                cost = travel_routes[destination]  # retrieve travel cost to destination
                self.add_cheapest_path(current_loc, destination,
                                       cost)  # update cheapest_price_table and cheapest_previous_stop_station
        while len(unvisited_stations) > 0:
            cheapest_unvisited_station = min(unvisited_stations,
                                             key=self.get_travel_route_price)  # find the cheapest unvisited station
            if cheapest_unvisited_station not in que:  # if cheapest_unvisited_station is not in queue
                que.appendleft(
                    cheapest_unvisited_station)  # add next unvisited station with the cheapest travel cost to queue
            unvisited_stations.remove(cheapest_unvisited_station)  # remove unvisited station from list

    def add_cheapest_path(self, current_loc, destination, cost):
        """
        retrieve travel cost to destination from self.cheapest_prices_table
        if destination travel cost isn't found in table or current travel cost to destination is greater than price to destination
            update self.cheapest_prices_table and self.cheapest_previous_stopped_station
        :param current_loc: begin travel location
        :param destination: travel to destination
        :param cost: travel fee from current location to destination
        :return: None
        """
        # use. get() to avoid KeyError, provide default value
        price_to_destination = cost + self.cheapest_prices_table.get(current_loc,
                                                                     0)  # calculate total travel cost from current location to destination
        if not self.cheapest_prices_table.get(destination, None) or price_to_destination < self.cheapest_prices_table[
            destination]:
            # add/update destination in self.cheapest_prices_table to price to destination
            self.cheapest_prices_table[destination] = price_to_destination
            # add destination to self.cheapest_previous_stopped_station as key and current location as value
            self.cheapest_previous_stopped_station[destination] = current_loc

    def get_travel_route_price(self, destination):
        """
        iterate for each station (key) in self.cheapest_prices_table and find its minimal/cheap travel cost
        :param destination:
        :return: destination travel cost
        """
        return self.cheapest_prices_table.get(destination, float('inf'))

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

    def find_shortest_path(self, start_loc, final_loc):
        """
        find the shortest path starting from the given location to the final location
        :param start_loc: where to begin
        :param final_loc: final destination
        :return: None
        """
        if self.cheapest_prices_table.get(start_loc, None) is None or self.cheapest_prices_table.get(final_loc,
                                                                                                     None) is None:
            return
        shortest_path = []  # list to hold the shortest path
        current_loc = final_loc  # set final destination to current location
        shortest_path.append(final_loc)  # add final destination to list
        while current_loc != start_loc:  # loop while current location not equal to starting location
            current_loc = self.cheapest_previous_stopped_station[
                current_loc]  # get the preceding stop immediately before the current location
            shortest_path.append(current_loc)  # add immediate preceding location to list
        return shortest_path

    def find_shortest_path_cost(self, final_loc):
        """
        get the total travel cost to final destination
        ternary operator:
            [on_true] if [condition] else [on_false]
        :param final_loc: final location
        :return: return 0, if final location doesn't exist else return travel cost
        """
        return self.cheapest_prices_table.get(final_loc, 0) if final_loc in self.cheapest_prices_table else 0


# A Common-Sense Guide to Data Structures and Algorithms, Second Edition, 2nd Edition. Chapter 18
# https://learning.oreilly.com/library/view/a-common-sense-guide/9781680508048/
graph = 1  # Flight route from Atlanta to El Paso
p1 = Place.create_graph(graph)
# p1.print_graph()
p1.bfs_traversal("Atlanta")
begin_loc = "Atlanta"
ending_loc = "El Paso"
short_path = p1.find_shortest_path(begin_loc, ending_loc)
formatted_path = " -> ".join(short_path[::-1])
print()
print(f"Shortest path from {begin_loc} to {ending_loc}: {formatted_path}")
print(f"\tShortest path travel cost: ${p1.find_shortest_path_cost(ending_loc)}")
# ----------------------------------------------------------------------------------------------------------
print()
graph = 2  # Buses and Link Light Rail route from Southcenter Mall to Seattle Center
p2 = Place.create_graph(graph)
# p2.print_graph()
p2.bfs_traversal("Southcenter Mall")
begin_loc = "Southcenter Mall"
ending_loc = "Seattle Center"
short_path = p2.find_shortest_path(begin_loc, ending_loc)
formatted_path = " -> ".join(short_path[::-1])
print()
print(f"Shortest path from {begin_loc} to {ending_loc}: {formatted_path}")
print(f"\tShortest path travel cost: ${p2.find_shortest_path_cost(ending_loc)}")
