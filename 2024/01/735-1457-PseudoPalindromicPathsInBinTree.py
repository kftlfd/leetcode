"""
Leetcode
1457. Pseudo-Palindromic Paths in a Binary Tree
Medium
2024-01-24

Given a binary tree where node values are digits from 1 to 9. A path in the binary tree is said to be pseudo-palindromic if at least one permutation of the node values in the path is a palindrome.

Return the number of pseudo-palindromic paths going from the root node to leaf nodes.

 

Example 1:

Input: root = [2,3,1,3,1,null,1]
Output: 2 
Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the red path [2,3,3], the green path [2,1,1], and the path [2,3,1]. Among these paths only red path and green path are pseudo-palindromic paths since the red path [2,3,3] can be rearranged in [3,2,3] (palindrome) and the green path [2,1,1] can be rearranged in [1,2,1] (palindrome).

Example 2:

Input: root = [2,1,1,1,3,null,null,null,null,null,1]
Output: 1 
Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the green path [2,1,1], the path [2,1,3,1], and the path [2,1]. Among these paths only the green path is pseudo-palindromic since [2,1,1] can be rearranged in [1,2,1] (palindrome).

Example 3:

Input: root = [9]
Output: 1

 

Constraints:

    The number of nodes in the tree is in the range [1, 10^5].
    1 <= Node.val <= 9
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
    Runtime: 385 ms, faster than 92.89% of Python3 online submissions for Pseudo-Palindromic Paths in a Binary Tree.
    Memory Usage: 42.8 MB, less than 99.11% of Python3 online submissions for Pseudo-Palindromic Paths in a Binary Tree.
    """

    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def is_pseudo_palindromic(arr: List[int]) -> bool:
            odd_found = False
            for num in arr:
                if num % 2 == 0:
                    continue
                if odd_found:
                    return False
                odd_found = True
            return True

        def dfs(node: Optional[TreeNode], freqs: List[int]) -> None:
            nonlocal ans

            if not node:
                return

            freqs[node.val - 1] += 1

            if not node.left and not node.right:
                if is_pseudo_palindromic(freqs):
                    ans += 1
            else:
                dfs(node.left, freqs)
                dfs(node.right, freqs)

            freqs[node.val - 1] -= 1
            return

        dfs(root, [0] * 9)
        return ans


class Solution1:
    """
    using bitwise operations (leetcode solution)
    Runtime: 339 ms, faster than 96.89% of Python3 online submissions for Pseudo-Palindromic Paths in a Binary Tree.
    Memory Usage: 43.5 MB, less than 98.67% of Python3 online submissions for Pseudo-Palindromic Paths in a Binary Tree.
    """

    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def is_pseudo_palindromic(path: int) -> bool:
            # path has at most one "1" bit
            return path & (path - 1) == 0

        def dfs(node: Optional[TreeNode], path: int) -> None:
            nonlocal ans

            if not node:
                return

            path = path ^ (1 << node.val)

            if not node.left and not node.right:
                if is_pseudo_palindromic(path):
                    ans += 1
            else:
                dfs(node.left, path)
                dfs(node.right, path)

        dfs(root, 0)
        return ans
