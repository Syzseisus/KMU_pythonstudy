#스택으로 풀기

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # for 문을 통해 s 속 괄호 stack에 저장
        for b in s: 
            
            # 시작으로 들어오는 괄호가 (,{,[ 인 경우 stack에 append
            if ((b == '(') or (b == '{') or (b == '[')):  
                stack.append(b)
                
            # 시작으로 들어오는 괄호가 ),},] 인 경우(=stack이 아닌 경우) 
            elif(not stack): 
                return False
            else:
                # stack에 들어온 (,{,[ 중 하나 를 pop 해 top에 저장
                top = stack.pop()
                #b에 다음으로 들어오는 값과 top에 저장해놓은 값이 짝을 이루는 괄호가 아닌 경우
                if(((b == ")") and (top != "(")) or
                   ((b == "}") and (top != "{")) or
                   ((b == "]") and (top != "["))):
                    return False
        return len(stack) == 0
