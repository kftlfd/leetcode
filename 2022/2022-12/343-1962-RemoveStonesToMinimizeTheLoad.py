"""
Leetcode
1962. Remove Stones to Minimize the Total (medium)
2022-12-28

You are given a 0-indexed integer array piles, where piles[i] represents the number of stones in the ith pile, and an integer k. You should apply the following operation exactly k times:

    Choose any piles[i] and remove floor(piles[i] / 2) stones from it.

Notice that you can apply the operation on the same pile more than once.

Return the minimum possible total number of stones remaining after applying the k operations.

floor(x) is the greatest integer that is smaller than or equal to x (i.e., rounds x down).
 
Example 1:
Input: piles = [5,4,9], k = 2
Output: 12
Explanation: Steps of a possible scenario are:
- Apply the operation on pile 2. The resulting piles are [5,4,5].
- Apply the operation on pile 0. The resulting piles are [3,4,5].
The total number of stones in [3,4,5] is 12.

Example 2:
Input: piles = [4,3,6,7], k = 3
Output: 12
Explanation: Steps of a possible scenario are:
- Apply the operation on pile 2. The resulting piles are [4,3,3,7].
- Apply the operation on pile 3. The resulting piles are [4,3,3,4].
- Apply the operation on pile 0. The resulting piles are [2,3,3,4].
The total number of stones in [2,3,3,4] is 12.
"""

from typing import List, Optional
import heapq


# Runtime: 1911 ms, faster than 83.71% of Python3 online submissions for Remove Stones to Minimize the Total.
# Memory Usage: 28.5 MB, less than 83.19% of Python3 online submissions for Remove Stones to Minimize the Total.
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        q = [-n for n in piles]
        heapq.heapify(q)
        for _ in range(k):
            pile = -heapq.heappop(q)
            pile -= pile // 2
            heapq.heappush(q, -pile)
        return -sum(q)


s = Solution()
tests = [
    (([5, 4, 9], 2),
     12),

    (([4, 3, 6, 7], 3),
     12)
]
for inp, exp in tests:
    piles, k = inp
    res = s.minStoneSum(piles, k)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
