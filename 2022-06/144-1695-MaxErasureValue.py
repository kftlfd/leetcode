"""
Leetcode
1695. Maximum Erasure Value (easy)
2022-06-12

You are given an array of positive integers nums and want to erase a subarray containing unique elements. The score you get by erasing the subarray is equal to the sum of its elements.

Return the maximum score you can get by erasing exactly one subarray.

An array b is called to be a subarray of a if it forms a contiguous subsequence of a, that is, if it is equal to a[l],a[l+1],...,a[r] for some (l,r).
"""

from typing import List



# Runtime: 2250 ms, faster than 24.73% of Python3 online submissions for Maximum Erasure Value.
# Memory Usage: 27.1 MB, less than 97.81% of Python3 online submissions for Maximum Erasure Value.
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:

        ht = {}
        l = 0
        r = 0
        maxsum = 0
        csum = 0

        while r < len(nums):

            while ht.get(nums[r], 0) == 1:
                csum -= nums[l]
                ht[nums[l]] -= 1
                l += 1
            
            csum += nums[r]
            ht[nums[r]] = 1
            maxsum = max(maxsum, csum)
            r += 1

        return maxsum



s = Solution()
tests = [
    [4,2,4,5,6],
    [5,2,1,2,5,2,1,2,5],
]
for t in tests:
    print(t)
    print(s.maximumUniqueSubarray(t))
    print()
