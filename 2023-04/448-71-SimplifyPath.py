"""
Leetcode
71. Simplify Path (medium)
2023-04-12

Given a string path, which is an absolute path (starting with a slash '/') to a file or directory in a Unix-style file system, convert it to the simplified canonical path.

In a Unix-style file system, a period '.' refers to the current directory, a double period '..' refers to the directory up a level, and any multiple consecutive slashes (i.e. '//') are treated as a single slash '/'. For this problem, any other format of periods such as '...' are treated as file/directory names.

The canonical path should have the following format:

    The path starts with a single slash '/'.
    Any two directories are separated by a single slash '/'.
    The path does not end with a trailing '/'.
    The path only contains the directories on the path from the root directory to the target file or directory (i.e., no period '.' or double period '..')

Return the simplified canonical path.

Example 1:
Input: path = "/home/"
Output: "/home"
Explanation: Note that there is no trailing slash after the last directory name.

Example 2:
Input: path = "/../"
Output: "/"
Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.

Example 3:
Input: path = "/home//foo/"
Output: "/home/foo"
Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.
"""


class Solution:
    """
    Runtime: 38 ms, faster than 38.74% of Python3 online submissions for Simplify Path.
    Memory Usage: 13.9 MB, less than 28.25% of Python3 online submissions for Simplify Path.
    """

    def simplifyPath(self, path: str) -> str:
        path_stack = []

        for node in path.split('/'):
            if node in ('', '.'):
                continue
            if node == '..':
                if path_stack:
                    path_stack.pop()
            else:
                path_stack.append(node)

        return '/' + '/'.join(path_stack)


s = Solution()
tests = [
    ("/home/",
     "/home"),

    ("/../",
     "/"),

    ("/home//foo/",
     "/home/foo"),
]
for inp, exp in tests:
    res = s.simplifyPath(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
