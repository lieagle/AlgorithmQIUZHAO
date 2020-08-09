#Leetcode 22

#解法一,深度优先搜索DFS（回溯算法）
#当前左右括号都有大于0个可以使用的时候，才产生分支；
#产生左分支的时候，只看当前是否还有左括号可以使用；
#产生右分支的时候，还受到左分支的限制，右边剩余可以使用的括号数量一定得在严格大于左边剩余的数量的时候，才可以产生分支；
#在左边和右边剩余的括号数都等于0的时候结算

#left,right是未用的括号数，空间O(2^n)?    时间O(2^n)
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        s = ''
        def dfs(s, left, right):
            if left == 0 and right == 0:
                res.append(s)
            if left > right:
                return
            if left > 0:
                dfs(s + '(', left - 1, right)
            if right > 0:
                dfs(s + ')', left, right - 1)
        dfs(s, n, n)
        return res


#left，right代表已用的括号数,空间O(2^n)?    时间O(2^n)
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        s = ''
        def dfs(s, left, right, n):
            if left == n and right == n:
                res. append(s)
                return
            if left < right:
                return 
            if left < n:
                dfs(s + '(', left + 1, right, n)
            if right < n:
                dfs(s + ')', left, right + 1, n)
        dfs(s, 0, 0, n)
        return res
