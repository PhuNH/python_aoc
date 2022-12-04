import copy
import heapq
import math
from collections import deque

from libs.vector import Area, Vector


class Path:
    def __init__(self, start):
        self.nodes = [start]
        self.node_set = set(self.nodes)

    def add_node(self, node):
        path = copy.deepcopy(self)
        path.nodes.append(node)
        path.node_set.add(node)
        return path

    def __contains__(self, item):
        return item in self.node_set


class MyDistances:
    def __init__(self, own: int, tentative: int = -1):
        self.own = own
        self.tentative = tentative


def my_shortest_path_tree(grid: [[int]], start: Vector[int]) -> Area[MyDistances]:
    area: Area[MyDistances] = Area([[MyDistances(e) for e in row] for row in grid])
    q: deque[(Vector, int)] = deque()
    q.append((start, 0))
    area.at(start).tentative = 0
    while q:
        current_node, current_tentative = q.popleft()
        current_distances = area.at(current_node)
        if current_tentative > current_distances.tentative:
            continue
        connected_nodes = area.adjacents(current_node)
        for n in connected_nodes:
            next_distances = area.at(n)
            next_tentative = current_tentative + next_distances.own
            if next_distances.tentative == -1 or next_tentative < next_distances.tentative:
                next_distances.tentative = next_tentative
                q.append((n, next_tentative))
    return area


class DijkstraDistances:
    def __init__(self, own: int, tentative: int = math.inf):
        self.own = own
        self.tentative = tentative


def dijkstra_shortest_path_tree(grid: [[int]], start: Vector[int]) -> Area[DijkstraDistances]:
    visited = set()
    area: Area[DijkstraDistances] = Area([[DijkstraDistances(e) for e in row] for row in grid])
    area.at(start).tentative = 0
    q = [(0, (start.x, start.y))]

    while q:
        current_tentative, current_node = heapq.heappop(q)
        current_node_vec = Vector(*current_node)
        for next_node in area.adjacents(current_node_vec):
            if next_node in visited:
                continue

            next_distances = area.at(next_node)
            next_tentative = current_tentative + next_distances.own
            if next_tentative < next_distances.tentative:
                next_distances.tentative = next_tentative
                heapq.heappush(q, (next_tentative, (next_node.x, next_node.y)))
        visited.add(current_node_vec)
    return area
