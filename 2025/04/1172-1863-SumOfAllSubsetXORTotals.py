"""
Leetcode
2025-04-05
1863. Sum of All Subset XOR Totals
Easy

The XOR total of an array is defined as the bitwise XOR of all its elements, or 0 if the array is empty.

    For example, the XOR total of the array [2,5,6] is 2 XOR 5 XOR 6 = 1.

Given an array nums, return the sum of all XOR totals for every subset of nums. 

Note: Subsets with the same elements should be counted multiple times.

An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b.

 

Example 1:

Input: nums = [1,3]
Output: 6
Explanation: The 4 subsets of [1,3] are:
- The empty subset has an XOR total of 0.
- [1] has an XOR total of 1.
- [3] has an XOR total of 3.
- [1,3] has an XOR total of 1 XOR 3 = 2.
0 + 1 + 3 + 2 = 6

Example 2:

Input: nums = [5,1,6]
Output: 28
Explanation: The 8 subsets of [5,1,6] are:
- The empty subset has an XOR total of 0.
- [5] has an XOR total of 5.
- [1] has an XOR total of 1.
- [6] has an XOR total of 6.
- [5,1] has an XOR total of 5 XOR 1 = 4.
- [5,6] has an XOR total of 5 XOR 6 = 3.
- [1,6] has an XOR total of 1 XOR 6 = 7.
- [5,1,6] has an XOR total of 5 XOR 1 XOR 6 = 2.
0 + 5 + 1 + 6 + 4 + 3 + 7 + 2 = 28

Example 3:

Input: nums = [3,4,5,6,7,8]
Output: 480
Explanation: The sum of all XOR totals for every subset is 480.

 

Constraints:

    1 <= nums.length <= 12
    1 <= nums[i] <= 20


Hint 1
Is there a way to iterate through all the subsets of the array?
Hint 2
Can we use recursion to efficiently iterate through all the subsets?
"""

from typing import List


class Solution:
    """
    Runtime 16ms Beats 41.98%
    Memory 17.80MB Beats 41.01%
    """

    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        ans = [0]

        def dfs(i: int, pick: bool, xor_total: int):
            xor_total ^= (nums[i] if pick else 0)
            if i + 1 >= n:
                ans[0] += xor_total
                return
            dfs(i + 1, True, xor_total)
            dfs(i + 1, False, xor_total)

        dfs(-1, False, 0)

        return ans[0]


class Solution2:
    """
    leetcode solution 2: Optimized Backtracking
    Runtime 9ms Beats 80.66%
    Memory 17.70MB Beats 83.05%
    """

    def subsetXORSum(self, nums: List[int]) -> int:

        def XOR_sum(nums: List[int], index: int, current_XOR: int) -> int:
            # Return current_XOR when all elements in nums are already considered
            if index == len(nums):
                return current_XOR

            # Calculate sum of subset xor with current element
            with_element = XOR_sum(nums, index + 1, current_XOR ^ nums[index])

            # Calculate sum of subset xor without current element
            without_element = XOR_sum(nums, index + 1, current_XOR)

            # Return sum of xor totals
            return with_element + without_element

        return XOR_sum(nums, 0, 0)


class Solution3:
    """
    leetcode solution 3: Bit Manipulation
    Runtime 0ms Beats 100.00%
    Memory 17.89MB Beats 41.01%
    """

    def subsetXORSum(self, nums: List[int]) -> int:
        result = 0
        # Capture each bit that is set in any of the elements
        for num in nums:
            result |= num
        # Multiply by the number of subset XOR totals that will have each bit set
        return result << (len(nums) - 1)
