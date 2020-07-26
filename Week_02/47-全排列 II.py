#Leetcode 47

#解法一,插空法。
#{1, 2, 3, …, n-1, n}的全排列可由{1, 2, 3, …, n-1}的全排列得出。
#具体做法为针对{1, 2, 3, …, n-1}的任意一个排列{a1, a2, a3, …, an-1}，将n插入n个不同的位置得到：
#即可得到{1, 2, 3, …, n-1, n}的全排列。
#利用set去重复，比如[1,2,2]的全排列会有重复，因此代码中多了很多类型转换的地方，但意思就和上面的原理是一样的。
#但是这样做的重复率是非常低的，和最多相同元素的个数指数相关。

class Solution:
    def permuteUnique(self, s: List[int]) -> List[List[int]]:
        q = (s[0],) 
        res = set() 
        res.add(q) 
        cur = 1 
        while cur < len(s): 
            temp = set() 
            for ele in res: 
                for i in range(len(ele)+1): 
                    tele = list(ele) 
                    tele.insert(i,s[cur]) 
                    new_ele = tuple(tele) 
                    temp.add(new_ele) 
            res = temp 
            cur+=1
        res.add(tuple(list(s)))
        res=list(res) 
        for ele in range(len(res)): 
            res[ele]=list(res[ele]) 
        return res
