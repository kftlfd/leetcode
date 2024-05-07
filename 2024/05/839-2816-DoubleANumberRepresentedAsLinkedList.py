"""
Leetcode
2816. Double a Number Represented as a Linked List
Medium
2024-05-07

You are given the head of a non-empty linked list representing a non-negative integer without leading zeroes.

Return the head of the linked list after doubling it.

 

Example 1:

Input: head = [1,8,9]
Output: [3,7,8]
Explanation: The figure above corresponds to the given linked list which represents the number 189. Hence, the returned linked list represents the number 189 * 2 = 378.

Example 2:

Input: head = [9,9,9]
Output: [1,9,9,8]
Explanation: The figure above corresponds to the given linked list which represents the number 999. Hence, the returned linked list reprersents the number 999 * 2 = 1998. 

 

Constraints:

    The number of nodes in the list is in the range [1, 10^4]
    0 <= Node.val <= 9
    The input is generated such that the list represents a number that does not have leading zeros, except the number 0 itself.
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Runtime: 245 ms, faster than 55.87% of Python3 online submissions for Double a Number Represented as a Linked List.
    Memory Usage: 20.7 MB, less than 8.14% of Python3 online submissions for Double a Number Represented as a Linked List.
    """

    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        def dfs(node: ListNode, is_root: bool) -> int:
            carry = 0

            if node.next:
                carry = dfs(node.next, False)

            doubled = node.val * 2 + carry

            node.val = doubled % 10

            carry = doubled // 10

            if is_root and carry > 0:
                new_node = ListNode(node.val, node.next)
                node.val = carry
                node.next = new_node
                return 0

            return carry

        dfs(head, True)

        return head


class Solution5:
    """
    leetcode solution 5: Single Pointer
    Runtime: 224 ms, faster than 78.25% of Python3 online submissions for Double a Number Represented as a Linked List.
    Memory Usage: 18.9 MB, less than 99.37% of Python3 online submissions for Double a Number Represented as a Linked List.
    """

    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # If the value of the head node is greater than 4,
        # insert a new node at the beginning
        if head.val > 4:
            head = ListNode(0, head)

        # Traverse the linked list
        node = head
        while node:
            # Double the value of the current node
            # and update it with the units digit
            node.val = (node.val * 2) % 10

            # If the current node has a next node
            # and the next node's value is greater than 4,
            # increment the current node's value to handle carry
            if node.next and node.next.val > 4:
                node.val += 1

            # Move to the next node
            node = node.next

        return head
