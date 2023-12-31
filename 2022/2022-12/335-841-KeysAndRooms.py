"""
Leetcode
841. Keys and Rooms (medium)
2022-12-20

There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.

When you visit a room, you may find a set of distinct keys in it. Each key has a number on it, denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.

Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, return true if you can visit all the rooms, or false otherwise.

Example 1:
Input: rooms = [[1],[2],[3],[]]
Output: true
Explanation: 
We visit room 0 and pick up key 1.
We then visit room 1 and pick up key 2.
We then visit room 2 and pick up key 3.
We then visit room 3.
Since we were able to visit every room, we return true.

Example 2:
Input: rooms = [[1,3],[3,0,1],[2],[0]]
Output: false
Explanation: We can not enter room number 2 since the only key that unlocks it is in that room.
"""

from typing import List, Optional


# Runtime: 74 ms, faster than 82.13% of Python3 online submissions for Keys and Rooms.
# Memory Usage: 14.4 MB, less than 87.57% of Python3 online submissions for Keys and Rooms.
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited_rooms = set([0])
        keys = rooms[0][:]
        while keys:
            key = keys.pop()
            if key in visited_rooms:
                continue
            visited_rooms.add(key)
            keys += rooms[key][:]
        return len(visited_rooms) == len(rooms)


s = Solution()
tests = [
    ([[1], [2], [3], []],
     True),

    ([[1, 3], [3, 0, 1], [2], [0]],
     False)
]
for inp, exp in tests:
    res = s.canVisitAllRooms(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
