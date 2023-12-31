"""
Leetcode
92. Reverse Linked List II (medium)
2023-09-07

Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

Example 1:

Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]

Constraints:

    The number of nodes in the list is n.
    1 <= n <= 500
    -500 <= Node.val <= 500
    1 <= left <= right <= n
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    https://leetcode.com/problems/reverse-linked-list-ii/discuss/1291559/Python-O(1)O(n)-spacetime-solution-explained
    Runtime: 39 ms, faster than 65.70% of Python3 online submissions for Reverse Linked List II.
    Memory Usage: 16.4 MB, less than 91.05% of Python3 online submissions for Reverse Linked List II.
    """

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head

        dummy = ListNode()
        dummy.next = head
        pre = dummy
        for i in range(left - 1):
            pre = pre.next

        cur = pre.next
        nxt = cur.next

        for i in range(right - left):
            tmp = nxt.next
            nxt.next = cur
            cur = nxt
            nxt = tmp

        pre.next.next = nxt
        pre.next = cur

        return dummy.next
