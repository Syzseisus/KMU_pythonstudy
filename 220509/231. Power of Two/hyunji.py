# 1부터 시작해서 계속 2를 곱해준다. n과 동일해지면 True, n과 다르면 False
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        def powerOfTwo(num):
            # 계속 2를 곱한 값이 n보다 커지면, n은 2의 제곱수가 아님
            if num > n:
                return False
            elif num == n:
                return True
            else:
                # num에 2를 곱해서 파라미터로 넣어줌
                num = num * 2
                return powerOfTwo(num)
        
        # 초기값은 1        
        return powerOfTwo(1)
