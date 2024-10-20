"""
Leetcode
2024-10-20
1106. Parsing A Boolean Expression
Hard

A boolean expression is an expression that evaluates to either true or false. It can be in one of the following shapes:

    't' that evaluates to true.
    'f' that evaluates to false.
    '!(subExpr)' that evaluates to the logical NOT of the inner expression subExpr.
    '&(subExpr1, subExpr2, ..., subExprn)' that evaluates to the logical AND of the inner expressions subExpr1, subExpr2, ..., subExprn where n >= 1.
    '|(subExpr1, subExpr2, ..., subExprn)' that evaluates to the logical OR of the inner expressions subExpr1, subExpr2, ..., subExprn where n >= 1.

Given a string expression that represents a boolean expression, return the evaluation of that expression.

It is guaranteed that the given expression is valid and follows the given rules.

 

Example 1:

Input: expression = "&(|(f))"
Output: false
Explanation: 
First, evaluate |(f) --> f. The expression is now "&(f)".
Then, evaluate &(f) --> f. The expression is now "f".
Finally, return false.

Example 2:

Input: expression = "|(f,f,f,t)"
Output: true
Explanation: The evaluation of (false OR false OR false OR true) is true.

Example 3:

Input: expression = "!(&(f,t))"
Output: true
Explanation: 
First, evaluate &(f,t) --> (false AND true) --> false --> f. The expression is now "!(f)".
Then, evaluate !(f) --> NOT false --> true. We return true.

 

Constraints:

    1 <= expression.length <= 2 * 10^4
    expression[i] is one following characters: '(', ')', '&', '|', '!', 't', 'f', and ','.
"""


from collections import deque


class Solution:
    """
    Runtime: 15 ms, faster than 100.00% of Python3 online submissions for Parsing A Boolean Expression.
    Memory Usage: 17 MB, less than 10.78% of Python3 online submissions for Parsing A Boolean Expression.
    """

    def parseBoolExpr(self, expression: str) -> bool:
        return self.parse(expression, 0)[0]

    def parse(self, expr: str, idx: int) -> tuple[bool, int]:
        if expr[idx] == 't':
            return [True, idx + 1]
        if expr[idx] == 'f':
            return [False, idx + 1]
        if expr[idx] == '!':
            return self.parse_not(expr, idx + 1)
        if expr[idx] == '&':
            return self.parse_and(expr, idx + 1)
        if expr[idx] == '|':
            return self.parse_or(expr, idx + 1)
        raise ValueError('bad expression')

    def parse_not(self, expr: str, idx: int) -> tuple[bool, int]:
        if expr[idx] != '(':
            raise ValueError('parse_not: must start with "("')
        sub_val, sub_end = self.parse(expr, idx + 1)
        if expr[sub_end] != ')':
            raise ValueError('parse_not: must end with ")"')
        return [not sub_val, sub_end + 1]

    def parse_and(self, expr: str, idx: int) -> tuple[bool, int]:
        if expr[idx] != '(':
            raise ValueError('parse_and: must start with "("')
        val = True
        i = idx + 1
        while expr[i] != ')':
            sub_val, sub_end = self.parse(expr, i)
            val &= sub_val
            i = sub_end
            if expr[sub_end] not in [',', ')']:
                raise ValueError('parse_and: expected "," or ")"')
            i += expr[sub_end] == ','
        return [val, i + 1]

    def parse_or(self, expr: str, idx: int) -> tuple[bool, int]:
        if expr[idx] != '(':
            raise ValueError('parse_or: must start with "("')
        val = False
        i = idx + 1
        while expr[i] != ')':
            sub_val, sub_end = self.parse(expr, i)
            val |= sub_val
            i = sub_end
            if expr[sub_end] not in [',', ')']:
                raise ValueError('parse_or: expected "," or ")"')
            i += expr[sub_end] == ','
        return [val, i + 1]


class Solution1:
    """
    leetcode solution 1: String Manipulation
    Runtime: 31 ms, faster than 99.10% of Python3 online submissions for Parsing A Boolean Expression.
    Memory Usage: 16.7 MB, less than 50.60% of Python3 online submissions for Parsing A Boolean Expression.
    """

    def parseBoolExpr(self, expression: str) -> bool:
        # Repeatedly simplify the expression by evaluating subexpressions
        while len(expression) > 1:
            start = max(
                expression.rfind("!"),
                expression.rfind("&"),
                expression.rfind("|"),
            )
            end = expression.find(")", start)
            sub_expr = expression[start: end + 1]
            result = self._evaluate_sub_expr(sub_expr)
            expression = expression[:start] + result + expression[end + 1:]

        return expression == "t"

    def _evaluate_sub_expr(self, sub_expr: str) -> str:
        # Extract the operator and the enclosed values
        op = sub_expr[0]
        values = sub_expr[2:-1]

        # Apply logical operations based on the operator
        if op == "!":
            return "f" if values == "t" else "t"
        if op == "&":
            return "f" if "f" in values else "t"
        if op == "|":
            return "t" if "t" in values else "f"

        return "f"  # This point should never be reached


