"""
Leetcode
167. Two Sum II - Input Array Is Sorted (medium)
2022-06-09

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.
"""

from typing import List



# Runtime: 238 ms, faster than 19.33% of Python3 online submissions for Two Sum II - Input Array Is Sorted.
# Memory Usage: 15 MB, less than 41.52% of Python3 online submissions for Two Sum II - Input Array Is Sorted.
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        lennums = len(numbers)
        
        for first in range(lennums):
            
            # set the first number
            n1 = numbers[first]
            if first > 0 and n1 == numbers[first - 1]:
                continue
                
            # define the number to search for
            n2 = target - n1
            
            # binary search
            l = first + 1
            r = len(numbers) - 1
            while l <= r:
                m = (l + r) // 2
                midnum = numbers[m]
                if midnum == n2:
                    return [first + 1, m + 1]
                elif midnum > n2:
                    r = m - 1
                else:
                    l = m + 1
        
        return [None, None]



# Runtime: 179 ms, faster than 48.98% of Python3 online submissions for Two Sum II - Input Array Is Sorted.
# Memory Usage: 15 MB, less than 11.40% of Python3 online submissions for Two Sum II - Input Array Is Sorted.
class Solution1:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # two pointers
        l = 0
        r = len(numbers) - 1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l + 1, r + 1]
            elif s > target:
                r -= 1
            else:
                l += 1
        return [None, None]



s = Solution()
tests = [
    [[2,7,11,15], 9],
    [[2,3,4], 6],
    [[-1,0], -1],
    [[3,4,4,6,7], 8]
]
for t in tests:
    print(t)
    print(s.twoSum(t[0], t[1]))
    print()
