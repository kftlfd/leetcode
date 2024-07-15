"""
Leetcode
2196. Create Binary Tree From Descriptions
Medium
2024-07-15

You are given a 2D integer array descriptions where descriptions[i] = [parenti, childi, isLefti] indicates that parenti is the parent of childi in a binary tree of unique values. Furthermore,

    If isLefti == 1, then childi is the left child of parenti.
    If isLefti == 0, then childi is the right child of parenti.

Construct the binary tree described by descriptions and return its root.

The test cases will be generated such that the binary tree is valid.

 

Example 1:

Input: descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
Output: [50,20,80,15,17,19]
Explanation: The root node is the node with value 50 since it has no parent.
The resulting binary tree is shown in the diagram.

Example 2:

Input: descriptions = [[1,2,1],[2,3,0],[3,4,1]]
Output: [1,2,null,null,3,4]
Explanation: The root node is the node with value 1 since it has no parent.
The resulting binary tree is shown in the diagram.

 

Constraints:

    1 <= descriptions.length <= 10^4
    descriptions[i].length == 3
    1 <= parent[i], child[i] <= 10^5
    0 <= isLeft[i] <= 1
    The binary tree described by descriptions is valid.
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
    Runtime: 1622 ms, faster than 26.94% of Python3 online submissions for Create Binary Tree From Descriptions.
    Memory Usage: 25.1 MB, less than 98.32% of Python3 online submissions for Create Binary Tree From Descriptions.
    """

    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}

        for parent, child, is_left in descriptions:
            if parent not in nodes:
                nodes[parent] = [TreeNode(parent), False]
            if child not in nodes:
                nodes[child] = [TreeNode(child), True]
            nodes[child][1] = True

            if is_left:
                nodes[parent][0].left = nodes[child][0]
            else:
                nodes[parent][0].right = nodes[child][0]

        ans = None
        for node, is_child in nodes.values():
            if not is_child:
                ans = node
                break

        return ans
