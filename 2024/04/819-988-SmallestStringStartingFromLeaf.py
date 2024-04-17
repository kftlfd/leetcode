"""
Leetcode
988. Smallest String Starting From Leaf
Medium
2024-04-17

You are given the root of a binary tree where each node has a value in the range [0, 25] representing the letters 'a' to 'z'.

Return the lexicographically smallest string that starts at a leaf of this tree and ends at the root.

As a reminder, any shorter prefix of a string is lexicographically smaller.

    For example, "ab" is lexicographically smaller than "aba".

A leaf of a node is a node that has no children.

 

Example 1:

Input: root = [0,1,2,3,4,3,4]
Output: "dba"

Example 2:

Input: root = [25,1,3,1,3,0,2]
Output: "adz"

Example 3:

Input: root = [2,2,1,null,1,0,null,0]
Output: "abc"

 

Constraints:

    The number of nodes in the tree is in the range [1, 8500].
    0 <= Node.val <= 25
"""

from itertools import zip_longest
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Runtime: 48 ms, faster than 28.96% of Python3 online submissions for Smallest String Starting From Leaf.
    Memory Usage: 17.9 MB, less than 34.37% of Python3 online submissions for Smallest String Starting From Leaf.
    """

    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        min_path: List[Optional[List[int]]] = [None]

        def update_min_path(path: List[int]):
            cur = min_path[0]

            if cur is None:
                min_path[0] = path[:]
                return

            for new_c, cur_c in zip_longest(path[::-1], cur[::-1], fillvalue=0):
                if new_c < cur_c:
                    min_path[0] = path[:]
                    return
                elif new_c > cur_c:
                    return

        def dfs(node, cur_path):
            if not node:
                return

            cur_path.append(node.val)

            if not node.left and not node.right:
                update_min_path(cur_path)
            else:
                dfs(node.left, cur_path)
                dfs(node.right, cur_path)

            cur_path.pop()

        dfs(root, [])

        final_path = min_path[0]
        final_path = final_path if final_path is not None else []

        return "".join(map(lambda x: chr(x + ord('a')), final_path[::-1]))
