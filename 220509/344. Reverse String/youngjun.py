class Solution(object):
    def reverseString(self, s):
        if len(s) == 1:
            return s
        return [s[-1]] + reverseString(s[0:-1])
