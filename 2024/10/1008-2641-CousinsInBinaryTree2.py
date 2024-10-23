"""
Leetcode
2024-10-23
2641. Cousins in Binary Tree II
Medium

Given the root of a binary tree, replace the value of each node in the tree with the sum of all its cousins' values.

Two nodes of a binary tree are cousins if they have the same depth with different parents.

Return the root of the modified tree.

Note that the depth of a node is the number of edges in the path from the root node to it.

 

Example 1:

Input: root = [5,4,9,1,10,null,7]
Output: [0,0,0,7,7,null,11]
Explanation: The diagram above shows the initial binary tree and the binary tree after changing the value of each node.
- Node with value 5 does not have any cousins so its sum is 0.
- Node with value 4 does not have any cousins so its sum is 0.
- Node with value 9 does not have any cousins so its sum is 0.
- Node with value 1 has a cousin with value 7 so its sum is 7.
- Node with value 10 has a cousin with value 7 so its sum is 7.
- Node with value 7 has cousins with values 1 and 10 so its sum is 11.

Example 2:

Input: root = [3,1,2]
Output: [0,0,0]
Explanation: The diagram above shows the initial binary tree and the binary tree after changing the value of each node.
- Node with value 3 does not have any cousins so its sum is 0.
- Node with value 1 does not have any cousins so its sum is 0.
- Node with value 2 does not have any cousins so its sum is 0.

 

Constraints:

    The number of nodes in the tree is in the range [1, 10^5].
    1 <= Node.val <= 10^4
"""

from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Runtime: 166 ms, faster than 95.80% of Python3 online submissions for Cousins in Binary Tree II.
    Memory Usage: 57.3 MB, less than 83.57% of Python3 online submissions for Cousins in Binary Tree II.
    """

    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        q = deque([(root, root.val)])

        while q:
            level_sum = sum(qval[0].val for qval in q)
            nxt_q = deque()

            for node, siblings_sum in q:
                node.val = level_sum - siblings_sum
                children_sum = (node.left.val if node.left else 0) + \
                    (node.right.val if node.right else 0)
                if node.left:
                    nxt_q.append((node.left, children_sum))
                if node.right:
                    nxt_q.append((node.right, children_sum))

            q = nxt_q

        return root


class Solution3:
    """
    leetcode solution 3: Single BFS with Running Sum (modified)
    Runtime: 97 ms, faster than 98.95% of Python3 online submissions for Cousins in Binary Tree II.
    Memory Usage: 57.2 MB, less than 83.57% of Python3 online submissions for Cousins in Binary Tree II.
    """

    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        q = deque([root])
        cur_level_sum = root.val

        while q:
            nxt_level_sum = 0

            for _ in range(len(q)):
                node = q.popleft()
                node.val = cur_level_sum - node.val

                children_sum = (node.left.val if node.left else 0) + \
                    (node.right.val if node.right else 0)
                if node.left:
                    node.left.val = children_sum
                    q.append(node.left)
                if node.right:
                    node.right.val = children_sum
                    q.append(node.right)
                nxt_level_sum += children_sum

            cur_level_sum = nxt_level_sum

        return root
