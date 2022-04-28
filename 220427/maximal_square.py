# https://leetcode.com/problems/maximal-square/
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        row = len(matrix)
        col = len(matrix[0])
        
        dp = [[0]*(col+1) for _ in range(row+1)]
        p.pprint(dp)
        max_len = 0
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == "1":
                    dp[i+1][j+1] = min(dp[i][j], dp[i][j+1], dp[i+1][j]) + 1
                    max_len = max(max_len, dp[i+1][j+1])
        return max_len**2
