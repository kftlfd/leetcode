"""
Leetcode
31. Next Permutation (medium)
2022-04-03

A permutation of an array of integers is an arrangement of its 
members into a sequence or linear order.

 - For example, for arr = [1,2,3], the following are considered 
 permutations of arr: [1,2,3], [1,3,2], [3,1,2], [2,3,1].

The next permutation of an array of integers is the next 
lexicographically greater permutation of its integer. More formally, 
if all the permutations of the array are sorted in one container 
according to their lexicographical order, then the next permutation 
of that array is the permutation that follows it in the sorted container. 
If such arrangement is not possible, the array must be rearranged as the 
lowest possible order (i.e., sorted in ascending order).

 - For example, the next permutation of arr = [1,2,3] is [1,3,2].
 - Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
 - While the next permutation of arr = [3,2,1] is [1,2,3] because 
   [3,2,1] does not have a lexicographical larger rearrangement.

Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.
"""

"""
Do not return anything, modify nums in-place instead.
"""

from typing import List



# leetcode solution
# Runtime: 67 ms, faster than 35.72% of Python3 online submissions for Next Permutation.
# Memory Usage: 13.9 MB, less than 79.00% of Python3 online submissions for Next Permutation.
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        
        # find where numbers stop increasing (going from right) - nums[i]
        i = len(nums) - 2
        while (i >= 0) and (nums[i+1] <= nums[i]): i -= 1
            
        # if found, i.e. array is not in descending order (and next permutation is possible)
        if i >= 0:
            
            # find next num bigger than nums[i]
            j = len(nums) - 1
            while nums[j] <= nums[i]: j -= 1
                
            # swap
            nums[i], nums[j] = nums[j], nums[i]
        
        #reverse array after nums[i]
        nums[i+1:] = nums[i+1:][::-1]



s = Solution()
tests = [
    [1,2,3],
    [3,2,1],
    [1,1,5],
    [1],
    [4,6,3,1,8,15,14,13,12,2]
]
for t in tests:
    print(t)
    s.nextPermutation(t)
    print(t)
    print()
