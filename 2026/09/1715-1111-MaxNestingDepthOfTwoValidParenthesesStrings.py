"""
Leetcode
2026-09-30
1111. Maximum Nesting Depth of Two Valid Parentheses Strings
Medium

A string is a valid parentheses string (denoted VPS) if and only if it consists of "(" and ")" characters only, and:

    It is the empty string, or
    It can be written as AB (A concatenated with B), where A and B are VPS's, or
    It can be written as (A), where A is a VPS.

We can similarly define the nesting depth depth(S) of any VPS S as follows:

    depth("") = 0
    depth(A + B) = max(depth(A), depth(B)), where A and B are VPS's
    depth("(" + A + ")") = 1 + depth(A), where A is a VPS.

For example, "", "()()", and "()(()())" are VPS's (with nesting depths 0, 1, and 2), and ")(" and "(()" are not VPS's.

Given a VPS seq, split it into two disjoint subsequences A and B, such that A and B are VPS's (and A.length + B.length = seq.length). The subsequences may not necessarily be contiguous.

For example, for the sequence 123456789, one possible split is:

    A = {1, 3, 5, 7, 9},

    B = {2, 4, 6, 8}.

This corresponds to the output [0, 1, 0, 1, 0, 1, 0, 1, 0]  where 0 indicates membership in A and 1 indicates membership in B.

Now choose any such A and B such that max(depth(A), depth(B)) is the minimum possible value.

Return an answer array (of length seq.length) that encodes such a choice of A and B:  answer[i] = 0 if seq[i] is part of A, else answer[i] = 1.  Note that even though multiple answers may exist, you may return any of them.

 

Example 1:

Input: seq = "(()())"
Output: [0,1,1,1,1,0]

Example 2:

Input: seq = "()(())()"
Output: [0,0,0,1,1,0,1,1]

 

Constraints:

    1 <= seq.size <= 10000


"""


class Solution:
    """
    Runtime 4ms Beats 18.98%
    Memory 19.18MB Beats 98.15%
    """

    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        A = 0
        B = 0
        ans = [0] * len(seq)

        for i, c in enumerate(seq):
            if c == "(":
                if A <= B:
                    A += 1
                else:
                    B += 1
                    ans[i] = 1
            else:
                if A >= B:
                    A -= 1
                else:
                    B -= 1
                    ans[i] = 1

        return ans


class Solution1:
    """
    leetcode solution 1: Bracket Matching Using a Stack
    Runtime 0ms Beats 100.00%
    Memory 19.41MB Beats 27.78%
    """

    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        ans = []
        d = 0
        for c in seq:
            if c == "(":
                d += 1
                ans.append(d % 2)
            if c == ")":
                ans.append(d % 2)
                d -= 1
        return ans


class Solution2:
    """
    leetcode solution 2: Find the Pattern
    Runtime 1ms Beats 60.65%
    Memory 19.18MB Beats 98.15%
    """

    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        ans = []
        for i, ch in enumerate(seq):
            if ch == "(":
                ans.append(i % 2)
            else:
                ans.append(1 - i % 2)
            # The above code can also be abbreviated to
            # ans.append((i & 1) ^ (ch == '('))
            # C++ and JavaScript code provide direct shorthand methods.
        return ans
