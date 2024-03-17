import main
import pytest


def find_cheapest_flight_path():
    graph = 1
    p1 = main.Place.create_graph(graph)
    begin_loc = "Atlanta"
    ending_loc = "El Paso"
    print(p1.find_shortest_path(begin_loc, ending_loc))
    short_path = ['El Paso', 'Chicago', 'Denver', 'Atlanta']
    assert p1.find_shortest_path(begin_loc, ending_loc) is None


def find_cheapest_path_travel_cost_atlanta():
    graph = 1
    p1 = main.Place.create_graph(graph)
    begin_loc = "Atlanta"
    ending_loc = "El Paso"
    p1.find_shortest_path_cost(ending_loc)
    cost = 280
    assert p1.find_shortest_path_cost(ending_loc) == cost


if __name__ == "__main__":
    pytest.main()
