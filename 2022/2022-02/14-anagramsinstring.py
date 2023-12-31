'''
Leetcode
438. Find All Anagrams in a String (medium)
2022-02-02
'''

'''
Given two strings s and p, return an array of all the start indices of 
p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a 
different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
'''

from typing import List



# Try 1
# brute force check every index
# Runtime: 2008 ms, faster than 8.00% of Python3 online submissions for Find All Anagrams in a String.
# Memory Usage: 15.3 MB, less than 41.94% of Python3 online submissions for Find All Anagrams in a String.
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        find = self.count_letters(p)
        out = []
        for i in range(len(s) - len(p) + 1):
            to_check = self.count_letters( s[i:i+len(p)] )
            if to_check == find: out.append(i)
        return out
    
    def count_letters(self, word):
        letters = "abcdefghijklmnopqrstuvwxyz"
        out = {}
        for c in letters:
            n = word.count(c)
            if n > 0: out[c] = n
        return out



# Try 2
# modified Try1
# Time Limit Exceeded
class Solution2:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ls, lp, out = len(s), len(p), []
        to_find = sorted(p)
        for i in range(ls - lp + 1):
            if sorted( s[i:i+lp] ) == to_find: out.append(i)
        return out



# Try 3
# sliding windows with hashmap
# https://leetcode.com/problems/find-all-anagrams-in-a-string/discuss/1737985/Python3-SLIDING-WINDOW-+-HASH-TABLE-Explained
# https://leetcode.com/problems/find-all-anagrams-in-a-string/discuss/1738052/A-very-deep-EXPLANATION-oror-Solved-without-using-HashTable
# Runtime: 176 ms, faster than 49.18% of Python3 online submissions for Find All Anagrams in a String.
# Memory Usage: 15.2 MB, less than 77.41% of Python3 online submissions for Find All Anagrams in a String.
class Solution3:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ls, lp = len(s), len(p)
        hashmap, out = {}, []
        
        # fill hashmap with chars from "p"
        for c in "abcdefghijklmnopqrstuvwxyz":
            hashmap[c] = p.count(c)
        
        # sliding window (of size len(p)): 
        # substract char in window from hashmap, 
        # if hashmap becomes all zeroes, that means the same chars and frequency 
        # of chars in window and hashmap, a.k.a. they are anagrams
        for i in range(ls - lp + 1):

            # first pass
            if i == 0:
                for j in range(lp):
                    hashmap[ s[j] ] -= 1

            # slide window: add back to hashmap char that is no longer in window, 
            # and substract char that is new
            else:
                hashmap[ s[i - 1] ] += 1
                hashmap[ s[i + lp - 1] ] -= 1
            
            # check
            if all(v == 0 for v in hashmap.values()):
                out.append(i)

        return out



tests = [
    ["cbaebabacd", "abc"],
    ["abab", "ab"]
]
solution = Solution3()
for test in tests:
    print(f'test: {test}')
    print(f'out:  {solution.findAnagrams(test[0], test[1])}')
