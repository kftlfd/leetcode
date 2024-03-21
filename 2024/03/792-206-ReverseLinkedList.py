"""
Leetcode
206. Reverse Linked List
Easy
2024-03-21

Given the head of a singly linked list, reverse the list, and return the reversed list.

 

Example 1:

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:

Input: head = [1,2]
Output: [2,1]

Example 3:

Input: head = []
Output: []

 

Constraints:

    The number of nodes in the list is the range [0, 5000].
    -5000 <= Node.val <= 5000

 

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
"""

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        if not self.next:
            return f"{self.val}."
        return f"{self.val}-> {self.next}"


class Solution:
    """
    Runtime: 39 ms, faster than 46.24% of Python3 online submissions for Reverse Linked List.
    Memory Usage: 17.6 MB, less than 77.25% of Python3 online submissions for Reverse Linked List.
    """

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = head
        cur_next = None

        while cur:
            cur_next = cur.next
            cur.next = dummy.next
            dummy.next = cur
            cur = cur_next

        return dummy.next


class Solution1:
    """
    recursive
    https://leetcode.com/problems/reverse-linked-list/discuss/58127/Python-Iterative-and-Recursive-Solution
    Runtime: 37 ms, faster than 58.28% of Python3 online submissions for Reverse Linked List.
    Memory Usage: 17.6 MB, less than 97.90% of Python3 online submissions for Reverse Linked List.
    """

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.reverse(head)

    def reverse(self, node: Optional[ListNode], prev: Optional[ListNode] = None) -> ListNode:
        if not node:
            return prev

        n = node.next
        node.next = prev
        return self.reverse(n, node)


def arr_to_list(arr: List[int]) -> ListNode:
    dummy = ListNode()
    cur = dummy
    for num in arr:
        cur.next = ListNode(num)
        cur = cur.next
    return dummy.next


def list_to_arr(head: Optional[ListNode]) -> List[int]:
    arr = []
    cur = head
    while cur:
        arr.append(cur.val)
        cur = cur.next
    return arr


s = Solution1()
tests = [
    ([1, 2, 3, 4, 5],
     [5, 4, 3, 2, 1]),
]
for inp, exp in tests:
    inp_list = arr_to_list(inp)
    res = s.reverseList(inp_list)
    res_arr = list_to_arr(res)
    if res_arr != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res_arr)
        print()
print('Completed testing')
