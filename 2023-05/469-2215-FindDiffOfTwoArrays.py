"""
Leetcode
2215. Find the Difference of Two Arrays (easy)
2023-05-03

Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

    answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
    answer[1] is a list of all distinct integers in nums2 which are not present in nums1.

Note that the integers in the lists may be returned in any order.

Example 1:
Input: nums1 = [1,2,3], nums2 = [2,4,6]
Output: [[1,3],[4,6]]
Explanation:
For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas nums1[0] = 1 and nums1[2] = 3 are not present in nums2. Therefore, answer[0] = [1,3].
For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas nums2[1] = 4 and nums2[2] = 6 are not present in nums2. Therefore, answer[1] = [4,6].

Example 2:
Input: nums1 = [1,2,3,3], nums2 = [1,1,2,2]
Output: [[3],[]]
Explanation:
For nums1, nums1[2] and nums1[3] are not present in nums2. Since nums1[2] == nums1[3], their value is only included once and answer[0] = [3].
Every integer in nums2 is present in nums1. Therefore, answer[1] = [].
"""

from typing import List


class Solution:
    """
    Runtime: 190 ms, faster than 40.97% of Python3 online submissions for Find the Difference of Two Arrays.
    Memory Usage: 16.7 MB, less than 9.53% of Python3 online submissions for Find the Difference of Two Arrays.
    """

    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        ht = {}

        for num in nums1:
            ht[num] = 1

        distinct2 = set()

        for num in nums2:
            if num in ht:
                ht[num] = 0
            else:
                distinct2.add(num)

        distinct1 = [n for n, v in ht.items() if v == 1]

        return [distinct1, list(distinct2)]


class Solution1:
    """
    Runtime: 192 ms, faster than 38.07% of Python3 online submissions for Find the Difference of Two Arrays.
    Memory Usage: 16.7 MB, less than 9.53% of Python3 online submissions for Find the Difference of Two Arrays.
    """

    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        s1 = set(nums1)
        s2 = set(nums2)

        return [s1 - s2, s2 - s1]


s = Solution()
tests = [
    (([-80, -15, -81, -28, -61, 63, 14, -45, -35, -10],
      [-1, -40, -44, 41, 10, -43, 69, 10, 2]),
     [[-81, -35, -10, -28, -61, -45, -15, 14, -80, 63],
      [-1, 2, 69, -40, 41, 10, -43, -44]]
     ),

    (([1, 2, 3], [2, 4, 6]),
     [[1, 3], [4, 6]]),

    (([1, 2, 3, 3], [1, 1, 2, 2]),
     [[3], []]),
]
for inp, exp in tests:
    exp1, exp2 = exp
    exp1.sort()
    exp2.sort()
    diff1, diff2 = s.findDifference(*inp)
    diff1.sort()
    diff2.sort()
    if diff1 != exp1 or diff2 != exp2:
        print('input:  ', inp)
        print('expect: ', [exp1, exp2])
        print('output: ', [diff1, diff2])
        print()
print('Completed testing')
