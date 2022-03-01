'''
Leetcode
169. Majority Element (easy)
2022-02-21

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than 
⌊n / 2⌋ times. You may assume that the majority element 
always exists in the array.
'''

from typing import List



# try 1
# Runtime: 228 ms, faster than 50.07% of Python3 online submissions for Majority Element.
# Memory Usage: 15.4 MB, less than 81.81% of Python3 online submissions for Majority Element.
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        # populate hashtable
        # {element: frequency}
        ht = {}
        for n in nums:
            ht[n] = ht.get(n, 0) + 1
            
        # go through hashtable
        # return element with frequency > len(nums)/2
        for e in ht:
            if ht[e] > len(nums)/2: return e



# hashtable 2
# Runtime: 345 ms, faster than 7.61% of Python3 online submissions for Majority Element.
# Memory Usage: 15.4 MB, less than 81.81% of Python3 online submissions for Majority Element.
class Solution4:
    def majorityElement(self, nums: List[int]) -> int:
        
        # hashtable {element: frequency}
        l = len(nums) // 2
        ht = {}
        for n in nums:
            tmp = ht.get(n, 0) + 1
            if tmp > l: return n
            else: ht[n] = tmp
            



# LC - sort
# Runtime: 176 ms, faster than 75.11% of Python3 online submissions for Majority Element.
# Memory Usage: 15.4 MB, less than 81.81% of Python3 online submissions for Majority Element.
class Solution2:
    def majorityElement(self, nums: List[int]) -> int:
        
        nums.sort()
        
        return nums[len(nums)//2]



# LC - Boyer-Moore Voting Algorithm
# Runtime: 179 ms, faster than 71.39% of Python3 online submissions for Majority Element.
# Memory Usage: 15.5 MB, less than 81.81% of Python3 online submissions for Majority Element.
class Solution3:
    def majorityElement(self, nums: List[int]) -> int:
        
        count = 0
        candidate = None

        for num in nums:
            
            if count == 0:
                candidate = num
            
            count += (1 if num == candidate else -1)

        return candidate