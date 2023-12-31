"""
Leetcode
1207. Unique Number of Occurrences (easy)
2022-11-30

Given an array of integers arr, return true if the number of occurrences of each value in the array is unique, or false otherwise.

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
"""

from typing import List, Optional
from collections import Counter


# Runtime: 44 ms, faster than 83.82% of Python3 online submissions for Unique Number of Occurrences.
# Memory Usage: 14 MB, less than 34.11% of Python3 online submissions for Unique Number of Occurrences.
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurences = Counter(arr)
        unique = Counter(occurences.values())
        return len(occurences) == len(unique)


# Runtime: 69 ms, faster than 52.28% of Python3 online submissions for Unique Number of Occurrences.
# Memory Usage: 13.9 MB, less than 72.74% of Python3 online submissions for Unique Number of Occurrences.
class Solution1:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        return len(set(arr)) == len(set(Counter(arr).values()))


s = Solution()
tests = [
    ([1, 2, 2, 1, 1, 3],
     True),

    ([1, 2],
     False),

    ([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0],
        True),
]
for inp, exp in tests:
    res = s.uniqueOccurrences(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
