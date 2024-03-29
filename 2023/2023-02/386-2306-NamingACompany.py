"""
Leetcode
2306. Naming a Company (hard)
2023-02-09

You are given an array of strings ideas that represents a list of names to be used in the process of naming a company. The process of naming a company is as follows:

    Choose 2 distinct names from ideas, call them ideaA and ideaB.
    Swap the first letters of ideaA and ideaB with each other.
    If both of the new names are not found in the original ideas, then the name ideaA ideaB (the concatenation of ideaA and ideaB, separated by a space) is a valid company name.
    Otherwise, it is not a valid name.

Return the number of distinct valid names for the company.

Example 1:
Input: ideas = ["coffee","donuts","time","toffee"]
Output: 6
Explanation: The following selections are valid:
- ("coffee", "donuts"): The company name created is "doffee conuts".
- ("donuts", "coffee"): The company name created is "conuts doffee".
- ("donuts", "time"): The company name created is "tonuts dime".
- ("donuts", "toffee"): The company name created is "tonuts doffee".
- ("time", "donuts"): The company name created is "dime tonuts".
- ("toffee", "donuts"): The company name created is "doffee tonuts".
Therefore, there are a total of 6 distinct company names.

The following are some examples of invalid selections:
- ("coffee", "time"): The name "toffee" formed after swapping already exists in the original array.
- ("time", "toffee"): Both names are still the same after swapping and exist in the original array.
- ("coffee", "toffee"): Both names formed after swapping already exist in the original array.

Example 2:
Input: ideas = ["lack","back"]
Output: 0
Explanation: There are no valid selections. Therefore, 0 is returned.
"""

from typing import List, Optional


class Solution:
    """
    naive brute force
    Time Limit Exceeded. 68 / 89 test cases passed.
    """

    def distinctNames(self, ideas: List[str]) -> int:
        ans = 0
        for A in range(len(ideas)):
            for B in range(A + 1, len(ideas)):
                if ideas[A] != ideas[B] and \
                   ideas[B][0] + ideas[A][1:] not in ideas and \
                   ideas[A][0] + ideas[B][1:] not in ideas:
                    ans += 2
        return ans


class Solution1:
    """
    leetcode solution
    Runtime: 554 ms, faster than 95.65% of Python3 online submissions for Naming a Company.
    Memory Usage: 28.8 MB, less than 28.26% of Python3 online submissions for Naming a Company.
    """

    def distinctNames(self, ideas: List[str]) -> int:
        ans = 0

        # Group idea by their initials.
        initial_groups = [set() for _ in range(26)]
        for idea in ideas:
            initial_groups[ord(idea[0]) - ord('a')].add(idea[1:])

        # Calculate number of valid names from every pair of groups.
        for i in range(25):
            for j in range(i+1, 26):
                # Get the number of mutual suffixes.
                num_of_mutual = len(initial_groups[i] & initial_groups[j])

                # Valid names are only from distinct suffixes in both groups.
                # Since we can swap a with b and swap b with a to create two valid names, multiple answer by 2.
                ans += 2 * \
                    (len(initial_groups[i]) - num_of_mutual) * \
                    (len(initial_groups[j]) - num_of_mutual)

        return ans


s = Solution1()
tests = [
    (["coffee", "donuts", "time", "toffee"],
     6),

    (["lack", "back"],
     0)
]
for inp, exp in tests:
    res = s.distinctNames(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
