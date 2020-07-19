#Leetcode 1.Two Sum

#哈希表：a+b == target转换成for each a: check (target  - a) exists in nums.
#时间复杂度：O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, n in enumerate(nums): 
            if n in dic:
                return [dic[n], i]
            dic[target-n] = i

#哈希表：与第一种解法同理，只有写法不一样
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, n in enumerate(nums):
            if target-n in dic:
                return (dic[target-n], i)
            dic[n] = i


#双指针法：
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = enumerate(nums)
        nums = sorted(nums, key=lambda x:x[1])
        left, right = 0, len(nums)-1
        while left < right:
            if nums[left][1]+nums[right][1] == target:
                return sorted([nums[left][0], nums[right][0]])
            elif nums[left][1]+nums[right][1] < target:
                left += 1
            else:
                right -= 1
