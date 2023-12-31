'''
Leetcode
316. Remove Duplicate Letters (medium)
2022-03-18

Given a string s, remove duplicate letters so that every letter appears
once and only once. You must make sure your result is the smallest in
lexicographical order among all possible results.

Example 1:
Input: s = "bcabc"
Output: "abc"

Example 2:
Input: s = "cbacdcbc"
Output: "acdb"
'''


# based on
# https://leetcode.com/problems/remove-duplicate-letters/discuss/1859410/JavaC++-DETAILED-+-VISUALLY-EXPLAINED-!!
# Runtime: 63 ms, faster than 34.23% of Python3 online submissions for Remove Duplicate Letters.
# Memory Usage: 13.9 MB, less than 87.68% of Python3 online submissions for Remove Duplicate Letters.
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:

        last_indexes = {}
        for i in range(len(s) - 1, -1, -1):
            if s[i] not in last_indexes.keys(): last_indexes[s[i]] = i

        st = []

        for i in range(len(s)):

            if s[i] in st: continue

            while st and ord(s[i]) < ord(st[-1]) and i < last_indexes[st[-1]]:
                st.pop()

            st.append(s[i])

        return ''.join(st)



# same approach, slight differences in implementation
# https://leetcode.com/problems/remove-duplicate-letters/discuss/1860300/93-Faster-oror-Python-Simple-Python-Solution-Using-Stack-and-Iterative-Approach
# Runtime: 56 ms, faster than 48.34% of Python3 online submissions for Remove Duplicate Letters.
# Memory Usage: 13.8 MB, less than 99.33% of Python3 online submissions for Remove Duplicate Letters.
class Solution1:
    def removeDuplicateLetters(self, s: str) -> str:


        LastIndex = {}

        for i in range(len(s)):
            LastIndex[s[i]] = i

        stack = []
        AlreadySeen = set()

        for i in range(len(s)):

            if s[i] in AlreadySeen:
                continue
            else:
                while stack and stack[-1] > s[i] and LastIndex[stack[-1]] > i:

                    AlreadySeen.remove(stack[-1])
                    stack.pop()

            stack.append(s[i])
            AlreadySeen.add(s[i])

        return ''.join(stack)



s = Solution1()
tests = [
    "bcabc",
    "cbacdcbc"
]
for t in tests:
    print(t)
    print('->', s.removeDuplicateLetters(t), '\n')
