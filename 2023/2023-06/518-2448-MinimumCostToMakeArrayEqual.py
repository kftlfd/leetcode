"""
Leetcode
2448. Minimum Cost to Make Array Equal (hard)
2023-06-21

You are given two 0-indexed arrays nums and cost consisting each of n positive integers.

You can do the following operation any number of times:

    Increase or decrease any element of the array nums by 1.

The cost of doing one operation on the ith element is cost[i].

Return the minimum total cost such that all the elements of the array nums become equal.

Example 1:

Input: nums = [1,3,5,2], cost = [2,3,1,14]
Output: 8
Explanation: We can make all the elements equal to 2 in the following way:
- Increase the 0th element one time. The cost is 2.
- Decrease the 1st element one time. The cost is 3.
- Decrease the 2nd element three times. The cost is 1 + 1 + 1 = 3.
The total cost is 2 + 3 + 3 = 8.
It can be shown that we cannot make the array equal with a smaller cost.

Example 2:

Input: nums = [2,2,2,2,2], cost = [4,2,8,1,3]
Output: 0
Explanation: All the elements are already equal, so no operations are needed.

Constraints:

    n == nums.length == cost.length
    1 <= n <= 10^5
    1 <= nums[i], cost[i] <= 10^6
"""

from typing import List


class Solution:
    """
    leetcode solution 1: Prefix Sum
    Time complexity: O(n⋅logn)
    Space complexity: O(n)
    Runtime: 497 ms, faster than 58.82% of Python3 online submissions for Minimum Cost to Make Array Equal.
    Memory Usage: 40.6 MB, less than 30.88% of Python3 online submissions for Minimum Cost to Make Array Equal.
    """

    def minCost(self, nums: List[int], cost: List[int]) -> int:
        # sort integers by values
        num_and_cost = sorted([num, c] for num, c in zip(nums, cost))
        n = len(nums)

        # get the prefix sum array of the costs
        prefix_cost = [0] * n
        prefix_cost[0] = num_and_cost[0][1]
        for i in range(1, n):
            prefix_cost[i] = num_and_cost[i][1] + prefix_cost[i - 1]

        # then we try every integer nums[i] and make every element equals nums[i]
        # starting with nums[0]
        total_cost = 0
        for i in range(1, n):
            total_cost += num_and_cost[i][1] * \
                (num_and_cost[i][0] - num_and_cost[0][0])
        answer = total_cost

        # then we try all other nums. The cost difference is made by the change of
        # two parts: 1) prefix sum of costs; 2) suffix sum of costs.
        # During the iteration, record the minimum cost we have met
        for i in range(1, n):
            gap = num_and_cost[i][0] - num_and_cost[i - 1][0]
            total_cost += prefix_cost[i - 1] * gap
            total_cost -= gap * (prefix_cost[n - 1] - prefix_cost[i - 1])
            answer = min(answer, total_cost)

        return answer


class Solution1:
    """
    leetcode solution 2: Binary Search
    Time: O(n*logk) -- Let nn be the length of the input array nums and kk be the difference between the maximum and minimum value of nums[i].
    Space: O(1)
    Runtime: 923 ms, faster than 39.71% of Python3 online submissions for Minimum Cost to Make Array Equal.
    Memory Usage: 32 MB, less than 50.00% of Python3 online submissions for Minimum Cost to Make Array Equal.
    """

    def minCost(self, nums: List[int], cost: List[int]) -> int:
        # get the cost of making every element equals base
        def get_cost(base: int) -> int:
            return sum(abs(base - num) * c for num, c in zip(nums, cost))

        # initiate binary search boundaries
        left = min(nums)
        right = max(nums)
        ans = get_cost(nums[0])

        while left < right:
            mid = (left + right) // 2
            cost_1 = get_cost(mid)
            cost_2 = get_cost(mid + 1)
            ans = min(cost_1, cost_2)

            if cost_1 > cost_2:
                left = mid + 1
            else:
                right = mid

        return ans


s = Solution()
tests = [
    (([1, 3, 5, 2], [2, 3, 1, 14]),
     8),

    (([2, 2, 2, 2, 2], [4, 2, 8, 1, 3]),
     0),
]
for inp, exp in tests:
    res = s.minCost(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
