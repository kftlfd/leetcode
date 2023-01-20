"""
Leetcode
491. Non-decreasing Subsequences (medium)
2023-01-20

Given an integer array nums, return all the different possible non-decreasing subsequences of the given array with at least two elements. You may return the answer in any order.

Example 1:
Input: nums = [4,6,7,7]
Output: [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]

Example 2:
Input: nums = [4,4,3,2,1]
Output: [[4,4]]
"""

from typing import List, Optional


# leetcode solution - Backtracking
# Runtime: 239 ms, faster than 67.50% of Python3 online submissions for Non-decreasing Subsequences.
# Memory Usage: 22.7 MB, less than 22.66% of Python3 online submissions for Non-decreasing Subsequences.
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:

        ans = set()
        sequence = []

        def backtrack(index):
            # if we have checked all elements
            if index == len(nums):
                if len(sequence) >= 2:
                    ans.add(tuple(sequence))
                return
            # if the sequence remains increasing after appending nums[index]
            if not sequence or sequence[-1] <= nums[index]:
                # append nums[index] to the sequence
                sequence.append(nums[index])
                # call recursively
                backtrack(index + 1)
                # delete nums[index] from the end of the sequence
                sequence.pop()
            # call recursively not appending an element
            backtrack(index + 1)

        backtrack(0)
        return ans


s = Solution()
tests = [
    ([4, 6, 7, 7],
     [[4, 6], [4, 6, 7], [4, 6, 7, 7], [4, 7], [4, 7, 7], [6, 7], [6, 7, 7], [7, 7]]),

    ([4, 4, 3, 2, 1],
     [[4, 4]])
]
for inp, exp in tests:
    res = s.findSubsequences(inp)
    if set(tuple(x) for x in res) != set(tuple(x) for x in exp):
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
