"""
Leetcode
2487. Remove Nodes From Linked List
MediumYou are given the head of a linked list.

Remove every node which has a node with a greater value anywhere to the right side of it.

Return the head of the modified linked list.

 

Example 1:

Input: head = [5,2,13,3,8]
Output: [13,8]
Explanation: The nodes that should be removed are 5, 2 and 3.
- Node 13 is to the right of node 5.
- Node 13 is to the right of node 2.
- Node 8 is to the right of node 3.

Example 2:

Input: head = [1,1,1,1]
Output: [1,1,1,1]
Explanation: Every node has value 1, so no nodes are removed.



Constraints:

    The number of the nodes in the given list is in the range [1, 10^5].
    1 <= Node.val <= 10^5
2024-05-06


"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Runtime: 391 ms, faster than 86.92% of Python3 online submissions for Remove Nodes From Linked List.
    Memory Usage: 61.9 MB, less than 24.00% of Python3 online submissions for Remove Nodes From Linked List.
    """

    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        def get_next(node: ListNode) -> ListNode:
            if not node.next:
                return node

            node.next = get_next(node.next)

            if node.next.val > node.val:
                return node.next
            else:
                return node

        return get_next(head)


class Solution1:
    """
    monotonic stack
    Runtime: 431 ms, faster than 49.57% of Python3 online submissions for Remove Nodes From Linked List.
    Memory Usage: 51.2 MB, less than 70.71% of Python3 online submissions for Remove Nodes From Linked List.
    """

    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []

        cur = head
        while cur:
            while stack and stack[-1].val < cur.val:
                stack.pop()
            stack.append(cur)
            cur = cur.next

        dummy = ListNode()
        cur = dummy
        for node in stack:
            cur.next = node
            cur = cur.next

        return dummy.next


class Solution3:
    """
    leetcode solution 3: Reverse Twice
    Runtime: 452 ms, faster than 38.39% of Python3 online submissions for Remove Nodes From Linked List.
    Memory Usage: 51.3 MB, less than 70.71% of Python3 online submissions for Remove Nodes From Linked List.
    """

    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Reverse the original linked list
        head = self.reverse_list(head)

        maximum = 0
        prev = None
        current = head

        # Traverse the list deleting nodes
        while current:
            maximum = max(maximum, current.val)

            # Delete nodes that are smaller than maximum
            if current.val < maximum:
                # Delete current by skipping
                prev.next = current.next
                deleted = current
                current = current.next
                deleted.next = None

            # Current does not need to be deleted
            else:
                prev = current
                current = current.next

        # Reverse and return the modified linked list
        return self.reverse_list(head)

    def reverse_list(self, head):
        prev = None
        current = head
        next_temp = None

        # Set each node's next pointer to the previous node
        while current:
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp

        return prev
