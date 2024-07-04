"""
Leetcode
2181. Merge Nodes in Between Zeros
Medium
2024-07-04

You are given the head of a linked list, which contains a series of integers separated by 0's. The beginning and end of the linked list will have Node.val == 0.

For every two consecutive 0's, merge all the nodes lying in between them into a single node whose value is the sum of all the merged nodes. The modified list should not contain any 0's.

Return the head of the modified linked list.

 

Example 1:

Input: head = [0,3,1,0,4,5,2,0]
Output: [4,11]
Explanation: 
The above figure represents the given linked list. The modified list contains
- The sum of the nodes marked in green: 3 + 1 = 4.
- The sum of the nodes marked in red: 4 + 5 + 2 = 11.

Example 2:

Input: head = [0,1,0,3,0,2,2,0]
Output: [1,3,4]
Explanation: 
The above figure represents the given linked list. The modified list contains
- The sum of the nodes marked in green: 1 = 1.
- The sum of the nodes marked in red: 3 = 3.
- The sum of the nodes marked in yellow: 2 + 2 = 4.

 

Constraints:

    The number of nodes in the list is in the range [3, 2 * 10^5].
    0 <= Node.val <= 1000
    There are no two consecutive nodes with Node.val == 0.
    The beginning and end of the linked list have Node.val == 0.
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Runtime: 992 ms, faster than 33.26% of Python3 online submissions for Merge Nodes in Between Zeros.
    Memory Usage: 74.8 MB, less than 47.36% of Python3 online submissions for Merge Nodes in Between Zeros.
    """

    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        dummy = ListNode()
        ans_cur = dummy
        val = 0
        cur = head.next

        while cur:
            if cur.val == 0:
                ans_cur.next = ListNode(val)
                ans_cur = ans_cur.next
                val = 0
            else:
                val += cur.val
            cur = cur.next

        return dummy.next


class Solution1:
    """
    leetcode solution 1: Two-Pointer (One-Pass)
    Runtime: 990 ms, faster than 34.36% of Python3 online submissions for Merge Nodes in Between Zeros.
    Memory Usage: 56.4 MB, less than 67.77% of Python3 online submissions for Merge Nodes in Between Zeros.
    """

    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize a sentinel/dummy node with the first non-zero value.
        modify = head.next
        next_sum = modify

        while next_sum:
            cur_sum = 0
            # Find the sum of all nodes until you encounter a 0.
            while next_sum.val != 0:
                cur_sum += next_sum.val
                next_sum = next_sum.next

            # Assign the sum to the current node's value.
            modify.val = cur_sum
            # Move nextSum to the first non-zero value of the next block.
            next_sum = next_sum.next
            # Move modify also to this node.
            modify.next = next_sum
            modify = modify.next

        return head.next


class Solution2:
    """
    leetcode solution 2: Recursion
    Runtime: 911 ms, faster than 67.53% of Python3 online submissions for Merge Nodes in Between Zeros.
    Memory Usage: 69.1 MB, less than 58.79% of Python3 online submissions for Merge Nodes in Between Zeros.
    """

    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Start with the first non-zero value.
        head = head.next
        if not head:
            return head

        # Initialize a dummy head node.
        temp = head
        cur_sum = 0
        while temp.val != 0:
            cur_sum += temp.val
            temp = temp.next

        # Store the sum in head's value.
        head.val = cur_sum
        # Store head's next node as the recursive result for temp node.
        head.next = self.mergeNodes(temp)

        return head


class Solution3:
    """
    sample 649 ms submission
    Runtime: 684 ms, faster than 96.85% of Python3 online submissions for Merge Nodes in Between Zeros.
    Memory Usage: 53.3 MB, less than 93.30% of Python3 online submissions for Merge Nodes in Between Zeros.
    """

    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        temp = head.next
        cur_sum = 0

        while temp:
            if temp.val == 0:
                curr = curr.next
                curr.val = cur_sum
                cur_sum = 0
            else:
                cur_sum += temp.val
            temp = temp.next

        curr.next = None
        return head.next
