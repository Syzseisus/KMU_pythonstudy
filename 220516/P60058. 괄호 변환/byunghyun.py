# 괄호를 뒤집는 함수
def reverse(u):
    result = ""
    for ele in u:
        if ele == "(":
            result += ")"
        else:
            result += "("
    return result

# 재귀적으로 문제를 풀어나가는 함수
def recursive(p):
    # 빈 문자열이 들어오면 그대로 반환
    if len(p) == 0:
        return ""
    
    # count를 통해 문자열을 u와 v로 나누어준다.
    count = 0
    for index, ele in enumerate(p):
        if ele == "(":
            count += 1
        else:
            count -= 1
        # u = () v = )(())( 이런식으로 나눌 수 있음 
        # u = )( v = () 이런식도 가능함
        if index != 0 and count == 0:
            u = p[:index + 1]
            v = p[index + 1:]
            break
    
    # 만약 u가 올바른 괄호라면
    if u[0] == "(":
        # 3-1 수행
        return u + recursive(v)
    
    # u가 올바르지 않은 괄호라면
    # 4의 과정을 수행한다.
    else:
        result = "(" # 4-1
        result += recursive(v) # 4-2
        result += ")" # 4-3
        result += reverse(u[1:len(u)-1]) # 4-4
        return result # 4-5
        
def solution(p):            
    answer = ''
    answer = recursive(p)
    return answer
