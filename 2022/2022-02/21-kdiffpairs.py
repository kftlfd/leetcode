'''
Leetcode
532. K-diff Pairs in an Array (medium)
2022-02-09

Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.
A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:
 - 0 <= i < j < nums.length
 - |nums[i] - nums[j]| == k
Notice that |val| denotes the absolute value of val.
'''

from typing import List
from collections import defaultdict



# Try 1
# sort then binary search
# Runtime: 200 ms, faster than 9.53% of Python3 online submissions for K-diff Pairs in an Array.
# Memory Usage: 16.5 MB, less than 24.86% of Python3 online submissions for K-diff Pairs in an Array.
class Solution:
    def search(self, start, end, snums, num, k):
        k *= -1
        while end >= start:
            index = (start + end) // 2
            if num - snums[index] == k: return index
            elif num - snums[index] > k: start = index + 1
            elif num - snums[index] < k: end = index - 1
        return None

    def findPairs(self, nums: List[int], k: int) -> int:
        snums = sorted(nums)
        pairs = set()
        l = len(snums)
        for i in range(l):
            sec_num = self.search(i+1, l-1, snums, snums[i], k)
            if sec_num != None: pairs.add((snums[i], snums[sec_num]))
        return len(pairs)



# Try 2
# hashmap
# Runtime: 80 ms, faster than 76.16% of Python3 online submissions for K-diff Pairs in an Array.
# Memory Usage: 15.6 MB, less than 84.25% of Python3 online submissions for K-diff Pairs in an Array.
class Solution2:
    def findPairs(self, nums: List[int], k: int) -> int:
        hashmap, out = {}, 0
        for i in nums:
            if i not in hashmap: hashmap[i] = 0
            hashmap[i] += 1
        
        if k == 0:
            for key in hashmap:
                if hashmap[key] > 1: out += 1
        
        else:           
            for key in hashmap:
                if key + k in hashmap: out += 1
        
        return out



# @lee215
# https://leetcode.com/problems/k-diff-pairs-in-an-array/discuss/100135/JavaPython-Easy-Understood-Solution
# Count the elements with Counter
# If k > 0, for each element i, check if i + k exist.
# If k == 0, for each element i, check if count[i] > 1
# Runtime: 128 ms, faster than 36.21% of Python3 online submissions for K-diff Pairs in an Array.
# Memory Usage: 15.6 MB, less than 71.76% of Python3 online submissions for K-diff Pairs in an Array.
from collections import Counter
class Solution3:
    def findPairs(self, nums: List[int], k: int) -> int:
        res = 0
        c = Counter(nums)
        for i in c:
            if k > 0 and i + k in c or k == 0 and c[i] > 1:
                res += 1
        return res



tests = [
    ([3,1,4,1,5], 2),
    ([1,2,3,4,5], 1),
    ([1,3,1,5,4], 0)
]
solution = Solution3()
for test in tests:
    print(f'test: {test}\tout: {solution.findPairs(test[0], test[1])}')