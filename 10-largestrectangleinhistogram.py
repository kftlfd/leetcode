'''
Leetcode
84. Largest Rectangle in Histogram (Hard)
2022-01-29
'''

# Given an array of integers heights representing the 
# histogram's bar height where the width of each bar is 1,
# return the area of the largest rectangle in the histogram.


# solution taken from:
# https://medium.com/techtofreedom/algorithms-for-interview-2-monotonic-stack-462251689da8

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ret = 0
        mono_stack = []
        heights.append(0)
        for i, v in enumerate(heights):
            while mono_stack and heights[mono_stack[-1]] > v:
                height = heights[mono_stack.pop()]
                if mono_stack:
                    length = i - mono_stack[-1]-1
                else:
                    length = i
                ret = max(ret, height * length)
            mono_stack.append(i)
        return ret
