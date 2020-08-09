#leetcode 70.Climbing Stairs
#数学归纳法：
#n=1:f(1)一步
#n=2:(2)一步一步+直接两步
#n=3：f(1)+f(2)要么从1跳两步到3，要么从2跳一步到3，所以是1的方法数+跳到2的方法数
#mutual exclusive(互斥的), complete exhanstive  f(n)=f(n-1)+f(n-2)，Fibonacci

#1.傻递归法,超出时间限制，可以用lru_cache缓存器。
#时间复杂度：O(2^n)，空间复杂度：o(n)，因为画成树共n层
class Solution:
    @functools.lru_cache(100)
    def climbStairs(self, n: int) -> int:
        if n < 3: return n
        for i in range(3, n + 1):
            res = self.climbStairs(i - 1) + self.climbStairs(i - 2)
        return res
        

#2.记忆化搜索，用字典或数组存储已经计算出来的值，下面是字典
#时间O(n),空间O(n),因为字典里元素n个
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}
        dp[1], dp[2] = 1, 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

#2.记忆化搜索，用字典或数组存储已经计算出来的值，下面是数组
#时间O(n)，空间O(n)，因为数组长度为n
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * 10
        dp[0], dp[1] = 1, 2
        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n-1]


#3.动态规划:只存储当前的几个向量值，时间O(n),空间O(1)
#只返回第n个Fibonacci数值：
class Solution(object):
	def climbStairs(self, n):
		f1, f2 = 0, 1
		for i in range(1, n+1):
			f3 =f1 + f2
			f1 = f2
			f2 = f3
		return f3

	
#扩展一下，返回n以内所有Fibonacci数值，输出结果：[1, 2, 3, 5]
#用数组存储，所以空间O(n)，时间还是O(n)
class Solution(object):
	def climbStairs(self, n):
		array = []
		f1, f2 = 0, 1
		for i in range(1, n + 1):
			f3 = f1 + f2
			f1 = f2
			f2 = f3
			array.append(f3)
		return array


#扩展中还可以用记忆化搜索方法，返回数组	
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * 10
        dp[0], dp[1] = 1, 2
        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp





