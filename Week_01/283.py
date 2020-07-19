#leetcode 283. Move Zeroes
#数组搜索一遍，不是0就往前放
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0  
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
                
#遇到0就去除，后面的前移，在结尾补0。每次去除一个0之后数组中非零元素数量都会减小1
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        n = len(nums)
        while i <n:
            if nums[i]==0:
                nums.pop(i)
                nums.append(0)
                n-=1
            else:
                i+=1