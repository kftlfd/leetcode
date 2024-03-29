"""
Leetcode
143. Reorder List
Medium
2024-03-23

You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln

Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

You may not modify the values in the list's nodes. Only nodes themselves may be changed.

 

Example 1:

Input: head = [1,2,3,4]
Output: [1,4,2,3]

Example 2:

Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]

 

Constraints:

    The number of nodes in the list is in the range [1, 5 * 10^4].
    1 <= Node.val <= 1000
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Runtime: 64 ms, faster than 16.06% of Python3 online submissions for Reorder List.
    Memory Usage: 24.5 MB, less than 98.03% of Python3 online submissions for Reorder List.
    """

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        slow = ListNode(0, head)
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second_half = slow.next
        slow.next = None

        part1 = []
        cur = head
        while cur:
            part1.append(cur)
            cur = cur.next

        part2 = []
        cur = self.reverse(second_half)
        while cur:
            part2.append(cur)
            cur = cur.next

        dummy = ListNode()
        cur = dummy
        for n1, n2 in zip(part1, part2):
            cur.next = n1
            n1.next = n2
            cur = n2

    def reverse(self, node: ListNode):
        dummy = ListNode()
        cur = node
        while cur:
            cur_next = cur.next
            cur.next = dummy.next
            dummy.next = cur
            cur = cur_next
        return dummy.next


class Solution1:
    """
    https://leetcode.com/problems/reorder-list/discuss/801883/Python-3-steps-to-success-explained
    Runtime: 52 ms, faster than 76.08% of Python3 online submissions for Reorder List.
    Memory Usage: 24.6 MB, less than 50.88% of Python3 online submissions for Reorder List.
    """

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return

        # step 1: find middle
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # step 2: reverse second half
        prev, curr = None, slow.next
        while curr:
            nextt = curr.next
            curr.next = prev
            prev = curr
            curr = nextt
        slow.next = None

        # step 3: merge lists
        head1, head2 = head, prev
        while head2:
            nextt = head1.next
            head1.next = head2
            head1 = head2
            head2 = nextt
