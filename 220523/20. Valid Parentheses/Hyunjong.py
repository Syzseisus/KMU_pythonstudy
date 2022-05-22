class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 스택 사용
        stack = []
        
        # 모든 s 탐방
        for i in s:
            
            # s안에 왼쪽 괄호가 있는 경우 
            if i in ['(', '{', '[']:
                # 스택에 왼쪽 괄호 append
                stack.append(i)
                
            # 오른쪽 괄호가 나온 경우
            elif len(stack) > 0:
                # 괄호의 종류에 맞춰 왼쪽 괄호를 스택에서 제외시켜 준다.
                if stack[-1] == '(' and i == ')':
                    stack.pop()
                elif stack[-1] == '[' and i == ']':
                    stack.pop()
                elif stack[-1] == '{' and i == '}':
                    stack.pop()
                # 오른쪽 괄호가 나왔지만 짝이 맞는 왼쪽 괄호가 스택에 없는 경우
                else:
                    return False
            
            # 스택에 왼쪽 괄호가 없을 때 오른쪽 괄호가 나온 경우
            else:
 
                return False
        
        # s를 다 돌고 스택이 비었는지 확인
        if len(stack) == 0:
            return True
        
        else:
            return False
