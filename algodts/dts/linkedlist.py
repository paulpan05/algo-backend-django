class SNode:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

class DNode(SNode):
    def __init__(self, data=None, prev_node=None, next_node=None):
        super.__init__(data, next_node)
        self.prev = prev_node
