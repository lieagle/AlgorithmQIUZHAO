#Leetcode 239

#解法一、直接counter,然后对生成的字典排序取前k个即可，
#时间复杂度为nlogn
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = Counter(nums)
        res = sorted(dic.items(), key=lambda item:item[1], reverse=True)
        return list(map(lambda x:x[0], res))[:k]


#解法二、也可以用堆来实现，这样时间复杂度就是nlogk了
#(python默认为小顶堆，所以压入堆中时要取负数)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = Counter(nums)
        queue, res = [], []
        for i in dic:
            heapq.heappush(queue, (-dic[i], i))
        for i in range(k):
            tmp = heapq.heappop(queue)
            res.append(tmp[1])
        return res 


#解法三、优先队列；使用python特性
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        import heapq
        count = Counter(nums)   
        return heapq.nlargest(k, count.keys(), key=count.get)




#解法四、优先队列；维护大小为k的堆 -- 时间复杂度O(nlogk)
#优先队列；n + nlogk， 时间复杂度： O(nlogk)
# 下面只从堆的角度考虑，从m个元素中，通过堆选出最大的k个数
# k大小的小根堆；堆满后，若新加的数大于堆首数，弹出堆首元素 -- 弹出了m-k个最小的
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        import heapq as hq
        lookup = Counter(nums)
        res = []
        heap = []
        for num, freq in lookup.items() :
            # 如果堆满了（k个元素）
            if len(heap) == k :
                # 弹出最小频率的元组
                if heap[0][0] < freq:
                    hq.heapreplace(heap, (freq, num))
            else : 
                hq.heappush(heap, (freq, num))
        while heap :
            res.append(hq.heappop(heap)[1])
        
        return res


#解法五、优先队列；维护大小为n-k的堆 -- 时间复杂度O(nlog(n-k))
# 时间复杂度：O(nlog(n-k))；当k和n相当时，用此法
# 从m个元素中，通过堆选出最大的k个数；m-k 大小的堆 -- 大根堆
# 堆满后，若新加的数小于堆首数，堆首元素加入结果，否则新加的数加入结果 -- 选了k次最大的
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        import heapq as hq
        res = []

        heap = []
        lookup = Counter(nums)
        n = len(lookup)
        for num, freq in lookup.items() :
            if len(heap) == n-k :
                if heap and -heap[0][0] > freq :
                    res.append(hq.heapreplace(heap, (-freq, num))[1])
                else : res.append(num)
            else :
                hq.heappush(heap, (-freq, num))
        return res













