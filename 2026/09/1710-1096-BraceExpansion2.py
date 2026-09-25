"""
Leetcode
2026-09-25
1096. Brace Expansion II
Hard

Under the grammar given below, strings can represent a set of lowercase words. Let R(expr) denote the set of words the expression represents.

The grammar can best be understood through simple examples:

    Single letters represent a singleton set containing that word.
        R("a") = {"a"}
        R("w") = {"w"}
    When we take a comma-delimited list of two or more expressions, we take the union of possibilities.
        R("{a,b,c}") = {"a","b","c"}
        R("{{a,b},{b,c}}") = {"a","b","c"} (notice the final set only contains each word at most once)
    When we concatenate two expressions, we take the set of possible concatenations between two words where the first word comes from the first expression and the second word comes from the second expression.
        R("{a,b}{c,d}") = {"ac","ad","bc","bd"}
        R("a{b,c}{d,e}f{g,h}") = {"abdfg", "abdfh", "abefg", "abefh", "acdfg", "acdfh", "acefg", "acefh"}

Formally, the three rules for our grammar:

    For every lowercase letter x, we have R(x) = {x}.
    For expressions e1, e2, ... , ek with k >= 2, we have R({e1, e2, ...}) = R(e1) ∪ R(e2) ∪ ...
    For expressions e1 and e2, we have R(e1 + e2) = {a + b for (a, b) in R(e1) × R(e2)}, where + denotes concatenation, and × denotes the cartesian product.

Given an expression representing a set of words under the given grammar, return the sorted list of words that the expression represents.

 

Example 1:

Input: expression = "{a,b}{c,{d,e}}"
Output: ["ac","ad","ae","bc","bd","be"]

Example 2:

Input: expression = "{{a,z},a{b,c},{ab,z}}"
Output: ["a","ab","ac","z"]
Explanation: Each distinct word is written only once in the final answer.

 

Constraints:

    1 <= expression.length <= 60
    expression[i] consists of '{', '}', ','or lowercase English letters.
    The given expression represents a set of words based on the grammar given in the description.


Hint 1
You can write helper methods to parse the next "chunk" of the expression. If you see eg. "a", the answer is just the set {a}. If you see "{", you parse until you complete the "}" (the number of { and } seen are equal) and that becomes a chunk that you find where the appropriate commas are, and parse each individual expression between the commas.
"""


class Solution:
    """
    Runtime 3ms Beats 79.78%
    Memory 19.64MB Beats 29.51%
    """

    def braceExpansionII(self, expression: str) -> list[str]:
        return list(sorted(self.parse(expression)))

    def parse(self, expr: str) -> set[str]:
        if not any((c in expr for c in ",}{")):
            return {expr}
        sets: list[set[str]] = []
        cur = set()
        i = 0
        while i < len(expr):
            c = expr[i]
            if c == ",":
                sets.append(cur)
                cur = set()
                i += 1
                continue
            nxt, di = self.nxt_expr(expr[i:])
            cur = self.concat(cur, self.parse(nxt))
            i += di
        sets.append(cur)
        return self.union(sets)

    def nxt_expr(self, expr: str) -> tuple[str, int]:
        if expr[0] == "{":
            cnt = 0
            for i, c in enumerate(expr):
                if c == "{":
                    cnt += 1
                elif c == "}":
                    cnt -= 1
                if cnt == 0:
                    return (expr[1:i], i + 1)
            raise ValueError("invalid expression")

        if expr[0] == "}":
            raise ValueError("invalid expression")

        i = 0
        while i < len(expr) and expr[i] not in ",}{":
            i += 1

        return (expr[:i], i)

    def concat(self, a: set[str], b: set[str]) -> set[str]:
        if not a:
            return b
        if not b:
            return a
        c: set[str] = set()
        for va in a:
            for vb in b:
                c.add(va + vb)
        return c

    def union(self, l: list[set[str]]) -> set[str]:
        u: set[str] = set()
        for s in l:
            u = u.union(s)
        return u


class Solution1:
    """
    leetcode solution 1: Recursive Parsing
    Runtime 1ms Beats 88.52%
    Memory 19.46MB Beats 81.97%
    """

    def braceExpansionII(self, expression: str) -> list[str]:
        idx = 0
        n = len(expression)

        def is_letter(c: str) -> bool:
            return "a" <= c <= "z"

        # Recursive descent parser
        def expr() -> set:
            nonlocal idx
            ret = set()
            while True:
                # Take the union with the result of term()
                ret |= term()
                # Continue if a comma is matched; otherwise, stop matching
                if idx < n and expression[idx] == ",":
                    idx += 1
                    continue
                else:
                    break
            return ret

        # term -> item | item term
        def term() -> set:
            nonlocal idx
            # Initialize an empty set and take its Cartesian product with subsequent results
            ret = {""}
            # An item starts with { or a lowercase letter; continue matching only when this condition is met
            while idx < n and (
                expression[idx] == "{" or is_letter(expression[idx])
            ):
                sub = item()
                tmp = set()
                for left in ret:
                    for right in sub:
                        tmp.add(left + right)
                ret = tmp
            return ret

        # item -> letter | { expr }
        def item() -> set:
            nonlocal idx
            ret = set()
            if expression[idx] == "{":
                idx += 1
                ret = expr()
            else:
                ret = {expression[idx]}
            idx += 1
            return ret

        ret = expr()
        return sorted(list(ret))


class Solution2:
    """
    leetcode solution 2: Stack
    Runtime 3ms Beats 79.78%
    Memory 19.61MB Beats 29.51%
    """

    def braceExpansionII(self, expression: str) -> list[str]:
        op = []  # Operator stack
        stk = []  # Set stack

        # Pop the operator at the top of the stack and perform the calculation
        def ope():
            l, r = len(stk) - 2, len(stk) - 1
            if op[-1] == "+":
                # Union operation
                stk[l] |= stk[r]
            else:
                # Cartesian product operation
                tmp = set()
                for left in stk[l]:
                    for right in stk[r]:
                        tmp.add(left + right)
                stk[l] = tmp
            op.pop()
            stk.pop()

        for i, ch in enumerate(expression):
            if ch == ",":
                # Keep popping operators from the top of the stack until the stack is empty or its top is not a multiplication sign
                while op and op[-1] == "*":
                    ope()
                op.append("+")
            elif ch == "{":
                # First determine whether a multiplication sign needs to be added, then push { onto the operator stack
                if i > 0 and (
                    expression[i - 1] == "}" or expression[i - 1].isalpha()
                ):
                    op.append("*")
                op.append("{")
            elif ch == "}":
                # Keep popping operators from the top of the stack until its top is {
                while op and op[-1] != "{":
                    ope()
                op.pop()
            else:
                # First determine whether a multiplication sign needs to be added, then push the newly constructed set onto the set stack
                if i > 0 and (
                    expression[i - 1] == "}" or expression[i - 1].isalpha()
                ):
                    op.append("*")
                stk.append({ch})

        while op:
            ope()

        return sorted(stk[-1])
