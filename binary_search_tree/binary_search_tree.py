from collections import deque
"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # what if the value is more than that of the root?
        # what if the value is the same as that of the root?
        if value >= self.value:
            # go right
            if not self.right:
                # there is nothing to the right--add the value here
                self.right = BSTNode(value)
                return
            else:
                return self.right.insert(value)
            
        # what if the value is less than that of the root?
        if value < self.value:
            # go left
            if not self.left:
                # there is nothing to the left--add the value here
                self.left = BSTNode(value)
                return
            else:
                return self.left.insert(value)
        

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        if target < self.value:
            # target is smaller--go left
            if self.left is not None:
                # continue the search left
                return self.left.contains(target)
            else:
                # we've reached the end with no matches
                return False
        if target > self.value:
            # target is larger--go right
            if self.right is not None:
                # continue the search right
                return self.right.contains(target)
            else:
                # we've reached the end with no matches
                return False
    
    # Return the maximum value found in the tree
    def get_max(self):
        # just go right until we reach the end
        if not self.right:
            return self.value
        return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # call on current value
        fn(self.value)
        # loop through both left and right
        if self.right:
            self.right.for_each(fn)
        if self.left:
            self.left.for_each(fn)
            
    
    def breadth_first_search(self, fn):
        queue = deque()
        
        queue.append(self)
        
        while len(queue) > 0:
            current = queue.popleft()
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
                
            fn(current.value)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        print(node.value)
        if self.left is not None:
            # continue the search left
            self.left.dft_print(self.left)

        if self.right is not None:
            # continue the search right
            self.right.dft_print(self.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


# bst = BSTNode(1)
# bst.insert(8)
# bst.insert(5)
# bst.insert(7)
# bst.insert(6)
# bst.insert(3)
# bst.insert(4)
# bst.insert(2)
# bst.dft_print(bst)