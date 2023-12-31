"""
Leetcode
985. Sum of Even Numbers After Queries (medium)
2022-09-21

You are given an integer array nums and an array queries where queries[i] = [vali, indexi].

For each query i, first, apply nums[indexi] = nums[indexi] + vali, then print the sum of the even values of nums.

Return an integer array answer where answer[i] is the answer to the ith query.

Example 1:
Input: nums = [1,2,3,4], queries = [[1,0],[-3,1],[-4,0],[2,3]]
Output: [8,6,2,4]
Explanation: At the beginning, the array is [1,2,3,4].
After adding 1 to nums[0], the array is [2,2,3,4], and the sum of even values is 2 + 2 + 4 = 8.
After adding -3 to nums[1], the array is [2,-1,3,4], and the sum of even values is 2 + 4 = 6.
After adding -4 to nums[0], the array is [-2,-1,3,4], and the sum of even values is -2 + 4 = 2.
After adding 2 to nums[3], the array is [-2,-1,3,6], and the sum of even values is -2 + 6 = 4.

Example 2:
Input: nums = [1], queries = [[4,0]]
Output: [0]
"""

from typing import List


# Runtime: 1390 ms, faster than 6.10% of Python3 online submissions for Sum of Even Numbers After Queries.
# Memory Usage: 20.5 MB, less than 75.57% of Python3 online submissions for Sum of Even Numbers After Queries.
class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:

        ans = []
        even_sum = sum([x for x in nums if x % 2 == 0])

        for val, index in queries:
            old_val = nums[index]
            new_val = old_val + val

            if old_val % 2 == 0:
                if new_val % 2 == 0:
                    # even old, even new
                    even_sum += new_val - old_val
                else:
                    # even old, odd new
                    even_sum -= old_val
            else:
                if new_val % 2 == 0:
                    # odd old, even new
                    even_sum += new_val
                else:
                    # odd old, odd new
                    pass

            nums[index] = new_val
            ans.append(even_sum)

        return ans


# leetcode solution
# Runtime: 1375 ms, faster than 6.86% of Python3 online submissions for Sum of Even Numbers After Queries.
# Memory Usage: 20.4 MB, less than 97.20% of Python3 online submissions for Sum of Even Numbers After Queries.
class Solution1:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:

        ans = []
        even_sum = sum([x for x in nums if x % 2 == 0])

        for val, index in queries:
            if nums[index] % 2 == 0:
                even_sum -= nums[index]
            nums[index] += val
            if nums[index] % 2 == 0:
                even_sum += nums[index]
            ans.append(even_sum)

        return ans


s = Solution()
tests = [
    ([1, 2, 3, 4], [[1, 0], [-3, 1], [-4, 0], [2, 3]]),
    ([1], [[4, 0]]),
]
for t in tests:
    print(t)
    print(s.sumEvenAfterQueries(t[0], t[1]))
    print()
