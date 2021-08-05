from enum import Enum


class State(Enum):
    unvisited = 0
    visiting = 1
    visited = 2


class Node:
    def __init__(self, key):
        self.key = key
        self.visit_state = State.unvisited
        self.incoming_edges = 0
        self.adj_nodes = {}
        self.adj_weights = {}

    def __repr__(self) -> str:
        return str(self.key)

    def __lt__(self, other):
        return self.key < other.key

    def upsert_neighbor(self, neighbor, weight=0):
        if neighbor is None or weight is None:
            raise TypeError('neighbor or weight cannot be None')
        if neighbor.key not in self.adj_nodes:
            neighbor.incoming_edges += 1
        self.adj_nodes[neighbor.key] = neighbor
        self.adj_weights[neighbor.key] = weight

    def remove_neighbor(self, neighbor):
        if not neighbor or neighbor.key not in self.adj_nodes:
            raise ValueError('not found')
        del self.adj_nodes[neighbor.key]
        del self.adj_weights[neighbor.key]
        neighbor.incoming_edges -= 1
        # what about removed neighbor's neighbors? (they need to update and be aware about it's deletion)


class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, key):
        if key is None:
            raise TypeError('key cannot be None')
        if key not in self.nodes:
            self.nodes[key] = Node(key)

    def add_edge(self, src_key, dest_key, weight=0):
        if src_key is None or dest_key is None:
            raise TypeError('source and destination keys cannot be None')
        if src_key not in self.nodes:
            self.nodes[src_key] = Node(src_key)
        if dest_key not in self.nodes:
            self.nodes[dest_key] = Node(dest_key)
        self.nodes[src_key].upsert_neighbor(self.nodes[dest_key], weight)

    def add_undirected_edge(self, src_key, dest_key, weight=0):
        if src_key is None or dest_key is None:
            raise TypeError('source and destination keys cannot be None')
        self.add_edge(src_key, dest_key, weight)
        self.add_edge(dest_key, src_key, weight)
