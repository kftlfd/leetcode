'''
Leetcode
560. Subarray Sum Equals K (medium)
2022-02-10

Given an array of integers nums and an integer k, 
return the total number of continuous subarrays whose sum equals to k.
https://leetcode.com/problems/subarray-sum-equals-k/
'''



# Leetcode solution
# Runtime: 333 ms, faster than 49.09% of Python3 online submissions for Subarray Sum Equals K.
# Memory Usage: 16.6 MB, less than 93.61% of Python3 online submissions for Subarray Sum Equals K.
# sum(i,j) = sum(0,j) - sum(0,i)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        count = 0
        s = 0
        hashmap = {0: 1} # sum: frequency
        
        for i in range(len(nums)):

            s += nums[i]
            hashmap[s] = hashmap.get(s, 0) + 1

            if s - k in hashmap:
                count += hashmap[s - k]
        
        return count
