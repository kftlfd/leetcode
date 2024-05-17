"""
Leetcode
1325. Delete Leaves With a Given Value
Medium
2024-05-17

Given a binary tree root and an integer target, delete all the leaf nodes with value target.

Note that once you delete a leaf node with value target, if its parent node becomes a leaf node and has the value target, it should also be deleted (you need to continue doing that until you cannot).

 

Example 1:

Input: root = [1,2,3,2,null,2,4], target = 2
Output: [1,null,3,null,4]
Explanation: Leaf nodes in green with value (target = 2) are removed (Picture in left). 
After removing, new nodes become leaf nodes with value (target = 2) (Picture in center).

Example 2:

Input: root = [1,3,3,3,2], target = 3
Output: [1,3,null,null,2]

Example 3:

Input: root = [1,2,null,2,null,2], target = 2
Output: [1]
Explanation: Leaf nodes in green with value (target = 2) are removed at each step.

 

Constraints:

    The number of nodes in the tree is in the range [1, 3000].
    1 <= Node.val, target <= 1000
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
    Runtime: 48 ms, faster than 40.20% of Python3 online submissions for Delete Leaves With a Given Value.
    Memory Usage: 17.1 MB, less than 80.39% of Python3 online submissions for Delete Leaves With a Given Value.
    """

    LEFT = 0
    RIGHT = 1

    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if not root:
            return root

        dummy = TreeNode(target-1, root)
        self.remove(root, dummy, self.LEFT, target)
        return dummy.left

    def remove(self, node: TreeNode, parent: TreeNode, side: int, target: int):
        if node.left:
            self.remove(node.left, node, self.LEFT, target)
        if node.right:
            self.remove(node.right, node, self.RIGHT, target)

        if not node.left and not node.right and node.val == target:
            if side == self.LEFT:
                parent.left = None
            else:
                parent.right = None


class Solution1:
    """
    leetcode solution 1: Recursion (Postorder Traversal)
    Runtime: 37 ms, faster than 95.42% of Python3 online submissions for Delete Leaves With a Given Value.
    Memory Usage: 17.1 MB, less than 28.92% of Python3 online submissions for Delete Leaves With a Given Value.
    """

    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        # Base case
        if root is None:
            return None

        # 1. Visit the left children
        root.left = self.removeLeafNodes(root.left, target)

        # 2. Visit the right children
        root.right = self.removeLeafNodes(root.right, target)

        # 3. Check if the current node is a leaf node and its value equals target
        if root.left is None and root.right is None and root.val == target:
            # Delete the node by returning None to the parent, effectively disconnecting it
            return None

        # Keep it untouched otherwise
        return root


class Solution2:
    """
    leetcode solution 2: Iterative (PostOrder Traversal)
    Runtime: 36 ms, faster than 96.73% of Python3 online submissions for Delete Leaves With a Given Value.
    Memory Usage: 17.1 MB, less than 28.92% of Python3 online submissions for Delete Leaves With a Given Value.
    """

    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if not root:
            return None

        stack = []
        current_node = root
        last_right_node = None

        while stack or current_node:
            # Push left nodes to the stack until reaching the leftmost node.
            while current_node:
                stack.append(current_node)
                current_node = current_node.left

            # Access the top node on the stack without removing it.
            # This node is the current candidate for processing.
            current_node = stack[-1]

            # Check if the current node has an unexplored right subtree.
            # If so, shift to the right subtree unless it's the subtree we just visited.
            if current_node.right and current_node.right is not last_right_node:
                current_node = current_node.right
                # Continue in the while loop to push this new subtree's leftmost nodes.
                continue

            # Remove the node from the stack, since we're about to process it.
            stack.pop()

            # If the node has no right subtree or the right subtree has already been visited,
            # then check if it is a leaf node with the target value.
            if not current_node.right and not current_node.left and current_node.val == target:
                # If the stack is empty after popping, it means the root was a target leaf node.
                if not stack:
                    # The tree becomes empty as the root itself is removed.
                    return None

                # Identify the parent of the current node.
                parent = stack[-1] if stack else None

                # Disconnect the current node from its parent.
                if parent and parent.left is current_node:
                    # If current is a left child, set the left pointer to null.
                    parent.left = None
                elif parent and parent.right is current_node:
                    # If current is a right child, set the right pointer to null.
                    parent.right = None

            # Mark this node as visited by setting 'last_right_node' to 'current_node' before moving to the next iteration.
            last_right_node = current_node
            # Reset 'current_node' to None to ensure the next node from the stack is processed.
            current_node = None

        return root  # Return the modified tree
