"""
Leetcode
41. First Missing Positive
Hard
2024-03-26

Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

 

Example 1:

Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.

Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.

Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.

 

Constraints:

    1 <= nums.length <= 10^5
    -2^31 <= nums[i] <= 2^31 - 1
"""

from typing import List


class Solution1:
    """
    leetcode solution 2: Index as a Hash Key
    Runtime: 290 ms, faster than 64.00% of Python3 online submissions for First Missing Positive.
    Memory Usage: 30.2 MB, less than 81.41% of Python3 online submissions for First Missing Positive.
    """

    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        has_1 = False

        # Replace negative numbers, zeros,
        # and numbers larger than n with 1s.
        # After this nums contains only positive numbers.
        for i, num in enumerate(nums):
            if num == 1:
                has_1 = True
            if num < 1 or num > n:
                nums[i] = 1

        if not has_1:
            return 1

        # Mark whether integers 1 to n are in nums
        # Use index as a hash key and negative sign as a presence detector.
        for i in range(n):
            val = abs(nums[i])
            # If you meet number a in the array - change the sign of a-th element.
            # Be careful with duplicates : do it only once.
            if val == n:
                nums[0] = -abs(nums[0])
            else:
                nums[val] = -abs(nums[val])

        # First positive in nums is smallest missing positive integer
        for i in range(1, n):
            if nums[i] > 0:
                return i

        # nums[0] stores whether n is in nums
        if nums[0] > 0:
            return n

        # If nums contained all elements 1 to n
        # the smallest missing positive number is n + 1
        return n + 1


class Solution2:
    """
    leetcode solution 3: Cycle Sort
    Runtime: 290 ms, faster than 64.00% of Python3 online submissions for First Missing Positive.
    Memory Usage: 30.2 MB, less than 94.68% of Python3 online submissions for First Missing Positive.
    """

    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        # Use cycle sort to place positive elements smaller than n
        # at the correct index
        i = 0
        while i < n:
            correct_idx = nums[i] - 1
            if 0 < nums[i] <= n and nums[i] != nums[correct_idx]:
                # swap
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
            else:
                i += 1

        # Iterate through nums
        # return smallest missing positive integer
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        # If all elements are at the correct index
        # the smallest missing positive number is n + 1
        return n + 1
