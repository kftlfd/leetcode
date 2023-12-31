"""
Leetcode
876. Middle of the Linked List (easy)
2022-12-05

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Example 1:
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Example 2:
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import List, Optional


# Runtime: 36 ms, faster than 85.77% of Python3 online submissions for Middle of the Linked List.
# Memory Usage: 13.8 MB, less than 55.96% of Python3 online submissions for Middle of the Linked List.
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return head

        slow = head
        fast = head

        while fast.next:
            slow = slow.next
            fast = fast.next
            if fast.next:
                fast = fast.next

        return slow
