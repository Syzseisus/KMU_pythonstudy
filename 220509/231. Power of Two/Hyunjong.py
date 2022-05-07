class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 2로 //할때 2의 거듭제곱 형태면 1이 되고 아니면 0이 된다.
        if n==0: # 최종 나눈 값이 0 => 2의 거듭 제곱이 아님
            return False
        elif n ==1: # 최종 나눈 값이 1 => 2의 거듭 제곱
            return True
        elif n%2 !=0: # 2로 나눌 때 몫이 0이 아님
            return False
        else:
            return self.isPowerOfTwo(n//2)
          
""" 시도했다가 틀린 목록
import math
def isPowerOfTwo(n):
    num = math.log2(n)
    int_num = int(num)

    if (num - int_num != 0.0):
        return False

    return True
#  맨 처음에 생각난 방법 => math import가 안 된다 ㅠ

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def recursive(num):
            quotient  = num / 2
            remainder  = num % 2
            if remainder != 0: # 즉시 종료 조건
                return False
            if quotient == 1: # 끝까지 돌았을 때 종료조건
                if remainder == 0:
                    return True
                else: 
                    return False
            aws = recursive(quotient)
            return aws
        
        if (n == 1): # 1일때 예외처리
            return True
        return recursive(n)
# 이렇게 짜면 test는 돌아는 가는데 문제는 runtime error가 뜬다.
"""
