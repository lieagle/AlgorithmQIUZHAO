#leetcode 215

#解法一,最简单的排序.sort()和sorted()区别：sort在原数组上排序，
#sorted返回一个新的排好序的数组。而且sorted能堆dic字典排序（按照键值）
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums)[-k]


#解法二，堆。建大顶堆，删去k-1次堆顶，第k个堆顶就是ans。
#时间O(NlogN)，空间O(logN)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapsize=len(nums)
        def maxheap(a,i,length):
            l=2*i+1
            r=2*i+2
            large=i
            if l<length and a[l]>a[large]:
                large=l
            if r<length and a[r]>a[large]:
                large=r
            if large!=i:
                a[large],a[i]=a[i],a[large]
                maxheap(a,large,length)
            
        def buildheap(a,length):
            for i in range(heapsize//2,-1,-1):
                maxheap(a,i,length)

        buildheap(nums,heapsize)
        for i in range(heapsize-1,heapsize-k,-1):
            nums[0],nums[i]=nums[i],nums[0]
            heapsize-=1
            maxheap(nums,0,heapsize)
        return nums[0]
        
        
        
        