from doubly_linked_list import DoublyLinkedList, ListNode
class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        # cache is for holding the items
        self.cache = DoublyLinkedList()
        # map is for holding indexes that point to items
        self.map = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key not in self.map.keys():
            return None
        node = self.map[key]
        # gets the value of the node stored at
        # the given key
        value = node.value[1]
        # update this node so it is the first
        # in the cache.
        self.cache.move_to_front(node)
        return value
    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        # what if the key exists?
        # if it does, update the value vs adding
        # and move to front
        if key in self.map.keys():
            # remove the value from the cache
            print(self.cache)
            self.cache.delete(self.map[key])
            # update the map with the new value
            self.map[key] = ListNode((key, value))
            # add the new value to the front of the cache
            
            self.cache.add_to_head(self.map[key])
            print(self.cache)
        # what if the key doesn't exist?
        # if it doesn't, add a new item to the cache
        # and update the map
        else:
            # add the new key/value to the map.
            # the key needs to be in the node because
            # we need a way to find the key of an item
            # being removed from the tail
            self.map[key] = ListNode((key, value))
            # add the new node to the cache
            self.cache.add_to_head(self.map[key])
        
        # what if the cache is over its limit?
        # if so, we need to evict the last item from the cache
        if self.cache.length > self.limit:
            # remove from the cache tail, and get the key back
            # with which to delete the map ref
            key_to_remove = self.cache.remove_from_tail().value[0]
            # delete the map ref
            del self.map[key_to_remove]
        
lru = LRUCache(3)
lru.set('item1', 'a')
lru.set('item2', 'b')
lru.set('item3', 'c')

lru.set('item4', 'd')

lru.set('item2', 'bbb')
