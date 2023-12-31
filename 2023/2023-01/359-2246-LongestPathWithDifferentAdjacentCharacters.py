"""
Leetcode
2246. Longest Path With Different Adjacent Characters (hard)
2023-01-13

You are given a tree (i.e. a connected, undirected graph that has no cycles) rooted at node 0 consisting of n nodes numbered from 0 to n - 1. The tree is represented by a 0-indexed array parent of size n, where parent[i] is the parent of node i. Since node 0 is the root, parent[0] == -1.

You are also given a string s of length n, where s[i] is the character assigned to node i.

Return the length of the longest path in the tree such that no pair of adjacent nodes on the path have the same character assigned to them.

Example 1:
Input: parent = [-1,0,0,1,1,2], s = "abacbe"
Output: 3
Explanation: The longest path where each two adjacent nodes have different characters in the tree is the path: 0 -> 1 -> 3. The length of this path is 3, so 3 is returned.
It can be proven that there is no longer path that satisfies the conditions. 

Example 2:
Input: parent = [-1,0,0,0], s = "aabc"
Output: 3
Explanation: The longest path where each two adjacent nodes have different characters is the path: 2 -> 0 -> 3. The length of this path is 3, so 3 is returned.
"""

from typing import List, Optional
from collections import defaultdict


# leetcode solution
# Runtime: 1588 ms, faster than 95.34% of Python3 online submissions for Longest Path With Different Adjacent Characters.
# Memory Usage: 149 MB, less than 75.30% of Python3 online submissions for Longest Path With Different Adjacent Characters.
class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:

        ans = 1

        children = defaultdict(list)
        for i in range(1, len(parent)):
            children[parent[i]].append(i)

        def dfs(currNode):
            nonlocal ans, children, s

            if currNode not in children:
                return 1

            longestChain = 0
            secondLongestChain = 0
            for child in children[currNode]:
                longestChainStartingFromChild = dfs(child)
                if s[currNode] == s[child]:
                    continue
                if longestChainStartingFromChild > longestChain:
                    secondLongestChain = longestChain
                    longestChain = longestChainStartingFromChild
                elif longestChainStartingFromChild > secondLongestChain:
                    secondLongestChain = longestChainStartingFromChild

            ans = max(ans, longestChain + secondLongestChain + 1)
            return longestChain + 1

        dfs(0)
        return ans


s = Solution()
tests = [
    (([-1, 0, 0, 1, 1, 2], "abacbe"),
     3),

    (([-1, 0, 0, 0], "aabc"),
     3)
]
for inp, exp in tests:
    parent, string = inp
    res = s.longestPath(parent, string)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
