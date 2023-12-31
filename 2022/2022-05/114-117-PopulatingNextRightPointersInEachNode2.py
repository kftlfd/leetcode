"""
Leetcode
117. Populating Next Right Pointers in Each Node II (medium)
2022-05-13

Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""



# try 1
# Runtime: 91 ms, faster than 17.19% of Python3 online submissions for Populating Next Right Pointers in Each Node II.
# Memory Usage: 15.4 MB, less than 48.93% of Python3 online submissions for Populating Next Right Pointers in Each Node II.
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        curr = root
        q1 = [curr]
        q2 = []
        while q1:
            for _ in range(len(q1)):
                node = q1.pop(0)
                if not node: continue
                node.next = q1[0] if q1 else None
                if node.left: q2.append(node.left)
                if node.right: q2.append(node.right)
            q1, q2 = q2, q1
        
        return root



# s = Solution()
# tests = []
# for t in tests:
#     print(t)
#     print()
#     print()
