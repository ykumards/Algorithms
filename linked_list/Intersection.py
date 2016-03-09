"""
Two linked lists intersect if they have a common node (not just
a node with common value). So the tail of the two linked lists
will be the same.
Hence, to determine if two linked lists intersect is simple, 
just look at the last element. But to find out where they intersect
we have to handle the case where they could have different lengths.
"""
import LinkedList as ll

def isEqual(node1, node2):
    if node1.data == node2.data and node1.next == node2.next:
        return True
    return False

def intersect(ll1, ll2):
    if isEqual(ll1.head, ll2.head):
        return runner1
    
    # Check if they have the same tail
    tail1 = ll1.head
    tail2 = ll2.head
    len1, len2 = 0, 0
    while tail1.next:
        len1 += 1
        tail1 = tail1.next
    while tail2.next:
        len2 += 1
        tail2 = tail2.next

    if not isEqual(tail1, tail2):
        return None

    # Now we know the tails are equal, so they must intersect
    # If they have equal length, they will meet when
    # runner1 == runner2 is True. But if they have different
    # lengths, we have to give the runner on longer ll a 
    # head start
    longer = ll1.head
    short = ll2.head
    if len1 < len2:
        longer = ll2.head
        short = ll1.head
    offset = abs(len1 - len2)
    while offset:
        offset -= 1
        longer = longer.next

    # Now simply look for a common node
    while longer.next and short.next:
        if isEqual(longer, short):
            return longer
        longer = longer.next
        short = short.next

    return None

if __name__ == "__main__":
    node1 = ll.Node(1)
    node2 = ll.Node(2)
    node3 = ll.Node(3)
    node4 = ll.Node(4)
    node5 = ll.Node(5)
    ll1 = ll.LinkedList(node1)
    ll2 = ll.LinkedList(node2)
    ll1.add(10)
    ll1.addNode(node3)
    ll1.addNode(node5)
    ll2.addNode(node4)
    ll2.addNode(node3)
    print "ll1:",
    print ll1.pretty_print()
    print "ll2:",
    print ll2.pretty_print()
 
    inter = intersect(ll1, ll2)
    if inter:
        print inter.data
    else:
        print "Not intersecting"     
