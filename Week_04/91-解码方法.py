#91动态规划。除了几个特殊情况，和爬楼梯问题思路是一样的
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0': return 0
        dp = [0] * len(s)
        dp[0] = 1
        if len(s) == 1: return 1
        if s[1] == '0':
            if int(s[0:2]) <= 26: dp[1] = 1
            else: return 0
        else:
            if int(s[0:2]) <= 26: dp[1] = 2
            else: dp[1] = 1
        for i in range(2, len(s)):
            if s[i] == '0':
                if s[i - 1] == '0': return 0
                elif int(s[i-1:i+1]) <= 26: dp[i] = dp[i - 2]
                else: return 0
            else: 
                if s[i - 1] == '0': dp [i] = dp[i - 1]
                elif int(s[i-1:i+1]) <= 26: dp[i] = dp[i - 1] + dp[i - 2]
                else: dp[i] = dp[i - 1]
        return dp[len(s) - 1]


