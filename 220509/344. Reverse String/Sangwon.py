class Solution:
    def reverseString(self, s: List[str]) -> None:
        i = 0
        j = len(s)-1
        def reverse(i, j, s):
            if i >= j:
                return 
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
            return reverse(i+1, j-1, s)
        reverse(i, j, s)
    
