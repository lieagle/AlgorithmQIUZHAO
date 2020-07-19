#leetcode 26.Remove Element
#数组第一个元素默认放在第一位，扫描整个数组，遇到不同元素就从数组前面依次往后排，
#相同元素就跳过继续扫描。
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        for j in range(len(nums) - 1):
            if (nums[j] != nums[j+1]):
                nums[i] = nums[j+1]
                i += 1
        return i


#另一种解法：
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = sorted(set(nums))
        return len(nums)

