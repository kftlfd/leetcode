"""
Leetcode
876. Middle of the Linked List
Easy
2024-03-07

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

 

Constraints:

    The number of nodes in the list is in the range [1, 100].
    1 <= Node.val <= 100
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Runtime: 40 ms, faster than 21.44% of Python3 online submissions for Middle of the Linked List.
    Memory Usage: 16.6 MB, less than 46.37% of Python3 online submissions for Middle of the Linked List.
    """

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        while slow and slow.next and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
