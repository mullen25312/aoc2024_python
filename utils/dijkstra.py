import math

class AbstractDijkstraSPF(object):

    """ Dijkstra's shortest path algorithm, abstract class. """

    def __init__(self, G, s):
        """ Calculate shortest path from s to other nodes in G. """
        self.__dist = dist = dict()
        self.__prev = prev = dict()
        visited = set()
        queue = set()

        dist[s] = 0
        prev[s] = [s]
        queue.add(s)

        while queue:
            u = min(queue, key=dist.get)
            for v in self.get_adjacent_nodes(G, u):
                if v in visited:
                    continue
                alt = self.get_distance(u) + self.get_edge_weight(G, u, v)
                if alt < self.get_distance(v):
                    dist[v] = alt
                    prev[v] = [u]
                    queue.add(v)
                elif alt == self.get_distance(v):
                    prev[v].append(u)
                    queue.add(v)
            queue.remove(u)
            visited.add(u)

    @staticmethod
    def get_adjacent_nodes(G, u):
        raise NotImplementedError()

    @staticmethod
    def get_edge_weight(G, u, v):
        raise NotImplementedError()

    def get_distance(self, u):
        """ Return the length of shortest path from s to u. """
        return self.__dist.get(u, math.inf)

    def get_path(self, v):
        """ Return the shortest path to v. """
        path = [v]
        while v not in self.__prev[v]:
            v = self.__prev[v][0]
            path.append(v)
        return path[::-1]

    def get_number_of_paths(self, v):
        if v in self.__prev[v]:
            return 1
        tmp = 0
        for option in self.__prev[v]:
                tmp += self.get_number_of_paths(option)
        return tmp

    def get_all_visited(self, v, visited):
        if v in self.__prev[v]:
            return visited
        else:
            for option in self.__prev[v]:
                visited.add(option)
                visited.update(self.get_all_visited(option, visited))
            return visited