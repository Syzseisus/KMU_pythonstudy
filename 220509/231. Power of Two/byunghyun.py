class Solution:
    # input이 3이라면
    # 3,0 -> 1, 1 === False
    # input이 8이라면
    # 8,0 -> 4,0 -> 2,0 -> 1,0 === True
    # input이 12라면
    # 12,0 -> 6,0 -> 3,0 -> 1,1 === False
    def solution(self, n, h):
        if h == 1 and n != 1:
            return False
        elif n == 1 and h == 0:
            return True
        return self.solution(n // 2, n % 2)
    
    def isPowerOfTwo(self, n: int) -> bool:
        # n이 0이라면 계산할 필요 X
        if n == 0:
            return False
        
        # 재귀 호출
        return self.solution(n, 0)
