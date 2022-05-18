# 힌트에 나온 대로, 열린 괄호를 스택에 계속 추가하다가 짝이 맞는 닫힌 괄호가 나올 경우 pop을 해주고, 짝이 맞지 않을 경우 바로 False를 반환한다.

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        # 문자열 s를 순환하며 계산함
        for ch in s:
            # 열린 괄호 stack에 추가
            if ch == '(' or ch == '{' or ch == '[':
                stack.append(ch)
            # 닫힌 괄호가 나올 경우, stack의 top에 있는 열린 괄호와 짝이 맞으면 stack에 저장한 열린 괄호 pop, 이때 stack에 원소가 남아있어야 함
            elif (len(stack) != 0 and stack[-1] == '(' and ch == ')') or (len(stack) != 0 and stack[-1] == '{' and ch == '}') or (len(stack) != 0 and stack[-1] == '[' and ch == ']'):
                stack.pop()
            # 위의 경우에 맞지 않을 경우 False 반환
            else:
                return False                  
                
        # 마지막으로 stack에 원소가 남아있을 경우, 짝이 맞지 않는 괄호가 있었다는 의미이므로 False 반환, 원소가 남아있지 않다면 True 반환
        if len(stack) != 0:
            return False
        else:
            return True
        
