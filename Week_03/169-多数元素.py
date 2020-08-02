#leetcode 169
#解法一，哈希表，直接遍历数组并计数，然后查找
#dic.get(num，0)是返回字典键值对应的值，没有这个键值就返回0.
#时间O(n)，空间O(n)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        n = len(nums)
        for i in nums:
            dic[i] = dic.get(i, 0) + 1
        for key in dic.keys():
            if dic[key] > n/2:
                return key


#解法二，哈希表，简单写法，collections.Counter()返回一个字典，
#其中键值是数组里的值，字典的值是数组中某个数出现的个数
#max()里以键值的规则求最大值，
#返回所有键值对应的值最大的那个键值，也就是数组里的某个数
#时间O(n)，空间O(n)
class Solution:
    def majorityElement(self, nums):
        counts = collections.Counter(nums)
        return max(counts.keys(), key = counts.get)
        
        

#解法三，排序，找数组中间的数
#题目中说多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
#并且给定的数组总是存在多数元素，所以将数组 nums 中的
所有元素按照单调递增或单调递减的顺序排序，
那么下标为n/2的元素（下标从 0 开始）一定是众数
class Solution:
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums)//2]



