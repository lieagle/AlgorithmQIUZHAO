#64.要想到达某个点的路径和最小，就需要到达左边的点或者上边的点时
# 路径和也最小，也就是满足最优子结构；而且每个点的最小路径和都是
# 由另外两个规模更小的点决定的，具有重叠子问题性质，
# 所以可以用动态规划。

#动态规划问题。求最小路径，分几种情况：
#用grid[i][j]表示走到这个点时的最小路径。
#1.当左边和上边都是矩阵边界,最小值就是这个点的值grid
#2.当只有左边是边界时，最小路径和只能是这个点的上边的点加上
# 这个点的值，
#也就是grid[i][j]=grid[i-1][j]+grid[i][j]
# 3,当只有上边是边界时，grid[i][j]=grid[i][j-1]+grid[i][j]
# 4.当左边和上边都不是边界,最小值就是从左边来的最小值
# 和从上边来的最小值之间较小的那个再加上当前点的值。
# grid[i][j]=min(grid[i-1][j], grid[i][j-1])+grid[i][j]
#时间复杂度：O(M*N)m是行数，n是列数，因为所有值都遍历到。
#空间复杂度O(1),没有占用额外的空间
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == j == 0: continue
                elif i == 0: grid[i][j] = grid[i][j - 1] + grid[i][j]
                elif j == 0: grid[i][j] = grid[i - 1][j] + grid[i][j]
                else: grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
        return grid[-1][-1]



#解法二，不在原数组上操作
#时间复杂度：O(M*N)m是行数，n是列数，因为所有值都遍历到。
#空间复杂度O(M*N),新建了一个dp二维数组
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: return 0
        rows, columns = len(grid), len(grid[0])
        dp = [[0] * columns for i in range(rows)]
        dp[0][0] = grid[0][0]
        for i in range(1, rows):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for j in range(1, columns):
            dp[0][j] = dp[0][j - 1] + grid[0][j]
        for i in range(1, rows):
            for j in range(1, columns):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[rows - 1][columns - 1]