"""
Leetcode
2024-09-10
2807. Insert Greatest Common Divisors in Linked List
Medium

Given the head of a linked list head, in which each node contains an integer value.

Between every pair of adjacent nodes, insert a new node with a value equal to the greatest common divisor of them.

Return the linked list after insertion.

The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.

 

Example 1:

Input: head = [18,6,10,3]
Output: [18,6,6,2,10,1,3]
Explanation: The 1st diagram denotes the initial linked list and the 2nd diagram denotes the linked list after inserting the new nodes (nodes in blue are the inserted nodes).
- We insert the greatest common divisor of 18 and 6 = 6 between the 1st and the 2nd nodes.
- We insert the greatest common divisor of 6 and 10 = 2 between the 2nd and the 3rd nodes.
- We insert the greatest common divisor of 10 and 3 = 1 between the 3rd and the 4th nodes.
There are no more adjacent nodes, so we return the linked list.

Example 2:

Input: head = [7]
Output: [7]
Explanation: The 1st diagram denotes the initial linked list and the 2nd diagram denotes the linked list after inserting the new nodes.
There are no pairs of adjacent nodes, so we return the initial linked list.

 

Constraints:

    The number of nodes in the list is in the range [1, 5000].
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
    Runtime: 72 ms, faster than 50.69% of Python3 online submissions for Insert Greatest Common Divisors in Linked List.
    Memory Usage: 19.5 MB, less than 79.95% of Python3 online submissions for Insert Greatest Common Divisors in Linked List.
    """

    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head

        while cur:
            if not cur.next:
                cur = cur.next
                continue

            nxt = cur.next
            cur.next = ListNode(self.gcd(cur.val, nxt.val), nxt)
            cur = nxt

        return head

    def gcd(self, x: int, y: int) -> int:
        while y != 0:
            x, y = y, x % y
        return x
