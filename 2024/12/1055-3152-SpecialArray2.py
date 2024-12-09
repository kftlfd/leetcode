"""
Leetcode
2024-12-09
3152. Special Array II
Medium

An array is considered special if every pair of its adjacent elements contains two numbers with different parity.

You are given an array of integer nums and a 2D integer matrix queries, where for queries[i] = [fromi, toi] your task is to check that subarray nums[fromi..toi] is special or not.

Return an array of booleans answer such that answer[i] is true if nums[fromi..toi] is special.

 

Example 1:

Input: nums = [3,4,1,2,6], queries = [[0,4]]

Output: [false]

Explanation:

The subarray is [3,4,1,2,6]. 2 and 6 are both even.

Example 2:

Input: nums = [4,3,1,6], queries = [[0,2],[2,3]]

Output: [false,true]

Explanation:

    The subarray is [4,3,1]. 3 and 1 are both odd. So the answer to this query is false.
    The subarray is [1,6]. There is only one pair: (1,6) and it contains numbers with different parity. So the answer to this query is true.

 

Constraints:

    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^5
    1 <= queries.length <= 10^5
    queries[i].length == 2
    0 <= queries[i][0] <= queries[i][1] <= nums.length - 1

Hints:
- Try to split the array into some non-intersected continuous special subarrays.
- For each query check that the first and the last elements of that query are in the same subarray or not.
"""

from typing import List


class Solution:
    """
    Runtime: 382 ms, faster than 5.09% of Python3 online submissions for Special Array II.
    Memory Usage: 48 MB, less than 21.46% of Python3 online submissions for Special Array II.
    """

    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        subarrs = [[0, 0]]
        prev_parity = (nums[0] % 2) ^ 1

        for i, num in enumerate(nums):
            cur_parity = num % 2
            if cur_parity != prev_parity:
                subarrs[-1][1] = i
                prev_parity = cur_parity
            else:
                subarrs.append([i, i])

        n = len(subarrs)

        def get_subarr_idx(i: int) -> int:
            lo = 0
            hi = n
            while lo < hi:
                mid = (lo + hi) // 2
                if subarrs[mid][1] < i:
                    lo = mid + 1
                elif subarrs[mid][0] > i:
                    hi = mid
                else:
                    return mid
            return -1

        return [get_subarr_idx(s) == get_subarr_idx(e) for s, e in queries]


class Solution1:
    """
    leetcode solution 1: binary search
    Runtime: 63 ms, faster than 41.67% of Python3 online submissions for Special Array II.
    Memory Usage: 47 MB, less than 32.39% of Python3 online submissions for Special Array II.
    """

    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        ans = [False] * len(queries)
        violating_indices = []

        for i in range(1, len(nums)):
            # same parity, found violating index
            if nums[i] % 2 == nums[i - 1] % 2:
                violating_indices.append(i)

        for i, (start, end) in enumerate(queries):
            found_violating_index = self.binarySearch(
                start + 1, end, violating_indices
            )

            if found_violating_index:
                ans[i] = False
            else:
                ans[i] = True

        return ans

    def binarySearch(
        self, start: int, end: int, violating_indices: List[int]
    ) -> bool:
        left = 0
        right = len(violating_indices) - 1
        while left <= right:
            mid = left + (right - left) // 2
            violating_index = violating_indices[mid]

            if violating_index < start:
                # check right half
                left = mid + 1
            elif violating_index > end:
                # check left half
                right = mid - 1
            else:
                # violatingIndex falls in between start and end
                return True

        return False


class Solution2:
    """
    leetcode solution 2: Prefix Sum
    Runtime: 40 ms, faster than 70.83% of Python3 online submissions for Special Array II.
    Memory Usage: 46.8 MB, less than 34.82% of Python3 online submissions for Special Array II.
    """

    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        ans = [False] * len(queries)
        prefix = [0] * len(nums)
        prefix[0] = 0

        for i in range(1, len(nums)):
            if nums[i] % 2 == nums[i - 1] % 2:
                # new violative index found
                prefix[i] = prefix[i - 1] + 1
            else:
                prefix[i] = prefix[i - 1]

        for i, (start, end) in enumerate(queries):
            ans[i] = prefix[end] - prefix[start] == 0

        return ans


class Solution3:
    """
    leetcode solution 3: Sliding Window
    Runtime: 63 ms, faster than 41.67% of Python3 online submissions for Special Array II.
    Memory Usage: 46.7 MB, less than 42.51% of Python3 online submissions for Special Array II.
    """

    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        max_reach = [0] * n
        end = 0

        # Step 1: Compute the maximum reachable index for each starting index
        for start in range(n):
            # Ensure 'end' always starts from the current index or beyond
            end = max(end, start)
            # Expand 'end' as long as adjacent elements have different parity
            while end < n - 1 and nums[end] % 2 != nums[end + 1] % 2:
                end += 1
            # Store the farthest index reachable from 'start'
            max_reach[start] = end

        ans = []

        # Step 2: Answer each query based on precomputed 'max_reach'
        for start, end_query in queries:
            # Check if the query range [start, end] lies within the max reachable range
            ans.append(end_query <= max_reach[start])
        return ans
