"""
Leetcode
623. Add One Row to Tree
Medium
2024-04-16

Given the root of a binary tree and two integers val and depth, add a row of nodes with value val at the given depth depth.

Note that the root node is at depth 1.

The adding rule is:

    Given the integer depth, for each not null tree node cur at the depth depth - 1, create two tree nodes with value val as cur's left subtree root and right subtree root.
    cur's original left subtree should be the left subtree of the new left subtree root.
    cur's original right subtree should be the right subtree of the new right subtree root.
    If depth == 1 that means there is no depth depth - 1 at all, then create a tree node with value val as the new root of the whole original tree, and the original tree is the new root's left subtree.

 

Example 1:

Input: root = [4,2,6,3,1,5], val = 1, depth = 2
Output: [4,1,1,2,null,null,6,3,1,5]

Example 2:

Input: root = [4,2,null,3,1], val = 1, depth = 3
Output: [4,2,null,1,1,3,null,null,1]

 

Constraints:

    The number of nodes in the tree is in the range [1, 10^4].
    The depth of the tree is in the range [1, 10^4].
    -100 <= Node.val <= 100
    -10^5 <= val <= 10^5
    1 <= depth <= the depth of tree + 1
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    bfs
    Runtime: 46 ms, faster than 61.00% of Python3 online submissions for Add One Row to Tree.
    Memory Usage: 17.8 MB, less than 32.50% of Python3 online submissions for Add One Row to Tree.
    """

    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root)

        cur_depth = 1
        q = [root]

        while cur_depth < depth:
            if cur_depth == depth - 1:
                for node in q:
                    l_node = TreeNode(val, node.left)
                    node.left = l_node

                    r_node = TreeNode(val, None, node.right)
                    node.right = r_node
                break

            nxt_q = []
            for node in q:
                if node.left:
                    nxt_q.append(node.left)
                if node.right:
                    nxt_q.append(node.right)
            q = nxt_q
            cur_depth += 1

        return root


class Solution1:
    """
    dfs
    Runtime: 50 ms, faster than 32.75% of Python3 online submissions for Add One Row to Tree.
    Memory Usage: 17.7 MB, less than 97.00% of Python3 online submissions for Add One Row to Tree.
    """

    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root)

        def dfs(node, cur_depth):
            if not node:
                return
            if cur_depth == depth - 1:
                node.left = TreeNode(val, node.left)
                node.right = TreeNode(val, None, node.right)
                return
            dfs(node.left, cur_depth + 1)
            dfs(node.right, cur_depth + 1)

        dfs(root, 1)
        return root
