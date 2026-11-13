"""
Leetcode
2026-11-13
3420. Count Non-Decreasing Subarrays After K Operations
Hard

You are given an array nums of n integers and an integer k.

For each subarray of nums, you can apply up to k operations on it. In each operation, you increment any element of the subarray by 1.

Note that each subarray is considered independently, meaning changes made to one subarray do not persist to another.

Return the number of subarrays that you can make non-decreasing after performing at most k operations.

An array is said to be non-decreasing if each element is greater than or equal to its previous element, if it exists.

 

Example 1:

Input: nums = [6,3,1,2,4,4], k = 7

Output: 17

Explanation:

Out of all 21 possible subarrays of nums, only the subarrays [6, 3, 1], [6, 3, 1, 2], [6, 3, 1, 2, 4] and [6, 3, 1, 2, 4, 4] cannot be made non-decreasing after applying up to k = 7 operations. Thus, the number of non-decreasing subarrays is 21 - 4 = 17.

Example 2:

Input: nums = [6,3,1,3,6], k = 4

Output: 12

Explanation:

The subarray [3, 1, 3, 6] along with all subarrays of nums with three or fewer elements, except [6, 3, 1], can be made non-decreasing after k operations. There are 5 subarrays of a single element, 4 subarrays of two elements, and 2 subarrays of three elements except [6, 3, 1], so there are 1 + 5 + 4 + 2 = 12 subarrays that can be made non-decreasing.

 

Constraints:

    1 <= nums.length <= 105
    1 <= nums[i] <= 109
    1 <= k <= 109


Hint 1
Use a sparse table.
Hint 2
Compute sp[e][i] = [lastElement, operations] where operations is the number of operations required to make the subarray nums[i...i + 2^e - 1] non-decreasing, and lastElement be the value of the last element after the operations were applied on it.
Hint 3
How can we combine sp[a][i] with sp[b][i + 2^a] to find the answer for the subarray nums[i...i + 2^a + 2^b - 1]?
"""

import heapq
from typing import List


class Solution:
    """
    leetcode solution: Sliding Window
    Runtime 858ms Beats 17.95%
    Memory 51.56MB Beats 10.26%
    """

    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        operations = 0
        # Maintain the window maximum with a priority queue
        q = []
        # Record the set of elements covered by this index
        cnt = [[] for _ in range(n)]
        # Index of the first greater-or-equal element to the right
        pos = [n] * n
        # Decreasing monotonic stack
        st = []

        left = 0
        for right in range(n):
            # Maintain the monotonic stack
            while st and nums[right] >= nums[st[-1]]:
                pos[st[-1]] = right
                st.pop()
            # The stack top is the nearest greater element to the left of nums[right]
            if st:
                cnt[st[-1]].append(right)
            st.append(right)

            # The priority queue front is the window maximum
            heapq.heappush(q, (-nums[right], right))
            # Adding nums[right] increases the operation count
            operations += max(0, -q[0][0] - nums[right])

            # The minimum operation count exceeds k; shrink the window
            while operations > k:
                # Removing nums[left] from the window decreases the operation count
                for i in cnt[left]:
                    # Subtract the contribution
                    operations -= (nums[left] - nums[i]) * (
                        min(pos[i], right + 1) - i
                    )
                left += 1

            # Remove elements with indices less than left from the priority queue
            while q and q[0][1] < left:
                heapq.heappop(q)

            # There are right - left + 1 valid contiguous subarrays ending at right
            ans += right - left + 1

        return ans
