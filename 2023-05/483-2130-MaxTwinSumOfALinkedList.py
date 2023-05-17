"""
Leetcode
2130. Maximum Twin Sum of a Linked List (medium)
2023-05-17

In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

    For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.

The twin sum is defined as the sum of a node and its twin.

Given the head of a linked list with even length, return the maximum twin sum of the linked list.

Example 1:
Input: head = [5,4,2,1]
Output: 6
Explanation:
Nodes 0 and 1 are the twins of nodes 3 and 2, respectively. All have twin sum = 6.
There are no other nodes with twins in the linked list.
Thus, the maximum twin sum of the linked list is 6. 

Example 2:
Input: head = [4,2,2,3]
Output: 7
Explanation:
The nodes with twins present in this linked list are:
- Node 0 is the twin of node 3 having a twin sum of 4 + 3 = 7.
- Node 1 is the twin of node 2 having a twin sum of 2 + 2 = 4.
Thus, the maximum twin sum of the linked list is max(7, 4) = 7. 

Example 3:
Input: head = [1,100000]
Output: 100001
Explanation:
There is only one node with a twin in the linked list having twin sum of 1 + 100000 = 100001.
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Runtime: 902 ms, faster than 61.72% of Python3 online submissions for Maximum Twin Sum of a Linked List.
    Memory Usage: 57 MB, less than 13.09% of Python3 online submissions for Maximum Twin Sum of a Linked List.
    """

    def pairSum(self, head: Optional[ListNode]) -> int:

        nums = []
        cur = head
        while cur:
            nums.append(cur.val)
            cur = cur.next

        return max(nums[k] + nums[-k-1] for k in range(len(nums) // 2))


class Solution1:
    """
    leetcode solution 3: reverse second part in place
    Runtime: 906 ms, faster than 59.99% of Python3 online submissions for Maximum Twin Sum of a Linked List.
    Memory Usage: 47.5 MB, less than 56.69% of Python3 online submissions for Maximum Twin Sum of a Linked List.
    """

    def pairSum(self, head: Optional[ListNode]) -> int:

        slow, fast = head, head
        max_sum = 0

        # Get middle of the linked list
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Reverse second half of the linked list
        cur, prev = slow, None
        while cur:
            cur.next, prev, cur = prev, cur, cur.next

        start = head
        while prev:
            max_sum = max(max_sum, start.val + prev.val)
            prev = prev.next
            start = start.next

        return max_sum
