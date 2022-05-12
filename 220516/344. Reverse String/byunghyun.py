class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        string_len = len(s) # 처음에 문자열의 길이를 미리 측정 -> 중복 측정 방지
        for i in range(string_len//2):
            s[i], s[string_len - 1 - i] = s[string_len - 1 - i], s[i] # 문자 swap
            
        
