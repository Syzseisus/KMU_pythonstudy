# stack = Last in First out

class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        brackets = {'(' : ')', '{' : '}', '[' : ']'}
        
        for bracket in s:
            # 열린 괄호만 stack에 append 해줌
            if bracket in brackets.keys():
                stack.append(bracket)
            else:
                # 현재 닫힌 괄호가 제일 나중에 들어온 열린 괄호랑 매치될 때
                if stack and bracket == brackets[stack[-1]]:
                    stack.pop()
                else:
                    return False
                
        if stack:
            return False
        else:
            return True
        
        
            
