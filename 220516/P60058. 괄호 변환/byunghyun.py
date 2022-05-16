# 괄호를 뒤집는 함수
def reverse(u):
    result = ""
    '''
    코멘트: elem까진 써줘도 좋을듯!
    '''
    for ele in u:
        '''
        result += ")" if ele == "(" else "("
        '''
        if ele == "(":
            result += ")"
        else:
            result += "("
    return result

# 재귀적으로 문제를 풀어나가는 함수
def recursive(p):
    # 빈 문자열이 들어오면 그대로 반환
    '''
    코멘트: len(p) == 0이면 p = ""이라 그냥 return p 해도 됨
    '''
    if len(p) == 0:
        return ""
    
    # count를 통해 문자열을 u와 v로 나누어준다.
    count = 0
    for index, ele in enumerate(p):
        '''
        위에랑 마찬가지.
        count += 1 if ele == "(" else -1
        '''
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
    '''very good'''
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

'''
그냥
def solution(p):
    return recursive(p)
'''
