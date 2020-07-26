#剑指offer 40

#解法一,最简单的排序，输出前k个。时间复杂度O(NlogN)
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        return arr[:k]


#解法二，布隆过滤器
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        # 布隆过滤器原理，因为知道数组的最大值
        nums = [0] * 10000  # 申请一个包含最大值个数的元素
        for ele in arr:
            nums[ele] += 1  # 对重复元素计数
        output = []
        i = 0  # 从0开始遍历（从最小值开始遍历）
        while len(output) < k:
            if nums[i] >= 1:  # 如果该索引处的值大于1，则说明该值存在至少1次，循环往output里面写
                for j in range(nums[i]):
                    output.append(i)
            i += 1
        return output[:k]  # 一定要注意单个重复的元素多余k个的情况



#解法三，用堆，即优先队列。维护一个堆，每次加进去值，就要遍历数组并插到堆里，
#每个值插入堆里的时间复杂度是o(logK),所以时间复杂度o(NlogK)     
#注意！！！优先队列PriorityQueue含有一个属性queue,输出队列中每个元素，
#三个方法，分别是qsize()，代表优先级队列中元素个数，put()，用heappush()方法将元素放入队列，
#get()，用heappop()方法将元素从队列取出。
#注意这个库在解答leetcode相关问题时(比如top-K问题，leetcode-215,347等)不能用
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k == 0:
            return []
        heaplist = HeapList()
        heaplist.buildHeap(arr[:k])
        for i in arr[k:]:
            if i < heaplist.heaplist[1]:
                heaplist.delMax()
                heaplist.insert(i)
        return heaplist.heaplist[1:]

class HeapList():
    """
    大顶堆
    """
    def __init__(self):
        self.heaplist = [0]
        self.size = 0

    def buildHeap(self, alist):
         i = len(alist) // 2
         self.size = len(alist)
         self.heaplist += alist[:]
         while i > 0:
             self.percDown(i)
             i -= 1

    def delMax(self):
        """删除堆顶最大元素"""
        retval = self.heaplist[1]
        self.heaplist[1] = self.heaplist[self.size]
        self.size -= 1
        self.heaplist.pop()
        self.percDown(1)
        return retval

    def insert(self, k):
        self.heaplist.append(k)
        self.size += 1
        self.percUP(self.size)

    def percUP(self, i):
        while i // 2 > 0:
            if self.heaplist[i] > self.heaplist[i // 2]:
                self.heaplist[i], self.heaplist[i // 2] = self.heaplist[i // 2], self.heaplist[i]
            i //= 2

    def percDown(self, i):
        while i * 2 <= self.size:
            mc = self.maxChild(i)
            if self.heaplist[i] < self.heaplist[mc]:
                self.heaplist[i], self.heaplist[mc] = self.heaplist[mc], self.heaplist[i]
            i = mc

    def maxChild(self, i):
        if 2 * i + 1 > self.size:
            return 2 * i
        else:
            if self.heaplist[2 * i] > self.heaplist[2 * i + 1]:
                return 2 * i
            else:
                return 2 * i + 1




#解法四，快排。
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        def partition(arr, l, r):
            #选定中值
            pivotvalue = arr[l]
            lmark = l + 1
            rmark = r
            done = False

            while not done:
                while lmark <= rmark and arr[lmark] <= pivotvalue:
                    lmark += 1
                while rmark >= lmark and arr[rmark] >= pivotvalue:
                    rmark -= 1
                if rmark < lmark:
                    done = True
                else:
                    arr[lmark], arr[rmark] = arr[rmark], arr[lmark]

            arr[l], arr[rmark] = arr[rmark], arr[l]
            return rmark
        
        def quicksort(arr, l, r, k):
            if l > r:
                return 
            pos = partition(arr, l, r)
            num = pos - l + 1
            if k == num:
                return
            if k < num:
                quicksort(arr, l, pos - 1, k)
            else:
                quicksort(arr, pos+1, r, k - num)

        if k == 0:
            return []
        quicksort(arr, 0, len(arr) - 1, k)
        return arr[:k]    