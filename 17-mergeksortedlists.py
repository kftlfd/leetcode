'''
Leetcode
23. Merge k Sorted Lists (hard)
2022-02-05

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.
https://leetcode.com/problems/merge-k-sorted-lists/
'''

from typing import List, Optional
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



###   Try 1
# Runtime: 5892 ms, faster than 5.00% of Python3 online submissions for Merge k Sorted Lists.
# Memory Usage: 17.7 MB, less than 90.95% of Python3 online submissions for Merge k Sorted Lists.
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        started = False
        
        # remove empty nodes
        for i in range(len(lists)-1, -1, -1):
            if lists[i] is None: lists.pop(i)
        
        while lists:
                    
            # find node with smallest val
            smallest = {'val': lists[0].val, 'index': 0}
                
            for i in range(1, len(lists)):
                if lists[i].val < smallest['val']:
                    smallest['val'] = lists[i].val
                    smallest['index'] = i
            
            # write to out
            if started:
                nxt.val = smallest['val']
            else:
                out = ListNode(val = smallest['val'])
                nxt = out
                started = True
            
            # remove node from sublist
            if lists[smallest['index']].next != None:
                lists[smallest['index']] = lists[smallest['index']].next
            else:
                lists.pop(smallest['index'])

            # prepare next node        
            if lists:
                nxt.next = ListNode()
                nxt = nxt.next
            
        if started: return out
        
        return
            