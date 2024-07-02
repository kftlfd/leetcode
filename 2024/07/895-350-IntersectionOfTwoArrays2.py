"""
Leetcode
350. Intersection of Two Arrays II
Easy
2024-07-02

Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.

 

Constraints:

    1 <= nums1.length, nums2.length <= 1000
    0 <= nums1[i], nums2[i] <= 1000

 

Follow up:

    What if the given array is already sorted? How would you optimize your algorithm?
    What if nums1's size is small compared to nums2's size? Which algorithm is better?
    What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
"""

from typing import List


class Solution:
    """
    Runtime: 50 ms, faster than 48.69% of Python3 online submissions for Intersection of Two Arrays II.
    Memory Usage: 16.7 MB, less than 71.02% of Python3 online submissions for Intersection of Two Arrays II.
    """

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)

        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1

        ans = []
        i1 = 0
        i2 = 0

        while i1 < len(nums1) and i2 < len(nums2):
            if nums1[i1] > nums2[i2]:
                i2 += 1
            elif nums1[i1] != nums2[i2]:
                i1 += 1
            else:
                ans.append(nums1[i1])
                i1 += 1
                i2 += 1

        return ans


s = Solution()
tests = [
    (([4, 9, 5], [9, 4, 9, 8, 4]),
     [4, 9]),
]
for inp, exp in tests:
    res = s.intersect(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
