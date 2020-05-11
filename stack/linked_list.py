
class LinkedList:
    def __init__(self):
        self.head = None
        
    def add_as_head(self, value):
        new_head = Node(value)
        # what if this is an empty list?
        if not self.head:
            self.head = new_head
        # what if there are already items in this list?
        else:
            new_head.set_next(self.head)
            self.head = new_head
            
    def add_as_tail(self, value):
        new_tail = Node(value)
        # what if this is an empty list?
        if not self.head:
            self.head = new_tail
        # what if there are already items in this list?
        else:
            current_node = self.head
            while current_node.get_next() is not None:
                current_node = current_node.get_next()
                
            # this is the end of the list; add the new tail
            current_node.set_next(new_tail)
            
    def count(self):
        # if list is empty, return
        if not self.head:
            return 0
        
        current_count = 0
        current_node = self.head
        while True:
            if current_node is not None:
                current_count += 1
                current_node = current_node.get_next()
            else:
                break
        
        return current_count
    
    def remove_head(self):
        if self.head is not None:
            value = self.head.value
            self.head = self.head.next_node()
            return value
        return None
    
    def remove_tail(self):
        if not self.head:
            return None
        
        current_node = self.head
        while current_node is not None:
            # check to see if the next node is the last node
            if current_node.next_node().next_node() is None:
                # sever off the last node, making the current
                # node the new tail
                current_node.set_next(None)
                break
            current_node = current_node.next_node()
                
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next_node = None
        
    def get_value(self):
        return self.value
        
    def get_next(self):
        return self.next_node
    
    def set_next(self, new_next):
        self.next_node = new_next