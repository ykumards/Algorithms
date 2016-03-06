class TreeNode(object):
    def __init__(self, val):
        self.name = val
        self.left = None
        self.right = None

class Tree(object):
    def __init__(self):
        self.root = None
    
    def _inOrder(self, node):
        if not node:
            return None
        self._inOrder(node.left)
        print node.name
        self._inOrder(node.right)

    def in_order_print(self):
        node = self.root
        self._inOrder(node)        


def minimal_tree(low, high, arr):
    """
    Sorted list, build a BST form it which has minimal height.
    """
    if low > high:
        return None
    mid = (high + low)/2
    node = TreeNode(arr[mid])
    node.left = minimal_tree(low, mid-1, arr)
    node.right = minimal_tree(mid+1, high, arr)
    return node


if __name__ == "__main__":
    # Testing minimal_tree
    arr = [2,3,5,10,13,15]
    t = Tree()
    t.root = minimal_tree(0, len(arr)-1, arr)
    t.in_order_print()

