"""
Leetcode
1110. Delete Nodes And Return Forest
Medium
2024-07-17

Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

Return the roots of the trees in the remaining forest. You may return the result in any order.

 

Example 1:

Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output: [[1,2,null,4],[6],[7]]

Example 2:

Input: root = [1,2,4,null,3], to_delete = [3]
Output: [[1,2,4]]

 

Constraints:

    The number of nodes in the given tree is at most 1000.
    Each node has a distinct value between 1 and 1000.
    to_delete.length <= 1000
    to_delete contains distinct values between 1 and 1000.
"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Runtime: 56 ms, faster than 51.04% of Python3 online submissions for Delete Nodes And Return Forest.
    Memory Usage: 17.1 MB, less than 7.26% of Python3 online submissions for Delete Nodes And Return Forest.
    """

    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        ans = []
        to_del = set(to_delete)

        def dfs(node: Optional[TreeNode], is_root: bool) -> bool:
            if not node:
                return False

            should_delete = node.val in to_del

            if not should_delete and is_root:
                ans.append(node)

            if dfs(node.left, should_delete):
                node.left = None
            if dfs(node.right, should_delete):
                node.right = None

            return should_delete

        dfs(root, True)
        return ans


class Solution1:
    """
    Runtime: 49 ms, faster than 87.07% of Python3 online submissions for Delete Nodes And Return Forest.
    Memory Usage: 17.1 MB, less than 24.30% of Python3 online submissions for Delete Nodes And Return Forest.
    """

    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        ans = []
        to_del = [False] * 1001

        for v in to_delete:
            to_del[v] = True

        def dfs(node, is_root):
            if not node:
                return None

            should_delete = to_del[node.val]

            if not should_delete and is_root:
                ans.append(node)

            node.left = dfs(node.left, should_delete)
            node.right = dfs(node.right, should_delete)

            return None if should_delete else node

        dfs(root, True)
        return ans
