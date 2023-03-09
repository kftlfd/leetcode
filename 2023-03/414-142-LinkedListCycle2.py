"""
Leetcode
142. Linked List Cycle II (medium)
2023-03-09

Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:
Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:
Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    Runtime: 50 ms, faster than 78.17% of Python3 online submissions for Linked List Cycle II.
    Memory Usage: 17.9 MB, less than 21.35% of Python3 online submissions for Linked List Cycle II.
    """

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        seen = set()

        curr = head

        while curr:
            if curr in seen:
                return curr
            seen.add(curr)
            curr = curr.next

        return None


class Solution1:
    """
    https://leetcode.com/problems/linked-list-cycle-ii/discuss/1701128/C++JavaPython-Slow-and-Fast-oror-Image-Explanation-oror-Beginner-Friendly
    Runtime: 54 ms, faster than 57.68% of Python3 online submissions for Linked List Cycle II.
    Memory Usage: 17.4 MB, less than 52.82% of Python3 online submissions for Linked List Cycle II.
    """

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                break
        else:
            return None  # if not (fast and fast.next): return None
        while head != slow:
            head, slow = head.next, slow.next
        return head
