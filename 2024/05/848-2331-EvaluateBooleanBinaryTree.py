"""
Leetcode
2331. Evaluate Boolean Binary Tree
Easy
2024-05-16

You are given the root of a full binary tree with the following properties:

    Leaf nodes have either the value 0 or 1, where 0 represents False and 1 represents True.
    Non-leaf nodes have either the value 2 or 3, where 2 represents the boolean OR and 3 represents the boolean AND.

The evaluation of a node is as follows:

    If the node is a leaf node, the evaluation is the value of the node, i.e. True or False.
    Otherwise, evaluate the node's two children and apply the boolean operation of its value with the children's evaluations.

Return the boolean result of evaluating the root node.

A full binary tree is a binary tree where each node has either 0 or 2 children.

A leaf node is a node that has zero children.

 

Example 1:

Input: root = [2,1,3,null,null,0,1]
Output: true
Explanation: The above diagram illustrates the evaluation process.
The AND node evaluates to False AND True = False.
The OR node evaluates to True OR False = True.
The root node evaluates to True, so we return true.

Example 2:

Input: root = [0]
Output: false
Explanation: The root node is a leaf node and it evaluates to false, so we return false.

 

Constraints:

    The number of nodes in the tree is in the range [1, 1000].
    0 <= Node.val <= 3
    Every node has either 0 or 2 children.
    Leaf nodes have a value of 0 or 1.
    Non-leaf nodes have a value of 2 or 3.
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
    Runtime: 56 ms, faster than 8.10% of Python3 online submissions for Evaluate Boolean Binary Tree.
    Memory Usage: 16.8 MB, less than 92.02% of Python3 online submissions for Evaluate Boolean Binary Tree.
    """

    def evaluateTree(self, root: Optional[TreeNode]) -> bool:

        def dfs(node: TreeNode) -> bool:
            if not node.left:
                # is leaf
                return node.val == 1

            l = dfs(node.left)
            r = dfs(node.right)

            if node.val == 2:
                return l or r

            return l and r

        return dfs(root)


class Solution1:
    """
    Runtime: 43 ms, faster than 81.84% of Python3 online submissions for Evaluate Boolean Binary Tree.
    Memory Usage: 16.9 MB, less than 49.94% of Python3 online submissions for Evaluate Boolean Binary Tree.
    """

    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if not root.left:
            return root.val == 1

        l = self.evaluateTree(root.left)
        r = self.evaluateTree(root.right)

        return l or r if root.val == 2 else l and r


class Solution2:
    """
    leetcode solution 2: Iterative approach (Depth First Search)
    Runtime: 51 ms, faster than 29.57% of Python3 online submissions for Evaluate Boolean Binary Tree.
Memory Usage: 16.9 MB, less than 11.53% of Python3 online submissions for Evaluate Boolean Binary Tree.
    """

    def evaluateTree(self, root: Optional[TreeNode]) -> bool:

        stack = [root]
        evaluated = {}

        while stack:
            top_node = stack[-1]

            # If the node is a leaf node, store its value in the evaluated dictionary
            # and continue
            if not top_node.left and not top_node.right:
                stack.pop()
                evaluated[top_node] = top_node.val == 1
                continue

            # If both the children have already been evaluated, use their
            # values to evaluate the current node.
            if top_node.left in evaluated and top_node.right in evaluated:
                stack.pop()
                if top_node.val == 2:
                    evaluated[top_node] = evaluated[top_node.left] or evaluated[top_node.right]
                else:
                    evaluated[top_node] = evaluated[top_node.left] and evaluated[top_node.right]
            else:
                # If both the children are not leaf nodes, push the current
                # node along with its left and right child back into the stack.
                if top_node.left:
                    stack.append(top_node.left)
                if top_node.right:
                    stack.append(top_node.right)

        return evaluated[root]
