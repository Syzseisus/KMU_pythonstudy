# 재귀로 풀이
class Solution:
    def reverseString(self, s: List[str]) -> None:
        # s = input, i = 앞글자 인덱스, j = 뒷글자 인뎃그
        def recursive (s, i , j):  
            if s and i <= j:  # input list와 첫번째 글자가 뒷글자보다 작거나 같다면
                s[i], s[j] = s[j], s[i]  # 앞글자와 뒷글자 요소를 바꿔준다
                recursive (s, i+1, j-1) # 앞글자 인덱스 +1 뒷글자 인덱스 -1 해주고 재귀
            
        return recursive(s, 0, len(s)-1) # 맨 처음 글자부터 중간까지 재귀 진행 후 return


            
