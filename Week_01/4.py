#leetcode 4. Median of Two Sorted Arrays
#不断从数组中间开始找
class Solution:
    def findk(self, nums1, start1, end1, nums2, start2, end2, k):
        while start1 <= end1 and start2 <= end2 and k > 1:
            len1 = end1 - start1 + 1
            len2 = end2 - start2 + 1
            i = start1 + min(len1, k//2) - 1
            j = start2 + min(len2, k//2) - 1
            if nums1[i] > nums2[j]:
                k -= j - start2 + 1
                start2 = j + 1
            else:
                k -= i - start1 + 1
                start1 = i + 1
        if start1 > end1:
            return nums2[start2 + k - 1]
        elif start2 > end2:
            return nums1[start1 + k - 1]
        else:
            return min(nums1[start1], nums2[start2])
        
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if (m + n) % 2 == 1:
            return self.findk(nums1, 0, m - 1, nums2, 0, n - 1, (m + n) // 2 + 1)
        result1 = self.findk(nums1, 0, m - 1, nums2, 0, n - 1, (m + n) // 2)
        result2 = self.findk(nums1, 0, m - 1, nums2, 0, n - 1, (m + n) // 2 + 1)
        return (result1 + result2) / 2 























