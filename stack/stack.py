"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return self.size

    def push(self, value):
        self.size +=1
        self.storage.insert(0, value)

    def pop(self):
        if len(self.storage) > 0:
            value = self.storage[0]
            self.storage.pop(0)
            self.size -=1
            return value
        return None

# **** ARRAY IMPLEMENTATION ****
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return self.size

#     def push(self, value):
#         self.size +=1
#         self.storage.insert(0, value)

#     def pop(self):
#         if len(self.storage) > 0:
#             value = self.storage[0]
#             self.storage.pop(0)
#             self.size -=1
#             return value
#         return None