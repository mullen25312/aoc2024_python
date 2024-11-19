import copy


class Tree:
    def __init__(self):
        self.children = {}

    def add_child(self, name):
        self.children[name] = Tree()

    def search_node(self, name):
        for child in self.children:
            if name in self.children:
                return [self.children[name]]
            tmp = self.children[child].search_node(name)
            if tmp is not None:
                return [self.children[child], *tmp]

    def checksum(self, cnt=0):
        if not self.children:
            return cnt
        else:
            return cnt + sum([self.children[child].checksum(cnt + 1) for child in self.children])

    def number_of_leaves(self, cnt=0):
        if not self.children:
            return cnt + 1
        else:
            return cnt + sum([self.children[child].number_of_leaves(cnt) for child in self.children])

    def number_of_specific_leaves(self, cnt=0, specific="end", chain=list()):
        if not self.children and chain[-1] == specific:
            return cnt + 1
        else:
            tmp = 0
            for child in self.children:
                tmp2 = copy.deepcopy(chain)
                tmp2.append(child)
                tmp += self.children[child].number_of_specific_leaves(cnt, specific, tmp2)
            return cnt + tmp

    def print_tree(self, chain_str=""):
        if not self.children:
            print(chain_str[:-3])
        else:
            for child in self.children:
                self.children[child].print_tree(chain_str + child + " -> ")
