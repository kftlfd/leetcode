"""
Leetcode
905. Sort Array By Parity (easy)
2022-05-02

Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.
"""

from typing import List



# try 1
# Runtime: 152 ms, faster than 12.80% of Python3 online submissions for Sort Array By Parity.
# Memory Usage: 14.6 MB, less than 63.70% of Python3 online submissions for Sort Array By Parity.
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
        even = []
        odd = []
        
        for n in nums:
            if n % 2:
                odd.append(n)
            else:
                even.append(n)
        
        return even + odd



# Runtime: 108 ms, faster than 46.92% of Python3 online submissions for Sort Array By Parity.
# Memory Usage: 14.6 MB, less than 96.65% of Python3 online submissions for Sort Array By Parity.
class Solution1:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:        
        return sorted(nums, key=lambda x: x % 2)



# Runtime: 85 ms, faster than 76.67% of Python3 online submissions for Sort Array By Parity.
# Memory Usage: 14.6 MB, less than 63.70% of Python3 online submissions for Sort Array By Parity.
class Solution2:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i = 0
        j = len(nums) - 1
        
        while i < j:
            if nums[i] % 2 and not nums[j] % 2:
                nums[i], nums[j] = nums[j], nums[i]
            if not nums[i] % 2: i += 1
            if nums[j] % 2: j -= 1
        
        return nums



s = Solution2()
tests = [
    [3,1,2,4],
    [0]
]
for t in tests:
    print(t)
    print(s.sortArrayByParity(t))
    print()
