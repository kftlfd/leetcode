"""
Leetcode
264. Ugly Number II
Medium
2024-08-18

An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return the nth ugly number.

 

Example 1:

Input: n = 10
Output: 12
Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.

Example 2:

Input: n = 1
Output: 1
Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.

 

Constraints:

    1 <= n <= 1690

Hints:
- The naive approach is to call isUgly for every number until you reach the nth one. Most numbers are not ugly. Try to focus your effort on generating only the ugly ones.
- An ugly number must be multiplied by either 2, 3, or 5 from a smaller ugly number.
- The key is how to maintain the order of the ugly numbers. Try a similar approach of merging from three sorted lists: L1, L2, and L3.
- Assume you have Uk, the kth ugly number. Then Uk+1 must be Min(L1 * 2, L2 * 3, L3 * 5).
"""


import heapq


class Solution1:
    """
    leetcode solution 1: Using Set
    Runtime: 434 ms, faster than 8.46% of Python3 online submissions for Ugly Number II.
    Memory Usage: 16.5 MB, less than 71.48% of Python3 online submissions for Ugly Number II.
    """

    def nthUglyNumber(self, n: int) -> int:
        # Set to store potential ugly numbers
        ugly_numbers_set = set()
        # Start with 1, the first ugly number
        ugly_numbers_set.add(1)

        current_ugly = 1
        for _ in range(n):
            # Get the smallest number from the set
            current_ugly = min(ugly_numbers_set)
            # Remove it from the set
            ugly_numbers_set.remove(current_ugly)

            # Insert the next potential ugly numbers
            ugly_numbers_set.add(current_ugly * 2)
            ugly_numbers_set.add(current_ugly * 3)
            ugly_numbers_set.add(current_ugly * 5)

        # Return the nth ugly number
        return current_ugly


class Solution2:
    """
    leetcode solution 2: Min-Heap/Priority Queue
    Runtime: 115 ms, faster than 45.10% of Python3 online submissions for Ugly Number II.
    Memory Usage: 16.6 MB, less than 36.75% of Python3 online submissions for Ugly Number II.
    """

    def nthUglyNumber(self, n: int) -> int:
        min_heap = []  # min-heap to store and retrieve the smallest ugly number
        seen_numbers = set()  # set to avoid duplicates
        prime_factors = [2, 3, 5]  # factors for generating new ugly numbers

        heapq.heappush(min_heap, 1)
        seen_numbers.add(1)

        current_ugly = 1
        for _ in range(n):
            current_ugly = heapq.heappop(min_heap)  # get the smallest number

            # generate and push the next ugly numbers
            for prime in prime_factors:
                next_ugly = current_ugly * prime
                if next_ugly not in seen_numbers:  # avoid duplicates
                    heapq.heappush(min_heap, next_ugly)
                    seen_numbers.add(next_ugly)

        return current_ugly  # return the nth ugly number


class Solution3:
    """
    leetcode solution 3: Dynamic Programming (DP)
    Runtime: 91 ms, faster than 66.89% of Python3 online submissions for Ugly Number II.
    Memory Usage: 16.5 MB, less than 93.61% of Python3 online submissions for Ugly Number II.
    """

    def nthUglyNumber(self, n: int) -> int:
        ugly_numbers = [0] * n  # DP array to store ugly numbers
        ugly_numbers[0] = 1  # The first ugly number is 1

        # Three pointers for the multiples of 2, 3, and 5
        index_multiple_of_2, index_multiple_of_3, index_multiple_of_5 = 0, 0, 0
        next_multiple_of_2, next_multiple_of_3, next_multiple_of_5 = 2, 3, 5

        # Generate ugly numbers until we reach the nth one
        for i in range(1, n):
            # Find the next ugly number as the minimum of the next multiples
            next_ugly_number = min(
                [next_multiple_of_2, next_multiple_of_3, next_multiple_of_5]
            )
            ugly_numbers[i] = next_ugly_number

            # Update the corresponding pointer and next multiple
            if next_ugly_number == next_multiple_of_2:
                index_multiple_of_2 += 1
                next_multiple_of_2 = ugly_numbers[index_multiple_of_2] * 2
            if next_ugly_number == next_multiple_of_3:
                index_multiple_of_3 += 1
                next_multiple_of_3 = ugly_numbers[index_multiple_of_3] * 3
            if next_ugly_number == next_multiple_of_5:
                index_multiple_of_5 += 1
                next_multiple_of_5 = ugly_numbers[index_multiple_of_5] * 5

        return ugly_numbers[n - 1]  # Return the nth ugly number
