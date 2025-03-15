"""
Leetcode
2025-03-15
2560. House Robber IV
Medium

There are several consecutive houses along a street, each of which has some money inside. There is also a robber, who wants to steal money from the homes, but he refuses to steal from adjacent homes.

The capability of the robber is the maximum amount of money he steals from one house of all the houses he robbed.

You are given an integer array nums representing how much money is stashed in each house. More formally, the ith house from the left has nums[i] dollars.

You are also given an integer k, representing the minimum number of houses the robber will steal from. It is always possible to steal at least k houses.

Return the minimum capability of the robber out of all the possible ways to steal at least k houses.

 

Example 1:

Input: nums = [2,3,5,9], k = 2
Output: 5
Explanation: 
There are three ways to rob at least 2 houses:
- Rob the houses at indices 0 and 2. Capability is max(nums[0], nums[2]) = 5.
- Rob the houses at indices 0 and 3. Capability is max(nums[0], nums[3]) = 9.
- Rob the houses at indices 1 and 3. Capability is max(nums[1], nums[3]) = 9.
Therefore, we return min(5, 9, 9) = 5.

Example 2:

Input: nums = [2,7,9,3,1], k = 2
Output: 2
Explanation: There are 7 ways to rob the houses. The way which leads to minimum capability is to rob the house at index 0 and 4. Return max(nums[0], nums[4]) = 2.

 

Constraints:

    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^9
    1 <= k <= (nums.length + 1)/2


Hint 1
Can we use binary search to find the minimum value of a non-contiguous subsequence of a given size k?
Hint 2
Initialize the search range with the minimum and maximum elements of the input array.
Hint 3
Use a check function to determine if it is possible to select k non-consecutive elements that are less than or equal to the current "guess" value.
Hint 4
Adjust the search range based on the outcome of the check function, until the range converges and the minimum value is found.
"""

from typing import List


class Solution:
    """
    Time Limit Exceeded
    """

    def minCapability(self, nums: List[int], k: int) -> int:
        n = len(nums)
        min_num = float('inf')
        max_num = float('-inf')

        for num in nums:
            min_num = min(min_num, num)
            max_num = max(max_num, num)

        def check(guess: int, i: int, rem: int) -> bool:
            if rem <= 0:
                return True
            if i >= n:
                return False
            if nums[i] <= guess and check(guess, i + 2, rem - 1):
                return True
            return check(guess, i + 1, rem)

        left = min_num
        right = max_num

        while left < right:
            mid = (left + right) // 2
            if check(mid, 0, k):
                right = mid
            else:
                left = mid + 1

        return right


class Solution1:
    """
    leetcode solution: Binary Search
    Runtime 311ms Beats 64.28%
    Memory 28.68MB Beats 50.00%
    """

    def minCapability(self, nums: List[int], k: int) -> int:
        # Store the maximum nums value in maxReward.
        min_reward, max_reward = 1, max(nums)
        total_houses = len(nums)

        # Use binary search to find the minimum reward possible.
        while min_reward < max_reward:
            mid_reward = (min_reward + max_reward) // 2
            possible_thefts = 0

            index = 0
            while index < total_houses:
                if nums[index] <= mid_reward:
                    possible_thefts += 1
                    index += 2  # Skip the next house to maintain the non-adjacent condition
                else:
                    index += 1

            if possible_thefts >= k:
                max_reward = mid_reward
            else:
                min_reward = mid_reward + 1

        return min_reward
