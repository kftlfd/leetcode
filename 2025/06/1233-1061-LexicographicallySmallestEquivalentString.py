"""
Leetcode
2025-06-05
1061. Lexicographically Smallest Equivalent String
Solved
Medium
Topics
premium lock iconCompanies
Hint

You are given two strings of the same length s1 and s2 and a string baseStr.

We say s1[i] and s2[i] are equivalent characters.

    For example, if s1 = "abc" and s2 = "cde", then we have 'a' == 'c', 'b' == 'd', and 'c' == 'e'.

Equivalent characters follow the usual rules of any equivalence relation:

    Reflexivity: 'a' == 'a'.
    Symmetry: 'a' == 'b' implies 'b' == 'a'.
    Transitivity: 'a' == 'b' and 'b' == 'c' implies 'a' == 'c'.

For example, given the equivalency information from s1 = "abc" and s2 = "cde", "acd" and "aab" are equivalent strings of baseStr = "eed", and "aab" is the lexicographically smallest equivalent string of baseStr.

Return the lexicographically smallest equivalent string of baseStr by using the equivalency information from s1 and s2.

 

Example 1:

Input: s1 = "parker", s2 = "morris", baseStr = "parser"
Output: "makkek"
Explanation: Based on the equivalency information in s1 and s2, we can group their characters as [m,p], [a,o], [k,r,s], [e,i].
The characters in each group are equivalent and sorted in lexicographical order.
So the answer is "makkek".

Example 2:

Input: s1 = "hello", s2 = "world", baseStr = "hold"
Output: "hdld"
Explanation: Based on the equivalency information in s1 and s2, we can group their characters as [h,w], [d,e,o], [l,r].
So only the second letter 'o' in baseStr is changed to 'd', the answer is "hdld".

Example 3:

Input: s1 = "leetcode", s2 = "programs", baseStr = "sourcecode"
Output: "aauaaaaada"
Explanation: We group the equivalent characters in s1 and s2 as [a,o,e,r,s,c], [l,p], [g,t] and [d,m], thus all letters in baseStr except 'u' and 'd' are transformed to 'a', the answer is "aauaaaaada".

 

Constraints:

    1 <= s1.length, s2.length, baseStr <= 1000
    s1.length == s2.length
    s1, s2, and baseStr consist of lowercase English letters.


Hint 1
Model these equalities as edges of a graph.
Hint 2
Group each connected component of the graph and assign each node of this component to the node with the lowest lexicographically character.
Hint 3
Finally convert the string with the precalculated information.
"""


class Solution00:
    """
    Runtime 7ms Beats 49.64%
    Memory 17.76MB Beats 87.59%
    """

    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        a = ord("a")
        chars = [i for i in range(26)]

        def get_root(idx: int) -> int:
            root = chars[idx]
            while root != chars[root]:
                root = chars[root]
            return root

        for c1, c2 in zip(s1, s2):
            val1, val2 = ord(c1) - a, ord(c2) - a
            root1, root2 = get_root(val1), get_root(val2)
            if root1 < root2:
                chars[root2] = root1
            else:
                chars[root1] = root2

        def to_smallest(c: str) -> str:
            return chr(get_root(ord(c) - a) + a)

        return "".join([to_smallest(c) for c in baseStr])


class Solution01:
    """
    Runtime 3ms Beats 94.40%
    Memory 18.01MB Beats 21.17%
    """

    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        a = ord("a")
        chars = [i for i in range(26)]

        def get_root(idx: int) -> int:
            root = chars[idx]
            while root != chars[root]:
                root = chars[root]
            return root

        for c1, c2 in zip(s1, s2):
            val1, val2 = ord(c1) - a, ord(c2) - a
            root1, root2 = get_root(val1), get_root(val2)
            if root1 < root2:
                chars[root2] = root1
            else:
                chars[root1] = root2

        smallest = [
            chr(get_root(i) + a)
            for i in range(26)
        ]

        return "".join([smallest[ord(c) - a] for c in baseStr])
