"""
Leetcode
2024-09-07
1367. Linked List in Binary Tree
Medium

Given a binary tree root and a linked list with head as the first node. 

Return True if all the elements in the linked list starting from the head correspond to some downward path connected in the binary tree otherwise return False.

In this context downward path means a path that starts at some node and goes downwards.

 

Example 1:

Input: head = [4,2,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output: true
Explanation: Nodes in blue form a subpath in the binary Tree.  

Example 2:

Input: head = [1,4,2,6], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output: true

Example 3:

Input: head = [1,4,2,6,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output: false
Explanation: There is no path in the binary tree that contains all the elements of the linked list from head.

 

Constraints:

    The number of nodes in the tree will be in the range [1, 2500].
    The number of nodes in the list will be in the range [1, 100].
    1 <= Node.val <= 100 for each node in the linked list and binary tree.


Hints:
- Create recursive function, given a pointer in a Linked List and any node in the Binary Tree. Check if all the elements in the linked list starting from the head correspond to some downward path in the binary tree.    
"""

from collections import deque
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution01:
    """
    Runtime: 62 ms, faster than 78.59% of Python3 online submissions for Linked List in Binary Tree.
    Memory Usage: 17.3 MB, less than 63.38% of Python3 online submissions for Linked List in Binary Tree.
    """

    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not head:
            return True
        if not root:
            return False
        return self.checkSubPath(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)

    def checkSubPath(self, list_node: Optional[ListNode], tree_node: Optional[TreeNode]) -> bool:
        if not list_node:
            return True
        if not tree_node or tree_node.val != list_node.val:
            return False
        return self.checkSubPath(list_node.next, tree_node.left) or self.checkSubPath(list_node.next, tree_node.right)


class Solution02:
    """
    Runtime: 63 ms, faster than 75.71% of Python3 online submissions for Linked List in Binary Tree.
    Memory Usage: 17.3 MB, less than 64.08% of Python3 online submissions for Linked List in Binary Tree.
    """

    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not head:
            return True
        if not root:
            return False

        def check_node(node: TreeNode) -> bool:
            is_sub_path = False
            q = deque([(head, node)])
            while q:
                cur_l, cur_t = q.popleft()
                if cur_l.val != cur_t.val:
                    continue
                if not cur_l.next:
                    is_sub_path = True
                    break
                if cur_t.left:
                    q.append((cur_l.next, cur_t.left))
                if cur_t.right:
                    q.append((cur_l.next, cur_t.right))
            return is_sub_path

        ans = False
        q = deque([root])
        while q:
            cur = q.popleft()
            if check_node(cur):
                ans = True
                break
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)

        return ans


class Solution3:
    """
    leetcode solution 3: Knuth-Morris-Pratt (KMP) Algorithm
    Runtime: 63 ms, faster than 75.71% of Python3 online submissions for Linked List in Binary Tree.
    Memory Usage: 17.2 MB, less than 64.08% of Python3 online submissions for Linked List in Binary Tree.
    """

    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        # Build the pattern and prefix table from the linked list
        pattern = [head.val]
        prefix_table = [0]
        pattern_index = 0
        head = head.next

        while head:
            while pattern_index > 0 and head.val != pattern[pattern_index]:
                pattern_index = prefix_table[pattern_index - 1]
            pattern_index += 1 if head.val == pattern[pattern_index] else 0
            pattern.append(head.val)
            prefix_table.append(pattern_index)
            head = head.next

        # Perform DFS to search for the pattern in the tree
        return self._search_in_tree(root, 0, pattern, prefix_table)

    def _search_in_tree(
        self,
        node: Optional[TreeNode],
        pattern_index: int,
        pattern: List[int],
        prefix_table: List[int],
    ) -> bool:
        if not node:
            return False

        while pattern_index > 0 and node.val != pattern[pattern_index]:
            pattern_index = prefix_table[pattern_index - 1]
        pattern_index += 1 if node.val == pattern[pattern_index] else 0

        # Check if the pattern is fully matched
        if pattern_index == len(pattern):
            return True

        # Recursively search left and right subtrees
        return self._search_in_tree(
            node.left, pattern_index, pattern, prefix_table
        ) or self._search_in_tree(
            node.right, pattern_index, pattern, prefix_table
        )
