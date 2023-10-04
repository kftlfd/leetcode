"""
Leetcode
706. Design HashMap (easy)
2023-10-04

Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:

    MyHashMap() initializes the object with an empty map.
    void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
    int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
    void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.

 

Example 1:

Input
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
Output
[null, null, null, 1, -1, null, 1, null, -1]

Explanation
MyHashMap myHashMap = new MyHashMap();
myHashMap.put(1, 1); // The map is now [[1,1]]
myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]

 

Constraints:

    0 <= key, value <= 10^6
    At most 10^4 calls will be made to put, get, and remove.
"""

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)


class MyHashMap:
    """
    Runtime: 209 ms, faster than 66.97% of Python3 online submissions for Design HashMap.
    Memory Usage: 20.1 MB, less than 58.72% of Python3 online submissions for Design HashMap.
    """

    class ListNode:
        def __init__(self, key, val, nxt=None):
            self.key = key
            self.val = val
            self.nxt = nxt

    def __init__(self):
        self.hash_key = 10**4
        self.arr = [None] * 10**4

    def get_index(self, key) -> int:
        return key % self.hash_key

    def put(self, key: int, value: int) -> None:
        i = self.get_index(key)
        cur = self.arr[i]

        if cur is None:
            self.arr[i] = self.ListNode(key, value)
            return

        while cur:
            if cur.key == key:
                cur.val = value
                break
            if cur.nxt:
                cur = cur.nxt
            else:
                cur.nxt = self.ListNode(key, value)

    def get(self, key: int) -> int:
        i = self.get_index(key)
        cur = self.arr[i]

        while cur:
            if cur.key == key:
                return cur.val
            cur = cur.nxt

        return -1

    def remove(self, key: int) -> None:
        i = self.get_index(key)
        cur = self.arr[i]
        if cur is None:
            return

        if cur.key == key:
            self.arr[i] = cur.nxt

        prev = cur
        cur = cur.nxt
        while cur:
            if cur.key == key:
                prev.nxt = cur.nxt
                return
            prev = cur
            cur = cur.nxt
