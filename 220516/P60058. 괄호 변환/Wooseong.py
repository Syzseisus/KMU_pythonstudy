def solution(p):
    # "완벽한 문자열" 확인하기
    def is_perfect(p):
        l = 0
        r = 0
        for s in p:
            if s == '(':
                l += 1
            else:
                r += 1
            
            if l < r:
                return False

        return True

    # (4-4) 앞 뒤 떼고 괄호 방향 뒤집기
    def swap(u):
        u = u[1:-1]
        swap_list = ["(" if s == ")" else ")" for s in u]
        return ''.join(swap_list)
    
    # 예외처리
    # (0) 완벽한 문자열은 그대로 반환
    # (1) 빈 문자열도 같이 처리 된다
    if is_perfect(p):
        return p

    # 제시된 알고리즘
    # (2) 분리: 같아지자마자 자르면 됨
    def split_uv(p):
        l = 0
        r = 0
        # enumerate: index 뽑아서 잘라내기 위함
        for i, s in enumerate(p, 1):
            if s == '(':
                l += 1
            else:
                r += 1
            
            if l == r:
                return p[:i], p[i:]
    
    u, v = split_uv(p)

    # u가 "올바른 괄호 문자열인가?"
    def u_is_perfect(u, v):
        # (3) 맞다면
        if is_perfect(u):
            # (3-1) p 대신 v를 이용해 과정을 수행하고
            #       u 뒤에 붙여서 반환
            return u + solution(v)
        # (4) 아니라면
        else:
            start = '('             # (4-1) 첫번째 문자로 '('
            start += solution(v)    # (4-2) p 대신 v를 이용해 과정을 수행한 결과 붙임
            start += ')'            # (4-3) 뒤에 ')'
            start += swap(u)        # (4-4) 해당 함수 실행
            return start            # (4-5) 생성된 문자열 반환

    return u_is_perfect(u, v)
