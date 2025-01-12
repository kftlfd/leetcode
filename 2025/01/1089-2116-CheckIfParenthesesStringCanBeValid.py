"""
Leetcode
2025-01-12
2116. Check if a Parentheses String Can Be Valid
Medium
Topics
Companies
Hint

A parentheses string is a non-empty string consisting only of '(' and ')'. It is valid if any of the following conditions is true:

    It is ().
    It can be written as AB (A concatenated with B), where A and B are valid parentheses strings.
    It can be written as (A), where A is a valid parentheses string.

You are given a parentheses string s and a string locked, both of length n. locked is a binary string consisting only of '0's and '1's. For each index i of locked,

    If locked[i] is '1', you cannot change s[i].
    But if locked[i] is '0', you can change s[i] to either '(' or ')'.

Return true if you can make s a valid parentheses string. Otherwise, return false.

 

Example 1:

Input: s = "))()))", locked = "010100"
Output: true
Explanation: locked[1] == '1' and locked[3] == '1', so we cannot change s[1] or s[3].
We change s[0] and s[4] to '(' while leaving s[2] and s[5] unchanged to make s valid.

Example 2:

Input: s = "()()", locked = "0000"
Output: true
Explanation: We do not need to make any changes because s is already valid.

Example 3:

Input: s = ")", locked = "0"
Output: false
Explanation: locked permits us to change s[0]. 
Changing s[0] to either '(' or ')' will not make s valid.

 

Constraints:

    n == s.length == locked.length
    1 <= n <= 10^5
    s[i] is either '(' or ')'.
    locked[i] is either '0' or '1'.

Hint 1
Can an odd length string ever be valid?
Hint 2
From left to right, if a locked ')' is encountered, it must be balanced with either a locked '(' or an unlocked index on its left. If neither exist, what conclusion can be drawn? If both exist, which one is more preferable to use?
Hint 3
After the above, we may have locked indices of '(' and additional unlocked indices. How can you balance out the locked '(' now? What if you cannot balance any locked '('?
"""


class Solution:
    """
    Runtime 99ms Beats 63.98%
    Memory 20.82MB Beats 21.33%
    """

    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = []
        first_open_idx = []

        for cs, lock in zip(s, locked):
            c = "*" if lock == "0" else cs

            if c == "(":
                first_open_idx.append(len(stack))
                stack.append(c)
                continue

            if c == ")":
                if not stack:
                    return False
                if first_open_idx:
                    stack.pop(first_open_idx.pop())
                else:
                    stack.pop()
                continue

            stack.append(c)

        blanks = 0
        opened = 0
        for c in stack:
            if c == "*":
                if opened > 0:
                    opened -= 1
                else:
                    blanks += 1
            else:
                opened += 1

        return opened == 0 and blanks % 2 == 0


class Solution1:
    """
    leetcode solution 1: Stack
    Runtime 64ms Beats 89.34%
    Memory 22.13MB Beats 6.05%
    """

    def canBeValid(self, s: str, locked: str) -> bool:
        length = len(s)

        # If length of string is odd, return false.
        if length % 2 == 1:
            return False

        open_brackets = []
        unlocked = []

        # Iterate through the string to handle '(' and ')'
        for i in range(length):
            if locked[i] == "0":
                unlocked.append(i)
            elif s[i] == "(":
                open_brackets.append(i)
            elif s[i] == ")":
                if open_brackets:
                    open_brackets.pop()
                elif unlocked:
                    unlocked.pop()
                else:
                    return False

        # Match remaining open brackets and the unlocked characters
        while open_brackets and unlocked and open_brackets[-1] < unlocked[-1]:
            open_brackets.pop()
            unlocked.pop()

        if open_brackets:
            return False

        return True


class Solution2:
    """
    leetcode solution 2: Constant Space
    Runtime 111ms Beats 45.24%
    Memory 18.57MB Beats 57.06%
    """

    def canBeValid(self, s: str, locked: str) -> bool:
        length = len(s)
        # If length of string is odd, return false.
        if length % 2 == 1:
            return False
        open_brackets = 0
        unlocked_count = 0
        # Iterate through the string to handle '(' and ')'.
        for i in range(length):
            if locked[i] == "0":
                unlocked_count += 1
            elif s[i] == "(":
                open_brackets += 1
            elif s[i] == ")":
                if open_brackets > 0:
                    open_brackets -= 1
                elif unlocked_count > 0:
                    unlocked_count -= 1
                else:
                    return False

        # Match remaining open brackets with unlocked characters.
        balance_count = 0
        for i in range(length - 1, -1, -1):
            if locked[i] == "0":
                balance_count -= 1
                unlocked_count -= 1
            elif s[i] == "(":
                balance_count += 1
                open_brackets -= 1
            elif s[i] == ")":
                balance_count -= 1
            if balance_count > 0:
                return False
            if unlocked_count == 0 and open_brackets == 0:
                break

        if open_brackets > 0:
            return False

        return True
