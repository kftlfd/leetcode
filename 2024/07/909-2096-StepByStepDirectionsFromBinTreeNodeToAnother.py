"""
Leetcode
2096. Step-By-Step Directions From a Binary Tree Node to Another
Medium
2024-07-16

You are given the root of a binary tree with n nodes. Each node is uniquely assigned a value from 1 to n. You are also given an integer startValue representing the value of the start node s, and a different integer destValue representing the value of the destination node t.

Find the shortest path starting from node s and ending at node t. Generate step-by-step directions of such path as a string consisting of only the uppercase letters 'L', 'R', and 'U'. Each letter indicates a specific direction:

    'L' means to go from a node to its left child node.
    'R' means to go from a node to its right child node.
    'U' means to go from a node to its parent node.

Return the step-by-step directions of the shortest path from node s to node t.

 

Example 1:

Input: root = [5,1,2,3,null,6,4], startValue = 3, destValue = 6
Output: "UURL"
Explanation: The shortest path is: 3 → 1 → 5 → 2 → 6.

Example 2:

Input: root = [2,1], startValue = 2, destValue = 1
Output: "L"
Explanation: The shortest path is: 2 → 1.

 

Constraints:

    The number of nodes in the tree is n.
    2 <= n <= 10^5
    1 <= Node.val <= n
    All the values in the tree are unique.
    1 <= startValue, destValue <= n
    startValue != destValue

Hints:
- The shortest path between any two nodes in a tree must pass through their Lowest Common Ancestor (LCA). The path will travel upwards from node s to the LCA and then downwards from the LCA to node t.
- Find the path strings from root → s, and root → t. Can you use these two strings to prepare the final answer?
- Remove the longest common prefix of the two path strings to get the path LCA → s, and LCA → t. Each step in the path of LCA → s should be reversed as 'U'.
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
    Runtime: 270 ms, faster than 65.27% of Python3 online submissions for Step-By-Step Directions From a Binary Tree Node to Another.
    Memory Usage: 51.3 MB, less than 72.48% of Python3 online submissions for Step-By-Step Directions From a Binary Tree Node to Another.
    """

    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        if not root:
            return ""

        def build_path(node: TreeNode, search_val: int, path: List[str]):
            if node.val == search_val:
                return True
            if node.left:
                path.append("L")
                if build_path(node.left, search_val, path):
                    return True
                path.pop()
            if node.right:
                path.append("R")
                if build_path(node.right, search_val, path):
                    return True
                path.pop()
            return False

        def get_path(val: int):
            path = []
            build_path(root, val, path)
            return path

        s_path = get_path(startValue)
        d_path = get_path(destValue)

        while s_path and d_path and s_path[0] == d_path[0]:
            s_path.pop(0)
            d_path.pop(0)

        return ("U" * len(s_path)) + "".join(d_path)
