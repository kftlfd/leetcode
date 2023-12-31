"""
Leetcode
1338. Reduce Array Size to The Half (medium)
2022-08-18

You are given an integer array arr. You can choose a set of integers and remove all the occurrences of these integers in the array.

Return the minimum size of the set so that at least half of the integers of the array are removed.

Example 1:
Input: arr = [3,3,3,3,5,5,5,2,2,7]
Output: 2
Explanation: Choosing {3,7} will make the new array [5,5,5,2,2] which has size 5 (i.e equal to half of the size of the old array).
Possible sets of size 2 are {3,5},{3,2},{5,2}.
Choosing set {2,7} is not possible as it will make the new array [3,3,3,3,5,5,5] which has a size greater than half of the size of the old array.

Example 2:
Input: arr = [7,7,7,7,7,7]
Output: 1
Explanation: The only possible set you can choose is {7}. This will make the new array empty.
"""

from typing import List
from heapq import heappush, heappop


# Runtime: 648 ms, faster than 89.33% of Python3 online submissions for Reduce Array Size to The Half.
# Memory Usage: 31.9 MB, less than 81.83% of Python3 online submissions for Reduce Array Size to The Half.
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        ht = {}
        for n in arr:
            ht[n] = ht.get(n, 0) + 1

        q = []
        for freq in ht.values():
            heappush(q, -freq)

        ans = 0
        s = 0
        l = len(arr) // 2
        while s < l:
            s += -heappop(q)
            ans += 1

        return ans


s = Solution()
tests = [
    [3, 3, 3, 3, 5, 5, 5, 2, 2, 7],
    [7, 7, 7, 7, 7, 7],
]
for t in tests:
    print(t)
    print(s.minSetSize(t))
    print()
