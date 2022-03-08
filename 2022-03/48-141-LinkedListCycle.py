'''
Leetcode
141. Linked List Cycle (easy)
2022-03-08

Given head, the head of a linked list, determine if the linked list 
has a cycle in it.

There is a cycle in a linked list if there is some node in the list 
that can be reached again by continuously following the next pointer. 
Internally, pos is used to denote the index of the node that tail's 
next pointer is connected to. Note that pos is not passed as a 
parameter.

Return true if there is a cycle in the linked list. Otherwise, 
return false.
'''

from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None



# try 1
# Runtime: 2657 ms, faster than 5.01% of Python3 online submissions for Linked List Cycle.
# Memory Usage: 17.1 MB, less than 99.27% of Python3 online submissions for Linked List Cycle.
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if (not head) or (not head.next): return False
        
        ht = [id(head)]
        curr = head.next
        while curr:
            if id(curr) in ht: return True
            ht.append(id(curr))
            curr = curr.next
            
        return False
# if saving nodes in [ht] instead of id(node)
# Runtime: 1500 ms, faster than 5.01% of Python3 online submissions for Linked List Cycle.
# Memory Usage: 17.6 MB, less than 42.75% of Python3 online submissions for Linked List Cycle.



# Floyd's Cycle Detection
# two pointers, going through a cycle fast will meet with slow
# Runtime: 76 ms, faster than 55.13% of Python3 online submissions for Linked List Cycle.
# Memory Usage: 17.5 MB, less than 74.54% of Python3 online submissions for Linked List Cycle.
class Solution1:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if (not head) or (not head.next): return False
        
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: return True
            
        return False
