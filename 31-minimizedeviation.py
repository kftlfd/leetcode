'''
Leetcode
1675. Minimize Deviation in Array (Hard)
2022-02-19

You are given an array nums of n positive integers.

You can perform two types of operations on any element of the array 
any number of times:

    If the element is even, divide it by 2.
        For example, if the array is [1,2,3,4], then you can do this 
        operation on the last element, and the array will be [1,2,3,2].
    If the element is odd, multiply it by 2.
        For example, if the array is [1,2,3,4], then you can do this 
        operation on the first element, and the array will be [2,2,3,4].

The deviation of the array is the maximum difference between any two 
elements in the array.

Return the minimum deviation the array can have after performing some 
number of operations.
'''

from typing import List



# wrong
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        
        nums.sort()
        nsum = sum(nums)
        sums = [nsum]
        diff = nums[-1] - nums[0]

        while True:
            new_changes = False
            sdiff = 0
            if nums[0] % 2 != 0: # odd
                sdiff += nums[0]
                nums[0] *= 2
                new_changes = True
            if nums[-1] % 2 == 0: # even
                sdiff -= nums[-1] // 2
                nums[-1] //= 2
                new_changes = True
            if not new_changes: break
            nums.sort()
            diff = min(diff, nums[-1] - nums[0])

            nsum += sdiff
            if nsum in sums: break
            sums.append(nsum)
                
        return diff



# wrong again
class Solution2:
    def minimumDeviation(self, nums: List[int]) -> int:
        
        nums.sort()
        diff = nums[-1] - nums[0]

        changes = [0]

        while True:
            change = 0

            for i in range(len(nums)-1, -1, -1):
                if nums[i] % 2 == 0: # even
                    nums[i] //= 2
                    if max(nums) - min(nums) > diff: nums[i] *= 2
                    else: change -= nums[i]
                
            for i in range(len(nums)):
                if nums[i] % 2 != 0: # odd
                    nums[i] *= 2
                    if max(nums) - min(nums) >= diff: nums[i] //= 2
                    else: change += nums[i] // 2

            nums.sort()
            diff = min(diff, nums[-1] - nums[0])

            if change in changes: break
            changes.append(change)

        return diff



# taken from
# https://leetcode.com/problems/minimize-deviation-in-array/discuss/1041766/Python-Heap-solution-explained
# Runtime: 1729 ms, faster than 36.89% of Python3 online submissions for Minimize Deviation in Array.
# Memory Usage: 30.1 MB, less than 40.78% of Python3 online submissions for Minimize Deviation in Array.
class Solution3:
    def minimumDeviation(self, nums: List[int]) -> int:

        import heapq

        # store in heap (min,max) values possible for every num:
        #  - if num is odd:  (num, num*2)
        #  - if num is even: (num divided by 2 until its odd, num)
        heap = []
        for num in nums:
            tmp = num
            while tmp%2 == 0: tmp//=2
            heap.append((tmp, max(num, tmp*2)))
        
        # reduce every num to its minimum value, find biggest among them,
        # which is the same as find biggest min value from heap;
        # this is the <smallest-Max> value for array
        Max = max(i for i,j in heap)
        heapq.heapify(heap)
        ans = float("inf")

        # take the smallest min from heap;
        # update deviation (ans) based on it against Max;
        # increase min if it does not exceeded its limit and put back to heap;
        # if min has reached its limit, then we found <biggest-Min> value for array;
        # smallest deviation is possible between <smallest-Max> and <biggest-Min>
        while len(heap) == len(nums):
            num, limit = heapq.heappop(heap)
            ans = min(ans, Max - num)
            if num < limit:
                heapq.heappush(heap, (num*2, limit))
                Max = max(Max, num*2)
            
        return ans



tests = [
    [[1,2,3,4], 1],
    [[4,1,5,20,3], 3],
    [[2,10,8], 3],
    [[2,8,6,1,6], 1],
    [[3,5], 1],
    [[10,4,3], 2],
    [[399,908,648,357,693,502,331,649,596,698], 315],
    [[10,5,10,1], 3]
]
solution = Solution3()
for test in tests:
    print(f'test: {test[0]}')
    res = solution.minimumDeviation(test[0])
    print(f'expect: {test[1]} \t out: {res} \t {res == test[1]}')
