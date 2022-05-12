class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """   
        n = len(s) - 1
        
        def reverse(s, idx):
            # 홀수인데, index 중간까지 도달한 경우
            if n % 2 and idx == n / 2:
                return
            
            if idx > (n - idx):
                return
            
            tmp = s[idx]
            s[idx] = s[n-idx]
            s[n-idx] = tmp
            
            return reverse(s, idx+1)
            
        return reverse(s, 0)
