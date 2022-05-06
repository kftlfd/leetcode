"""
Leetcode
1209. Remove All Adjacent Duplicates in String II (medium)
2022-05-06

You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them, causing the left and the right side of the deleted substring to concatenate together.

We repeatedly make k duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.
"""



# try 1
# Time Limit Exceeded
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        def remove(s, k):
            stack = []            
            prev = None
            count = 0
            for c in s:
                stack.append(c)
                if c == prev:
                    count += 1
                    if count == k:
                        for _ in range(k): stack.pop()
                else:
                    prev = c
                    count = 1
            return stack
        
        s1 = [c for c in s]
        s2 = remove(s1, k)
        
        while len(s1) != len(s2):
            s1 = s2
            s2 = remove(s1, k)
            
        return ''.join(s2)



class Solution1:

    # https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/discuss/392933/JavaC++Python-Two-Pointers-and-Stack-Solution
    #     Runtime: 111 ms, faster than 89.64% of Python3 online submissions for Remove All Adjacent Duplicates in String II.
    # Memory Usage: 18.8 MB, less than 39.82% of Python3 online submissions for Remove All Adjacent Duplicates in String II.
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [['#', 0]]
        for c in s:
            if stack[-1][0] == c:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([c, 1])
        return ''.join(c * k for c, k in stack)

    # https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/discuss/1161100/Python-stack-solution-explained
    # Runtime: 168 ms, faster than 45.86% of Python3 online submissions for Remove All Adjacent Duplicates in String II.
    # Memory Usage: 18.7 MB, less than 39.82% of Python3 online submissions for Remove All Adjacent Duplicates in String II.
    def removeDuplicates2(self, s, k):
        stack = [["!", 1]]
        for elem in s:
            if elem == stack[-1][0]:
                stack[-1][1] += 1
            else:
                stack.append([elem, 1])
            
            while stack[-1][1] >= k:
                stack[-1][1] -= k
                if stack[-1][1] == 0: stack.pop()
        return "".join(i*j for i, j in stack[1:])



s = Solution()
tests = [
    ["abcd", 2],
    ["deeedbbcccbdaa", 3],
    ["pbbcggttciiippooaais", 2]
]
for t in tests:
    print(*t)
    print(s.removeDuplicates(t[0], t[1]))
    print()
