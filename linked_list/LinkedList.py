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

    ###### Delete Mid ########
    def delete_node(self, del_node):
        """
        Pretend that we only have access to the node del_node, delete it
        without having access to any other element
        """
        if not del_node or not del_node.next:
            return "Error: Nothing ahead of del_node"

        current = del_node.next
        del_node.data = current.data
        del_node.next = current.next
        return "Done. Print to verify."

######### Remove Duplicates ########################
def removeDups(l, useBuffer):
    """
    Wrapper method around the two remove dup methods
    Decides based on a boolean useBuffer
    """
    if useBuffer:
        return _removeDups(l)
    else:
        return _removeDups_mem(l)
    
def _removeDups(l):
    """
    Input is some linked list, and the function returns a
    linked list without any duplicate elements
    The function runs in O(n) time but needs extra buffer space
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

def _removeDups_mem(l):
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

###### Kth to last element ##########
def k_to_last_iter(head, k):
    """
    Method returns the index of last element iteratively
    It uses a fast pointer that is ahead of the slow pointer
    by k hops. So when the fast pointer hits the end, the slow
    points to the kth last elements

    NOTE: k has to be greater than 0. So 1st last element is 
    the last element 
    """
    if k < 1:
        return "ERROR: k has to be > 0"
    slow = head
    fast = head
    ctr = 0
    while ctr < k:
        fast = fast.next
        ctr += 1
    while fast:
        slow = slow.next
        fast = fast.next
    
    return slow.data
       
############# Addition in Linked List #############
def addition(l1, l2):
    """
    Given two linked lists, whose each node represents a number's digit
    (e.g., 1254 == 4 -> 5 -> 2 -> 1 -> NULL)
    Add these two numbers and return the linked list
    """
    

         
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
    #l_m = removeDups(l, True)
    #l_m.pretty_print()
    print k_to_last_iter(l.head, 0)
     
