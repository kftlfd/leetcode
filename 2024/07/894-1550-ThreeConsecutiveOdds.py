"""
Leetcode
1550. Three Consecutive Odds
Easy
2024-07-01

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
    Runtime: 41 ms, faster than 89.04% of Python3 online submissions for Three Consecutive Odds.
    Memory Usage: 16.6 MB, less than 93.64% of Python3 online submissions for Three Consecutive Odds.
    """

    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False

        arr = [num % 2 for num in arr]

        count = arr[0] + arr[1]

        for end in range(2, len(arr)):
            count += arr[end]
            if count == 3:
                return True
            count -= arr[end - 2]

        return False


class Solution2:
    """
    leetcode solution 2: Counting
    Runtime: 52 ms, faster than 23.68% of Python3 online submissions for Three Consecutive Odds.
    Memory Usage: 16.7 MB, less than 67.76% of Python3 online submissions for Three Consecutive Odds.
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
