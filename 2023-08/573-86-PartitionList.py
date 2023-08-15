"""
Leetcode
86. Partition List (medium)
2023-08-15

Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example 1:

Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]

Example 2:

Input: head = [2,1], x = 2
Output: [1,2]

Constraints:

    The number of nodes in the list is in the range [0, 200].
    -100 <= Node.val <= 100
    -200 <= x <= 200
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Runtime: 43 ms, faster than 78.43% of Python3 online submissions for Partition List.
    Memory Usage: 16.3 MB, less than 83.82% of Python3 online submissions for Partition List.
    """

    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return head

        left = []
        right = []

        cur = head
        while cur:
            if cur.val >= x:
                right.append(cur)
            else:
                left.append(cur)
            cur = cur.next

        nodes = left + right
        nodes[-1].next = None
        for i in range(len(nodes) - 1, 0, -1):
            nodes[i-1].next = nodes[i]

        return nodes[0]


class Solution1:
    """
    Runtime: 43 ms, faster than 78.43% of Python3 online submissions for Partition List.
    Memory Usage: 16.2 MB, less than 83.82% of Python3 online submissions for Partition List.
    """

    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return head

        left_head = ListNode()
        right_head = ListNode()

        left_cur = left_head
        right_cur = right_head
        cur = head

        while cur:
            if cur.val >= x:
                right_cur.next = cur
                right_cur = right_cur.next
            else:
                left_cur.next = cur
                left_cur = left_cur.next
            cur = cur.next

        left_cur.next = right_head.next
        right_cur.next = None

        return left_head.next
