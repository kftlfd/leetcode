"""
Leetcode
881. Boats to Save People (medium)
2023-04-03

You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.

Example 1:
Input: people = [1,2], limit = 3
Output: 1
Explanation: 1 boat (1, 2)

Example 2:
Input: people = [3,2,2,1], limit = 3
Output: 3
Explanation: 3 boats (1, 2), (2) and (3)

Example 3:
Input: people = [3,5,3,4], limit = 5
Output: 4
Explanation: 4 boats (3), (3), (4), (5)
"""

from typing import List


class Solution:
    """
    Runtime: 459 ms, faster than 71.16% of Python3 online submissions for Boats to Save People.
    Memory Usage: 21 MB, less than 18.19% of Python3 online submissions for Boats to Save People.
    """

    def numRescueBoats(self, people: List[int], limit: int) -> int:

        boats = 0

        people = sorted(people)

        l = 0

        r = len(people) - 1

        while l < r:
            if people[l] + people[r] <= limit:
                l += 1
            r -= 1
            boats += 1

        if l == r:
            boats += 1

        return boats


s = Solution()
tests = [
    (([1, 2], 3),
     1),

    (([3, 2, 2, 1], 3),
     3),

    (([3, 5, 3, 4], 5),
     4),
]
for inp, exp in tests:
    res = s.numRescueBoats(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
