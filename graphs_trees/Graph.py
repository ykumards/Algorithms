class STATE:
    white = 0
    grey = 1
    black = 2


class GraphNode(object):
    def __init__(self, val):
        self.name = val
        self.state = STATE.white
        self.adj = []
    def add(self, node):
        """
        Adding a new node to the adj list
        """
        self.adj.append(node)

class Graph(object):
    def __init__(self):
        self.nodes = []

    def add(self, node):
        """
        Append nodes one by one to the list
        """
        self.nodes.append(node)

    def _search(self,s):
        s.state = STATE.grey
        print s.name
        for node in s.adj:
            if node.state == STATE.white:
                self._search(node)
        s.state = STATE.black        

    def dfs(self):
        for node in self.nodes:
            if node.state == STATE.white:   
                self._search(node)
    
    def bfs(self, s):
        s.state = STATE.grey
        q = []
        q.insert(0, s)
        while q:
            l = q.pop()
            print l.name
            for node in l.adj:
                if node.state == STATE.white:
                    q.insert(0, node)
                    node.state = STATE.grey
            l.state = STATE.black 

    def is_route(self, node1, node2):
        """
        If we are given a graph and two nodes as input, the function
        returns true if there is a path from node1 to node2 and false
        otherwise
        """
        if node1.name == node2.name:
            return True
        s = node1
        s.state = STATE.grey
        q = []
        q.insert(0, s)
        while q:
            l = q.pop()
            for node in l.adj:
                if node.name == node2.name:
                    return True
                q.insert(0, node)
                node.state = STATE.grey
            l.state = STATE.black
        return False

if __name__ == "__main__":
    g = Graph()
    node1 = GraphNode(1)
    node2 = GraphNode(2)
    node3 = GraphNode(3)
    node4 = GraphNode(4)
    node5 = GraphNode(5)
    node1.add(node2)
    node2.add(node3)
    node3.add(node5)
    node4.add(node2)
    g.add(node1)
    g.add(node2)
    g.add(node3)
    g.add(node4)
    g.add(node5)
    #print "Running DFS"
    #g.dfs()
    print "Running BFS"
    g.bfs(node4)
    print "Is route"
    print g.is_route(node4, node2)
