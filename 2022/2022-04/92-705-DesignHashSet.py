"""
Leetcode
705. Design HashSet (easy)
2022-04-21

Design a HashSet without using any built-in hash table libraries.

Implement MyHashSet class:

 - void add(key) Inserts the value key into the HashSet.
 - bool contains(key) Returns whether the value key exists in the HashSet 
   or not.
 - void remove(key) Removes the value key in the HashSet. If key does not 
   exist in the HashSet, do nothing.
"""

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)



# try 1
# Time Limit Exceeded
class MyHashSet:

    def __init__(self):
        self.hs = []
        self.l = 0

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.hs.append(key)
            self.l += 1

    def remove(self, key: int) -> None:
        for i in range(self.l):
            if self.hs[i] == key:
                del self.hs[i]
                self.l -= 1
                return

    def contains(self, key: int) -> bool:
        for i in range(self.l):
            if self.hs[i] == key:
                return True
        return False



# python cheating
class MyHashSet1:

    def __init__(self):
        self.hs = set()

    def add(self, key: int) -> None:
        self.hs.add(key)    

    def remove(self, key: int) -> None:
        if key in self.hs: self.hs.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.hs



tests = [
    [["MyHashSet","add","remove","add","remove","remove","add","add","add","add","remove"],
     [[],[9],[19],[14],[19],[9],[0],[3],[4],[0],[9]]],
    [["MyHashSet","add","add","contains","contains","add","contains","remove","contains"],
     [[],[1],[2],[1],[3],[2],[2],[2],[2]]
]
]
for t in tests:
    print(t[0])
    print(*t[1])
    for i in range(len(t[0])):
        if t[0][i] == "MyHashSet":
            mhs = MyHashSet()
        elif t[0][i] == "add":
            mhs.add(t[1][i])
        elif t[0][i] == "remove":
            mhs.remove(t[1][i])
        elif t[0][i] == "contains":
            print(mhs.contains(t[1][i]))
    print()