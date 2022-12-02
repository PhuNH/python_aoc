import copy


class Path:
    def __init__(self, start):
        self.nodes = [start]
        self.node_set = set(self.nodes)

    def add_node(self, node):
        path = copy.deepcopy(self)
        path.nodes.append(node)
        path.node_set = set(path.nodes)
        return path

    def __contains__(self, item):
        return item in self.node_set
