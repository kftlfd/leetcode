"""
Leetcode
2025-05-11
1550. Three Consecutive Odds
Solved
Easy
Topics
Companies
Hint
Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.

 

Example 1:

Input: arr = [2,6,4,1]
Output: false
Explanation: There are no three consecutive odds.

Example 2:

Input: arr = [1,2,34,3,4,5,7,23,12]
Output: true
Explanation: [5,7,23] are three consecutive odds.

 

Constraints:

    1 <= arr.length <= 1000
    1 <= arr[i] <= 1000


"""

from typing import List


class Solution:
    """
    Runtime 0ms Beats 100.00%
    Memory 17.79MB Beats 88.31%
    """

    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for i in range(2, len(arr)):
            if arr[i] & 1 == 0:
                continue
            if arr[i - 1] & 1 == 1 and arr[i - 2] & 1 == 1:
                return True

        return False


class Solution2:
    """
    leetcode solution 2: Counting
    Runtime 0ms Beats 100.00%
    Memory 18.11MB Beats 18.18%
    """

    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        consecutive_odds = 0

        # Increment the counter if the number is odd,
        # else reset the counter
        for num in arr:
            # Check if the current number is odd
            if num % 2 == 1:
                consecutive_odds += 1
            else:
                consecutive_odds = 0

            # Check if there are three consecutive odd numbers
            if consecutive_odds == 3:
                return True

        return False


class Solution3:
    """
    leetcode solution 3: Product of Three Numbers
    Runtime 0ms Beats 100.00%
    Memory 17.96MB Beats 38.15%
    """

    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        # Loop through the array up to the third-to-last element
        for i in range(len(arr) - 2):
            product = arr[i] * arr[i + 1] * arr[i + 2]
            # Check if the product is odd
            if product % 2 == 1:
                return True
        return False
