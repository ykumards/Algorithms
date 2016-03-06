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

    def reverse_iter(self):
        current = self.head
        previous = None
        nextNode = current.next
        while nextNode:
            current.next = previous
            previous = current
            current = nextNode
            nextNode = nextNode.next

def reverse(l):
    current = l.head
    _reverse(current)

def _reverse(current):
    if not current.next:
        return current
    previous = _reverse(current.next)
    previous.next = current
    return current

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
    TODO: Design a recursive solution
    """
    num1 = l1.head
    num2 = l2.head
    carry = 0
    # Creating a place holder head for the result LL
    # this will be chopped off just before returning
    result_head = Node(-1)
    current = result_head
    while num1 or num2 or carry: # Important not to forget the leftover carry (think 99 + 1)
        item1 = item2 = 0
        if num1:
            item1 = num1.data
            num1 = num1.next
        if num2:
            item2 = num2.data
            num2 = num2.next
        summed= item1 + item2 + carry
        digit = summed % 10 # 23 % 10 = 3
        carry = summed / 10 # Integer division
        new_node = Node(digit)
        current.next = new_node
        current = current.next
    result_list = LinkedList(result_head.next)
    return result_list

def circular_ll(l):
    """
    Given a circular linked list, this would return the beginning of the circular loop
    Returns False if the list is linear. This is a toughie!
    Observations:
    1. We will use two pointers, one moving twice as fast as the other. Then if the two
       meet again, we have a loop.
    2. If they both started from the same place, they will meet at the start. (fast ptr
       would have made two laps by the time the slow ptr made just one!)
    3. If They didn't start at the same place, but say the fast ptr started k steps ahead,
       then they will meet k steps before the start of the loop.
    So we just have to run these two pointers, the place where they meet will be k steps 
    before the start of the loop. Also, this k is the head start that fast ptr got before the small
    ptr entered the loop, so head is k steps away from the start of the loop.
    Reset slow ptr back to head, and leave the fast ptr at the meeting place. Since both these starting
    points are k steps away from the loop start, by running both the pointers AT THE SAME PACE, we 
    are guaranteed that they will meet again at the loop start.
    """
    fast = l.head
    slow = l.head
    # Run one to make them meet
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast.data == slow.data:
            break

    # Handle the case of no circularity
    if not fast.next:
        return False
    # Setting slow back to head
    slow = l.head
    while slow.data != fast.data:
        slow = slow.next
        fast = fast.next

    return fast.data
    
    
         
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

    l1 = LinkedList(Node(3))
    l1.add(9)
    l1.add(9)
    l2 = LinkedList(Node(5))
    l2.add(9)
    l2.add(9)
    l1.pretty_print()
    l2.pretty_print()
    result = addition(l1, l2)
    result.pretty_print()
    

