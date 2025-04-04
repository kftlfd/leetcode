"""
Leetcode
2025-04-04
1123. Lowest Common Ancestor of Deepest Leaves
Medium

Given the root of a binary tree, return the lowest common ancestor of its deepest leaves.

Recall that:

    The node of a binary tree is a leaf if and only if it has no children
    The depth of the root of the tree is 0. if the depth of a node is d, the depth of each of its children is d + 1.
    The lowest common ancestor of a set S of nodes, is the node A with the largest depth such that every node in S is in the subtree with root A.

 

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4]
Output: [2,7,4]
Explanation: We return the node with value 2, colored in yellow in the diagram.
The nodes coloured in blue are the deepest leaf-nodes of the tree.
Note that nodes 6, 0, and 8 are also leaf nodes, but the depth of them is 2, but the depth of nodes 7 and 4 is 3.

Example 2:

Input: root = [1]
Output: [1]
Explanation: The root is the deepest node in the tree, and it's the lca of itself.

Example 3:

Input: root = [0,1,3,null,2]
Output: [2]
Explanation: The deepest leaf node in the tree is 2, the lca of one node is itself.

 

Constraints:

    The number of nodes in the tree will be in the range [1, 1000].
    0 <= Node.val <= 1000
    The values of the nodes in the tree are unique.


    
Note: This question is the same as 865: https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/


Hint 1
Do a postorder traversal.
Hint 2
Then, if both subtrees contain a deepest leaf, you can mark this node as the answer (so far).
Hint 3
The final node marked will be the correct answer.
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
    Runtime 0ms Beats 100.00%
    Memory 18.08MB Beats 92.69%
    """

    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        deepest_child = {}

        def dfs(node: TreeNode):
            left = dfs(node.left) if node.left else 0
            right = dfs(node.right) if node.right else 0
            cur = max(left, right) + 1
            deepest_child[node] = cur
            return cur
        dfs(root)

        ans = root
        while True:
            left = deepest_child[ans.left] if ans.left else 0
            right = deepest_child[ans.right] if ans.right else 0
            if left > right:
                ans = ans.left
            elif right > left:
                ans = ans.right
            else:
                break

        return ans


class Solution1:
    """
    leetcode solution: Recursion
    Runtime 4ms Beats 37.41%
    Memory 18.27MB Beats 45.35%
    """

    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root):
            if not root:
                return 0, None

            left = dfs(root.left)
            right = dfs(root.right)

            if left[0] > right[0]:
                return left[0] + 1, left[1]
            if left[0] < right[0]:
                return right[0] + 1, right[1]
            return left[0] + 1, root

        return dfs(root)[1]
