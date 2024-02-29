"""
Leetcode
1609. Even Odd Tree
Medium
2024-02-29

A binary tree is named Even-Odd if it meets the following conditions:

    The root of the binary tree is at level index 0, its children are at level index 1, their children are at level index 2, etc.
    For every even-indexed level, all nodes at the level have odd integer values in strictly increasing order (from left to right).
    For every odd-indexed level, all nodes at the level have even integer values in strictly decreasing order (from left to right).

Given the root of a binary tree, return true if the binary tree is Even-Odd, otherwise return false.

 

Example 1:

Input: root = [1,10,4,3,null,7,9,12,8,6,null,null,2]
Output: true
Explanation: The node values on each level are:
Level 0: [1]
Level 1: [10,4]
Level 2: [3,7,9]
Level 3: [12,8,6,2]
Since levels 0 and 2 are all odd and increasing and levels 1 and 3 are all even and decreasing, the tree is Even-Odd.

Example 2:

Input: root = [5,4,2,3,3,7]
Output: false
Explanation: The node values on each level are:
Level 0: [5]
Level 1: [4,2]
Level 2: [3,3,7]
Node values in level 2 must be in strictly increasing order, so the tree is not Even-Odd.

Example 3:

Input: root = [5,9,1,3,5,7]
Output: false
Explanation: Node values in the level 1 should be even integers.

 

Constraints:

    The number of nodes in the tree is in the range [1, 105].
    1 <= Node.val <= 106
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
    Runtime: 195 ms, faster than 98.77% of Python3 online submissions for Even Odd Tree.
    Memory Usage: 37.6 MB, less than 82.92% of Python3 online submissions for Even Odd Tree.
    """

    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        EVEN = 0
        ODD = 1

        q = [root]
        turn = ODD

        while q:
            nxt_q = []
            prev_val = None

            for node in q:
                if prev_val is None:
                    prev_val = node.val + (1 if turn == EVEN else -1)

                if node.val % 2 != turn or (node.val <= prev_val if turn == ODD else node.val >= prev_val):
                    return False

                prev_val = node.val
                if node.left:
                    nxt_q.append(node.left)
                if node.right:
                    nxt_q.append(node.right)

            q = nxt_q
            turn = (turn + 1) % 2

        return True


class Solution1:
    """
    leetcode solution 1: DFS (preorder traversal)
    Runtime: 233 ms, faster than 53.29% of Python3 online submissions for Even Odd Tree.
    Memory Usage: 51.3 MB, less than 14.40% of Python3 online submissions for Even Odd Tree.
    """

    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        prev = []

        def dfs(current: TreeNode, level: int) -> bool:
            # Base case, an empty tree is Even-Odd
            if current is None:
                return True

            # Compare the parity of current and level
            if current.val % 2 == level % 2:
                return False

            # Add a new level to prev if we've reached a new level
            while (len(prev) <= level):
                prev.append(0)

            # If there are previous nodes on this level, check increasing/decreasing
            # If on an even level, check that current's value is greater than the previous on this level
            # If on an odd level, check that current's value is less than the previous on this level
            if prev[level] != 0 and \
                    ((level % 2 == 0 and current.val <= prev[level]) or
                     (level % 2 == 1 and current.val >= prev[level])):
                return False

            # Add current value to prev at index level
            prev[level] = current.val

            # Recursively call DFS on the left and right children
            return dfs(current.left, level + 1) and dfs(current.right, level + 1)

        return dfs(root, 0)
