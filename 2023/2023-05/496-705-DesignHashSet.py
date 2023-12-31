"""
Leetcode
705. Design HashSet (easy)
2023-05-30

Design a HashSet without using any built-in hash table libraries.

Implement MyHashSet class:

    void add(key) Inserts the value key into the HashSet.
    bool contains(key) Returns whether the value key exists in the HashSet or not.
    void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.

Example 1:

Input
["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
[[], [1], [2], [1], [3], [2], [2], [2], [2]]
Output
[null, null, null, true, false, null, true, null, false]

Explanation
MyHashSet myHashSet = new MyHashSet();
myHashSet.add(1);      // set = [1]
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(1); // return True
myHashSet.contains(3); // return False, (not found)
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(2); // return True
myHashSet.remove(2);   // set = [1]
myHashSet.contains(2); // return False, (already removed)

Constraints:
    0 <= key <= 106
    At most 104 calls will be made to add, remove, and contains.
"""

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)


class MyHashSet:
    """
    https://leetcode.com/problems/design-hashset/discuss/768659/Python-Easy-Multiplicative-Hash-explained
    https://en.wikipedia.org/wiki/Hash_function#Multiplicative_hashing
    Runtime: 290 ms, faster than 35.85% of Python3 online submissions for Design HashSet.
Memory Usage: 24.9 MB, less than 17.03% of Python3 online submissions for Design HashSet.    
    """

    def __init__(self):
        self.arr = [[] for _ in range(1<<15)]
        
    
    def hash(self, key: int) -> int:
        """
        h(K) = (a * K % 2^w) / (2^(w-m))
        
        1. a -- is some big odd number (maybe prime)
        2. m -- is length in bits of output we want to have
        3. w -- is size of machine word (doesn't matter here, choose any w > m)
        
        trick for fast bit operation modulo 2^t: for any s: s % (2^t) = s & (1<<t) - 1
        """
        return ((key*1031237) & (1<<20) - 1)>>5
        

    def add(self, key: int) -> None:
        h = self.hash(key)
        if key not in self.arr[h]:
            self.arr[h].append(key)
        

    def remove(self, key: int) -> None:
        h = self.hash(key)
        if key in self.arr[h]:
            self.arr[h].remove(key)
        

    def contains(self, key: int) -> bool:
        h = self.hash(key)
        return key in self.arr[h]
        