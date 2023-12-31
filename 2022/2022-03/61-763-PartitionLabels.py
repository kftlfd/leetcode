"""
Leetcode
763. Partition Labels (medium)
2022-03-21

You are given a string s. We want to partition the string into as many 
parts as possible so that each letter appears in at most one part.

Note that the partition is done so that after concatenating all the 
parts in order, the resultant string should be s.

Return a list of integers representing the size of these parts.

Example 1:
Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.

Example 2:
Input: s = "eccbbbbdec"
Output: [10]
"""

from typing import List



# try 1
# Runtime: 56 ms, faster than 56.35% of Python3 online submissions for Partition Labels.
# Memory Usage: 13.9 MB, less than 78.97% of Python3 online submissions for Partition Labels.
class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        ht = {} # {letter: [first index, last index]}
        for i in range(len(s)):
            if s[i] not in ht:
                ht[s[i]] = [i,i]
            else:
                ht[s[i]][1] = i

        out = []
        tmp = ht[s[0]][1] # last occurence of the first letter
        size = 0
        for i in range(len(s) + 1):

            if i == len(s):
                out.append(size)

            elif ht[s[i]][0] <= tmp:
                tmp = max(tmp, ht[s[i]][1])
 
            else:
                out.append(size)
                size = 0
                tmp = ht[s[i]][1]

            size += 1

        return out



# leetcode solution
# Runtime: 40 ms, faster than 92.01% of Python3 online submissions for Partition Labels.
# Memory Usage: 13.8 MB, less than 78.97% of Python3 online submissions for Partition Labels.
class Solution1:
    def partitionLabels(self, s: str) -> List[int]:
        
        last = {c: i for i, c in enumerate(s)}
        start = 0
        end = 0
        ans = []
        for i, c in enumerate(s):
            end = max(end, last[c])
            if i == end:
                ans.append(i - start + 1)
                start = i + 1
            
        return ans



s = Solution1()
tests = [
    "eaaaabaaec",
    "ababcbacadefegdehijhklij",
    "eccbbbbdec"
]
for t in tests:
    print(t)
    print(s.partitionLabels(t))
    print()
