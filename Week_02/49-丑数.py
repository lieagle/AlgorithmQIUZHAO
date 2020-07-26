#Leetcode 49丑数

#解法一,动态规划
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # x(n),x(n+1),x(n+2) 可以分解成为 2*x(a),3*x(b),5*x(c)  x(n),x(n+1),x(n+2)是要
        # 求的 而x(a),x(b),x(c) 自然是之前已经求出来的  我们不知道x(n)是哪一个 但是它一定
        # 是  2*x(a),3*x(b),4*x(c) 中最小的  x(n) = min(2*x(a),3*x(b),4*x(c)) 这是核心表达式
        # 找出来了  我们只需要更新a,b,c即可找出所有的x(n)了   其中0=<a,b,c 
        # 也就是第i个丑数 与 a,b,c索引相关  
        dp, a, b, c = [1] * n, 0, 0, 0
        for i in range(1, n):
            n2, n3, n5 = dp[a] * 2, dp[b] * 3, dp[c] * 5
            dp[i] = min(n2, n3, n5)
            # 下面更新索引 不能使用elif  因为存在2*某个丑数 ,3*某个丑数,5*某个丑数相同的情况 
            # 出现相同的情况 所以要直接跳过 重复的情况 
            # 说明是第a个较小的丑数dp[a]与因子(2,3,5) 产生的dp[i]  所以右移a
            if dp[i] == n2: a += 1
            if dp[i] == n3: b += 1
            if dp[i] == n5: c += 1
        return dp[-1]