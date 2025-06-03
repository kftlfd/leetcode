"""
Leetcode
2025-06-03
1298. Maximum Candies You Can Get from Boxes
Hard

You have n boxes labeled from 0 to n - 1. You are given four arrays: status, candies, keys, and containedBoxes where:

    status[i] is 1 if the ith box is open and 0 if the ith box is closed,
    candies[i] is the number of candies in the ith box,
    keys[i] is a list of the labels of the boxes you can open after opening the ith box.
    containedBoxes[i] is a list of the boxes you found inside the ith box.

You are given an integer array initialBoxes that contains the labels of the boxes you initially have. You can take all the candies in any open box and you can use the keys in it to open new boxes and you also can use the boxes you find in it.

Return the maximum number of candies you can get following the rules above.

 

Example 1:

Input: status = [1,0,1,0], candies = [7,5,4,100], keys = [[],[],[1],[]], containedBoxes = [[1,2],[3],[],[]], initialBoxes = [0]
Output: 16
Explanation: You will be initially given box 0. You will find 7 candies in it and boxes 1 and 2.
Box 1 is closed and you do not have a key for it so you will open box 2. You will find 4 candies and a key to box 1 in box 2.
In box 1, you will find 5 candies and box 3 but you will not find a key to box 3 so box 3 will remain closed.
Total number of candies collected = 7 + 4 + 5 = 16 candy.

Example 2:

Input: status = [1,0,0,0,0,0], candies = [1,1,1,1,1,1], keys = [[1,2,3,4,5],[],[],[],[],[]], containedBoxes = [[1,2,3,4,5],[],[],[],[],[]], initialBoxes = [0]
Output: 6
Explanation: You have initially box 0. Opening it you can find boxes 1,2,3,4 and 5 and their keys.
The total number of candies will be 6.

 

Constraints:

    n == status.length == candies.length == keys.length == containedBoxes.length
    1 <= n <= 1000
    status[i] is either 0 or 1.
    1 <= candies[i] <= 1000
    0 <= keys[i].length <= n
    0 <= keys[i][j] < n
    All values of keys[i] are unique.
    0 <= containedBoxes[i].length <= n
    0 <= containedBoxes[i][j] < n
    All values of containedBoxes[i] are unique.
    Each box is contained in one box at most.
    0 <= initialBoxes.length <= n
    0 <= initialBoxes[i] < n


Hint 1
Use Breadth First Search (BFS) to traverse all possible boxes you can open. Only push to the queue the boxes the you have with their keys.
"""

from collections import deque
from typing import List


class Solution:
    """
    Runtime 11ms Beats 92.34%
    Memory 28.13MB Beats 65.13%
    """

    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        n = len(status)

        box_open = status[:]

        box_known = [0] * n
        for box in initialBoxes:
            box_known[box] = 1

        q = deque(initialBoxes)

        changes = True
        while changes:
            changes = False

            for _ in range(len(q)):
                cur_box = q.popleft()

                if not box_open[cur_box]:
                    q.append(cur_box)
                    continue

                for box in keys[cur_box]:
                    box_open[box] = 1
                    changes = True

                for box in containedBoxes[cur_box]:
                    box_known[box] = 1
                    q.append(box)
                    changes = True

        return sum(
            candy * is_known * is_open
            for candy, is_known, is_open in zip(candies, box_known, box_open)
        )


class Solution1:
    """
    leetcode solution: Breadth-First Search
    Runtime 16ms Beats 74.71%
    Memory 28.41MB Beats 6.51%
    """

    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        n = len(status)
        can_open = [status[i] == 1 for i in range(n)]
        has_box, used = [False] * n, [False] * n

        q = deque()
        ans = 0
        for box in initialBoxes:
            has_box[box] = True
            if can_open[box]:
                q.append(box)
                used[box] = True
                ans += candies[box]

        while len(q) > 0:
            big_box = q.popleft()
            for key in keys[big_box]:
                can_open[key] = True
                if not used[key] and has_box[key]:
                    q.append(key)
                    used[key] = True
                    ans += candies[key]
            for box in containedBoxes[big_box]:
                has_box[box] = True
                if not used[box] and can_open[box]:
                    q.append(box)
                    used[box] = True
                    ans += candies[box]

        return ans
