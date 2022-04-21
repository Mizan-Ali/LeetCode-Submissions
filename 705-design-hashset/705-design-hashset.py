class MyHashSet:

    def __init__(self):
        self.hashset = [-1 for _ in range(10**6+1)]

    def add(self, key: int) -> None:
        self.hashset[key] = 1

    def remove(self, key: int) -> None:
        self.hashset[key] = -1

    def contains(self, key: int) -> bool:
        if self.hashset[key] == -1:
            return False
        return True


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)