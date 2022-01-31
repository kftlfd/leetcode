'''
Leetcode
189. Rotate Array (medium)
2022-01-30
'''

# Given an array, rotate the array to the right by k steps, where k is non-negative.

# Example 1:
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

from typing import List



# Try 1
# ez
# Runtime: 1136 ms, faster than 18.91% 
# Memory Usage: 25.3 MB, less than 96.40%
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.reverse()  # first reverse
        for i in range(k):  # k rotations
            nums.append(nums.pop(0))  # take first element and make it last
        nums.reverse()  # second reverse
        


# Try 2
# create new array with rotated values
# Runtime: 220 ms, faster than 81.00% of Python3
# Memory Usage: 25.3 MB, less than 96.40% of Python3
class Solution2:
    def rotate(self, nums: List[int], k: int) -> None:

        l = len(nums) 
        
        tmp = []

        for i in range(l):
            tmp.append(nums[(l - k + i) % l])
            
        for i in range(l):
            nums[i] = tmp[i]
            
        
        
# Try 3
# Runtime: 334 ms, faster than 40.15% of Python3 online submissions for Rotate Array.
# Memory Usage: 25.4 MB, less than 96.40% of Python3 online submissions for Rotate Array.
class Solution3:
    def rotate(self, nums: List[int], k: int) -> None:
        # taken from
        # https://leetcode.com/problems/rotate-array/discuss/1730564/Python-1-Line-oror-Detailed-Explanation-oror-Clean-and-Easy-to-Understand
        # and
        # https://leetcode.com/problems/rotate-array/discuss/1729973/Python3-IN-PLACE-()-Exaplained/1243155
        
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]    
    
    

# Try 4
# do left rotations
# Runtime: 1068 ms, faster than 19.19% of Python3 online submissions for Rotate Array.
# Memory Usage: 25.3 MB, less than 96.15% of Python3 online submissions for Rotate Array.
class Solution4:
    def rotate(self, nums: List[int], k: int) -> None:
        
        # left_rotations = len(nums) - right_rotations
        k = len(nums) - (k % len(nums))
        for i in range(k):
            nums.append(nums.pop(0))



nums = [0,1,2,3,4,5,6,7,8,9]
k = int(input('k: '))

print(f'{nums}  k={k}  -->')
Solution2().rotate(nums, k)
print(f'{nums} \n')
