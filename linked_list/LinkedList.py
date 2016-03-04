class Node(object):
    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList(object):
    def __init__(self, head):
        self.head = head

    def add(self, value):
        new_node = Node(value)
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def pretty_print(self):
        current = self.head
        while current:
            print current.data, "->",
            current = current.next
        print "NULL"

    def mid_point(self):
        """
        This can be used to find the mid-point of the LL
        without knowing its length. Fast runner runs twice
        as fast as the slow runner, so when the fast reaches
        the end, slow is at the mid-point     
        """
        slow = self.head
        fast = self.head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow.data

def removeDups(l):
    """
    Input is some linked list, and the function returns a
    linked list without any duplicate elements
    """
    if not l.head:
        return None
    alphas = {}
    current = l.head
    previous = None
    while current:
        item = current.data
        if item not in alphas:
            alphas[item] = 1
            previous = current
        else:
            # for deletion we just update previous.next
            # previous pointer stays put
            previous.next = current.next
        current = current.next
    return l

def removeDups_mem(l):
    """
    To remove duplicates without using a buffer, runtime has to be sacrificed
    We get O(n^2) but O(1) space
    """
    if not l.head:
        return None

    current = l.head
    while current:
        item = current.data
        runner = current
        while runner and runner.next:
            if item == runner.next.data:
                # Have to delete runner.next node for this case
                runner.next = runner.next.next
            runner = runner.next
        current = current.next
    return l

if __name__ == "__main__":
    l = LinkedList(Node(1))
    l.add(2)
    l.add(3)
    l.add(4)
    l.add(5)
    l.add(3)
    l.add(2)
    l.add(1)
    l.pretty_print()
    l_m = removeDups_mem(l)
    l_m.pretty_print()
        
