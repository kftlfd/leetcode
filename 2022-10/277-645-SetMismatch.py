"""
Leetcode
645. Set Mismatch (easy)
2022-10-23

You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.

Example 1:
Input: nums = [1,2,2,4]
Output: [2,3]
Example 2:
Input: nums = [1,1]
Output: [1,2]
"""

from typing import List, Optional


# wrong
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        for i, n in enumerate(sorted(nums)):
            if n != i + 1:
                return [n, i + 1]


# wrong
class Solution1:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        arr = sorted(nums)
        duplicate = None
        missing = None

        for i, n in enumerate(arr):
            if not missing and n != i + 1:
                missing = i + 1
            if i > 0 and n == arr[i-1]:
                duplicate = n

            if duplicate and missing:
                break

        return [duplicate, missing]


# https://leetcode.com/problems/set-mismatch/discuss/2733774/Python-3-oror-3-lines-sets-oror-TM%3A-9744
# Runtime: 279 ms, faster than 76.95% of Python3 online submissions for Set Mismatch.
# Memory Usage: 15.9 MB, less than 41.20% of Python3 online submissions for Set Mismatch.
class Solution2:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        n = len(nums)
        a = sum(nums)
        b = sum(set(nums))

        s = n * (n + 1) // 2

        return [a-b, s-b]


s = Solution2()
tests = [
    ([3, 2, 3, 4, 6, 5],
     [3, 1]),

    ([3, 2, 2],
     [2, 1]),

    ([1, 2, 2, 4],
     [2, 3]),

    ([1, 1],
     [1, 2])
]
for inp, exp in tests:
    res = s.findErrorNums(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
