"""
Leetcode
347. Top K Frequent Elements (medium)
2023-05-22

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]
"""

from typing import List
from collections import Counter


class Solution:
    """
    Runtime: 102 ms, faster than 85.96% of Python3 online submissions for Top K Frequent Elements.
    Memory Usage: 21.1 MB, less than 30.27% of Python3 online submissions for Top K Frequent Elements.
    """

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        priority = sorted(cnt.items(), key=lambda x: -x[1])
        return [x[0] for x in priority[:k]]


s = Solution()
tests = [
    (([1, 1, 1, 2, 2, 3], 2),
     [1, 2]),

    (([1], 1),
     [1]),
]
for inp, exp in tests:
    res = s.topKFrequent(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
