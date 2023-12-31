"""
Leetcode
706. Design HashMap (easy)
2022-04-22

Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:

 - MyHashMap() initializes the object with an empty map.
 - void put(int key, int value) inserts a (key, value) pair into the 
   HashMap. If the key already exists in the map, update the corresponding 
   value.
 - int get(int key) returns the value to which the specified key is mapped, 
   or -1 if this map contains no mapping for the key.
 - void remove(key) removes the key and its corresponding value if the map 
   contains the mapping for the key.
"""

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)



# try 1
# Runtime: 1123 ms, faster than 18.60% of Python3 online submissions for Design HashMap.
# Memory Usage: 17.4 MB, less than 51.47% of Python3 online submissions for Design HashMap.
class MyHashMap:

    def __init__(self):
        self.keys = []
        self.vals = []
        
    def put(self, key: int, value: int) -> None:
        if key not in self.keys:
            self.keys.append(key)
            self.vals.append(value)
        else:
            self.vals[self.keys.index(key)] = value

    def get(self, key: int) -> int:
        if key in self.keys:
            return self.vals[self.keys.index(key)]
        else:
            return -1

    def remove(self, key: int) -> None:
        if key in self.keys:
            idx = self.keys.index(key)
            del self.keys[idx]
            del self.vals[idx]



# python cheating
# Runtime: 212 ms, faster than 95.69% of Python3 online submissions for Design HashMap.
# Memory Usage: 17.1 MB, less than 96.99% of Python3 online submissions for Design HashMap.
class MyHashMap:

    def __init__(self):
        self.mhm = {}
        
    def put(self, key: int, value: int) -> None:
        self.mhm[key] = value

    def get(self, key: int) -> int:
        return self.mhm.get(key, -1)

    def remove(self, key: int) -> None:
        self.mhm.pop(key, None)



# s = Solution()
# tests = []
# for t in tests:
#     print(t)
#     print()
#     print()
