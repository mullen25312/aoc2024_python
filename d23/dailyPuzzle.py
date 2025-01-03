from dxx.superDailyPuzzle import SuperDailyPuzzle

from utils.graph import Graph

def BronKerbosch(graph, R, P, X, result):
    if not (P or X): # if P and X are both empty
        return result.append(R)
    for node in P:
        BronKerbosch(graph, R.union({node}), P.intersection(graph.get_adjacent_nodes(node)), X.intersection(graph.get_adjacent_nodes(node)), result)
        P = P.difference({node})
        X = X.union({node})

# advent of code 2024 day 23
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self, **kwargs):
        
        connections = []
        for line in self.data.splitlines():
            connections.append(line.split("-"))
        self.parsed = connections
           
    def part_one(self, **kwargs): 
        connections = self.parsed

        connections_graph = Graph()
        for connection in connections:
            connections_graph.add_edge(connection[0], connection[1], 0)
            connections_graph.add_edge(connection[1], connection[0], 0)

        triplets = set()
        for node in connections_graph.get_nodes():
            adjacents = connections_graph.get_adjacent_nodes(node)
            for adjacent in adjacents:

                ad_adjacents = connections_graph.get_adjacent_nodes(adjacent).copy()
                # ad_adjacents.remove(node)
                for ad_adjacent in ad_adjacents:
                        
                    ad_ad_adjacents = connections_graph.get_adjacent_nodes(ad_adjacent).copy()
                    # ad_ad_adjacents.remove(adjacent)
                    if node in ad_ad_adjacents: triplets.add(frozenset({node, adjacent, ad_adjacent}))

        # connections_graph.__str__()
        self.part_one_result = [any(map(lambda x: x[0] == 't', triplet)) for triplet in map(lambda x: list(x), triplets)].count(True)

    def part_two(self, **kwargs): 
        connections = self.parsed

        connections_graph = Graph()
        for connection in connections:
            connections_graph.add_edge(connection[0], connection[1], 0)
            connections_graph.add_edge(connection[1], connection[0], 0)

        result = []
        BronKerbosch(connections_graph, set(), set(connections_graph.get_nodes()), set(), result)

        self.part_two_result = ','.join(sorted(max(result, key=lambda x: len(x))))
