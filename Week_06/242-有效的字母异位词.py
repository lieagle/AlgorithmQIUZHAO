#用到哈希表
#s和t分别存进哈希表，比较元素和元素的个数都一样即可
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        Hash1 = {}
        Hash2 = {}
        for i in s:
            Hash1[i] = Hash1.get(i, 0) + 1
        for j in t:
            Hash2[j] = Hash2.get(j, 0) + 1
        if Hash1 == Hash2: 
            return True
        else:
            return False