class Solution2:
    """
    leetcode solution 2: Recursive
    Runtime: 11 ms, faster than 100.00% of Python3 online submissions for Parsing A Boolean Expression.
    Memory Usage: 16.7 MB, less than 50.60% of Python3 online submissions for Parsing A Boolean Expression.
    """

    def parseBoolExpr(self, expression: str) -> bool:
        index = [
            0
        ]  # using a list because python variables are pass by object reference
        return self._evaluate(expression, index)

    # Recursively parse and evaluate the boolean expression
    def _evaluate(self, expr: str, index: list) -> bool:
        curr_char = expr[index[0]]
        index[0] += 1

        # Base cases: true ('t') or false ('f')
        if curr_char == "t":
            return True
        if curr_char == "f":
            return False

        # Handle NOT operation '!(...)'
        if curr_char == "!":
            index[0] += 1  # skip '('
            result = not self._evaluate(expr, index)
            index[0] += 1  # skip ')'
            return result

        # Handle AND '&(...)' and OR '|(...)'
        values = []
        index[0] += 1  # skip '('
        while expr[index[0]] != ")":
            if expr[index[0]] != ",":
                values.append(
                    self._evaluate(expr, index)
                )  # collect results of subexpressions
            else:
                index[0] += 1  # skip commas
        index[0] += 1  # skip ')'

        # Manual AND operation: returns false if any value is false
        if curr_char == "&":
            return all(values)

        # Manual OR operation: returns true if any value is true
        if curr_char == "|":
            return any(values)

        return False  # this point should never be reached


class Solution3:
    """
    leetcode solution 3: Using Stack
    Runtime: 8 ms, faster than 100.00% of Python3 online submissions for Parsing A Boolean Expression.
    Memory Usage: 16.8 MB, less than 19.76% of Python3 online submissions for Parsing A Boolean Expression.
    """

    def parseBoolExpr(self, expression: str) -> bool:
        st = deque()

        # Traverse the entire expression
        for curr_char in expression:
            if curr_char == ")":
                values = []

                # Gather all values inside the parentheses
                while st[-1] != "(":
                    values.append(st.pop())
                st.pop()  # Remove '('
                op = st.pop()  # Remove the operator

                # Evaluate the subexpression and push the result back
                result = self._evaluate_sub_expr(op, values)
                st.append(result)
            elif curr_char != ",":
                # Push non-comma characters into the stack
                st.append(curr_char)

        # Final result is on the top of the stack
        return st[-1] == "t"

    # Evaluates a subexpression based on the operator and list of values
    def _evaluate_sub_expr(self, op, values):
        if op == "!":
            return "f" if values[0] == "t" else "t"

        # AND: return 'f' if any value is 'f', otherwise return 't'
        if op == "&":
            for value in values:
                if value == "f":
                    return "f"
            return "t"

        # OR: return 't' if any value is 't', otherwise return 'f'
        if op == "|":
            for value in values:
                if value == "t":
                    return "t"
            return "f"

        return "f"  # This point should never be reached


class Solution4:
    """
    leetcode solution 4: Optimized Stack
    Runtime: 15 ms, faster than 100.00% of Python3 online submissions for Parsing A Boolean Expression.
    Memory Usage: 16.7 MB, less than 80.84% of Python3 online submissions for Parsing A Boolean Expression.
    """

    def parseBoolExpr(self, expression: str) -> bool:
        st = deque()

        # Traverse through the expression
        for curr_char in expression:
            if curr_char == "," or curr_char == "(":
                # curr_char  # Skip commas and open parentheses
                continue

            # Push operators and boolean values to the stack
            if curr_char in ["t", "f", "!", "&", "|"]:
                st.append(curr_char)

            # Handle closing parentheses and evaluate the subexpression
            elif curr_char == ")":
                has_true = False
                has_false = False

                # Process the values inside the parentheses
                while st[-1] not in ["!", "&", "|"]:
                    top_value = st.pop()
                    if top_value == "t":
                        has_true = True
                    elif top_value == "f":
                        has_false = True

                # Pop the operator and evaluate the subexpression
                op = st.pop()
                if op == "!":
                    st.append("t" if not has_true else "f")
                elif op == "&":
                    st.append("f" if has_false else "t")
                else:
                    st.append("t" if has_true else "f")

        # The final result is at the top of the stack
        return st[-1] == "t"
