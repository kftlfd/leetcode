"""
Leetcode
1171. Remove Zero Sum Consecutive Nodes from Linked List
Medium
2024-03-12

Given the head of a linked list, we repeatedly delete consecutive sequences of nodes that sum to 0 until there are no such sequences.

After doing so, return the head of the final linked list.  You may return any such answer.

 

(Note that in the examples below, all sequences are serializations of ListNode objects.)

Example 1:

Input: head = [1,2,-3,3,1]
Output: [3,1]
Note: The answer [1,2,1] would also be accepted.

Example 2:

Input: head = [1,2,3,-3,4]
Output: [1,2,4]

Example 3:

Input: head = [1,2,3,-3,-2]
Output: [1]

 

Constraints:

    The given linked list will contain between 1 and 1000 nodes.
    Each node in the linked list has -1000 <= node.val <= 1000.

Hints:
- Convert the linked list into an array.
- While you can find a non-empty subarray with sum = 0, erase it.
- Convert the array into a linked list.
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1:
    """
    leetcode solution 1: Prefix Sum for Each Consecutive Sequence
    Runtime: 70 ms, faster than 10.36% of Python3 online submissions for Remove Zero Sum Consecutive Nodes from Linked List.
    Memory Usage: 16.8 MB, less than 89.64% of Python3 online submissions for Remove Zero Sum Consecutive Nodes from Linked List
    """

    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        front = ListNode(0, head)
        start = front

        while start is not None:
            prefix_sum = 0
            end = start.next

            while end is not None:
                # Add end's value to the prefix sum
                prefix_sum += end.val
                # Delete zero sum consecutive sequence
                # by setting node before sequence to node after
                if prefix_sum == 0:
                    start.next = end.next
                end = end.next

            start = start.next

        return front.next


class Solution2:
    """
    leetcode solution 2: Prefix Sum Hash Table
    Runtime: 35 ms, faster than 93.63% of Python3 online submissions for Remove Zero Sum Consecutive Nodes from Linked List.
    Memory Usage: 17 MB, less than 29.48% of Python3 online submissions for Remove Zero Sum Consecutive Nodes from Linked List.
    """

    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        front = ListNode(0, head)
        current = front
        prefix_sum = 0
        prefix_sum_to_node = {0: front}

        # Calculate the prefix sum for each node and add to the hashmap
        # Duplicate prefix sum values will be replaced
        while current is not None:
            prefix_sum += current.val
            prefix_sum_to_node[prefix_sum] = current
            current = current.next

        # Reset prefix sum and current
        prefix_sum = 0
        current = front

        # Delete zero sum consecutive sequences
        # by setting node before sequence to node after
        while current is not None:
            prefix_sum += current.val
            current.next = prefix_sum_to_node[prefix_sum].next
            current = current.next

        return front.next


class Solution3:
    """
    leetcode solution 3: Prefix Sum Hash Table (one pass)
    Runtime: 34 ms, faster than 95.62% of Python3 online submissions for Remove Zero Sum Consecutive Nodes from Linked List.
    Memory Usage: 16.8 MB, less than 53.78% of Python3 online submissions for Remove Zero Sum Consecutive Nodes from Linked List.
    """

    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        front = ListNode(0, head)
        current = front
        prefix_sum = 0
        prefix_sum_to_node = {}
        while current is not None:
            # Add current's value to the prefix sum
            prefix_sum += current.val

            # If prefix_sum is already in the hashmap,
            # we have found a zero-sum sequence:
            if prefix_sum in prefix_sum_to_node:
                prev = prefix_sum_to_node[prefix_sum]
                current = prev.next

                # Delete zero sum nodes from hashmap
                # to prevent incorrect deletions from linked list
                p = prefix_sum + current.val
                while p != prefix_sum:
                    del prefix_sum_to_node[p]
                    current = current.next
                    p += current.val

                # Make connection from the node before
                # the zero sum sequence to the node after
                prev.next = current.next
            else:
                # Add new prefix_sum to hashmap
                prefix_sum_to_node[prefix_sum] = current

            # Progress to next element in list
            current = current.next

        return front.next
