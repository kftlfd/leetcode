'''
Leetcode
941. Valid Mountain Array (easy)
2022-01-25
'''


class Solution:
    def validMountainArray(self, arr):
        '''
        return true if and only if it is a valid mountain array.
        arr is a mountain array if and only if:
            1) arr.length >= 3
            2) There exists some i with 0 < i < arr.length - 1 such that:
                arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
                arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

        '''

        if len(arr) < 3:
            return False

        mountain = [True, False] # [increasing, decreasing]
        check = []

        # go through arr
        for i in range(1, len(arr)):

            # determine if numbers are rising
            if arr[i] == arr[i - 1]:
                return False
            elif arr[i] > arr[i - 1]:
                increasing = True
            else:
                increasing = False

            # write changes of direction to [check]
            if len(check) == 0 or check[len(check) - 1] != increasing:
                check.append(increasing)

            # if more than one change of direction, or started from decreasing
            if len(check) > 2 or check[0] == False:
                return False
        
        return check == mountain



class Solution2:
    # after looking at Leetcode's solution

    def validMountainArray(self, arr):

        i = 0 # index of first element of arr
        n = len(arr) - 1 # index of last element of arr

        if n < 2:
            return False

        # go up
        while i != n and arr[i + 1] > arr[i]:
            i += 1
        
        # check if not start or end
        if i == 0 or i == n:
            return False
        
        # go down
        while i != n and arr[i + 1] < arr[i]:
            i += 1
        
        return i == n



class Solution3:
    # based on solution by @ssomani7
    # https://leetcode.com/problems/valid-mountain-array/solution/382520

    def validMountainArray(self, arr):

        n = len(arr) - 1
        if n < 2: return False

        foundPeak = False

        for i in range(n):

            if arr[i] == arr[i + 1]: return False

            if not foundPeak: foundPeak = arr[i] > arr [i + 1]

            elif foundPeak and (arr[i] < arr[i + 1] or i == 1): return False

        return foundPeak



class Solution4:
    def validMountainArray(self, arr):
        # inspired by @artod
        # https://leetcode.com/problems/valid-mountain-array/discuss/1717215/Python3-DOUBLE-BARREL-(**)..:*-Explained
        # worst time (somehow)

        end = len(arr) - 1
        left, right = 0, end
        
        if end < 2: return False

        # go up from left
        # for i in range(right):
        #     if arr[i] >= arr[i + 1]:
        #         left = i
        #         break
        while left < end and arr[left] < arr[left + 1]:
            left += 1

        # go up from right
        # for i in range(right, 0, -1):
        #     if arr[i] >= arr[i - 1]:
        #         right = i
        #         break
        while right > 0 and arr[right] < arr[ right - 1]:
            right -= 1

        return left == right and left != 0 and right != end



tests = [
    [0],
    [0,1,2,3,2,1,0],
    [0,2,2,3,2,3,0],
    [1,2],
    [4,5,6,7],
    [4,3,2,1],
    [0,10,100,10,100,100],
    [3,5,5],
    [1,1,5,5,4,3],
    [0,1,2,100,400,10,-1]
]

for test in tests:
    print('test:', test, '\tout:', Solution4().validMountainArray(test))