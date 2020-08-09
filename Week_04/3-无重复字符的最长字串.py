#3，哈希表存储不重复的字符，双指针：左指针从最左边往右走，右指针也从最左端走，
#当右指针所指的值重复了，就把左指针的值移除，左指针往右移动一格。继续判断。
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        occ = set()
        n = len(s)
        right, ans = 0, 0
        for left in range(n):
            while right < n and s[right] not in occ:
                occ.add(s[right])
                right += 1
            if len(occ) > ans:
                ans = len(occ)
            occ.remove(s[left])
        return ans
