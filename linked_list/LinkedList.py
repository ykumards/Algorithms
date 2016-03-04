class Node(object):
    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList(object):
    def __init__(self, head_val):
        head = Node(head_val)
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

if __name__ == "__main__":
    l = LinkedList(1)
    l.add(2)
    l.add(3)
    l.add(4)
    l.add(5)
    l.pretty_print()
    print l.mid_point()
        
