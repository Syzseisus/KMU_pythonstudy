class Solution:
    def is_power(self, number):
        if number == 1: 
            return True
        elif number % 2 != 0:
            return False
        
        else:
            return self.is_power(number / 2)
    
    
    def isPowerOfTwo(self, n: int) -> bool:
        answer = False
        
        if n == 0:
            return False
        answer = self.is_power(n)
        return answer
