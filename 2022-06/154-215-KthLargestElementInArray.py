"""
Leetcode
215. Kth Largest Element in an Array (medium)
2022-06-22

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.
"""



# Runtime: 80 ms, faster than 74.54% of Python3 online submissions for Kth Largest Element in an Array.
# Memory Usage: 14.7 MB, less than 71.94% of Python3 online submissions for Kth Largest Element in an Array.
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums)[-k]



# https://leetcode.com/problems/kth-largest-element-in-an-array/discuss/1019513/Python-QuickSelect-average-O(n)-explained
# Runtime: 80 ms, faster than 74.54% of Python3 online submissions for Kth Largest Element in an Array.
# Memory Usage: 15 MB, less than 21.49% of Python3 online submissions for Kth Largest Element in an Array.
class Solution1:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums: return
        pivot = random.choice(nums)
        left =  [x for x in nums if x > pivot]
        mid  =  [x for x in nums if x == pivot]
        right = [x for x in nums if x < pivot]
        
        L, M = len(left), len(mid)
        
        if k <= L:
            return self.findKthLargest(left, k)
        elif k > L + M:
            return self.findKthLargest(right, k - L - M)
        else:
            return mid[0]



s = Solution()
tests = [
    ([3,2,1,5,6,4], 2),
    ([3,2,3,1,2,4,5,5,6], 4)
]
for t in tests:
    print(t)
    print(s.findKthLargest(t[0], t[1]))
    print()
