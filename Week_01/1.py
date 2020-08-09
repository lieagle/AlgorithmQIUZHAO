#Leetcode 1.Two Sum

#哈希表：a+b == target转换成for each a: check (target  - a) exists in nums.
#enumerate()返回一个数组中的元素和元素下标
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




1题：

遍历这个数组，然后遍历这个数组之前可以存两个变量，
一个是嗯，我要计算的这个数组的盒儿，
另外一个是我需要回退的这个次数，我这个遍历数组的时候
会存在一个临界指就是介于大于这个K值小于K值之间的，
这个只把这个纸记下来，然后呢，如果加上下一个数的时候，
超过了这个K纸，那我就需要代表着我需要回退，
把这个回退的这个值加一，
然后这个盒儿还是不变的，就是大概就是这个样子。



import sys
if __name__ == "__main__":
    # 读取第一行的n
    N, M, T = int(sys.stdin.readline().strip())
    if T == 0: return 0
    for i in range(N):
        # 读取每一行
        line1 = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        list1 = list(map(int, line1.split()))
    for i in range(M):
        # 读取每一行
        line2 = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        list2 = list(map(int, line2.split()))
    minhot = -1
    minhot1 = minhot2 = minhot3 = 0
    meiwei_zhong = [i[1] for i in list1]
    meiwei_wan = [i[1] for i in list2]
    reliang_zhong = [i[0] for i in list1]
    reliang_wan = [i[0] for i in list2]
    if T in meiwei_zhong: 
        idx1 = meiwei_zhong.index(T)
        minhot1 = reliang_zhong[idx1]
    if T in meiwei_wan: 
        idx2 = meiwei_wan.index(T)
        minhot2 = reliang_wan[idx2]
    for i in meiwei_zhong:
        for j in meiwei_wan:
            if i + j == T:
                minhot3 = reliang_zhong[meiwei_zhong.index(i)] + reliang_wan[meiwei_wan.index(j)]
    if minhot1 == 0 and minhot2 == 0 and minhot3 ==0: return -1
    return min(minhot1, minhot2, minhot3)