"""
Leetcode
1732. Find the Highest Altitude (easy)
2023-06-19

There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. The biker starts his trip on point 0 with altitude equal 0.

You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i and i + 1 for all (0 <= i < n). Return the highest altitude of a point.

Example 1:

Input: gain = [-5,1,5,0,-7]
Output: 1
Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.

Example 2:

Input: gain = [-4,-3,-2,-1,4,3,2]
Output: 0
Explanation: The altitudes are [0,-4,-7,-9,-10,-6,-3,-1]. The highest is 0.

Constraints:

    n == gain.length
    1 <= n <= 100
    -100 <= gain[i] <= 100
"""

from typing import List
from itertools import accumulate


class Solution:
    """
    Runtime: 56 ms, faster than 23.11% of Python3 online submissions for Find the Highest Altitude.
    Memory Usage: 16.3 MB, less than 66.27% of Python3 online submissions for Find the Highest Altitude.
    """

    def largestAltitude(self, gain: List[int]) -> int:
        cur_height = 0
        highest = cur_height

        for n in gain:
            cur_height += n
            if cur_height > highest:
                highest = cur_height

        return highest


class Solution1:
    """
    https://leetcode.com/problems/find-the-highest-altitude/solution/1935311
    Runtime: 55 ms, faster than 29.15% of Python3 online submissions for Find the Highest Altitude.
    Memory Usage: 16.3 MB, less than 26.06% of Python3 online submissions for Find the Highest Altitude.
    """

    def largestAltitude(self, gain: List[int]) -> int:
        return max(accumulate(gain, initial=0))


s = Solution1()
tests = [
    ([-5, 1, 5, 0, -7],
     1),

    ([-4, -3, -2, -1, 4, 3, 2],
     0),
]
for inp, exp in tests:
    res = s.largestAltitude(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
