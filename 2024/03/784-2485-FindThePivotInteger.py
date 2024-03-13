"""
Leetcode
2485. Find the Pivot Integer
Easy
2024-03-13

Given a positive integer n, find the pivot integer x such that:

    The sum of all elements between 1 and x inclusively equals the sum of all elements between x and n inclusively.

Return the pivot integer x. If no such integer exists, return -1. It is guaranteed that there will be at most one pivot index for the given input.

 

Example 1:

Input: n = 8
Output: 6
Explanation: 6 is the pivot integer since: 1 + 2 + 3 + 4 + 5 + 6 = 6 + 7 + 8 = 21.

Example 2:

Input: n = 1
Output: 1
Explanation: 1 is the pivot integer since: 1 = 1.

Example 3:

Input: n = 4
Output: -1
Explanation: It can be proved that no such integer exist.

 

Constraints:

    1 <= n <= 1000
"""


from itertools import accumulate
from math import sqrt


class Solution:
    """
    Runtime: 49 ms, faster than 51.36% of Python3 online submissions for Find the Pivot Integer.
    Memory Usage: 16.8 MB, less than 13.83% of Python3 online submissions for Find the Pivot Integer.
    """

    def pivotInteger(self, n: int) -> int:
        if n == 1:
            return 1

        prefix_sums = list(accumulate(range(1, n + 1)))
        total_sum = prefix_sums[-1]

        for i in range(1, len(prefix_sums)):
            p_sum = prefix_sums[i]
            if p_sum == total_sum - prefix_sums[i - 1]:
                return i + 1

        return -1


class Solution2:
    """
    leetcode solution 2: Two Pointer
    Runtime: 50 ms, faster than 47.88% of Python3 online submissions for Find the Pivot Integer.
    Memory Usage: 16.5 MB, less than 59.17% of Python3 online submissions for Find the Pivot Integer.
    """

    def pivotInteger(self, n: int) -> int:
        if n == 1:
            return 1

        left_value = 1
        right_value = n
        sum_left = left_value
        sum_right = right_value

        # Iterate until the pointers meet
        while left_value < right_value:
            # Adjust sums and pointers based on comparison
            if sum_left < sum_right:
                sum_left += left_value + 1
                left_value += 1
            else:
                sum_right += right_value - 1
                right_value -= 1

            # Check for pivot condition
            if sum_left == sum_right and left_value + 1 == right_value - 1:
                return left_value + 1

        return -1  # Return -1 if no pivot is found


class Solution3:
    """
    leetcode solution 3: Binary Search
    Runtime: 44 ms, faster than 67.73% of Python3 online submissions for Find the Pivot Integer.
    Memory Usage: 16.6 MB, less than 23.99% of Python3 online submissions for Find the Pivot Integer.
    """

    def pivotInteger(self, n: int) -> int:
        # Initialize left and right pointers for binary search
        left, right = 1, n

        # Calculate the total sum of the sequence
        total_sum = n * (n + 1) // 2

        # Binary search for the pivot point
        while left < right:
            # Calculate the mid-point
            mid = (left + right) // 2

            # Check if the difference between the square of mid and the total sum is negative
            if mid * mid - total_sum < 0:
                left = mid + 1  # Adjust the left bound if the sum is smaller
            else:
                right = mid  # Adjust the right bound if the sum is equal or greater

        # Check if the square of the left pointer minus the total sum is zero
        if left * left - total_sum == 0:
            return left
        else:
            return -1


class Solution5:
    """
    leetcode solution 5: Using Math
    Runtime: 33 ms, faster than 94.45% of Python3 online submissions for Find the Pivot Integer.
    Memory Usage: 16.5 MB, less than 59.17% of Python3 online submissions for Find the Pivot Integer.
    """

    def pivotInteger(self, n: int) -> int:
        """
        1+2+...+x = x+...+n
        using arithmetic progression:
        (x(x+1))/2 = ((x+n)(n-x+1))/2
        2(x^2) = n^2 + n
        x = sqrt((n^2 + n) / 2)

        midpoint of a sequence that grows linearly = max / 2
        midpoint of s sequence that grows quadratically = sqrt(sum)

        n*(n+1)/2 -- grows qudratically
        """

        total_sum = n * (n + 1) // 2
        pivot = int(sqrt(total_sum))
        # If pivot * pivot is equal to sum (pivot found) return pivot, else return -1
        return pivot if pivot * pivot == total_sum else -1
