#Leetcode 77

#解法一,和全排列问题一样，这是一道使用回溯算法解决的经典问题
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # 先把不符合条件的情况去掉
        if n <= 0 or k <= 0 or k > n:
            return []
        res = []
        self.__dfs(1, k, n, [], res)
        return res

    def __dfs(self, start, k, n, pre, res):
        # 当前已经找到的组合存储在 pre 中，需要从 start 开始搜索新的元素
        # 在第 k 层结算
        if len(pre) == k:
            res.append(pre[:])
            return

        for i in range(start, n + 1):
            pre.append(i)
            # 因为已经把 i 加入到 pre 中，下一轮就从 i + 1 开始
            # 注意和全排列问题的区别，因为按顺序选择，因此无须使用 used 数组
            self.__dfs(i + 1, k, n, pre, res)
            # 回溯的时候，状态重置
            pre.pop()
            
   
#解法二、迭代器   
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(itertools.combinations(range(1,n+1),k))

