"""
Leetcode
609. Find Duplicate File in System (medium)
2022-09-20

Given a list paths of directory info, including the directory path, and all the files with contents in this directory, return all the duplicate files in the file system in terms of their paths. You may return the answer in any order.

A group of duplicate files consists of at least two files that have the same content.

A single directory info string in the input list has the following format:

 - "root/d1/d2/.../dm f1.txt(f1_content) f2.txt(f2_content) ... fn.txt(fn_content)"

It means there are n files (f1.txt, f2.txt ... fn.txt) with content (f1_content, f2_content ... fn_content) respectively in the directory "root/d1/d2/.../dm". Note that n >= 1 and m >= 0. If m = 0, it means the directory is just the root directory.

The output is a list of groups of duplicate file paths. For each group, it contains all the file paths of the files that have the same content. A file path is a string that has the following format:

 - "directory_path/file_name.txt"

Example 1:
Input: paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]
Output: [["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]]

Example 2:
Input: paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)"]
Output: [["root/a/2.txt","root/c/d/4.txt"],["root/a/1.txt","root/c/3.txt"]]
"""

from typing import List
from collections import defaultdict


# https://leetcode.com/problems/find-duplicate-file-in-system/discuss/1215599/Python-Solution-using-defaultdict-explained
# Runtime: 86 ms, faster than 98.99% of Python3 online submissions for Find Duplicate File in System.
# Memory Usage: 24 MB, less than 54.47% of Python3 online submissions for Find Duplicate File in System.
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for path in paths:
            l = path.split()
            for i in range(1, len(l)):
                name, cont = l[i].split("(")
                ans[cont[:-1]].append(l[0] + "/" + name)
        return [i for i in ans.values() if len(i) > 1]


s = Solution()
tests = [
    ["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)",
     "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"],
    ["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)",
     "root/c/d 4.txt(efgh)"],
]
for t in tests:
    print(t)
    print(s.findDuplicate(t))
    print()
