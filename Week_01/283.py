#leetcode 283. Move Zeroes

（1）#数组搜索一遍，不是0就往前放,
#只需遍历一次数组即可完成，时间O(N),
#在常数的空间类完成排序，空间O(1)
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
             



             
（2）#遇到0就去除，后面的前移，在结尾补0。
#每次去除一个0之后数组中非零元素数量都会减小1
#时间：O(N),空间O(1)
#class Solution:
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
                
                

（3）将数组里面的0移动到末尾，有几个0就移几个，其他的保持不变
法一：统计0元素
法二：双指针滑动，交换非零元素和零元素的位置
法三：非零元素替换零元素法

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 循环记录0元素的个数，并且遇到非0元素时候，将非0元素替换到0元素的位置
        # count 记录0元素的个数， i - count实际上是记录了零元素的位置。
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
            elif count > 0:
                nums[i - count], nums[i] = nums[i], 0
        return nums



