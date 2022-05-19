'''
스택의 특징, LIFO 사용.
닫는 괄호가 나오면 바로 직전에 똑같은 타입의 여는 괄호가 나와야함
바로 직전에 => LIFO
'''

class Solution:
    def isValid(self, s):
        # 예외처리: 길이가 홀수면 무조건 invalid
        if len(s)%2:
            return False

        # 스택 설정
        bracket_stack = []

        # 하나씩 돌면서
        for bracket in s:
            # 첫 번째 if: 닫는 괄호이고 스택이 남아 있으면
            # 두 번째 if: pop해서 같은 타입의 여는 괄호인지 확인
            #             -> 아니면 False
            if bracket == ")" and bracket_stack:
                if bracket_stack.pop() != "(":
                    return False
            elif bracket == "]" and bracket_stack:
                if bracket_stack.pop() != "[":
                    return False
            elif bracket == "}" and bracket_stack:
                if bracket_stack.pop() != "{":
                    return False

            # 여는 괄호이면 스택에 넣음
            elif bracket in ["(", "[", "{"]:
                bracket_stack.append(bracket)
            
            # 닫는 괄호인데 스택이 비어있으면 안됨
            else:
                return False
        
        # for문 다 돌고나서
        # 스택 비어 있으면 (닫는 괄호들이 여는 괄호들 다 가져 갔으면) True
        # 스택 남아 있으면 False
        return not bracket_stack
