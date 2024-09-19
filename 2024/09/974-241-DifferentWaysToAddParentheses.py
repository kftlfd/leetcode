"""
Leetcode
2024-09-19
241. Different Ways to Add Parentheses
Medium

Given a string expression of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. You may return the answer in any order.

The test cases are generated such that the output values fit in a 32-bit integer and the number of different results does not exceed 104.

 

Example 1:

Input: expression = "2-1-1"
Output: [0,2]
Explanation:
((2-1)-1) = 0 
(2-(1-1)) = 2

Example 2:

Input: expression = "2*3-4*5"
Output: [-34,-14,-10,-10,10]
Explanation:
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10

 

Constraints:

    1 <= expression.length <= 20
    expression consists of digits and the operator '+', '-', and '*'.
    All the integer values in the input expression are in the range [0, 99].
"""

from typing import List


class Solution1:
    """
    leetcode solution 1: Recursion
    Runtime: 38 ms, faster than 57.91% of Python3 online submissions for Different Ways to Add Parentheses.
    Memory Usage: 16.7 MB, less than 27.58% of Python3 online submissions for Different Ways to Add Parentheses.
    """

    def diffWaysToCompute(self, expression: str) -> List[int]:
        results = []

        # Base case: if the string is empty, return an empty list
        if len(expression) == 0:
            return results

        # Base case: if the string is a single character, treat it as a number and return it
        if len(expression) == 1:
            return [int(expression)]

        # If the string has only two characters and the first character is a digit, parse it as a number
        if len(expression) == 2 and expression[0].isdigit():
            return [int(expression)]

        # Recursive case: iterate through each character
        for i, current_char in enumerate(expression):

            # Skip if the current character is a digit
            if current_char.isdigit():
                continue

            # Split the expression into left and right parts
            left_results = self.diffWaysToCompute(expression[:i])
            right_results = self.diffWaysToCompute(expression[i + 1:])

            # Combine results from left and right parts
            for left_value in left_results:
                for right_value in right_results:
                    # Perform the operation based on the current character
                    if current_char == "+":
                        results.append(left_value + right_value)
                    elif current_char == "-":
                        results.append(left_value - right_value)
                    elif current_char == "*":
                        results.append(left_value * right_value)

        return results


class Solution3:
    """
    leetcode solution 3: Tabulation
    Runtime: 34 ms, faster than 80.10% of Python3 online submissions for Different Ways to Add Parentheses.
    Memory Usage: 16.9 MB, less than 8.08% of Python3 online submissions for Different Ways to Add Parentheses.
    """

    def diffWaysToCompute(self, expression: str) -> List[int]:
        n = len(expression)
        # Create a 2D array of lists to store results of subproblems
        dp = [[[] for _ in range(n)] for _ in range(n)]

        self._initialize_base_cases(expression, dp)

        # Fill the dp table for all possible subexpressions
        for length in range(3, n + 1):
            for start in range(n - length + 1):
                end = start + length - 1
                self._process_subexpression(expression, dp, start, end)

        # Return the results for the entire expression
        return dp[0][n - 1]

    def _initialize_base_cases(
        self, expression: str, dp: List[List[List[int]]]
    ):
        # Handle base cases: single digits and two-digit numbers
        for i, char in enumerate(expression):
            if char.isdigit():
                # Check if it's a two-digit number
                dig1 = ord(char) - ord("0")
                if i + 1 < len(expression) and expression[i + 1].isdigit():
                    dig2 = ord(expression[i + 1]) - ord("0")
                    number = dig1 * 10 + dig2
                    dp[i][i + 1].append(number)
                # Single digit case
                dp[i][i].append(dig1)

    def _process_subexpression(
        self, expression: str, dp: List[List[List[int]]], start: int, end: int
    ):
        # Try all possible positions to split the expression
        for split in range(start, end + 1):
            if expression[split].isdigit():
                continue

            left_results = dp[start][split - 1]
            right_results = dp[split + 1][end]

            self._compute_results(
                expression[split], left_results, right_results, dp[start][end]
            )

    def _compute_results(
        self,
        op: str,
        left_results: List[int],
        right_results: List[int],
        results: List[int],
    ):
        # Compute results based on the operator at position 'split'
        for left_value in left_results:
            for right_value in right_results:
                if op == "+":
                    results.append(left_value + right_value)
                elif op == "-":
                    results.append(left_value - right_value)
                elif op == "*":
                    results.append(left_value * right_value)
