'''
Leetcode
71. Simplify Path (medium)
2022-03-14

Given a string path, which is an absolute path (starting with 
a slash '/') to a file or directory in a Unix-style file system, 
convert it to the simplified canonical path.

In a Unix-style file system, a period '.' refers to the current 
directory, a double period '..' refers to the directory up a level, 
and any multiple consecutive slashes (i.e. '//') are treated as 
a single slash '/'. For this problem, any other format of periods 
such as '...' are treated as file/directory names.

The canonical path should have the following format:

 - The path starts with a single slash '/'.
 - Any two directories are separated by a single slash '/'.
 - The path does not end with a trailing '/'.
 - The path only contains the directories on the path from the root 
   directory to the target file or directory (i.e., no period '.' or 
   double period '..')

Return the simplified canonical path.
'''



# try 1
# Runtime: 67 ms, faster than 11.96% of Python3 online submissions for Simplify Path.
# Memory Usage: 14.1 MB, less than 32.22% of Python3 online submissions for Simplify Path.
class Solution:
    def simplifyPath(self, path: str) -> str:
        
        if not path: return path

        # remove slashes
        stack = path.split('/')
        stack[:] = [x for x in stack if x != '']

        # go through stack
        i = 0
        while i < len(stack):

            # remove single dots
            if stack[i] == '.':
                del stack[i]
                i -= 1

            # remove double dots
            elif stack[i] == '..':
                del stack[i]
                i -= 1
                if i != -1:
                    del stack[i]
                    i -= 1

            i += 1
        
        return '/' + '/'.join(stack)



# optimize try 1
# Runtime: 38 ms, faster than 73.28% of Python3 online submissions for Simplify Path.
# Memory Usage: 14 MB, less than 57.22% of Python3 online submissions for Simplify Path.
class Solution1:
    def simplifyPath(self, path: str) -> str:
        
        if not path: return path

        # remove slashes and single dots
        stack = path.split('/')
        stack[:] = [x for x in stack if x != '' and x != '.']

        # remove double dots
        i = 0
        while i < len(stack):
            if stack[i] == '..':
                del stack[i]
                if i != 0:
                    del stack[i-1]
                    i -= 1
            else: i += 1
        
        return '/' + '/'.join(stack)



# https://leetcode.com/problems/simplify-path/discuss/1050573/Python-Short-stack-solution-explained
# https://leetcode.com/problems/simplify-path/discuss/25691/9-lines-of-Python-code/24725
# Runtime: 35 ms, faster than 83.68% of Python3 online submissions for Simplify Path.
# Memory Usage: 13.8 MB, less than 87.69% of Python3 online submissions for Simplify Path.
class Solution2:
    def simplifyPath(self, path: str) -> str:
        
        stack = []

        for x in path.split('/'):
            if x == '..' and stack: stack.pop()
            elif x not in ['', '.', '..']: stack.append(x)
        
        return '/' + '/'.join(stack)



s = Solution2()
tests = [
    "/.",
    "/home/",
    "/../",
    "/home////foo/",
    "/home/./../.../foo/",
    "/home/home/home/home/home/../../../foo/",
    "/home/home/home/home/home/../../../../foo/"
]
for t in tests:
    print(t)
    print(s.simplifyPath(t), '\n')
