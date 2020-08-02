#Leetcode 122

#解法一、[1 2 3 4]连续增长的价格利润是：
#p[4]-p[1]=(p[2]-p[1])+(p[3]-p[2])+(p[4]-p[3])
#相当于每天都卖出并买入
#当连续降价时，不买入。
#时间复杂度O(n)，空间O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            tmp = prices[i] - prices[i - 1]
            if tmp > 0: profit += tmp
        return profit
        

？？？#解法二，解法一的不同方法实现。用python内置的zip函数，
#把两个迭代器中的元素组成元组tuple，最后组成列表输出
#时间复杂度O(n)，空间O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum(x - y for x, y in zip(prices[1:], prices) if x - y > 0)