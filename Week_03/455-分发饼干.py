#Leetcode 122

#解法一，贪心算法
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if len(g) == 0 or len(s) == 0: return 0
        g.sort()
        s.sort()
        gi = si = 0
        while(gi < len(g) and si < len(s)):
            if g[gi] <= s[si]:
                gi += 1
            si += 1
        return gi