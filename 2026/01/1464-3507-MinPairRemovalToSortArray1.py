"""
Leetcode
2026-01-22
3507. Minimum Pair Removal to Sort Array I
Easy

Given an array nums, you can perform the following operation any number of times:

    Select the adjacent pair with the minimum sum in nums. If multiple such pairs exist, choose the leftmost one.
    Replace the pair with their sum.

Return the minimum number of operations needed to make the array non-decreasing.

An array is said to be non-decreasing if each element is greater than or equal to its previous element (if it exists).

 

Example 1:

Input: nums = [5,2,3,1]

Output: 2

Explanation:

    The pair (3,1) has the minimum sum of 4. After replacement, nums = [5,2,4].
    The pair (2,4) has the minimum sum of 6. After replacement, nums = [5,6].

The array nums became non-decreasing in two operations.

Example 2:

Input: nums = [1,2,2]

Output: 0

Explanation:

The array nums is already sorted.

 

Constraints:

    1 <= nums.length <= 50
    -1000 <= nums[i] <= 1000

 
"""

from typing import List


class Solution:
    """
    Runtime 11ms Beats 78.95%
    Memory 19.34MB Beats 18.99%
    """

    def minimumPairRemoval(self, nums: List[int]) -> int:
        ops = 0
        nums = nums[:]
        is_sorted = False

        while not is_sorted:
            is_sorted = True
            min_pair_sum = 999999
            min_pair_idx = -1
            for i in range(len(nums) - 1):
                cur_sum = nums[i] + nums[i + 1]
                if cur_sum < min_pair_sum:
                    min_pair_sum = cur_sum
                    min_pair_idx = i
                if nums[i + 1] < nums[i]:
                    is_sorted = False
            if not is_sorted:
                nums[min_pair_idx:min_pair_idx + 2] = [min_pair_sum]
                ops += 1

        return ops


class Solution2:
    """
    leetcode solution 2: Simulation + Array Simulation of Linked List
    Runtime 15ms Beats 45.68%
    Memory 19.44MB Beats 8.08%
    """

    def minimumPairRemoval(self, nums: List[int]) -> int:
        next_node = list(range(1, len(nums) + 1))
        next_node[-1] = None
        count = 0

        while len(nums) - count > 1:
            curr = 0
            target = 0
            target_adj_sum = nums[target] + nums[next_node[target]]
            is_ascending = True

            while curr is not None and next_node[curr] is not None:
                if nums[curr] > nums[next_node[curr]]:
                    is_ascending = False

                curr_adj_sum = nums[curr] + nums[next_node[curr]]
                if curr_adj_sum < target_adj_sum:
                    target = curr
                    target_adj_sum = curr_adj_sum

                curr = next_node[curr]

            if is_ascending:
                break

            count += 1
            next_node[target] = next_node[next_node[target]]
            nums[target] = target_adj_sum

        return count
