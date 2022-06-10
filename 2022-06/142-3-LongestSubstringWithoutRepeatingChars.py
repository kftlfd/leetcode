"""
Leetcode
3. Longest Substring Without Repeating Characters (medium)
2022-06-10

Given a string s, find the length of the longest substring without repeating characters.
"""



# Runtime: 148 ms, faster than 24.68% of Python3 online submissions for Longest Substring Without Repeating Characters.
# Memory Usage: 14 MB, less than 93.04% of Python3 online submissions for Longest Substring Without Repeating Characters.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if not s: return 0
        
        ht = {s[0]: 1}
        l = 0
        r = 1
        maxlen = 1

        while r < len(s):

            while ht.get(s[r], 0) == 1:
                ht[s[l]] = 0
                l += 1

            ht[s[r]] = 1
            r += 1
            maxlen = max(maxlen, r - l)

        return maxlen



# https://leetcode.com/problems/longest-substring-without-repeating-characters/discuss/1731/A-Python-solution-85ms-O(n)/2176
# Runtime: 106 ms, faster than 42.25% of Python3 online submissions for Longest Substring Without Repeating Characters.
# Memory Usage: 14.1 MB, less than 49.19% of Python3 online submissions for Longest Substring Without Repeating Characters.
class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        used = {}
        start = 0
        maxlen = 0

        for i, c in enumerate(s):
            if c in used and start <= used[c]:
                start = used[c] + 1
            else:
                maxlen = max(maxlen, i + 1 - start)
            used[c] = i
        
        return maxlen



s = Solution1()
tests = [
    "abcabcbb",
    "bbbbb",
    "pwwkew",
    "nnfdsisidjfnflajsprufbvhqlpdjmgnvhdyfkeh"
]
for t in tests:
    print(t)
    print(s.lengthOfLongestSubstring(t))
    print()
