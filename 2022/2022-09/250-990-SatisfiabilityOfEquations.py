"""
Leetcode
990. Satisfiability of Equality Equations (medium)
2022-09-26

You are given an array of strings equations that represent relationships between variables where each string equations[i] is of length 4 and takes one of two different forms: "xi==yi" or "xi!=yi".Here, xi and yi are lowercase letters (not necessarily different) that represent one-letter variable names.

Return true if it is possible to assign integers to variable names so as to satisfy all the given equations, or false otherwise.

Example 1:
Input: equations = ["a==b","b!=a"]
Output: false
Explanation: If we assign say, a = 1 and b = 1, then the first equation is satisfied, but not the second.
There is no way to assign the variables to satisfy both equations.

Example 2:
Input: equations = ["b==a","a==b"]
Output: true
Explanation: We could assign a = 1 and b = 1 to satisfy both equations.

Constraints:
 - 1 <= equations.length <= 500
 - equations[i].length == 4
 - equations[i][0] is a lowercase letter.
 - equations[i][1] is either '=' or '!'.
 - equations[i][2] is '='.
 - equations[i][3] is a lowercase letter.
"""

from typing import List


# https://leetcode.com/problems/satisfiability-of-equality-equations/discuss/234486/JavaC++Python-Easy-Union-Find
# Runtime: 95 ms, faster than 25.41% of Python3 online submissions for Satisfiability of Equality Equations.
# Memory Usage: 14.1 MB, less than 35.38% of Python3 online submissions for Satisfiability of Equality Equations.
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        def find(x):
            if x != uf[x]:
                uf[x] = find(uf[x])
            return uf[x]
        uf = {a: a for a in [chr(x) for x in range(ord('a'), ord('z') + 1)]}
        for a, e, _, b in equations:
            if e == "=":
                uf[find(a)] = find(b)
        return not any(e == "!" and find(a) == find(b) for a, e, _, b in equations)


# Wrong
class Solution1:
    def equationsPossible(self, equations: List[str]) -> bool:
        group = 0
        eq = {}

        for a, e, _, b in equations:
            if e == "=":
                if a in eq.keys() or b in eq.keys():
                    eq[a] = eq[a] if a in eq.keys() else eq[b]
                    eq[b] = eq[a] if a in eq.keys() else eq[b]
                else:
                    eq[a] = eq[b] = group
                    group += 1

        for a, e, _, b in equations:
            if e == "!":
                if a == b:
                    return False
                if a in eq.keys() and b in eq.keys() and eq[a] == eq[b]:
                    return False

        return True


s = Solution1()
tests = [
    ["a==b", "e==c", "b==c", "a!=e"],
    ["a!=a"],
    ["c==c", "b==d", "x!=z"],
    ["a==b", "b!=c", "c==a"],
    ["a==b", "b==c", "a==c"],
    ["a==b", "b!=a"],
    ["b==a", "a==b"],
]
for t in tests:
    print(t)
    print(s.equationsPossible(t))
    print()
