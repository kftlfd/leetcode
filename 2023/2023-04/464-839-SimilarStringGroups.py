"""
Leetcode
839. Similar String Groups (hard)
2023-04-28

Two strings X and Y are similar if we can swap two letters (in different positions) of X, so that it equals Y. Also two strings X and Y are similar if they are equal.

For example, "tars" and "rats" are similar (swapping at positions 0 and 2), and "rats" and "arts" are similar, but "star" is not similar to "tars", "rats", or "arts".

Together, these form two connected groups by similarity: {"tars", "rats", "arts"} and {"star"}.  Notice that "tars" and "arts" are in the same group even though they are not similar.  Formally, each group is such that a word is in the group if and only if it is similar to at least one other word in the group.

We are given a list strs of strings where every string in strs is an anagram of every other string in strs. How many groups are there?

Example 1:
Input: strs = ["tars","rats","arts","star"]
Output: 2

Example 2:
Input: strs = ["omv","ovm"]
Output: 1
"""

from typing import List


class Solution:
    """
    https://leetcode.com/problems/similar-string-groups/solution/1875898
    Runtime: 385 ms, faster than 58.36% of Python3 online submissions for Similar String Groups.
    Memory Usage: 16.7 MB, less than 10.16% of Python3 online submissions for Similar String Groups.
    """

    def numSimilarGroups(self, strs: List[str]) -> int:
        parent = list(range(len(strs)))
        rank = [1] * len(strs)
        ans = len(strs)

        def find(u):
            if u != parent[u]:
                parent[u] = find(parent[u])
            return parent[u]

        def union(u, v):
            nonlocal ans

            par_u, par_v = find(u), find(v)
            if par_u == par_v:
                return

            if rank[par_v] < rank[par_u]:
                parent[par_v] = par_u
            else:
                if rank[par_u] == rank[par_v]:
                    rank[par_v] += 1
                parent[par_u] = par_v
            ans -= 1

        for i, s1 in enumerate(strs):
            for k in range(i + 1, len(strs)):
                s2 = strs[k]
                idx, n = 0, 0
                while idx < len(s1) and n <= 2:
                    if s1[idx] != s2[idx]:
                        n += 1
                    idx += 1

                if n <= 2:
                    union(i, k)

        return ans


s = Solution()
tests = [
    (["tars", "rats", "arts", "star"],
     2),

    (["omv", "ovm"],
     1),
]
for inp, exp in tests:
    res = s.numSimilarGroups(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
