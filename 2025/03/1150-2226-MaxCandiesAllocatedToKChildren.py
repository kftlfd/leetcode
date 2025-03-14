"""
Leetcode
2025-03-14
2226. Maximum Candies Allocated to K Children
Medium
Topics
Companies
Hint

You are given a 0-indexed integer array candies. Each element in the array denotes a pile of candies of size candies[i]. You can divide each pile into any number of sub piles, but you cannot merge two piles together.

You are also given an integer k. You should allocate piles of candies to k children such that each child gets the same number of candies. Each child can be allocated candies from only one pile of candies and some piles of candies may go unused.

Return the maximum number of candies each child can get.

 

Example 1:

Input: candies = [5,8,6], k = 3
Output: 5
Explanation: We can divide candies[1] into 2 piles of size 5 and 3, and candies[2] into 2 piles of size 5 and 1. We now have five piles of candies of sizes 5, 5, 3, 5, and 1. We can allocate the 3 piles of size 5 to 3 children. It can be proven that each child cannot receive more than 5 candies.

Example 2:

Input: candies = [2,5], k = 11
Output: 0
Explanation: There are 11 children but only 7 candies in total, so it is impossible to ensure each child receives at least one candy. Thus, each child gets no candy and the answer is 0.

 

Constraints:

    1 <= candies.length <= 10^5
    1 <= candies[i] <= 10^7
    1 <= k <= 10^12


Hint 1
For a fixed number of candies c, how can you check if each child can get c candies?
Hint 2
Use binary search to find the maximum c as the answer.
"""

from typing import List


class Solution:
    """
    leetcode solution
    Runtime 390ms Beats 48.18%
    Memory 29.69MB Beats 88.94%
    """

    def maximumCandies(self, candies: List[int], k: int) -> int:
        # Find the maximum number of candies in any pile
        max_candies_in_pile = 0
        for candy in candies:
            max_candies_in_pile = max(max_candies_in_pile, candy)

        # Set the initial search range for binary search
        left = 0
        right = max_candies_in_pile

        # Binary search to find the maximum number of candies each child can get
        while left < right:
            # Calculate the middle value of the current range
            middle = (left + right + 1) // 2

            # Check if it's possible to allocate candies so that each child gets 'middle' candies
            if self._can_allocate_candies(candies, k, middle):
                # If possible, move to the upper half to search for a larger number
                left = middle
            else:
                # Otherwise, move to the lower half
                right = middle - 1

        return left

    def _can_allocate_candies(self, candies, k, num_of_candies):
        # Initialize the total number of children that can be served
        max_num_of_children = 0

        # Iterate over all piles to calculate how many children each pile can serve
        for pile in candies:
            max_num_of_children += pile // num_of_candies

        return max_num_of_children >= k
