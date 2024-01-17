"""
Leetcode
1207. Unique Number of Occurrences
Easy
2024-01-17

Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

 

Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

Example 2:

Input: arr = [1,2]
Output: false

Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true

 

Constraints:

    1 <= arr.length <= 1000
    -1000 <= arr[i] <= 1000
"""

from collections import Counter
from typing import List


class Solution:
    """
    Runtime: 43 ms, faster than 62.10% of Python3 online submissions for Unique Number of Occurrences.
    Memory Usage: 17.6 MB, less than 9.52% of Python3 online submissions for Unique Number of Occurrences.
    """

    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = Counter(arr).values()
        return len(counts) == len(set(counts))
