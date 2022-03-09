'''
Leetcode
82. Remove Duplicates from Sorted List II (medium)         
2022-03-09

Given the head of a sorted linked list, delete all nodes 
that have duplicate numbers, leaving only distinct numbers 
from the original list. Return the linked list sorted as well.
'''

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        if not self.next: return f"({self.val})."
        else: return f"({self.val})-> {self.next}"



# try 1
# wrong
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # check input
        if not head: return head
        
        # helper function
        def move_node(node: ListNode) -> bool:
            moved = False
            while (node.next) and (node.val == node.next.val):
                node = node.next
                moved = True
            if (moved) and (node.next): 
                node = node.next
            return node

        # move head
        while head != move_node(head):
            head = move_node(head)
            
        # delete duplicates
        curr = head.next
        prev = head
        while curr:
            while curr != move_node(curr):
                curr = move_node(curr)
            prev.next = curr
            curr = curr.next
            prev = prev.next
        
        return head



# leetcode solution
# Runtime: 80 ms, faster than 13.63% of Python3 online submissions for Remove Duplicates from Sorted List II.
# Memory Usage: 13.9 MB, less than 54.61% of Python3 online submissions for Remove Duplicates from Sorted List II.
class Solution1:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # sentinel
        sentinel = ListNode(0, head)

        # predecessor = the last node 
        # before the sublist of duplicates
        pred = sentinel
        
        while head:
            # if it's a beginning of duplicates sublist 
            # skip all duplicates
            if head.next and head.val == head.next.val:
                # move till the end of duplicates sublist
                while head.next and head.val == head.next.val:
                    head = head.next
                # skip all duplicates
                pred.next = head.next 
            # otherwise, move predecessor
            else:
                pred = pred.next 
                
            # move forward
            head = head.next
            
        return sentinel.next
        
        

s = Solution1()
tests = [
    [1,2,3,3,4,4,5],
    [1,1,1,2,3],
    [1,1],
    [1],
    []
]
for t in tests:

    # create linked list
    if t:
        head = ListNode(val=t[0])
        curr = head
        for i in range(1, len(t)):
            curr.next = ListNode(val=t[i])
            curr = curr.next
    else:
        head = None

    print(t)
    print(s.deleteDuplicates(head), '\n')
