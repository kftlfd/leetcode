"""
Leetcode
2025-11-05
3321. Find X-Sum of All K-Long Subarrays II
Hard

You are given an array nums of n integers and two integers k and x.

The x-sum of an array is calculated by the following procedure:

    Count the occurrences of all elements in the array.
    Keep only the occurrences of the top x most frequent elements. If two elements have the same number of occurrences, the element with the bigger value is considered more frequent.
    Calculate the sum of the resulting array.

Note that if an array has less than x distinct elements, its x-sum is the sum of the array.

Return an integer array answer of length n - k + 1 where answer[i] is the x-sum of the

nums[i..i + k - 1].

 

Example 1:

Input: nums = [1,1,2,2,3,4,2,3], k = 6, x = 2

Output: [6,10,12]

Explanation:

    For subarray [1, 1, 2, 2, 3, 4], only elements 1 and 2 will be kept in the resulting array. Hence, answer[0] = 1 + 1 + 2 + 2.
    For subarray [1, 2, 2, 3, 4, 2], only elements 2 and 4 will be kept in the resulting array. Hence, answer[1] = 2 + 2 + 2 + 4. Note that 4 is kept in the array since it is bigger than 3 and 1 which occur the same number of times.
    For subarray [2, 2, 3, 4, 2, 3], only elements 2 and 3 are kept in the resulting array. Hence, answer[2] = 2 + 2 + 2 + 3 + 3.

Example 2:

Input: nums = [3,8,7,8,7,5], k = 2, x = 2

Output: [11,15,15,15,12]

Explanation:

Since k == x, answer[i] is equal to the sum of the subarray nums[i..i + k - 1].

 

Constraints:

    nums.length == n
    1 <= n <= 10^5
    1 <= nums[i] <= 10^9
    1 <= x <= k <= nums.length


Hint 1
Use sliding window.
Hint 2
Use two sets ordered by frequency. One of the sets will only contain the top x frequent elements, and the second will contain all other elements.
Hint 3
Update the two sets whenever you slide the window, and maintain a sum of the elements in the set with x elements
"""

from collections import defaultdict
from typing import List

from sortedcontainers import SortedList


class Solution1:
    """
    leetcode solution: Hash Table + Ordered Set
    Runtime 2955ms Beats 80.95%
    Memory 43.40MB Beats 100.00%
    """

    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        helper = self.Helper(x)
        ans = []

        for i in range(len(nums)):
            helper.insert(nums[i])
            if i >= k:
                helper.remove(nums[i - k])
            if i >= k - 1:
                ans.append(helper.get())

        return ans

    class Helper:
        def __init__(self, x):
            self.x = x
            self.result = 0
            self.large = SortedList()
            self.small = SortedList()
            self.occ = defaultdict(int)

        def insert(self, num):
            if self.occ[num] > 0:
                self.internal_remove((self.occ[num], num))
            self.occ[num] += 1
            self.internal_insert((self.occ[num], num))

        def remove(self, num):
            self.internal_remove((self.occ[num], num))
            self.occ[num] -= 1
            if self.occ[num] > 0:
                self.internal_insert((self.occ[num], num))

        def get(self):
            return self.result

        def internal_insert(self, p):
            if len(self.large) < self.x or p > self.large[0]:
                self.result += p[0] * p[1]
                self.large.add(p)
                if len(self.large) > self.x:
                    to_remove = self.large[0]
                    self.result -= to_remove[0] * to_remove[1]
                    self.large.remove(to_remove)
                    self.small.add(to_remove)
            else:
                self.small.add(p)

        def internal_remove(self, p):
            if p >= self.large[0]:
                self.result -= p[0] * p[1]
                self.large.remove(p)
                if self.small:
                    to_add = self.small[-1]
                    self.result += to_add[0] * to_add[1]
                    self.small.remove(to_add)
                    self.large.add(to_add)
            else:
                self.small.remove(p)
