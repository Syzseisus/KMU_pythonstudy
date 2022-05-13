def split_u_v(p):
    l, r = 0, 0
    u, v = '', ''
    
    '''
    코멘트:
    pp 대신 string의 앞글자 s나 character의 앞글자 c를 쓰는 것도?
    이건 개인 취향 (밑에 uu도 마찬가지)
    '''
    for pp in p:
        if l != 0 and l == r:
            v += pp
            continue        '''코멘트: if~else와 if>continue는 똑같다. 개인 취향'''
        
        '''
        코멘트:
        PEP8에, "절대로 다음은 하지말기"라고 적혀있다.
        '''
        if pp == '(': l += 1
        else: r += 1
        
        u += pp
    return u, v
    
def solution(p):
    
    # 1
    if not p:
        return ""   '''코멘트: not p == ""이므로 return p해도 될 거 같다.'''
    
    # 2
    u, v = split_u_v(p)
    
    # 3. u가 '올바른 괄호 문자열'인 경우
    '''
    코멘트:
    '균형잡힌'이 전제되어 있다면 시작이 "("기만 해도 '올바르다'
    그니까 and 뒤에는 버려도 돼요
    '''
    if u[0] == '(' and u[-1] == ')':
        return u + solution(v)
    
    # 4. u가 '올바른 괄호 문자열'이 아닌 경우
    else:
        # 4-1
        answer = '('
        # 4-2
        answer += solution(v)
        # 4-3
        answer += ')'
        # 4-4
        u = u[1:-1]
        '''
        코멘트:
        내가 쓴 list comprehension + join 활용하기
        1600개짜리 string 기준 0.00410 vs 0.00054로 10배 가까이 느림
        '''
        for uu in u:
            if uu == '(': 
                answer += ')'
            else: 
                answer += '('
        
    return answer
