class Solution:
    def reverseWords(self, s: str) -> str:
        #提取，反转，拼接
        s = s.strip()
        s2 = s.split()
        s2.reverse()
        return ' '.join(s2)




#注意：s2.reverse()不能写成s3 = s2.reverse().