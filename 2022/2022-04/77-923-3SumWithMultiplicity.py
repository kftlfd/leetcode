"""
Leetcode
923. 3Sum With Multiplicity (medium)
2022-04-06

Given an integer array arr, and an integer target, return the number of 
tuples i, j, k such that i < j < k and arr[i] + arr[j] + arr[k] == target.

As the answer can be very large, return it modulo 109 + 7.
"""

from typing import List



# leetcode solution
# https://leetcode.com/problems/3sum-with-multiplicity/solution/
# Runtime: 106 ms, faster than 70.93% of Python3 online submissions for 3Sum With Multiplicity.
# Memory Usage: 14.1 MB, less than 62.21% of Python3 online submissions for 3Sum With Multiplicity.
class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:

        MOD = 10**9 + 7
        count = collections.Counter(arr)
        keys = sorted(count)

        ans = 0

        # Now, let's do a 3sum on "keys", for i <= j <= k.
        # We will use count to add the correct contribution to ans.
        for i, x in enumerate(keys):
            T = target - x
            j = i
            k = len(keys) - 1
            while j <= k:
                y = keys[j]
                z = keys[k]
                if y + z < T:
                    j += 1
                elif y + z > T:
                    k -= 1
                else: # x+y+z == T, now calculate the size of the contribution
                    if i < j < k:
                        ans += count[x] * count[y] * count[z]
                    elif i == j < k:
                        ans += count[x] * (count[x] - 1) / 2 * count[z]
                    elif i < j == k:
                        ans += count[x] * count[y] * (count[y] - 1) / 2
                    else:  # i == j == k
                        ans += count[x] * (count[x] - 1) * (count[x] - 2) / 6
                    j += 1
                    k -= 1

        return int(ans % MOD)



s = Solution()
tests = [
    [[1,1,2,2,3,3,4,4,5,5], 8],
    [[1,1,2,2,2,2], 5]
]
for t in tests:
    print(t)
    print(s.threeSumMulti(t[0], t[1]))
    print()
