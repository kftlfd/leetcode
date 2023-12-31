"""
Leetcode
429. N-ary Tree Level Order Traversal (medium)
2022-09-05

Given an n-ary tree, return the level order traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

Example 1:
Input: root = [1,null,3,2,4,null,5,6]
Output: [[1],[3,2,4],[5,6]]
"""

from typing import List


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


# Runtime: 116 ms, faster than 7.00% of Python3 online submissions for N-ary Tree Level Order Traversal.
# Memory Usage: 16.1 MB, less than 50.08% of Python3 online submissions for N-ary Tree Level Order Traversal.
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return None

        out = []
        q = [root]

        while q:
            level = []
            q2 = []
            for node in q:
                if not node:
                    continue
                level.append(node.val)
                q2 += node.children
            out.append(level)
            q = q2

        return out


# s = Solution()
# tests = []
# for t in tests:
#     print(t)
#     print()
#     print()
