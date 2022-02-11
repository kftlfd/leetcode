'''
Leetcode
567. Permutation in String (medium)
2022-02-11

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.
https://leetcode.com/problems/permutation-in-string/
'''



# Try 1
# Runtime: 98 ms, faster than 64.17% of Python3 online submissions for Permutation in String.
# Memory Usage: 13.9 MB, less than 93.32% of Python3 online submissions for Permutation in String.
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        check = {}
        for i in range(len(s1)):
            check[s1[i]] = check.get(s1[i], 0) - 1
        
        # sliding window
        for i in range(len(s2) + 1 - len(s1)):
            
            if i == 0:
                for j in range(len(s1)):
                    check[s2[j]] = check.get(s2[j], 0) + 1
            
            else:
                # slide window
                check[s2[i - 1]] -= 1
                check[s2[i + len(s1) - 1]] = check.get(s2[i + len(s1) - 1], 0) + 1
            
            if all(x == 0 for x in check.values()): return True
            
        return False
                


tests = [
    # ["abc", "cba"],
    # ["g", "bbbbbbbbbbbbbbbbbbbbgr"],
    ["abc", "ccccbbbbaaaa"]
]
solution = Solution()
for test in tests:
    print(f'test: {test}\tout: {solution.checkInclusion(test[0], test[1])}')