#1题.leetcode 26.Remove Element
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


#2题 leetcode 189. Rotate Array
#使用一个额外的数组，其中将数组的每个元素放置在其正确位置，将新数组复制到原始数组。
#时间复杂度：O(n)，由于使用另外一个数组，时间复杂度大。
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a = [0] * len(nums)
        for i in range(len(nums)):
            a[(i+k)%len(nums)] = nums[i] #recycle
        for i in range(len(nums)):
            nums[i] = a[i]


#使用循环替换
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        count = 0
        start = 0
        while count < len(nums):
            current = start 
            prev = nums[start] #store the value in the position
            
            while True:
                next = (current + k) % len(nums) #
                temp = nums[next] #store it temporaly 
                nums[next] = prev #overide the next 
                prev = temp #reset prev
                current = next #reset current
                count += 1

                if start == current:
                    break 



#3题 leetcode 21. Merge Two Sorted Lists
#迭代，先保证较小的链表为l1，然后依次比两个链表的头节点，把小的放到新链表的头，不断比较和加长新链表
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        newhead = ListNode(0, None)
        result = newhead
        while l1 and l2:
            if l1.val < l2.val:
                result.next = l1
                l1 = l1.next
            else:
                result.next = l2
                l2 = l2.next
            result = result.next
        if l1:
            result.next = l1
        elif l2:
            result.next = l2
        return newhead.next

#递归解法：
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
        return l2


#链表内迭代
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if None in (l1, l2):
            return l1 or l2
        dummy = cur = ListNode(0)
        dummy.next = l1
        while l1 and l2:
            if l1.val < l2.val:
                l1 = l1.next
            else:
                nxt = cur.next
                cur.next = l2
                tmp = l2.next
                l2.next = nxt
                l2 = tmp
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next

#4题 leetcode 88. Merge Sorted Array
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        nums1[:n] = nums2[:n]
        
        
#与上一解法类似        
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        m, n = m-1, n-1
        while m >= 0 and n >= 0:
            if nums1[m] > nums2[n]:
                nums1[m+n+1] = nums1[m]
                m -= 1
            else:
                nums1[m+n+1] = nums2[n]
                n -= 1
        if n != -1: # nums2 is still left
            nums1[:n+1] = nums2[:n+1]   
        





#5题.Leetcode 1.Two Sum

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


#6题. leetcode 242.Valid Anagram有效的字母异位词
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic1, dic2 = {}, {}
        for item in s:
            dic1[item] = dic1.get(item, 0) + 1
        for item in t:
            dic2[item] = dic2.get(item, 0) + 1
        return dic1 == dic2


#与上一解法类似，字母只有a~z共26个，所以：
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic1, dic2 = [0]*26, [0]*26
        for item in s:
            dic1[ord(item)-ord('a')] += 1
        for item in t:
            dic2[ord(item)-ord('a')] += 1
        return dic1 == dic2

#排序之后的比较即可
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
















