"""
Leetcode
146. LRU Cache (medium)
2023-07-18

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

    LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
    int get(int key) Return the value of the key if the key exists, otherwise return -1.
    void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4

Constraints:

    1 <= capacity <= 3000
    0 <= key <= 10^4
    0 <= value <= 10^5
    At most 2 * 105 calls will be made to get and put.
"""

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


class LRUCache:
    """
    Runtime: 4563 ms, faster than 5.00% of Python3 online submissions for LRU Cache.
    Memory Usage: 78.7 MB, less than 14.03% of Python3 online submissions for LRU Cache.
    """

    def __init__(self, capacity: int):
        self.ht = {}
        self.capacity = capacity
        self.time = 0

    def get(self, key: int) -> int:
        if key not in self.ht:
            return -1

        self.ht[key][1] = self.time
        self.time += 1
        return self.ht[key][0]

    def put(self, key: int, value: int) -> None:
        if key in self.ht or len(self.ht) < self.capacity:
            self.ht[key] = [value, self.time]
        else:
            least_used_k = None
            least_used_t = float('inf')
            for k, v in self.ht.items():
                if v[1] < least_used_t:
                    least_used_t = v[1]
                    least_used_k = k
            del self.ht[least_used_k]
            self.ht[key] = [value, self.time]

        self.time += 1


class LRUCache1:
    """
    ordered dict
    https://leetcode.com/problems/lru-cache/discuss/45952/Python-concise-solution-with-comments-(Using-OrderedDict)./804819
    Runtime: 722 ms, faster than 83.45% of Python3 online submissions for LRU Cache.
    Memory Usage: 76.9 MB, less than 97.62% of Python3 online submissions for LRU Cache.
    """

    def __init__(self, capacity: int):
        self.d = {}
        self.size = capacity

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1

        self.d[key] = self.d.pop(key)
        return self.d[key]

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.d.pop(key)

        self.d[key] = value

        if len(self.d) > self.size:
            self.d.pop(next(iter(self.d)))


class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache2:
    """
    hash table + doubly linked list
    https://leetcode.com/problems/lru-cache/discuss/352295/Python3-doubly-linked-list-and-dictionary
    Runtime: 783 ms, faster than 76.50% of Python3 online submissions for LRU Cache.
    Memory Usage: 78.4 MB, less than 59.29% of Python3 online submissions for LRU Cache.
    """

    def __init__(self, capacity: int):
        self.dic = dict()  # key to node
        self.capacity = capacity
        self.head = ListNode(0, 0)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.dic:
            node = self.dic[key]
            self.removeFromList(node)
            self.insertIntoHead(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dic:             # similar to get()
            node = self.dic[key]
            self.removeFromList(node)
            self.insertIntoHead(node)
            node.value = value         # replace the value len(dic)
        else:
            if len(self.dic) >= self.capacity:
                self.removeFromTail()
            node = ListNode(key, value)
            self.dic[key] = node
            self.insertIntoHead(node)

    def removeFromList(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insertIntoHead(self, node):
        headNext = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = headNext
        headNext.prev = node

    def removeFromTail(self):
        if len(self.dic) == 0:
            return
        tail_node = self.tail.prev
        del self.dic[tail_node.key]
        self.removeFromList(tail_node)


tests = [
    ((
        ["LRUCache", "put", "put", "get", "put",
            "get", "put", "get", "get", "get"],
        [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    ),
        [None, None, None, 1, None, -1, None, -1, 3, 4]),
]
for inp, exp in tests:
    s = None
    res = []
    for command, arg in zip(*inp):
        if command == 'LRUCache':
            s = LRUCache(*arg)
            res.append(None)
        elif command == 'get':
            res.append(s.get(*arg))
        elif command == 'put':
            res.append(s.put(*arg))

    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
