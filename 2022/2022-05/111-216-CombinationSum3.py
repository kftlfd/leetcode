"""
Leetcode
216. Combination Sum III (medium)
2022-05-10

Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

 - Only numbers 1 through 9 are used.
 - Each number is used at most once.

Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

Example 1:
Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.

Example 2:
Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.

Example 3:
Input: k = 4, n = 1
Output: []
Explanation: There are no valid combinations.
Using 4 different numbers in the range [1,9], the smallest sum we can get is 1+2+3+4 = 10 and since 10 > 1, there are no valid combination.
"""

from typing import List



# try 1 - brute-force
# Runtime: 43 ms, faster than 54.48% of Python3 online submissions for Combination Sum III.
# Memory Usage: 13.9 MB, less than 29.87% of Python3 online submissions for Combination Sum III.
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        # generate all combinations of k numbers
        out = [[x] for x in range(1,10)]
        for _ in range(k - 1):
            for i in range(len(out)):
                comb = out.pop(0)
                for j in range(comb[-1] + 1, 10):
                    out.append(comb + [j])

        # filter results
        for i in range(len(out))[::-1]:
            if len(out[i]) != k or sum(out[i]) != n:
                out.pop(i)

        return out



s = Solution()
tests = [
    [3, 7],
    [3, 9],
    [4, 1]
]
for t in tests:
    print(t)
    print(s.combinationSum3(t[0], t[1]))
    print()
