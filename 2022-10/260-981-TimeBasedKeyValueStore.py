"""
Leetcode
981. Time Based Key-Value Store (medium)
2022-10-06

Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:

 - TimeMap() Initializes the object of the data structure.
 - void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
 - String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".

Example 1:
Input
["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
Output
[null, null, "bar", "bar", null, "bar2", "bar2"]
Explanation
TimeMap timeMap = new TimeMap();
timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
timeMap.get("foo", 1);         // return "bar"
timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
timeMap.get("foo", 4);         // return "bar2"
timeMap.get("foo", 5);         // return "bar2"
"""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

# from sortedcontainers import SortedDict
from typing import List, Optional
import heapq


# Wrong Answer
class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = {"timestamps": []}

        # keep priority qeue of timestamps
        heapq.heappush(self.map[key]["timestamps"], timestamp)
        self.map[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""

        # binary search for closest timestamp
        l = 0
        r = len(self.map[key]["timestamps"])
        while l < r:
            m = (l + r) // 2
            t = self.map[key]["timestamps"][m]
            v = self.map[key][t]
            if t == timestamp:
                return v
            elif t > timestamp:
                r = m - 1
            else:
                l = m + 1

        return v


# leetcode solution - Approach 2: Sorted Map + Binary Search
# Runtime: 1954 ms, faster than 18.23% of Python3 online submissions for Time Based Key-Value Store.
# Memory Usage: 70.1 MB, less than 90.23% of Python3 online submissions for Time Based Key-Value Store.
class TimeMap2:

    def __init__(self):
        self.key_time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # If the 'key' does not exist in dictionary.
        if not key in self.key_time_map:
            self.key_time_map[key] = SortedDict()

        # Store '(timestamp, value)' pair in 'key' bucket.
        self.key_time_map[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        # If the 'key' does not exist in dictionary we will return empty string.
        if not key in self.key_time_map:
            return ""

        it = self.key_time_map[key].bisect_right(timestamp)
        # If iterator points to first element it means, no time <= timestamp exists.
        if it == 0:
            return ""

        # Return value stored at previous position of current iterator.
        return self.key_time_map[key].peekitem(it - 1)[1]


tests = [
    (
        (
            ["TimeMap", "set", "get", "get", "set", "get", "get"],
            [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3],
                ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
        ),
        (
            '[null, null, "bar", "bar", null, "bar2", "bar2"]'
        )
    ),

    (
        (
            ["TimeMap", "set", "set", "get", "get", "get", "get", "get"],
            [[], ["love", "high", 10], ["love", "low", 20], ["love", 5],
                ["love", 10], ["love", 15], ["love", 20], ["love", 25]]
        ),
        (
            '[null, null, null, "", "high", "high", "low", "low"]'
        )
    )
]
for t in tests:
    print("input: ", t[0])
    print("expect: ", t[1])
    s = None
    out = []
    instructions, inputs = t[0]
    for instr, inp in zip(instructions, inputs):
        if instr == "TimeMap":
            s = TimeMap()
        elif instr == "set":
            out.append(s.set(*inp))
        elif instr == "get":
            out.append(s.get(*inp))
    print("output: ", out)
    print()
