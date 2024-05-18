"""
Leetcode
979. Distribute Coins in Binary Tree
Medium
2024-05-18

You are given the root of a binary tree with n nodes where each node in the tree has node.val coins. There are n coins in total throughout the whole tree.

In one move, we may choose two adjacent nodes and move one coin from one node to another. A move may be from parent to child, or from child to parent.

Return the minimum number of moves required to make every node have exactly one coin.

 

Example 1:

Input: root = [3,0,0]
Output: 2
Explanation: From the root of the tree, we move one coin to its left child, and one coin to its right child.

Example 2:

Input: root = [0,3,0]
Output: 3
Explanation: From the left child of the root, we move two coins to the root [taking two moves]. Then, we move one coin from the root of the tree to the right child.

 

Constraints:

    The number of nodes in the tree is n.
    1 <= n <= 100
    0 <= Node.val <= n
    The sum of all Node.val is n.
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
    Runtime: 34 ms, faster than 79.96% of Python3 online submissions for Distribute Coins in Binary Tree.
    Memory Usage: 16.5 MB, less than 38.65% of Python3 online submissions for Distribute Coins in Binary Tree.
    """

    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        moves = [0]

        def dfs(node: TreeNode) -> tuple[int, int]:
            balance = node.val

            if node.left:
                l_take, l_give = dfs(node.left)
                balance += l_give - l_take

            if node.right:
                r_take, r_give = dfs(node.right)
                balance += r_give - r_take

            take = max(0, 1 - balance)
            give = max(0, balance - 1)

            moves[0] += take + give
            return (take, give)

        dfs(root)

        return moves[0]


class Solution1:
    """
    leetcode solution
    Runtime: 44 ms, faster than 20.45% of Python3 online submissions for Distribute Coins in Binary Tree.
    Memory Usage: 16.6 MB, less than 38.65% of Python3 online submissions for Distribute Coins in Binary Tree.
    """

    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.moves = 0

        def dfs(current):
            if current is None:
                return 0

            # Calculate the coins each subtree has available to exchange
            left_coins = dfs(current.left)
            right_coins = dfs(current.right)

            # Add the total number of exchanges to moves
            self.moves += abs(left_coins) + abs(right_coins)

            # The number of coins current has available to exchange
            return (current.val - 1) + left_coins + right_coins

        dfs(root)

        return self.moves
