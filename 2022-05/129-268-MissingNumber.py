"""
Leetcode
268. Missing Number (easy)
2022-05-28

Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Example 1:
Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

Example 2:
Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
"""

from typing import List



# try 1
# Runtime: 281 ms, faster than 19.80% of Python3 online submissions for Missing Number.
# Memory Usage: 15.3 MB, less than 34.52% of Python3 online submissions for Missing Number.
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return sum([x for x in range(len(nums) + 1)]) - sum(nums)



# https://leetcode.com/problems/missing-number/discuss/69791/4-Line-Simple-Java-Bit-Manipulate-Solution-with-Explaination
# Runtime: 189 ms, faster than 50.20% of Python3 online submissions for Missing Number.
# Memory Usage: 15.1 MB, less than 98.72% of Python3 online submissions for Missing Number.
class Solution1:
    def missingNumber(self, nums: List[int]) -> int:
        l = len(nums)
        n = l
        i = 0
        while i < l:
            n = n ^ i ^ nums[i]
            i += 1
        return n



s = Solution()
tests = [
    [3,0,1],
    [0,1],
    [9,6,4,2,3,5,7,0,1],
    [0],
]
for t in tests:
    print(t)
    print(s.missingNumber(t))
    print()
