"""
Leetcode
1721. Swapping Nodes in a Linked List (medium)
2022-04-04

You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values 
of the kth node from the beginning and the kth node from the 
end (the list is 1-indexed).
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        if not self.next: return f"{self.val}."
        return f"{self.val}-> {self.next}"



# try 1
# Runtime: 1213 ms, faster than 68.34% of Python3 online submissions for Swapping Nodes in a Linked List.
# Memory Usage: 48.6 MB, less than 19.34% of Python3 online submissions for Swapping Nodes in a Linked List.
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head: return head

        # break down linked list to array
        ll = []
        curr = head
        while curr:
            ll.append(curr)
            curr = curr.next
        for node in ll:
            node.next = None

        # swap
        ll[k-1], ll[len(ll)-k] = ll[len(ll)-k], ll[k-1]

        # rebuild linked list
        out = ListNode()
        curr = out
        for node in ll:
            curr.next = node
            curr = curr.next

        return out.next



s = Solution()
tests = [
    [[1,2], 1],
    [[1,2,3,4,5], 2],
    [[7,9,6,6,7,8,3,0,9,5], 5]
]
for t in tests:
    
    print(*t)

    # create linked list
    head = ListNode()
    curr = head
    for num in t[0]:
        curr.next = ListNode(val=num)
        curr = curr.next
    head = head.next

    print(s.swapNodes(head, t[1]))
    print()
