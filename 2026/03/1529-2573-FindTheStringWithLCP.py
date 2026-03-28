"""
Leetcode
2026-03-28
2573. Find the String with LCP
Hard

We define the lcp matrix of any 0-indexed string word of n lowercase English letters as an n x n grid such that:

    lcp[i][j] is equal to the length of the longest common prefix between the substrings word[i,n-1] and word[j,n-1].

Given an n x n matrix lcp, return the alphabetically smallest string word that corresponds to lcp. If there is no such string, return an empty string.

A string a is lexicographically smaller than a string b (of the same length) if in the first position where a and b differ, string a has a letter that appears earlier in the alphabet than the corresponding letter in b. For example, "aabd" is lexicographically smaller than "aaca" because the first position they differ is at the third letter, and 'b' comes before 'c'.

 

Example 1:

Input: lcp = [[4,0,2,0],[0,3,0,1],[2,0,2,0],[0,1,0,1]]
Output: "abab"
Explanation: lcp corresponds to any 4 letter string with two alternating letters. The lexicographically smallest of them is "abab".

Example 2:

Input: lcp = [[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,1]]
Output: "aaaa"
Explanation: lcp corresponds to any 4 letter string with a single distinct letter. The lexicographically smallest of them is "aaaa". 

Example 3:

Input: lcp = [[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,3]]
Output: ""
Explanation: lcp[3][3] cannot be equal to 3 since word[3,...,3] consists of only a single letter; Thus, no answer exists.

 

Constraints:

    1 <= n == lcp.length == lcp[i].length <= 1000
    0 <= lcp[i][j] <= n


Hint 1
Use the LCP array to determine which groups of elements must be equal.
Hint 2
Match the smallest letter to the group that contains the smallest unassigned index.
Hint 3
Build the LCP matrix of the resulting string then check if it is equal to the target LCP.
"""

from typing import List


class Solution1:
    """
    leetcode solution: Greedy Construction
    Runtime 124ms Beats 100.00%
    Memory 73.09MB Beats 77.78%
    """

    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        word = [""] * n
        current = ord("a")

        # construct the string starting from 'a' to 'z' sequentially
        for i in range(n):
            if not word[i]:
                if current > ord("z"):
                    return ""
                word[i] = chr(current)
                for j in range(i + 1, n):
                    if lcp[i][j]:
                        word[j] = word[i]
                current += 1

        # verify if the constructed string meets the LCP matrix requirements
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if word[i] != word[j]:
                    if lcp[i][j]:
                        return ""
                else:
                    if i == n - 1 or j == n - 1:
                        if lcp[i][j] != 1:
                            return ""
                    else:
                        if lcp[i][j] != lcp[i + 1][j + 1] + 1:
                            return ""

        return "".join(word)
