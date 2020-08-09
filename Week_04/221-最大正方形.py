#221 最大正方形
动态规划方法，二维数组dp[i][j]表示以第i行，第j列为右下角的最大
正方形的边长。此处为1才有可能构成正方形。如果当前位置为1，
则此处可以构成的最大正方形的边长是由其左边，上边，左上角
共同约束的，是三者中最小值加1 
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if(not matrix):
            return 0
        m=len(matrix)
        n=len(matrix[0])
        res=0
        dp=[[0]*(n+1) for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if(matrix[i-1][j-1]=="1"):
                    dp[i][j]=min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1
                    res=max(dp[i][j],res)
        return res*res