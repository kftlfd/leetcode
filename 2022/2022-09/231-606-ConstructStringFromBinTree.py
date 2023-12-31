"""
Leetcode
606. Construct String from Binary Tree (easy)
2022-09-07

Given the root of a binary tree, construct a string consisting of parenthesis and integers from a binary tree with the preorder traversal way, and return it.

Omit all the empty parenthesis pairs that do not affect the one-to-one mapping relationship between the string and the original binary tree.

Example 1:
Input: root = [1,2,3,4]
Output: "1(2(4))(3)"
Explanation: Originally, it needs to be "1(2(4)())(3()())", but you need to omit all the unnecessary empty parenthesis pairs. And it will be "1(2(4))(3)"

Example 2:
Input: root = [1,2,3,null,4]
Output: "1(2()(4))(3)"
Explanation: Almost the same as the first example, except we cannot omit the first parenthesis pair to break the one-to-one mapping relationship between the input and the output.
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# leetcode solution 1 - recursion
# Runtime: 122 ms, faster than 12.10% of Python3 online submissions for Construct String from Binary Tree.
# Memory Usage: 16.2 MB, less than 95.12% of Python3 online submissions for Construct String from Binary Tree.
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:

        if not root:
            return ""

        if not root.left and not root.right:
            return str(root.val) + ""

        if not root.right:
            return str(root.val) + "(" + self.tree2str(root.left) + ")"

        return str(root.val) + "(" + self.tree2str(root.left) + ")(" + self.tree2str(root.right) + ")"


# leetcode solution 2 - stack
# Runtime: 87 ms, faster than 44.65% of Python3 online submissions for Construct String from Binary Tree.
# Memory Usage: 16.2 MB, less than 96.90% of Python3 online submissions for Construct String from Binary Tree.
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:

        if not root:
            return ""

        stack = [root]
        visited = set()
        s = []

        while stack:
            node = stack[-1]
            if node in visited:
                stack.pop()
                s.append(")")
            else:
                visited.add(node)
                s.append("(" + str(node.val))
                if not node.left and node.right:
                    s.append("()")
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)

        return ("".join(s))[1:-1]


# s = Solution()
# tests = []
# for t in tests:
#     print(t)
#     print()
#     print()
