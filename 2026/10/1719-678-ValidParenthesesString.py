"""
Leetcode
2026-10-04
678. Valid Parenthesis String
Medium

Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

    Any left parenthesis '(' must have a corresponding right parenthesis ')'.
    Any right parenthesis ')' must have a corresponding left parenthesis '('.
    Left parenthesis '(' must go before the corresponding right parenthesis ')'.
    '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".

 

Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "(*)"
Output: true

Example 3:

Input: s = "(*))"
Output: true

Example 4:

Input: s = "("
Output: false

 

Constraints:

    1 <= s.length <= 100
    s[i] is '(', ')' or '*'.


Hint 1
Use backtracking to explore all possible combinations of treating '*' as either '(', ')', or an empty string. If any combination leads to a valid string, return true.
Hint 2
DP[i][j] represents whether the substring s[i:j] is valid.
Hint 3
Keep track of the count of open parentheses encountered so far. If you encounter a close parenthesis, it should balance with an open parenthesis. Utilize a stack to handle this effectively.
Hint 4
How about using 2 stacks instead of 1? Think about it.
"""


from functools import cache


class Solution:
    """
    Runtime 7ms Beats 10.77%
    Memory 21.08MB Beats 7.87%
    """

    def checkValidString(self, s: str) -> bool:

        @cache
        def check(i: int, cnt: int) -> bool:
            if i >= len(s):
                return cnt == 0

            c = s[i]
            if c == "(":
                return check(i + 1, cnt + 1)

            if c == ")":
                if cnt - 1 < 0:
                    return False
                return check(i + 1, cnt - 1)

            if check(i + 1, cnt):
                return True
            if check(i + 1, cnt + 1):
                return True
            if cnt - 1 < 0:
                return False
            if check(i + 1, cnt - 1):
                return True

            return False

        return check(0, 0)


class Solution1:
    """
    leetcode solution 1: Top-Down Dynamic Programming - Memoization
    Runtime 7ms Beats 10.77%
    Memory 19.48MB Beats 14.36%
    """

    def checkValidString(self, s: str) -> bool:
        n = len(s)
        memo = [[-1] * n for _ in range(n)]
        return self.is_valid_string(0, 0, s, memo)

    def is_valid_string(self, index: int, open_count: int, s: str, memo: list[list[int]]) -> bool:
        # If reached end of the string, check if all brackets are balanced
        if index == len(s):
            return open_count == 0

        # If already computed, return memoized result
        if memo[index][open_count] != -1:
            return memo[index][open_count] == 1

        is_valid = False
        # If encountering '*', try all possibilities
        if s[index] == '*':
            is_valid |= self.is_valid_string(
                index + 1, open_count + 1, s, memo)  # Treat '*' as '('
            if open_count > 0:
                is_valid |= self.is_valid_string(
                    index + 1, open_count - 1, s, memo)  # Treat '*' as ')'
            is_valid |= self.is_valid_string(
                index + 1, open_count, s, memo)  # Treat '*' as empty
        else:
            # Handle '(' and ')'
            if s[index] == '(':
                is_valid = self.is_valid_string(
                    # Increment count for '('
                    index + 1, open_count + 1, s, memo)
            elif open_count > 0:
                # Decrement count for ')'
                is_valid = self.is_valid_string(
                    index + 1, open_count - 1, s, memo)

        # Memoize and return the result
        memo[index][open_count] = 1 if is_valid else 0
        return is_valid


class Solution2:
    """
    leetcode solution 2: Bottom-Up Dynamic Programming - Tabulation
    Runtime 23ms Beats 5.07%
    Memory 19.51MB Beats 11.12%
    """

    def checkValidString(self, s: str) -> bool:
        n = len(s)
        # dp[i][j] represents if the substring starting from index i is valid with j opening brackets
        dp = [[False] * (n + 1) for _ in range(n + 1)]

        # base case: an empty string with 0 opening brackets is valid
        dp[n][0] = True

        for index in range(n - 1, -1, -1):
            for open_bracket in range(n):
                is_valid = False

                # '*' can represent '(' or ')' or '' (empty)
                if s[index] == '*':
                    if open_bracket < n:
                        # try '*' as '('
                        is_valid |= dp[index + 1][open_bracket + 1]
                    # opening brackets to use '*' as ')'
                    if open_bracket > 0:
                        # try '*' as ')'
                        is_valid |= dp[index + 1][open_bracket - 1]
                    is_valid |= dp[index + 1][open_bracket]  # ignore '*'
                else:
                    # If the character is not '*', it can be '(' or ')'
                    if s[index] == '(':
                        is_valid |= dp[index + 1][open_bracket + 1]  # try '('
                    elif open_bracket > 0:
                        is_valid |= dp[index + 1][open_bracket - 1]  # try ')'
                dp[index][open_bracket] = is_valid

        # check if the entire string is valid with no excess opening brackets
        return dp[0][0]


class Solution3:
    """
    leetcode solution 3: Using Two Stacks
    Runtime 0ms Beats 100.00%
    Memory 19.10MB Beats 89.99%
    """

    def checkValidString(self, s: str) -> bool:
        # Stacks to store indices of open brackets and asterisks
        open_brackets = []
        asterisks = []

        for i, ch in enumerate(s):
            # If current character is an open bracket, push its index onto the stack
            if ch == "(":
                open_brackets.append(i)
            # If current character is an asterisk, push its index onto the stack
            elif ch == "*":
                asterisks.append(i)
            # current character is a closing bracket ')'
            else:
                # If there are open brackets available, use them to balance the closing bracket
                if open_brackets:
                    open_brackets.pop()
                elif asterisks:
                    # If no open brackets are available, use an asterisk to balance the closing bracket
                    asterisks.pop()
                else:
                    # nnmatched ')' and no '*' to balance it.
                    return False

        # Check if there are remaining open brackets and asterisks that can balance them
        while open_brackets and asterisks:
            # If an open bracket appears after an asterisk, it cannot be balanced, return false
            if open_brackets.pop() > asterisks.pop():
                return False  # '*' before '(' which cannot be balanced.

        # If all open brackets are matched and there are no unmatched open brackets left, return true
        return not open_brackets


class Solution4:
    """
    leetcode solution 4: Two Pointer
    Runtime 0ms Beats 100.00%
    Memory 19.35MB Beats 28.53%
    """

    def checkValidString(self, s: str) -> bool:
        open_count = 0
        close_count = 0
        length = len(s) - 1

        # Traverse the string from both ends simultaneously
        for i in range(length + 1):
            # Count open parentheses or asterisks
            if s[i] == '(' or s[i] == '*':
                open_count += 1
            else:
                open_count -= 1

            # Count close parentheses or asterisks
            if s[length - i] == ')' or s[length - i] == '*':
                close_count += 1
            else:
                close_count -= 1

            # If at any point open count or close count goes negative, the string is invalid
            if open_count < 0 or close_count < 0:
                return False

        # If open count and close count are both non-negative, the string is valid
        return True
