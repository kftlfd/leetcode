"""
Leetcode
2025-06-08
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
    Runtime 68ms Beats 21.94%
    Memory 22.76MB Beats 44.24%
    """

    def lexicalOrder(self, n: int) -> List[int]:
        ans = []

        def dfs(cur: int):
            if cur > n:
                return
            ans.append(cur)
            nxt = cur * 10
            for i in range(10):
                dfs(nxt + i)

        for i in range(1, 10):
            dfs(i)

        return ans


class Solution1:
    """
    leetcode solution
    Runtime 8ms Beats 82.85%
    Memory 21.06MB Beats 98.92%
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
