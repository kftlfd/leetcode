"""
Leetcode
2025-02-06
1726. Tuple with Same Product
Medium
Topics
Companies
Hint

Given an array nums of distinct positive integers, return the number of tuples (a, b, c, d) such that a * b = c * d where a, b, c, and d are elements of nums, and a != b != c != d.

 

Example 1:

Input: nums = [2,3,4,6]
Output: 8
Explanation: There are 8 valid tuples:
(2,6,3,4) , (2,6,4,3) , (6,2,3,4) , (6,2,4,3)
(3,4,2,6) , (4,3,2,6) , (3,4,6,2) , (4,3,6,2)

Example 2:

Input: nums = [1,2,4,5,10]
Output: 16
Explanation: There are 16 valid tuples:
(1,10,2,5) , (1,10,5,2) , (10,1,2,5) , (10,1,5,2)
(2,5,1,10) , (2,5,10,1) , (5,2,1,10) , (5,2,10,1)
(2,10,4,5) , (2,10,5,4) , (10,2,4,5) , (10,2,5,4)
(4,5,2,10) , (4,5,10,2) , (5,4,2,10) , (5,4,10,2)

 

Constraints:

    1 <= nums.length <= 1000
    1 <= nums[i] <= 10^4
    All elements in nums are distinct.

Hint 1
Note that all of the integers are distinct. This means that each time a product is formed it must be formed by two unique integers.
Hint 2
Count the frequency of each product of 2 distinct numbers. Then calculate the permutations formed.
"""

from collections import Counter, defaultdict
from functools import cache
from itertools import combinations
from math import comb
from typing import List


class Solution:
    """
    Runtime 327ms Beats 81.99%
    Memory 46.48MB Beats 41.71%
    """

    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)
        product = defaultdict(int)

        for i in range(n-1):
            for j in range(i+1, n):
                product[nums[i] * nums[j]] += 1

        ans = 0

        @cache
        def edges_count(i: int):
            if i == 1:
                return 0
            return edges_count(i-1) + i-1

        for cnt in product.values():
            if cnt < 2:
                continue
            ans += edges_count(cnt) * 8

        return ans


class Solution3:
    """
    leetcode solution 3: Product Frequency Hash Map
    Runtime 318ms Beats 84.83%
    Memory 46.23MB Beats 78.20%
    """

    def tupleSameProduct(self, nums: List[int]) -> int:
        nums_length = len(nums)

        # Initialize a dictionary to store the frequency of each product of pairs
        pair_products_frequency = {}

        total_number_of_tuples = 0

        # Iterate through each pair of numbers in `nums`
        for first_index in range(nums_length):
            for second_index in range(first_index + 1, nums_length):
                # Increment the frequency of the product of the current pair
                product_value = nums[first_index] * nums[second_index]
                if product_value in pair_products_frequency:
                    pair_products_frequency[product_value] += 1
                else:
                    pair_products_frequency[product_value] = 1

        # Iterate through each product value and its frequency in the dictionary
        for product_frequency in pair_products_frequency.values():
            # Calculate the number of ways to choose two pairs with the same product
            pairs_of_equal_product = (
                (product_frequency - 1) * product_frequency // 2
            )

            # Add the number of tuples for this product to the total (each pair
            # can form 8 tuples)
            total_number_of_tuples += 8 * pairs_of_equal_product

        return total_number_of_tuples


class Solution4:
    """
    https://leetcode.com/problems/tuple-with-same-product/editorial/comments/2840266
    Runtime 274ms Beats 97.63%
    Memory 46.51MB Beats 22.27%
    """

    def tupleSameProduct(self, nums: List[int]) -> int:
        product_counts = Counter(a * b for a, b in combinations(nums, 2))
        return 8 * sum(comb(C, 2) for C in product_counts.values())
