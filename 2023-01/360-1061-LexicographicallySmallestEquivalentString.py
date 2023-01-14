"""
Leetcode
1061. Lexicographically Smallest Equivalent String 
2023-01-14

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
"""

from typing import List, Optional
from collections import defaultdict
from heapq import heappush, heappop


# Runtime: 43 ms, faster than 82.76% of Python3 online submissions for Lexicographically Smallest Equivalent String.
# Memory Usage: 13.9 MB, less than 56.90% of Python3 online submissions for Lexicographically Smallest Equivalent String.
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:

        # Union-Find / Disjoint set
        UF = {}

        def find(char):
            if char not in UF:
                UF[char] = char
                return char
            elif UF[char] == char:
                return char
            return find(UF[char])

        def union(c1, c2):
            g1 = find(c1)
            g2 = find(c2)
            if g1 < g2:
                UF[g2] = g1
            else:
                UF[g1] = g2

        for c1, c2 in zip(s1, s2):
            union(c1, c2)

        smallest_eqs = {chr(c): find(chr(c))
                        for c in range(ord('a'), ord('z') + 1)}

        ans = [smallest_eqs[c] for c in baseStr]
        return "".join(ans)


s = Solution()
tests = [
    (("parker", "morris", "parser"),
     "makkek"),

    (("hello", "world", "hold"),
     "hdld"),

    (("leetcode", "programs", "sourcecode"),
     "aauaaaaada")
]
for inp, exp in tests:
    s1, s2, baseStr = inp
    res = s.smallestEquivalentString(s1, s2, baseStr)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
