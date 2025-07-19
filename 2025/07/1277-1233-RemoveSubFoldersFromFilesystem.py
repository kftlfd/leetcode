"""
Leetcode
2025-07-19
1233. Remove Sub-Folders from the Filesystem
Medium

Given a list of folders folder, return the folders after removing all sub-folders in those folders. You may return the answer in any order.

If a folder[i] is located within another folder[j], it is called a sub-folder of it. A sub-folder of folder[j] must start with folder[j], followed by a "/". For example, "/a/b" is a sub-folder of "/a", but "/b" is not a sub-folder of "/a/b/c".

The format of a path is one or more concatenated strings of the form: '/' followed by one or more lowercase English letters.

    For example, "/leetcode" and "/leetcode/problems" are valid paths while an empty string and "/" are not.

 

Example 1:

Input: folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
Output: ["/a","/c/d","/c/f"]
Explanation: Folders "/a/b" is a subfolder of "/a" and "/c/d/e" is inside of folder "/c/d" in our filesystem.

Example 2:

Input: folder = ["/a","/a/b/c","/a/b/d"]
Output: ["/a"]
Explanation: Folders "/a/b/c" and "/a/b/d" will be removed because they are subfolders of "/a".

Example 3:

Input: folder = ["/a/b/c","/a/b/ca","/a/b/d"]
Output: ["/a/b/c","/a/b/ca","/a/b/d"]

 

Constraints:

    1 <= folder.length <= 4 * 10^4
    2 <= folder[i].length <= 100
    folder[i] contains only lowercase letters and '/'.
    folder[i] always starts with the character '/'.
    Each folder name is unique.


Hint 1
Sort the folders lexicographically.
Hint 2
Insert the current element in an array and then loop until we get rid of all of their subfolders, repeat this until no element is left.
"""

from typing import List


class Solution:
    """
    Runtime 159ms Beats 27.22%
    Memory 42.22MB Beats 28.35%
    """

    class Node:
        def __init__(self):
            self.is_folder = False
            self.nxt = {}

    def removeSubfolders(self, folder: List[str]) -> List[str]:
        fs_root = self.Node()

        for path in folder:
            cur = fs_root
            for segm in path.split("/")[1:]:
                if segm not in cur.nxt:
                    cur.nxt[segm] = self.Node()
                cur = cur.nxt[segm]
            cur.is_folder = True

        ans = []

        def dfs(cur: Solution.Node, path: List[str]):
            if cur.is_folder:
                ans.append("/".join(path))
                return

            for segm, nxt_node in cur.nxt.items():
                path.append(segm)
                dfs(nxt_node, path)
                path.pop()

        dfs(fs_root, [""])

        return ans


class Solution1:
    """
    leetcode solution 1: Using Set
    Runtime 47ms Beats 67.70%
    Memory 30.50MB Beats 95.49%
    """

    def removeSubfolders(self, folder: List[str]) -> List[str]:
        # Create a set to store all folder paths for fast lookup
        folder_set = set(folder)
        result = []

        # Iterate through each folder to check if it's a sub-folder
        for f in folder:
            is_sub_folder = False
            prefix = f

            # Check all prefixes of the current folder path
            while prefix:
                pos = prefix.rfind("/")
                if pos == -1:
                    break

                # Reduce the prefix to its parent folder
                prefix = prefix[:pos]

                # If the parent folder exists in the set, mark as sub-folder
                if prefix in folder_set:
                    is_sub_folder = True
                    break

            # If not a sub-folder, add it to the result
            if not is_sub_folder:
                result.append(f)

        return result


class Solution2:
    """
    leetcode solution 2: Using Sorting
    Runtime 19ms Beats 94.36%
    Memory 30.67MB Beats 60.37%
    """

    def removeSubfolders(self, folder: List[str]) -> List[str]:
        # Sort the folders alphabetically
        folder = sorted(folder)

        # Initialize the result list and add the first folder
        result = [folder[0]]

        # Iterate through each folder and check if it's a sub-folder of the last added folder in the result
        for i in range(1, len(folder)):
            last_folder = result[-1]
            last_folder += "/"

            # Check if the current folder starts with the last added folder path
            if not folder[i].startswith(last_folder):
                result.append(folder[i])

        # Return the result containing only non-sub-folders
        return result
