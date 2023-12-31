"""
Leetcode
88. Merge Sorted Array (easy)
2022-06-07

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
"""

from typing import List

"""
Do not return anything, modify nums1 in-place instead.
"""



# Runtime: 57 ms, faster than 37.87% of Python3 online submissions for Merge Sorted Array.
# Memory Usage: 13.9 MB, less than 85.45% of Python3 online submissions for Merge Sorted Array.
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[m:] = nums2
        nums1.sort()
        return nums1



# Runtime: 59 ms, faster than 33.94% of Python3 online submissions for Merge Sorted Array.
# Memory Usage: 13.9 MB, less than 85.45% of Python3 online submissions for Merge Sorted Array.
class Solution1:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[:] = sorted(nums1[:m] + nums2)
        return nums1



# Runtime: 55 ms, faster than 41.99% of Python3 online submissions for Merge Sorted Array.
# Memory Usage: 13.9 MB, less than 37.34% of Python3 online submissions for Merge Sorted Array.
class Solution2:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        a = m - 1
        b = n - 1
        
        for i in range(len(nums1))[::-1]:

            if a < 0:
                nums1[:i+1] = nums2[:b+1]
                break

            if b < 0:
                break
            
            if nums1[a] > nums2[b]:
                nums1[i] = nums1[a]
                a -= 1
            
            else:
                nums1[i] = nums2[b]
                b -= 1
            
            i -= 1
    
        return nums1



s = Solution2()
tests = [
    [[1,2,3,0,0,0], 3, [2,5,6], 3],
    [[1], 1, [], 0],
    [[0], 0, [1], 1]
]
for t in tests:
    print(t)
    print(s.merge(t[0], t[1], t[2], t[3]))
    print()
