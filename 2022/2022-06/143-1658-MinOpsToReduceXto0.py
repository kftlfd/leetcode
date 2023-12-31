"""
Leetcode
1658. Minimum Operations to Reduce X to Zero (medium)
2022-06-11

You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.

Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.
"""

from typing import List



# https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/discuss/1080880/Are-you-stuck-once-read-this-.-logic-explained-clearly-or-easy-to-understand
# Runtime: 1278 ms, faster than 81.37% of Python3 online submissions for Minimum Operations to Reduce X to Zero.
# Memory Usage: 28.1 MB, less than 50.24% of Python3 online submissions for Minimum Operations to Reduce X to Zero.
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        
        # find longest subarray which sum = sum(nums) - x
        fsum = sum(nums) - x # find-sum
        if fsum < 0: return -1
        if fsum == 0: return len(nums)
        if nums[0] > x and nums[-1] > x: return -1

        # sliding window
        maxlen = -1
        l = 0
        r = 0
        csum = 0 # current (window) sum
        while r < len(nums):
            csum += nums[r]
            while csum > fsum:
                csum -= nums[l]
                l += 1
            if csum == fsum:
                maxlen = max(maxlen, r - l + 1)
            r += 1
        
        if maxlen == -1:
            return -1
        else:
            return len(nums) - maxlen



s = Solution()
tests = [
    [[5,1,1,5], 4],
    [[1,1,4,2,3], 5], # 2
    [[5,6,7,8,9], 4], # -1
    [[3,2,20,1,1,3], 10] # 5
]
for t in tests:
    print(t)
    print(s.minOperations(t[0], t[1]))
    print()
