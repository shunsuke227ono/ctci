import Queue

class Node(object):
    def __init__(self):
        self.visted = False
        self.adjacents = []

class IsConnected(object):
    def __init__(self):
        pass
    def connected(self, start, end):
        # DFS
        q = Queue.Queue()
        q.put(start)
        while not q.empty():
            node = q.get()
            if node == end:
                return True
            else:
                for next_node in node.adjacents:
                    if next_node.visted:
                        continue
                    else:
                        q.put(next_node)
                        next_node.visted = True
        return False

def test():
    node0 = Node()
    node1 = Node()
    node2 = Node()
    node3 = Node()
    node4 = Node()
    node5 = Node()
    node6 = Node()
    node7 = Node()
    node8 = Node()
    node9 = Node()
    node10 = Node()
    node0.adjacents = [node1, node6]
    node1.adjacents = [node5, node2]
    node2.adjacents = [node3]
    node3.adjacents = [node4]
    node4.adjacents = [node2]
    node5.adjacents = [node6]
    node6.adjacents = [node7]
    node7.adjacents = [node8]
    node8.adjacents = []
    node9.adjacents = [node10]
    node10.adjacents = []
    ic = IsConnected()
    print ic.connected(node0, node9)
if __name__ == "__main__":
    test()
