"""
Leetcode
47. Permutations II (medium)
2022-05-12

Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.
"""

from typing import List



# leetcode solution
# Runtime: 68 ms, faster than 76.98% of Python3 online submissions for Permutations II.
# Memory Usage: 14.3 MB, less than 47.48% of Python3 online submissions for Permutations II.
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        results = []
        def backtrack(comb, counter):
            if len(comb) == len(nums):
                # make a deep copy of the resulting permutation,
                # since the permutation would be backtracked later.
                results.append(list(comb))
                return

            for num in counter:
                if counter[num] > 0:
                    # add this number into the current combination
                    comb.append(num)
                    counter[num] -= 1
                    # continue the exploration
                    backtrack(comb, counter)
                    # revert the choice for the next exploration
                    comb.pop()
                    counter[num] += 1

        backtrack([], Counter(nums))

        return results



s = Solution()
tests = [
    [1,1,2],
    [1,2,3]
]
for t in tests:
    print(t)
    print(s.permuteUnique(t))
    print()
