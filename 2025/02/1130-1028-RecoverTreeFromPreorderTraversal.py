"""
Leetcode
2025-02-22
1028. Recover a Tree From Preorder Traversal
Hard

We run a preorder depth-first search (DFS) on the root of a binary tree.

At each node in this traversal, we output D dashes (where D is the depth of this node), then we output the value of this node.  If the depth of a node is D, the depth of its immediate child is D + 1.  The depth of the root node is 0.

If a node has only one child, that child is guaranteed to be the left child.

Given the output traversal of this traversal, recover the tree and return its root.

 

Example 1:

Input: traversal = "1-2--3--4-5--6--7"
Output: [1,2,5,3,4,6,7]

Example 2:

Input: traversal = "1-2--3---4-5--6---7"
Output: [1,2,5,3,null,6,null,4,null,7]

Example 3:

Input: traversal = "1-401--349---90--88"
Output: [1,401,null,349,88,90]

 

Constraints:

    The number of nodes in the original tree is in the range [1, 1000].
    1 <= Node.val <= 10^9


Hint 1
Do an iterative depth first search, parsing dashes from the string to inform you how to link the nodes together.
"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.val}"


class Solution:
    """
    Runtime 12ms Beats 92.35%
    Memory 18.38MB Beats 56.47%
    """

    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        dummy = TreeNode()
        cur_depth = -1
        stack = [dummy]
        traversal = self.parse_traversal(traversal)
        n = len(traversal)
        idx = 0

        while idx < n and stack:
            cur_node = stack[-1]
            depth, value = traversal[idx]

            if depth <= cur_depth:
                stack.pop()
                cur_depth -= 1
                continue

            if depth == cur_depth + 1:
                if not cur_node.left:
                    cur_node.left = TreeNode(value)
                    stack.append(cur_node.left)
                    idx += 1
                    cur_depth += 1
                    continue
                elif not cur_node.right:
                    cur_node.right = TreeNode(value)
                    stack.append(cur_node.right)
                    idx += 1
                    cur_depth += 1
                    continue
                else:
                    stack.pop()
                    continue

            raise AssertionError('unreachable node depth')

        if idx < n:
            raise AssertionError('traversal not fully replicated')

        return dummy.left

    def parse_traversal(self, traversal: str) -> List[tuple[int, int]]:
        out = []
        cur_depth = 0
        cur_val = 0
        for c in traversal:
            if c == "-":
                if cur_val != 0:
                    out.append((cur_depth, cur_val))
                    cur_val = 0
                    cur_depth = 0
                cur_depth += 1
            else:
                cur_val = cur_val * 10 + int(c)
        if cur_val != 0:
            out.append((cur_depth, cur_val))
        return out


class Solution2:
    """
    leetcode solution 2: Iterative Approach with Stack (Single Pass)
    Runtime 23ms Beats 42.94%
    Memory 18.51MB Beats 18.82%
    """

    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        stack = []
        index = 0

        while index < len(traversal):
            # Count the number of dashes
            depth = 0
            while index < len(traversal) and traversal[index] == "-":
                depth += 1
                index += 1

            # Extract the node value
            value = 0
            while index < len(traversal) and traversal[index].isdigit():
                value = value * 10 + int(traversal[index])
                index += 1

            # Create the current node
            node = TreeNode(value)

            # Adjust the stack to the correct depth
            while len(stack) > depth:
                stack.pop()

            # Attach the node to the parent
            if stack:
                if stack[-1].left is None:
                    stack[-1].left = node
                else:
                    stack[-1].right = node

            # Push the current node onto the stack
            stack.append(node)

        return stack[0]


class Solution3:
    """
    leetcode solution 3: Iterative Approach with List
    Runtime 19ms Beats 64.41%
    Memory 18.38MB Beats 56.47%
    """

    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        levels = []  # List to track the last node at each depth
        index, n = 0, len(traversal)

        while index < n:
            # Count depth (number of dashes)
            depth = 0
            while index < n and traversal[index] == "-":
                depth += 1
                index += 1

            # Extract node value
            value = 0
            while index < n and traversal[index].isdigit():
                value = value * 10 + int(traversal[index])
                index += 1

            # Create the new node
            node = TreeNode(value)

            # Adjust levels list to match the current depth
            if depth < len(levels):
                levels[depth] = node
            else:
                levels.append(node)

            # Attach the node to its parent
            if depth > 0:
                parent = levels[depth - 1]
                if parent.left is None:
                    parent.left = node
                else:
                    parent.right = node

        # The root node is always at index 0
        return levels[0]
