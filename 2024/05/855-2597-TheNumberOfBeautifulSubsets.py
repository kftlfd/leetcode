"""
Leetcode
2597. The Number of Beautiful Subsets
Medium
2024-05-23

You are given an array nums of positive integers and a positive integer k.

A subset of nums is beautiful if it does not contain two integers with an absolute difference equal to k.

Return the number of non-empty beautiful subsets of the array nums.

A subset of nums is an array that can be obtained by deleting some (possibly none) elements from nums. Two subsets are different if and only if the chosen indices to delete are different.

 

Example 1:

Input: nums = [2,4,6], k = 2
Output: 4
Explanation: The beautiful subsets of the array nums are: [2], [4], [6], [2, 6].
It can be proved that there are only 4 beautiful subsets in the array [2,4,6].

Example 2:

Input: nums = [1], k = 1
Output: 1
Explanation: The beautiful subset of the array nums is [1].
It can be proved that there is only 1 beautiful subset in the array [1].

 

Constraints:

    1 <= nums.length <= 20
    1 <= nums[i], k <= 1000

Hints:
- Sort the array nums and create another array cnt of size nums[i].
- Use backtracking to generate all the beautiful subsets. If cnt[nums[i] - k] is positive, then it is impossible to add nums[i] in the subset, and we just move to the next index. Otherwise, it is also possible to add nums[i] in the subset, in this case, increase cnt[nums[i]], and move to the next index.
- Bonus: Can you solve the problem in O(n log n)?
"""

from collections import defaultdict
from typing import List


class Solution:
    """
    Runtime: 3348 ms, faster than 32.22% of Python3 online submissions for The Number of Beautiful Subsets.
    Memory Usage: 16.4 MB, less than 96.46% of Python3 online submissions for The Number of Beautiful Subsets.
    """

    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        n = len(nums)
        max_num = max(nums)
        cnt = [0] * (max_num + 1)
        ans = [0]

        def dfs(i: int, pick: bool) -> int:
            if i >= n:
                return

            picked = False

            if pick:
                num = nums[i]
                dif1, dif2 = num - k, num + k
                if (dif1 < 1 or cnt[dif1] < 1) and (dif2 > max_num or cnt[dif2] < 1):
                    cnt[num] += 1
                    ans[0] += 1
                    picked = True

            if pick and not picked:
                return

            dfs(i + 1, True)
            dfs(i + 1, False)

            if picked:
                cnt[num] -= 1

        dfs(-1, False)
        return ans[0]


class Solution1:
    """
    leetcode solution 1: Using Bitset
    Runtime: 9903 ms, faster than 5.07% of Python3 online submissions for The Number of Beautiful Subsets.
    Memory Usage: 16.5 MB, less than 96.46% of Python3 online submissions for The Number of Beautiful Subsets.
    """

    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        return self._count_beautiful_subsets(nums, k, 0, 0)

    def _count_beautiful_subsets(self, nums, difference, index, mask):
        # Base case: Return 1 if mask is greater than 0 (non-empty subset)
        if index == len(nums):
            return 1 if mask > 0 else 0

        # Flag to check if the current subset is beautiful
        is_beautiful = True

        # Check if the current number forms a beautiful pair with any
        # previous number in the subset
        for j in range(index):
            if ((1 << j) & mask) == 0 or \
               abs(nums[j] - nums[index]) != difference:
                continue
            else:
                is_beautiful = False
                break

        # Recursively calculate beautiful subsets including and excluding
        # the current number
        skip = self._count_beautiful_subsets(nums, difference, index + 1, mask)
        take = (
            self._count_beautiful_subsets(
                nums, difference, index + 1, mask + (1 << index)
            )
            if is_beautiful
            else 0
        )

        return skip + take


class Solution2:
    """
    leetcode solution 2: Recursion with Backtracking
    Runtime: 2774 ms, faster than 55.15% of Python3 online submissions for The Number of Beautiful Subsets.
    Memory Usage: 16.5 MB, less than 96.46% of Python3 online submissions for The Number of Beautiful Subsets.
    """

    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        # Frequency map to track elements
        freq_map = defaultdict(int)
        # Sort nums array
        nums.sort()
        return self._count_beautiful_subsets(nums, k, freq_map, 0) - 1

    def _count_beautiful_subsets(self, nums, difference, freq_map, i):
        # Base case: Return 1 for a subset of size 1
        if i == len(nums):
            return 1

        # Count subsets where nums[i] is not taken
        total_count = self._count_beautiful_subsets(
            nums, difference, freq_map, i + 1)

        # If nums[i] can be taken without violating the condition
        if nums[i] - difference not in freq_map:
            freq_map[nums[i]] += 1  # Mark nums[i] as taken

            # Recursively count subsets where nums[i] is taken
            total_count += self._count_beautiful_subsets(
                nums, difference, freq_map, i + 1
            )
            freq_map[nums[i]] -= 1  # Backtrack: mark nums[i] as not taken

            # Remove nums[i] from freq_map if its count becomes 0
            if freq_map[nums[i]] == 0:
                del freq_map[nums[i]]

        return total_count


class Solution6:
    """
    leetcode solution 6: Dynamic Programming - Optimized Iterative
    Runtime: 52 ms, faster than 92.41% of Python3 online submissions for The Number of Beautiful Subsets.
    Memory Usage: 16.6 MB, less than 84.32% of Python3 online submissions for The Number of Beautiful Subsets.
    """

    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        total_count = 1
        freq_map = defaultdict(dict)

        # Calculate frequencies based on remainder
        for num in nums:
            freq_map[num % k][num] = freq_map[num % k].get(num, 0) + 1

        # Iterate through each remainder group
        for fr in freq_map.values():
            prev_num, curr, prev1, prev2 = -k, 1, 1, 0

            # Iterate through each number in the current remainder group
            for num, freq in sorted(fr.items()):
                # Count of subsets skipping the current number
                skip = prev1

                # Count of subsets including the current number
                # Check if the current number and the previous number
                # form a beautiful pair
                if num - prev_num == k:
                    take = ((1 << freq) - 1) * prev2
                else:
                    take = ((1 << freq) - 1) * prev1

                # Store the total count for the current number
                curr = skip + take
                prev2, prev1 = prev1, curr
                prev_num = num
            total_count *= curr
        return total_count - 1


s = Solution()
tests = [
    (([2, 4, 6], 2),
     4),
]
for inp, exp in tests:
    res = s.beautifulSubsets(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
