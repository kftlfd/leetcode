"""
Leetcode
652. Find Duplicate Subtrees (medium)
2023-02-28

Given the root of a binary tree, return all duplicate subtrees.

For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with the same node values.

Example 1:
Input: root = [1,2,3,4,null,2,4,null,null,4]
Output: [[2,4],[4]]

Example 2:
Input: root = [2,1,1]
Output: [[1]]

Example 3:
Input: root = [2,2,2,3,null,3,null]
Output: [[2,3],[3]]
"""

from typing import List, Optional
from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    leetcode solution 1
    Runtime: 54 ms, faster than 67.97% of Python3 online submissions for Find Duplicate Subtrees.
    Memory Usage: 24.3 MB, less than 27.68% of Python3 online submissions for Find Duplicate Subtrees.
    """

    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:

        cnt = defaultdict(int)
        res = []

        def traverse(node):
            if not node:
                return ""
            node_str = f"({traverse(node.left)}){node.val}({traverse(node.right)})"
            cnt[node_str] += 1
            if cnt[node_str] == 2:
                res.append(node)
            return node_str

        traverse(root)
        return res


class Solution1:
    """
    leetcode solution 2
    Runtime: 44 ms, faster than 94.31% of Python3 online submissions for Find Duplicate Subtrees.
    Memory Usage: 16.5 MB, less than 86.50% of Python3 online submissions for Find Duplicate Subtrees.
    """

    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:

        triplets = {}
        cnt = defaultdict(int)
        res = []

        def traverse(node):
            if not node:
                return 0
            triplet = (traverse(node.left), node.val, traverse(node.right))
            if triplet not in triplets:
                triplets[triplet] = len(triplets) + 1
            triplet_id = triplets[triplet]
            cnt[triplet_id] += 1
            if cnt[triplet_id] == 2:
                res.append(node)
            return triplet_id

        traverse(root)
        return res
