"""
Leetcode
1838. Frequency of the Most Frequent Element (medium)
2023-11-19

The frequency of an element is the number of times it occurs in an array.

You are given an integer array nums and an integer k. In one operation, you can choose an index of nums and increment the element at that index by 1.

Return the maximum possible frequency of an element after performing at most k operations.

 

Example 1:

Input: nums = [1,2,4], k = 5
Output: 3
Explanation: Increment the first element three times and the second element two times to make nums = [4,4,4].
4 has a frequency of 3.

Example 2:

Input: nums = [1,4,8,13], k = 5
Output: 2
Explanation: There are multiple optimal solutions:
- Increment the first element three times to make nums = [4,4,8,13]. 4 has a frequency of 2.
- Increment the second element four times to make nums = [1,8,8,13]. 8 has a frequency of 2.
- Increment the third element five times to make nums = [1,4,13,13]. 13 has a frequency of 2.

Example 3:

Input: nums = [3,9,6], k = 2
Output: 1

 

Constraints:

    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^5
    1 <= k <= 10^5
"""

from typing import List
from collections import Counter


class Solution:
    """
    Wrong Answer
    """

    def maxFrequency(self, nums: List[int], k: int) -> int:

        cnt = Counter(nums)

        freqs = sorted(((f, k) for k, f in cnt.items()),
                       key=lambda x: (-x[0], -x[1]))

        max_freq = freqs[0][0]

        ans = 1

        for freq, num in freqs:
            if freq + k <= max_freq:
                break

            cur_ans = freq
            nxt_num = num - 1
            ops_left = k
            while ops_left > 0 and nxt_num > 0:
                while nxt_num in cnt and cnt[nxt_num] > 0:
                    add = num - nxt_num
                    if add <= ops_left:
                        cur_ans += 1
                        cnt[nxt_num] -= 1
                        ops_left -= add
                    else:
                        break
                if ops_left > 0:
                    nxt_num -= 1
                else:
                    break

            ans = max(ans, cur_ans)

        return ans


class Solution1:
    """
    leetcode solution 1: Sliding Window
    Runtime: 1159 ms, faster than 60.21% of Python3 online submissions for Frequency of the Most Frequent Element.
    Memory Usage: 30.9 MB, less than 85.86% of Python3 online submissions for Frequency of the Most Frequent Element.
    """

    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        left = 0
        ans = 0
        cur = 0

        for right, target in enumerate(nums):
            cur += target

            while (right - left + 1) * target - cur > k:
                cur -= nums[left]
                left += 1

            ans = max(ans, right - left + 1)

        return ans


class Solution2:
    """
    leetcode solution 2: Advanced Sliding Window
    Runtime: 1003 ms, faster than 97.02% of Python3 online submissions for Frequency of the Most Frequent Element.
    Memory Usage: 31 MB, less than 85.86% of Python3 online submissions for Frequency of the Most Frequent Element.
    """

    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        left = 0
        cur = 0

        for right, target in enumerate(nums):
            cur += target

            if (right - left + 1) * target - cur > k:
                cur -= nums[left]
                left += 1

        return len(nums) - left


class Solution3:
    """
    leetcode solution 3: Binary Search
    Runtime: 3923 ms, faster than 5.00% of Python3 online submissions for Frequency of the Most Frequent Element.
    Memory Usage: 30.4 MB, less than 94.99% of Python3 online submissions for Frequency of the Most Frequent Element.
    """

    def maxFrequency(self, nums: List[int], k: int) -> int:

        def check(i):
            target = nums[i]
            left = 0
            right = i
            best = i

            while left <= right:
                mid = (left + right) // 2
                count = i - mid + 1
                final_sum = count * target
                original_sum = prefix[i] - prefix[mid] + nums[mid]
                operations_required = final_sum - original_sum

                if operations_required > k:
                    left = mid + 1
                else:
                    best = mid
                    right = mid - 1

            return i - best + 1

        nums.sort()
        prefix = [nums[0]]

        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[-1])

        ans = 0
        for i in range(len(nums)):
            ans = max(ans, check(i))

        return ans


s = Solution()
tests = [
    (([1, 2, 4], 5),
     3),

    (([1, 4, 8, 13], 5),
     2),

    (([3, 9, 6], 2),
     1),

    (([9940, 9995, 9944, 9937, 9941, 9952, 9907, 9952, 9987, 9964, 9940, 9914, 9941, 9933, 9912, 9934, 9980, 9907, 9980, 9944, 9910, 9997], 7925),
     22),
]
for inp, exp in tests:
    res = s.maxFrequency(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
