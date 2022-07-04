"""
Leetcode
135. Candy (hard)
2022-07-04

There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

 - Each child must have at least one candy.
 - Children with a higher rating get more candies than their neighbors.

Return the minimum number of candies you need to have to distribute the candies to the children.

Example 1:
Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.

Example 2:
Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.
"""

from typing import List


# https://leetcode.com/problems/candy/discuss/1300194/Python-O(n)-time-solution-explained
# Runtime: 385 ms, faster than 7.25% of Python3 online submissions for Candy.
# Memory Usage: 16.8 MB, less than 74.92% of Python3 online submissions for Candy.
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        ans = [1] * n

        for i in range(n - 1):
            if ratings[i] < ratings[i+1]:
                ans[i+1] = max(1 + ans[i], ans[i+1])

        for i in range(n - 2, -1, -1):
            if ratings[i+1] < ratings[i]:
                ans[i] = max(1 + ans[i+1], ans[i])

        return sum(ans)


s = Solution()
tests = [
    [1, 0, 2],
    [1, 2, 2],
]
for t in tests:
    print(t)
    print(s.candy(t))
    print()
