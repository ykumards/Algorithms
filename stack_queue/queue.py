"""
Queue class to handle common tasks in a queue
"""
class Node(object):
    def __init__(self, value):
        self.data = value
        self.next = None

class Queue(object):
    def __init__(self):
        self.items = []

    def __str__(self):
        return ("Queue of size %d" % len(self.items))

    def isEmpty(self):
        return len(self.items) == 0

    def enqueue(self, value):
        new_node = Node(value)
        self.items.insert(0, new_node)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


if __name__ == "__main__":
    
        
