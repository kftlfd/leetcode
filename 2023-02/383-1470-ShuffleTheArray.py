"""
Leetcode
1470. Shuffle the Array (easy)
2023-02-06

Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].

Example 1:
Input: nums = [2,5,1,3,4,7], n = 3
Output: [2,3,5,4,1,7] 
Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].

Example 2:
Input: nums = [1,2,3,4,4,3,2,1], n = 4
Output: [1,4,2,3,3,2,4,1]

Example 3:
Input: nums = [1,1,2,2], n = 2
Output: [1,2,1,2]
"""

from typing import List, Optional


class Solution:
    """
    Runtime: 58 ms, faster than 88.71% of Python3 online submissions for Shuffle the Array.
    Memory Usage: 14.2 MB, less than 33.52% of Python3 online submissions for Shuffle the Array.
    """

    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return [num for pair in zip(nums[:n], nums[n:]) for num in pair]


class Solution1:
    """
    https://leetcode.com/problems/shuffle-the-array/solution/1789825
    Runtime: 69 ms, faster than 42.92% of Python3 online submissions for Shuffle the Array.
    Memory Usage: 14.1 MB, less than 33.52% of Python3 online submissions for Shuffle the Array.
    """

    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return [nums[j] for i in range(n) for j in range(i, i+n+1, n)]


s = Solution()
tests = [
    (([2, 5, 1, 3, 4, 7], 3),
     [2, 3, 5, 4, 1, 7]),

    (([1, 2, 3, 4, 4, 3, 2, 1], 4),
     [1, 4, 2, 3, 3, 2, 4, 1]),

    (([1, 1, 2, 2], 2),
     [1, 2, 1, 2])
]
for inp, exp in tests:
    res = s.shuffle(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
