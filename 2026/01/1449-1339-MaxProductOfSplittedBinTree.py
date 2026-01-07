"""
Leetcode
2026-01-07
1339. Maximum Product of Splitted Binary Tree
Medium

Given the root of a binary tree, split the binary tree into two subtrees by removing one edge such that the product of the sums of the subtrees is maximized.

Return the maximum product of the sums of the two subtrees. Since the answer may be too large, return it modulo 109 + 7.

Note that you need to maximize the answer before taking the mod and not after taking it.

 

Example 1:

Input: root = [1,2,3,4,5,6]
Output: 110
Explanation: Remove the red edge and get 2 binary trees with sum 11 and 10. Their product is 110 (11*10)

Example 2:

Input: root = [1,null,2,3,4,null,null,5,6]
Output: 90
Explanation: Remove the red edge and get 2 binary trees with sum 15 and 6.Their product is 90 (15*6)

 

Constraints:

    The number of nodes in the tree is in the range [2, 5 * 10^4].
    1 <= Node.val <= 10^4


Hint 1
If we know the sum of a subtree, the answer is max( (total_sum - subtree_sum) * subtree_sum) in each node.
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
    Runtime 72ms Beats 45.63%
    Memory 46.15MB Beats 5.32%
    """

    def maxProduct(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def dfs_sum(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            return node.val + dfs_sum(node.left) + dfs_sum(node.right)

        total_sum = dfs_sum(root)
        ans = 0

        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal ans
            if not node:
                return 0
            subtree_sum = node.val + dfs(node.left) + dfs(node.right)
            ans = max(ans, (total_sum - subtree_sum) * subtree_sum)
            return subtree_sum

        dfs(root)
        return ans % (10**9 + 7)


class Solution1:
    """
    sample 28ms solution
    Runtime 31ms Beats 98.48%
    Memory 45.93MB Beats 5.32%
    """

    def maxProduct(self, root: Optional[TreeNode]) -> int:
        return self.get_max_product(root)

    def get_subtree_sum(self, node: Optional[TreeNode], subtree_sums: list):
        if node is None:
            return 0

        total_sum = node.val

        total_sum += self.get_subtree_sum(node.left, subtree_sums)

        total_sum += self.get_subtree_sum(node.right, subtree_sums)

        subtree_sums.append(total_sum)

        return total_sum

    def get_max_product(self, node: Optional[TreeNode]):
        subtree_sums = list()

        total_sum = self.get_subtree_sum(node, subtree_sums)

        max_product = 0

        for s in subtree_sums:
            product = s * (total_sum - s)

            if product > max_product:
                max_product = product

        return max_product % (10**9 + 7)
