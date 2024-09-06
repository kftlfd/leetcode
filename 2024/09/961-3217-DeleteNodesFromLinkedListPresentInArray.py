"""
Leetcode
2024-09-06
3217. Delete Nodes From Linked List Present in Array
Medium

You are given an array of integers nums and the head of a linked list. Return the head of the modified linked list after removing all nodes from the linked list that have a value that exists in nums.

 

Example 1:

Input: nums = [1,2,3], head = [1,2,3,4,5]

Output: [4,5]

Explanation:

Remove the nodes with values 1, 2, and 3.

Example 2:

Input: nums = [1], head = [1,2,1,2,1,2]

Output: [2,2,2]

Explanation:

Remove the nodes with value 1.

Example 3:

Input: nums = [5], head = [1,2,3,4]

Output: [1,2,3,4]

Explanation:

No node has value 5.

 

Constraints:

    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^5
    All elements in nums are unique.
    The number of nodes in the given list is in the range [1, 10^5].
    1 <= Node.val <= 10^5
    The input is generated such that there is at least one node in the linked list that has a value not present in nums.
"""

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Runtime: 736 ms, faster than 33.90% of Python3 online submissions for Delete Nodes From Linked List Present in Array.
    Memory Usage: 54.6 MB, less than 81.13% of Python3 online submissions for Delete Nodes From Linked List Present in Array.
    """

    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        nums_set = set(nums)
        dummy = ListNode(0, head)
        cur = head
        prev = dummy

        while cur:
            if cur.val in nums_set:
                prev.next = cur.next
            else:
                prev = prev.next
            cur = cur.next

        return dummy.next


class Solution1:
    """
    https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/solution/2610409
    Runtime: 714 ms, faster than 69.85% of Python3 online submissions for Delete Nodes From Linked List Present in Array.
    Memory Usage: 55 MB, less than 63.82% of Python3 online submissions for Delete Nodes From Linked List Present in Array.
    """

    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums_set = set(nums)
        dummy = ListNode(0, head)
        cur = dummy

        while cur.next:
            if cur.next.val in nums_set:
                cur.next = cur.next.next
            else:
                cur = cur.next

        return dummy.next
