#621
利用桶思想，要求间隔为n时，桶的大小是n+1个单位时间，
相同的任务必须放在不同的桶中。假如出现次数最多的任务是A,A的数量
就是桶的个数m，需要的最短时间=(m-1)*(n+1)，最后一个桶内的时间是
出现次数和A一样多的任务个数。
有一个特殊情况是任务种类太多，n时间间隔不够用，也就是一个桶不能把
所有种类的任务都装一遍，这时候按照这个方法得到的值是小于tasks数组
长度的，这时返回数组长度即可。

步骤：
1.计算各种类任务出现的次数
2.把次数排序，选出次数最多的任务的数量
3.利用公式计算最短时间
4.考虑特殊情况，时间小于数组长度就返回数组长度

dict.get(key, 0)：在字典里查找键对应的值，如果没有这个键，
就返回默认值0，这里键是各种任务，值是任务出现的次数。

dict.items():返回一个列表，列表中的元素是元组样式的，元组由
字典里的键值对组成。

sorted(iterable, key = None, reverse = False)：对迭代器iterable
排序，根据key规则排序，reverse=False是升序，True是降序。
不在原来迭代器上操作，而是返回重新排序的一个新列表。
与list.sort()区别是sort在原列表上操作，返回排序后的原列表。
>>L=[2 1 3 4]
>>L1 = sorted(L)
输出：L = [2 1 3 4], L1 = [1 2 3 4]

>>array = [(a, 2), (b, 1), (c, 3)]
>>sorted(array, key = lambda s: s[1], reverse = True) #按照数字的顺序排序
输出：[(c, 3), (a, 2), (b, 1)]

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        length = len(tasks)
        if length <= 1:
            return length
        
        # 用于记录每个任务出现的次数
        task_map = dict()
        for task in tasks:
            task_map[task] = task_map.get(task, 0) + 1
        # 按任务出现的次数从大到小排序
        task_sort = sorted(task_map.items(), key=lambda x: x[1], reverse=True)
        
        # 出现最多次任务的次数
        max_task_count = task_sort[0][1]
        # 至少需要的最短时间
        res = (max_task_count - 1) * (n + 1)
        
        for sort in task_sort:
            if sort[1] == max_task_count:
                res += 1
        
        # 如果结果比任务数量少，则返回总任务数
        return res if res >= length else length

