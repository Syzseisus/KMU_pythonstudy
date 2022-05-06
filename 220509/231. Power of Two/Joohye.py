# 재귀, 2의 거듭제곱 수 구하는 문제
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # 0 or 음수면 False
        if n <= 0:  
            return False
        # 2의 거듭제곱수 조건 1)짝수 2)2로 한번더 나눴을때도 짝수(재귀사용)
        elif (n % 2 == 0 and self.isPowerOfTwo(n / 2)) or n == 1: 
            return True
        # 0보다 크지만, 위 조건을 만족하지 못한 경우 = 거듭제곱수가 아닌 경우
        else:
            return False
