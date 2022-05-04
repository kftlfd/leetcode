"""
Leetcode
1679. Max Number of K-Sum Pairs (easy)
2022-05-04

You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.
"""

from typing import List
from collections import Counter


# try 1
# Runtime: 988 ms, faster than 28.13% of Python3 online submissions for Max Number of K-Sum Pairs.
# Memory Usage: 28.3 MB, less than 5.13% of Python3 online submissions for Max Number of K-Sum Pairs.
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        pairs = 0
        count = Counter(nums)
        checked = set()
        
        for num in nums:
            if num in checked: continue

            if num == k / 2:
                pairs += count[num] // 2
                checked.add(num)
            else:
                pairs += min(count[num], count[k - num])
                checked.add(num)
                checked.add(k - num)
        
        return pairs



# https://leetcode.com/problems/max-number-of-k-sum-pairs/discuss/1022699/Python-Short-Counter-solution-+-Oneliner-explained
# Runtime: 1443 ms, faster than 5.14% of Python3 online submissions for Max Number of K-Sum Pairs.
# Memory Usage: 27.2 MB, less than 33.48% of Python3 online submissions for Max Number of K-Sum Pairs.
class Solution1:
    def maxOperations(self, nums: List[int], k: int) -> int:
        pairs = 0
        count = Counter(nums)
        
        for num in count:
            pairs += min(count[num], count[k-num])
        
        return pairs // 2



# https://leetcode.com/problems/max-number-of-k-sum-pairs/discuss/1023159/C++Python-HashMap-one-pass-Clean-and-Concise-O(N)
# Runtime: 1495 ms, faster than 5.14% of Python3 online submissions for Max Number of K-Sum Pairs.
# Memory Usage: 27 MB, less than 54.91% of Python3 online submissions for Max Number of K-Sum Pairs.
class Solution2:
    def maxOperations(self, nums: List[int], k: int) -> int:
        pairs = 0
        seen = {}
        
        for num in nums:
            if seen.get(k - num, 0) > 0:
                pairs += 1
                seen[k - num] -= 1
            else:
                seen[num] = seen.get(num, 0) + 1
        
        return pairs



s = Solution2()
tests = [
    [[1,2,3,4], 5],
    [[3,1,3,4,3], 6]
]
for t in tests:
    print(t)
    print(s.maxOperations(t[0], t[1]))
    print()
