'''
Leetcode
165. Compare Version Numbers (medium)
2022-02-25

Given two version numbers, version1 and version2, compare them.

Version numbers consist of one or more revisions joined by a 
dot '.'. Each revision consists of digits and may contain leading 
zeros. Every revision contains at least one character. Revisions 
are 0-indexed from left to right, with the leftmost revision being 
revision 0, the next revision being revision 1, and so on. For 
example 2.5.33 and 0.1 are valid version numbers.

To compare version numbers, compare their revisions in left-to-right 
order. Revisions are compared using their integer value ignoring any 
leading zeros. This means that revisions 1 and 001 are considered 
equal. If a version number does not specify a revision at an index, 
then treat the revision as 0. For example, version 1.0 is less than 
version 1.1 because their revision 0s are the same, but their revision 
1s are 0 and 1 respectively, and 0 < 1.

Return the following:
 - If version1 < version2, return -1.
 - If version1 > version2, return 1.
 - Otherwise, return 0.
'''



# try 1
# Runtime: 48 ms, faster than 36.95% of Python3 online submissions for Compare Version Numbers.
# Memory Usage: 14 MB, less than 68.52% of Python3 online submissions for Compare Version Numbers.
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        
        v1 = [ int(x) for x in version1.split(sep='.')]
        v2 = [ int(x) for x in version2.split(sep='.')]
        m = max(len(v1), len(v2))
        pad = abs(len(v1) - len(v2))
        if pad:
            if len(v1) != m:
                v1 += [0] * pad
            else:
                v2 += [0] * pad

        for i in range(m):
            if v1[i] > v2[i]:
                return 1
            elif v1[i] < v2[i]:
                return -1

        return 0


tests = [
    ["1.1.1","1.1"],
    ['0.0.1', '0.0.1.1'],
    ["1.01", "1.001"],
    ["1.0", "1.0.0"],
    ["0.1", "1.1"]
]
s = Solution()
for test in tests:
    print(*test, "-->", s.compareVersion(test[0], test[1]))