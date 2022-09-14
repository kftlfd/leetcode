"""
Leetcode
1457. Pseudo-Palindromic Paths in a Binary Tree (medium)
2022-09-14

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
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Runtime: 2683 ms, faster than 5.30% of Python3 online submissions for Pseudo-Palindromic Paths in a Binary Tree.
# Memory Usage: 104.9 MB, less than 8.10% of Python3 online submissions for Pseudo-Palindromic Paths in a Binary Tree.
class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:

        if not root:
            return None

        def dfs(node, freq={}):
            if not node:
                return 0
            freq[node.val] = freq.get(node.val, 0) + 1
            if not node.left and not node.right:
                return 1 if len([x for x in freq.values() if x % 2 == 1]) <= 1 else 0
            else:
                return dfs(node.left, {**freq}) + dfs(node.right, {**freq})

        return dfs(root)


# leetcode solution - Approach 1: Iterative Preorder Traversal.
# Runtime: 1738 ms, faster than 22.43% of Python3 online submissions for Pseudo-Palindromic Paths in a Binary Tree.
# Memory Usage: 50.2 MB, less than 98.44% of Python3 online submissions for Pseudo-Palindromic Paths in a Binary Tree.
class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:

        count = 0
        stack = [(root, 0)]

        while stack:
            node, path = stack.pop()
            if node:
                # compute occurences of each digit
                # in the corresponding register
                path ^= 1 << node.val
                # if it's a leaf, check if the path is pseudo-palindromic
                if not node.left and not node.right:
                    # check if at most one digit has an odd frequency
                    if path & (path - 1) == 0:
                        count += 1
                else:
                    stack.append((node.right, path))
                    stack.append((node.left, path))

        return count


# leetcode solution - Approach 2: Recursive Preorder Traversal.
# Runtime: 1925 ms, faster than 13.09% of Python3 online submissions for Pseudo-Palindromic Paths in a Binary Tree.
# Memory Usage: 85.6 MB, less than 52.96% of Python3 online submissions for Pseudo-Palindromic Paths in a Binary Tree.
class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:

        def preorder(node, path):
            nonlocal count
            if node:
                # compute occurences of each digit
                # in the corresponding register
                path ^= (1 << node.val)
                # if it's a leaf, check if the path is pseudo-palindromic
                if not node.left and not node.right:
                    # check if at most one digit has an odd frequency
                    if path & (path - 1) == 0:
                        count += 1
                else:
                    preorder(node.left, path)
                    preorder(node.right, path)

        count = 0
        preorder(root, 0)
        return count


# s = Solution()
# tests = []
# for t in tests:
#     print(t)
#     print()
#     print()
