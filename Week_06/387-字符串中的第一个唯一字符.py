#解法一、暴力搜索，遍历两遍字符串，第一遍i从0到len(s)-1，
#第二遍从i到len(s)-1
class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in range(len(s)):
            for j in range(len(s)):
                if i != j and s[j] == s[i]:
                    break
            else:
                return i
        return -1

#解法二、用哈希表，把s中元素和元素个数存到哈希表。
#找元素个数为1的元素下标即可。
class Solution:
    def firstUniqChar(self, s: str) -> int:
        Hash = {}
        for i in s:
            Hash[i] = Hash.get(i, 0) + 1
        for j in Hash.keys():
            if Hash[j] == 1:
                return s.find(j)
        return -1