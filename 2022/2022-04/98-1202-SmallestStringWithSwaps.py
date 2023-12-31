"""
Leetcode
1202. Smallest String With Swaps (medium)
2022-04-27

You are given a string s, and an array of pairs of indices in the string pairs where pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string.

You can swap the characters at any pair of indices in the given pairs any number of times.

Return the lexicographically smallest string that s can be changed to after using the swaps.
"""

from typing import List



# wrong
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        out = [c for c in s]
        swaps = True
        while swaps:
            swaps = False
            for a,b in pairs:
                if ord(out[b]) < ord(out[a]):
                    out[a], out[b] = out[b], out[a]
                    swaps = True
        return ''.join(out)



# https://leetcode.com/problems/smallest-string-with-swaps/discuss/1985185/Python3-UNION-FIND-()**-Explained
# Runtime: 921 ms, faster than 52.05% of Python3 online submissions for Smallest String With Swaps.
# Memory Usage: 50.4 MB, less than 69.64% of Python3 online submissions for Smallest String With Swaps.
from collections import defaultdict
class Solution1:
    def union(self, a, b):
        self.parent[self.find(a)] = self.find(b)
		
    def find(self, a):
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])

        return self.parent[a]
        
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
		# 1. Union-Find
        self.parent = list(range(len(s)))
        for a, b in pairs:
            self.union(a, b)

		# 2. Grouping
        group = defaultdict(lambda: ([], []))  
        for i, ch in enumerate(s):
            parent = self.find(i)
            group[parent][0].append(i)
            group[parent][1].append(ch)

		# 3. Sorting
        res = [''] * len(s)
        for ids, chars in group.values():
            ids.sort()
            chars.sort()
            for ch, i in zip(chars, ids):
                res[i] = ch
                
        return ''.join(res)



s = Solution1()
tests = [
    ["dcab", [[0,3],[1,2]]],
    ["dcab", [[0,3],[1,2],[0,2]]],
    ["cba", [[0,1],[1,2]]]
]
for t in tests:
    print(*t)
    print(s.smallestStringWithSwaps(t[0], t[1]))
    print()
