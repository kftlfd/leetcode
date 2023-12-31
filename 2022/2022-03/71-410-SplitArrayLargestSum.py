"""
Leetcode
410. Split Array Largest Sum (hard)
2022-03-31

Given an array nums which consists of non-negative integers and an 
integer m, you can split the array into m non-empty continuous subarrays.

Write an algorithm to minimize the largest sum among these m subarrays.
"""

from typing import List



# leetcode solution - binary search
# https://leetcode.com/problems/split-array-largest-sum/solution/
# Runtime: 47 ms, faster than 72.49% of Python3 online submissions for Split Array Largest Sum.
# Memory Usage: 13.9 MB, less than 69.95% of Python3 online submissions for Split Array Largest Sum.
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        
        def min_subarrays_required(max_sum_allowed: int) -> int:
            current_sum = 0
            splits_required = 0
            
            for element in nums:
                # Add element only if the sum doesn't exceed max_sum_allowed
                if current_sum + element <= max_sum_allowed:
                    current_sum += element
                else:
                    # If the element addition makes sum more than max_sum_allowed
                    # Increment the splits required and reset sum
                    current_sum = element
                    splits_required += 1

            # Return the number of subarrays, which is the number of splits + 1
            return splits_required + 1
        
        # Define the left and right boundary of binary search
        left = max(nums)
        right = sum(nums)
        while left <= right:
            # Find the mid value
            max_sum_allowed = (left + right) // 2
            
            # Find the minimum splits. If splits_required is less than
            # or equal to m move towards left i.e., smaller values
            if min_subarrays_required(max_sum_allowed) <= m:
                right = max_sum_allowed - 1
                minimum_largest_split_sum = max_sum_allowed
            else:
                # Move towards right if splits_required is more than m
                left = max_sum_allowed + 1
        
        return minimum_largest_split_sum



s = Solution()
tests = [
    [[7,2,5,10,8], 2],
    [[1,2,3,4,5], 2],
    [[1,4,4], 3]
]
for t in tests:
    print(t)
    print(s.splitArray(t[0], t[1]))
    print()
