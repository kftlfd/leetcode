'''
Leetcode
21. Merge Two Sorted Lists (easy)
2022-03-07

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by 
splicing together the nodes of the first two lists.

Return the head of the merged linked list.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



# try 1
# Runtime: 32 ms, faster than 97.89% of Python3 online submissions for Merge Two Sorted Lists.
# Memory Usage: 14 MB, less than 40.05% of Python3 online submissions for Merge Two Sorted Lists.
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        t1 = list1
        t2 = list2
        if not (t1 and t2):
            if t1: return t1
            return t2
        
        if list1.val <= list2.val:
            out = list1
            t1 = list1.next
        else:
            out = list2
            t2 = list2.next
        curr = out
        
        while t1 and t2:
            if t1.val <= t2.val:
                curr.next = t1
                t1 = t1.next
            else:
                curr.next = t2
                t2 = t2.next
            curr = curr.next
            
        rest = t1 if t1 else t2
        while rest:
            curr.next = rest
            rest = rest.next
            curr = curr. next
            
        return out



# optimized (better space, worse time?) try 1
# Runtime: 43 ms, faster than 71.72% of Python3 online submissions for Merge Two Sorted Lists.
# Memory Usage: 13.8 MB, less than 89.81% of Python3 online submissions for Merge Two Sorted Lists.
class Solution1:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not list1: return list2
        if not list2: return list1

        # root node
        if list1.val <= list2.val:
            out = list1
            list1 = list1.next
        else:
            out = list2
            list2 = list2.next
        curr = out
        
        # merge lists
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
            
        # add remainder
        curr.next = list1 if list1 else list2
            
        return out