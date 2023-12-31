"""
Leetcode
2007. Find Original Array From Doubled Array (medium)
2022-09-15

An integer array original is transformed into a doubled array changed by appending twice the value of every element in original, and then randomly shuffling the resulting array.

Given an array changed, return original if changed is a doubled array. If changed is not a doubled array, return an empty array. The elements in original may be returned in any order.

Example 1:
Input: changed = [1,3,4,2,6,8]
Output: [1,3,4]
Explanation: One possible original array could be [1,3,4]:
- Twice the value of 1 is 1 * 2 = 2.
- Twice the value of 3 is 3 * 2 = 6.
- Twice the value of 4 is 4 * 2 = 8.
Other original arrays could be [4,3,1] or [3,1,4].

Example 2:
Input: changed = [6,3,0,1]
Output: []
Explanation: changed is not a doubled array.

Example 3:
Input: changed = [1]
Output: []
Explanation: changed is not a doubled array.
"""

from typing import List
from collections import Counter

# Time Limit Exceeded


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:

        if not changed or len(changed) % 2 == 1:
            return []

        original = []
        changed.sort()

        for _ in range(len(changed) // 2):
            num = changed.pop(0)
            if (num * 2) in changed:
                original.append(num)
                changed.remove(num * 2)
            else:
                return []

        return original


# https://leetcode.com/problems/find-original-array-from-doubled-array/discuss/1470869/Python-Greedy-solution-explained
# Runtime: 4257 ms, faster than 5.13% of Python3 online submissions for Find Original Array From Doubled Array.
# Memory Usage: 32.6 MB, less than 58.13% of Python3 online submissions for Find Original Array From Doubled Array.
class Solution1:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        cnt, ans = Counter(changed), []
        for num in sorted(changed, key=lambda x: abs(x)):
            if cnt[num] == 0:
                continue
            if cnt[2*num] == 0:
                return []
            ans += [num]
            if num == 0 and cnt[num] <= 1:
                return []
            cnt[num] -= 1
            cnt[2*num] -= 1
        return ans


s = Solution1()
tests = [
    [1, 3, 4, 2, 6, 8],
    [6, 3, 0, 1],
    [1],
    [0, 0, 0, 0]
]
for t in tests:
    print(t)
    print(s.findOriginalArray(t))
    print()
