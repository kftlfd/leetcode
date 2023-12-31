"""
Leetcode
111. Minimum Depth of Binary Tree (easy)
2023-07-10

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: 2

Example 2:

Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5

Constraints:

    The number of nodes in the tree is in the range [0, 10^5].
    -1000 <= Node.val <= 1000
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
    Runtime: 497 ms, faster than 87.72% of Python3 online submissions for Minimum Depth of Binary Tree.
    Memory Usage: 50.8 MB, less than 99.30% of Python3 online submissions for Minimum Depth of Binary Tree.
    """

    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        depth = 1
        q = [root]

        while q:
            nxt_q = []
            for _ in range(len(q)):
                node = q.pop(0)
                if not node.left and not node.right:
                    return depth
                if node.left:
                    nxt_q.append(node.left)
                if node.right:
                    nxt_q.append(node.right)
            q = nxt_q
            depth += 1

        return depth


class Solution1:
    """
    leetcode solution: DFS
    Runtime: 620 ms, faster than 27.95% of Python3 online submissions for Minimum Depth of Binary Tree.
    Memory Usage: 57.3 MB, less than 21.03% of Python3 online submissions for Minimum Depth of Binary Tree.
    """

    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        if not root.left:
            return 1 + self.minDepth(root.right)
        if not root.right:
            return 1 + self.minDepth(root.left)

        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
