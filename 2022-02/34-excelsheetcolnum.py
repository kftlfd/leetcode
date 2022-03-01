'''
Leetcode
171. Excel Sheet Column Number (easy)
2022-02-22

Given a string columnTitle that represents the column title 
as appear in an Excel sheet, return its corresponding column number.
'''



# try 1
# Runtime: 56 ms, faster than 27.42% of Python3 online submissions for Excel Sheet Column Number.
# Memory Usage: 13.9 MB, less than 83.72% of Python3 online submissions for Excel Sheet Column Number.
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        
        columnNumber = 0
        digit = 0
        
        for c in columnTitle[::-1]:
            columnNumber += (ord(c) - ord("A") + 1) * (26 ** digit)
            digit += 1

        return columnNumber



tests = [
    "A",
    "AB",
    "ABC"
]
sol = Solution()
for test in tests:
    print(f"{test}  -->  {sol.titleToNumber(test)}")