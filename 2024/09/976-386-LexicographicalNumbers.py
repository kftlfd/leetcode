"""
Leetcode
2024-09-21
386. Lexicographical Numbers
Medium

Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.

You must write an algorithm that runs in O(n) time and uses O(1) extra space. 

 

Example 1:

Input: n = 13
Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]

Example 2:

Input: n = 2
Output: [1,2]

 

Constraints:

    1 <= n <= 5 * 10^4
"""

from typing import List


class Solution:
    """
    Runtime: 75 ms, faster than 60.60% of Python3 online submissions for Lexicographical Numbers.
    Memory Usage: 22.3 MB, less than 85.99% of Python3 online submissions for Lexicographical Numbers.
    """

    def lexicalOrder(self, n: int) -> List[int]:
        ans = [1]
        cur = 10

        while cur > 1:
            if cur <= n:
                ans.append(cur)
                cur *= 10
            else:
                cur //= 10
                while str(cur)[-1] == "9":
                    cur //= 10
                cur += 1

        return ans


class Solution1:
    """
    leetcode solution 1: DFS
    Runtime: 87 ms, faster than 34.01% of Python3 online submissions for Lexicographical Numbers.
    Memory Usage: 22.4 MB, less than 85.99% of Python3 online submissions for Lexicographical Numbers.
    """

    def lexicalOrder(self, n: int) -> List[int]:
        lexicographical_numbers = []
        # Start generating numbers from 1 to 9
        for start in range(1, 10):
            self._generate_lexical_numbers(start, n, lexicographical_numbers)
        return lexicographical_numbers

    def _generate_lexical_numbers(
        self, current_number: int, limit: int, result: List[int]
    ):
        # If the current number exceeds the limit, stop recursion
        if current_number > limit:
            return
        # Add the current number to the result
        result.append(current_number)

        # Try to append digits from 0 to 9 to the current number
        for next_digit in range(10):
            next_number = current_number * 10 + next_digit
            # If the next number is within the limit, continue recursion
            if next_number <= limit:
                self._generate_lexical_numbers(next_number, limit, result)
            else:
                break  # No need to continue if next_number exceeds limit


class Solution2:
    """
    leetcode solution 2: Iterative Approach
    Runtime: 73 ms, faster than 68.26% of Python3 online submissions for Lexicographical Numbers.
    Memory Usage: 22.2 MB, less than 95.69% of Python3 online submissions for Lexicographical Numbers.
    """

    def lexicalOrder(self, n: int) -> List[int]:
        lexicographical_numbers = []
        current_number = 1

        # Generate numbers from 1 to n
        for _ in range(n):
            lexicographical_numbers.append(current_number)

            # If multiplying the current number by 10 is within the limit, do it
            if current_number * 10 <= n:
                current_number *= 10
            else:
                # Adjust the current number by moving up one digit
                while current_number % 10 == 9 or current_number >= n:
                    current_number //= 10  # Remove the last digit
                current_number += 1  # Increment the number

        return lexicographical_numbers
