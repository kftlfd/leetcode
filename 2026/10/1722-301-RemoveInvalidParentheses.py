"""
Leetcode
2026-10-07
301. Remove Invalid Parentheses
Hard

Given a string s that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.

Return a list of unique strings that are valid with the minimum number of removals. You may return the answer in any order.



Example 1:

Input: s = "()())()"
Output: ["(())()","()()()"]

Example 2:

Input: s = "(a)())()"
Output: ["(a())()","(a)()()"]

Example 3:

Input: s = ")("
Output: [""]



Constraints:

    1 <= s.length <= 25
    s consists of lowercase English letters and parentheses '(' and ')'.
    There will be at most 20 parentheses in s.


Hint 1
Since we do not know which brackets can be removed, we try all the options! We can use recursion.
Hint 2
In the recursion, for each bracket, we can either use it or remove it.
Hint 3
Recursion will generate all the valid parentheses strings but we want the ones with the least number of parentheses deleted.
Hint 4
We can count the number of invalid brackets to be deleted and only generate the valid strings in the recusrion.
"""


from collections import deque


class Solution1:
    """
    leetcode solution 1: Backtracking
    Runtime 1688ms Beats 11.41%
    Memory 19.40MB Beats 94.37%
    """

    def removeInvalidParentheses(self, s: str) -> list[str]:
        # Reset the class level variables that we use for every test case.
        self.reset()

        # Recursive call
        self.remaining(s, 0, 0, 0, [], 0)
        return list(self.valid_expressions)

    def __init__(self):
        self.valid_expressions = set()
        self.min_removed = None

    def reset(self):
        self.valid_expressions = set()
        self.min_removed = float("inf")

    def remaining(self, string, index, left_count, right_count, expr, rem_count):
        """
        string: The original string we are recursing on.
        index: current index in the original string.
        left: number of left parentheses till now.
        right: number of right parentheses till now.
        ans: the resulting expression in this particular recursion.
        ignored: number of parentheses ignored in this particular recursion.
        """

        # If we have reached the end of string.
        if index == len(string):

            # If the current expression is valid. The only scenario where it can be
            # invalid here is if left > right. The other way around we handled early on in the recursion.
            if left_count == right_count:

                if rem_count <= self.min_removed:
                    # This is the resulting expression.
                    # Strings are immutable in Python so we move around a list in the recursion
                    # and eventually join to get the final string.
                    possible_ans = "".join(expr)

                    # If the current count of brackets removed < current minimum, ignore
                    # previous answers and update the current minimum count.
                    if rem_count < self.min_removed:
                        self.valid_expressions = set()
                        self.min_removed = rem_count

                    self.valid_expressions.add(possible_ans)
        else:

            current_char = string[index]

            # If the current character is not a parenthesis, just recurse one step ahead.
            if current_char != '(' and current_char != ')':
                expr.append(current_char)
                self.remaining(string, index + 1, left_count,
                               right_count, expr, rem_count)
                expr.pop()
            else:
                # Else, one recursion is with ignoring the current character.
                # So, we increment the ignored counter and leave the left and right untouched.
                self.remaining(string, index + 1, left_count,
                               right_count, expr, rem_count + 1)

                expr.append(current_char)

                # If the current parenthesis is an opening bracket, we consider it
                # and increment left and  move forward
                if string[index] == '(':
                    self.remaining(string, index + 1, left_count +
                                   1, right_count, expr, rem_count)
                elif right_count < left_count:
                    # If the current parenthesis is a closing bracket, we consider it only if we
                    # have more number of opening brackets and increment right and move forward.
                    self.remaining(string, index + 1, left_count,
                                   right_count + 1, expr, rem_count)

                expr.pop()


class Solution2:
    """
    leetcode solution 2: Limited Backtracking!
    Runtime 1388ms Beats 16.06%
    Memory 19.43MB Beats 80.04%
    """

    def removeInvalidParentheses(self, s: str) -> list[str]:
        """
        :type s: str
        :rtype: List[str]
        """

        left = 0
        right = 0

        # First, we find out the number of misplaced left and right parentheses.
        for char in s:

            # Simply record the left one.
            if char == '(':
                left += 1
            elif char == ')':
                # If we don't have a matching left, then this is a misplaced right, record it.
                right = right + 1 if left == 0 else right

                # Decrement count of left parentheses because we have found a right
                # which CAN be a matching one for a left.
                left = left - 1 if left > 0 else left

        result = {}

        def recurse(s, index, left_count, right_count, left_rem, right_rem, expr):
            # If we reached the end of the string, just check if the resulting expression is
            # valid or not and also if we have removed the total number of left and right
            # parentheses that we should have removed.
            if index == len(s):
                if left_rem == 0 and right_rem == 0:
                    ans = "".join(expr)
                    result[ans] = 1
            else:

                # The discard case. Note that here we have our pruning condition.
                # We don't recurse if the remaining count for that parenthesis is == 0.
                if (s[index] == '(' and left_rem > 0) or (s[index] == ')' and right_rem > 0):
                    recurse(s, index + 1,
                            left_count,
                            right_count,
                            left_rem - (s[index] == '('),
                            right_rem - (s[index] == ')'), expr)

                expr.append(s[index])

                # Simply recurse one step further if the current character is not a parenthesis.
                if s[index] != '(' and s[index] != ')':
                    recurse(s, index + 1,
                            left_count,
                            right_count,
                            left_rem,
                            right_rem, expr)
                elif s[index] == '(':
                    # Consider an opening bracket.
                    recurse(s, index + 1,
                            left_count + 1,
                            right_count,
                            left_rem,
                            right_rem, expr)
                elif s[index] == ')' and left_count > right_count:
                    # Consider a closing bracket.
                    recurse(s, index + 1,
                            left_count,
                            right_count + 1,
                            left_rem,
                            right_rem, expr)

                # Pop for backtracking.
                expr.pop()

        # Now, the left and right variables tell us the number of misplaced left and
        # right parentheses and that greatly helps pruning the recursion.
        recurse(s, 0, 0, 0, left, right, [])
        return list(result.keys())


class Solution3:
    """
    https://leetcode.com/problems/remove-invalid-parentheses/editorial/comments/621538/
    Runtime 79ms Beats 57.54%
    Memory 20.06MB Beats 34.36%
    """

    def removeInvalidParentheses(self, s: str) -> list[str]:

        # helper to check if the expression is valid
        def isValid(expr):
            count = 0
            for ch in expr:
                if ch not in '()':
                    continue
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1
                if count < 0:
                    return False
            return count == 0

        if len(s) == 0:
            return [""]

        visited = set()

        queue = deque()
        queue.append(s)
        visited.add(s)

        found = False
        output = []

        while queue:
            expr = queue.popleft()

            if isValid(expr):
                output.append(expr)
                found = True

            if found:
                continue

            for i in range(len(expr)):
                if expr[i] not in '()':
                    continue

                candidate = expr[:i] + expr[i+1:]
                if candidate not in visited:
                    queue.append(candidate)
                    visited.add(candidate)

        return output if output else [""]
