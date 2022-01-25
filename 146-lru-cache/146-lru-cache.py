class DLL:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hmap = {} # to store the <key:node_addr> pair  
        self.head = DLL(-1, -1)
        self.tail = DLL(-1, -1)
        self.head.right = self.tail
        self.tail.left = self.head
    def delete(self, node):
        node.left.right = node.right
        node.right.left = node.left
        
    def insert(self, node):
        node.right = self.head.right 
        self.head.right.left = node
        self.head.right = node
        node.left = self.head

    def get(self, key: int) -> int:
        if key in self.hmap:
            addr = self.hmap[key]
            value = addr.val
            # Delete the node
            self.delete(addr)
            
            # Insert the node at start (LRU)
            self.insert(addr)
            
            return value
        else:
            return -1
    def put(self, key: int, value: int) -> None:
        if key in self.hmap:
            # simply update the hmap with the new <key: value> pair
            self.delete(self.hmap[key])
            node = DLL(key, value)
            self.insert(node)
            self.hmap[key] = node
            
        elif len(self.hmap) < self.capacity:
            node = DLL(key, value)
            self.insert(node)
            self.hmap[key] = node
        elif len(self.hmap) >= self.capacity:
            nodeToDel = self.tail.left
            del self.hmap[nodeToDel.key]
            self.delete(nodeToDel)
            node = DLL(key, value)
            self.insert(node)
            self.hmap[key] = node
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)