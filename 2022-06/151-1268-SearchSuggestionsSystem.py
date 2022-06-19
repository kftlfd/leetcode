"""
Leetcode
1268. Search Suggestions System (medium)
2022-06-19

You are given an array of strings products and a string searchWord.

Design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

Return a list of lists of the suggested products after each character of searchWord is typed.
"""

from typing import List



# Runtime: 196 ms, faster than 61.91% of Python3 online submissions for Search Suggestions System.
# Memory Usage: 17.2 MB, less than 58.95% of Python3 online submissions for Search Suggestions System.
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        result = []        
        start = 0
        prefix = ''
        for c in searchWord:
            prefix += c
            suggestions = []
            i = self.binarySearch(products, prefix, start)
            if i > -1:
                suggestions.append(products[i])
                for j in range(1, 3):
                    if i+j >= len(products) or products[i+j][:len(prefix)] != prefix: break
                    suggestions.append(products[i+j])
            result.append(suggestions)
            start = i
        return result
            
    def binarySearch(self, words, prefix, start):
        l = start
        r = len(words) - 1
        out = -1
        while l <= r:
            m = (l + r) // 2
            if words[m][:len(prefix)] == prefix:
                out = m
                break
            elif words[m][:len(prefix)] > prefix:
                r = m - 1
            else:
                l = m + 1
        while out > 0:
            if words[out - 1][:len(prefix)] == prefix:
                out -= 1
            else: break
        return out
                


s = Solution()
tests = [
    (["havana"], "tatiana"),
    (["bags","baggage","banner","box","cloths"], "bags"),
    (["mobile","mouse","moneypot","monitor","mousepad"], "mouse"),
    (["havana"], "havana"),
]
for t in tests:
    print(t)
    print(s.suggestedProducts(t[0], t[1]))
    print()
