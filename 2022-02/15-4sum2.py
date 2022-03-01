'''
Leetcode
454. 4Sum II (medium)
2022-02-03
'''

'''
Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, 
return the number of tuples (i, j, k, l) such that:
 - 0 <= i, j, k, l < n
 - nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
'''

from typing import List
from collections import defaultdict, Counter



# solution 1
# https://leetcode.com/problems/4sum-ii/discuss/1740570/Python3-O(n2)-_(-)_-Explained
# Runtime: 716 ms, faster than 85.08% of Python3 online submissions for 4Sum II.
# Memory Usage: 14.2 MB, less than 90.85% of Python3 online submissions for 4Sum II.
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        n, hashtable, out = len(nums1), defaultdict(int), 0
        
        # sums of first two lists
        # hashtable = {sum: frequency}
        for i in range(n):
            for j in range(n):
                hashtable[ nums1[i] + nums2[j] ] += 1

        # check is sums of last two lists add up to 0 with sums in hashtable
        # i.e. if in hashtable there is a sum that = -(n3 + n4), then 
        # add the frequency of that sum to out
        for i in range(n):
            for j in range(n):
                out += hashtable[ (nums3[i] + nums4[j]) * -1 ]

        return out



# solution 2
# https://leetcode.com/problems/4sum-ii/discuss/93917/Easy-2-lines-O(N2)-Python
# Runtime: 1393 ms, faster than 18.35% of Python3 online submissions for 4Sum II.
# Memory Usage: 14.2 MB, less than 98.30% of Python3 online submissions for 4Sum II.
class Solution2:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        AB = Counter(a+b for a in nums1 for b in nums2)
        return sum(AB[-c-d] for c in nums3 for d in nums4)



tests = [
    [ [1,2], [-2,-1], [-1,2], [0,2] ],
    [ [0], [0], [0], [0] ]
]
solution = Solution2()
for test in tests:
    print(f'test: {test} \t -->  {solution.fourSumCount(test[0], test[1], test[2], test[3])}')