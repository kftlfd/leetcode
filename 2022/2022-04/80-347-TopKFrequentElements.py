"""
Leetcode
347. Top K Frequent Elements (medium)
2022-04-09

Given an integer array nums and an integer k, return the k most frequent 
elements. You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

https://leetcode.com/problems/top-k-frequent-elements/solution/
"""

from typing import List



# try 1
# Runtime: 100 ms, faster than 96.24% of Python3 online submissions for Top K Frequent Elements.
# Memory Usage: 18.7 MB, less than 40.43% of Python3 online submissions for Top K Frequent Elements.
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        ht = {}
        for n in nums:
            ht[n] = ht.get(n, 0) + 1
        
        fs = []
        for key in ht:
            fs.append((ht[key],key))

        fs.sort(key=lambda x: x[0], reverse=True)

        out = []
        for i in range(k):
            out.append(fs[i][1])

        return out



s = Solution()
tests = [
    [[1,1,1,2,2,3], 2],
    [[1], 1]
]
for t in tests:
    print(t)
    print(s.topKFrequent(t[0], t[1]))
    print()
