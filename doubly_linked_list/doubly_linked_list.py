"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev
            
    def __str__(self):
        return f'{self.value}'


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        # what if there is no head?
        # in this case, self.head will be None and we will simply
        # be setting next to None
        
        new_head = ListNode(value, next=self.head)
        
        if self.head is not None:
            self.head.prev = new_head
        self.head = new_head
        
        # if this was an empty list, update the tail to
        # point to this head
        if self.tail is None:
            self.tail = self.head
        self.length +=1

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        # what if there is no head?
        # what if there's only one item in the list?
        if self.head is None:
            return None
        
        # ensure the length of the list is updated
        self.length -=1
        # set value for return
        value = self.head.value
        
        if self.head is self.tail:
            # the head and the tail point to the same item
            # i.e. there's only one item in this list
            self.head = None
            self.tail = None
            return value
        
        # all other cases--the list has more than one item
        self.head = self.head.next
        self.head.prev = None
        
        return value
        

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        # what if the list is empty?
        new_node = ListNode(value, prev=self.tail)
        
        if self.head is None and self.tail is None:
            # the list is empty
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1
        
        
        

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        # what if the list is empty?
        if self.head is None and self.tail is None:
            return None
        
        value = self.tail.value
        
        # what if there are only two items in the list?
        if self.head is self.tail.prev:
            self.tail = self.head
            self.head.next = None
            
        else:
            # there are more than two items
            if self.tail is not self.head:
                self.tail.prev.next = None
            self.tail = self.tail.prev
        
        self.length -=1
        return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        # remove the node from its current spot
        node_value = node.value
        self.delete(node)
        # add node to the head
        self.add_to_head(node_value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        # remove the node from its current spot
        node_value = node.value
        self.delete(node)
        # add node to the tail
        self.add_to_tail(node_value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        # what if this is the head?
        # what if this is the tail?
        # what if it's both?
        if node is self.head:
            self.head = node.next
        if node is self.tail:
            self.tail = node.prev
        self.length -=1
        return node.delete()
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        highest = 0
        curr = self.head
        while curr is not None:
            if curr.value > highest:
                highest = curr.value
            curr = curr.next
        return highest
    
    def __str__(self):
        list_str = ''
        curr = self.head
        while curr is not None:
            flags = ''
            if curr is self.head:
                flags += '[H]'
            if curr is self.tail:
                flags += '[T]'
            list_str += f'{curr.prev} <-- {flags}{curr} --> {curr.next}\n'
            curr = curr.next
        return list_str
    
node = ListNode(1)
dll = DoublyLinkedList(node)
dll.remove_from_head()
print(dll)
print(dll.head)
print(dll.tail)
print(dll.length)



