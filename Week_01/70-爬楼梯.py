#leetcode 70.Climbing Stairs
#数学归纳法：
#n=1:f(1)一步
#n=2:(2)一步一步+直接两步
#n=3：f(1)+f(2)要么从1跳两步到3，要么从2跳一步到3，所以是1的方法数+跳到2的方法数
#mutual exclusive(互斥的), complete exhanstive  f(n)=f(n-1)+f(n-2)，Fibonacci

#1.傻递归法
#2.记忆化搜索
#3.动态规划:用一个数组进行循环，例如：
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
	





