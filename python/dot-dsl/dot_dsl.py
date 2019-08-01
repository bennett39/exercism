NODE, EDGE, ATTR = range(3)


class Node(object):
    def __init__(self, name, attrs):
        self.name = name
        self.attrs = attrs

    def __eq__(self, other):
        return self.name == other.name and self.attrs == other.attrs


class Edge(object):
    def __init__(self, src, dst, attrs):
        self.src = src
        self.dst = dst
        self.attrs = attrs

    def __eq__(self, other):
        return (self.src == other.src and
                self.dst == other.dst and
                self.attrs == other.attrs)


class Graph(object):
    def __init__(self, data=[]):
        self.nodes = []
        self.edges = []
        self.attrs = {}
        self._parse(data)

    def _parse(self, data):
        if type(data) != type([]):
            raise TypeError("Initialize Graph with a list")
        for n in data:
            try:
                data_type = n[0]
            except:
                raise TypeError("Message")
            if n[0] == ATTR:
                if len(n) != 3:
                    raise ValueError("Invalid input type or format")
                self.attrs[n[1]] = n[2]
            elif n[0] == NODE:
                if len(n) != 3:
                    raise ValueError("Invalid input type or format")
                self.nodes.append(Node(n[1], n[2]))
            elif n[0] == EDGE:
                if len(n) != 4:
                    raise ValueError("Invalid input type or format")
                self.edges.append(Edge(n[1], n[2], n[3]))
            else:
                raise TypeError("Must be NODE, ATTR, or EDGE")

