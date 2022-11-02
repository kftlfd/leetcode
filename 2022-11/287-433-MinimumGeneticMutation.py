"""
Leetcode
433. Minimum Genetic Mutation (medium)
2022-11-02

A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.

Suppose we need to investigate a mutation from a gene string start to a gene string end where one mutation is defined as one single character changed in the gene string.

 - For example, "AACCGGTT" --> "AACCGGTA" is one mutation.

There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it a valid gene string.

Given the two gene strings start and end and the gene bank bank, return the minimum number of mutations needed to mutate from start to end. If there is no such a mutation, return -1.

Note that the starting point is assumed to be valid, so it might not be included in the bank.

Example 1:
Input: start = "AACCGGTT", end = "AACCGGTA", bank = ["AACCGGTA"]
Output: 1

Example 2:
Input: start = "AACCGGTT", end = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
Output: 2

Example 3:
Input: start = "AAAAACCC", end = "AACCCCCC", bank = ["AAAACCCC","AAACCCCC","AACCCCCC"]
Output: 3
"""

from typing import List, Optional
from queue import deque


# leetcode solution
# Runtime: 57 ms, faster than 46.48% of Python3 online submissions for Minimum Genetic Mutation.
# Memory Usage: 13.9 MB, less than 37.03% of Python3 online submissions for Minimum Genetic Mutation.
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        q = deque([(start, 0)])
        seen = set()
        seen.add(start)

        while q:
            node, steps = q.popleft()
            if node == end:
                return steps

            for c in "ACGT":
                for i in range(len(node)):
                    neighbor = node[:i] + c + node[i+1:]
                    if neighbor not in seen and neighbor in bank:
                        q.append((neighbor, steps + 1))
                        seen.add(neighbor)

        return -1


s = Solution()
tests = [
    (("AACCGGTT", "AACCGGTA", ["AACCGGTA"]),
     1),

    (("AACCGGTT", "AAACGGTA", ["AACCGGTA", "AACCGCTA", "AAACGGTA"]),
     2),

    (("AAAAACCC", "AACCCCCC", ["AAAACCCC", "AAACCCCC", "AACCCCCC"]),
     3),
]
for inp, exp in tests:
    start, end, bank = inp
    res = s.minMutation(start, end, bank)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
