# solution1: recursion
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        # 2로 계속 해서 나누는 recursive function
        def div(n):
            # 1이면 True (1은 나머지가 1이라 따로 처리 해줘야 함)
            if n == 1:
                return True
            
            # 나머지가 0이 아니면 False
            elif n%2 != 0:
                return False
            
            else:
                return div(n//2)
        
        # 0 이하는 일단 False
        if n <= 0:
            return False

        # 1은 True
        elif n == 1:
            return True
        
        # 나머지는 recursive 돌려보기
        else:
            return div(n)
                       
# solution2: binary
'''
bin()이란 내장함수가 있다.
숫자를 2진수로 변환해준다
2^n꼴만 0b100...이다.
그래서 네번째자리부터 봐서 1이 없으면 (0만 있으면) True를 반환한다.

0은 0b0이라서 네번째자리가 없다.
따라서 예외처리해준다

* 음수는 앞에 -가 붙어서 네번째자리부터 보면 -0b가 떨어지고 2진법 수만 남는다.
따라서 무조건 1이 있다.
'''
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        
        return '1' not in bin(n)[3:]
