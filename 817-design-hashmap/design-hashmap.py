class MyHashMap:

    def __init__(self):
        self.a = [False] * 1000001
        self.b = [1] * 1000001

    def put(self, key: int, value: int) -> None:
        self.a[key] = True
        self.b[key] = value

    def get(self, key: int) -> int:
        if self.a[key]:
            return self.b[key]
        return -1
        
    def remove(self, key: int) -> None:
        self.a[key] = False
        self.b[key] = 1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)